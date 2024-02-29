import ply.lex as lex
import ply.yacc as yacc
from urllib.request import Request, urlopen
import os

countries = ['France', 'UK', 'Russia', 'Italy', 'Germany', 'Spain', 'Poland', 'Netherlands', 'Ukraine', 'Belgium','USA', 'Mexico', 'Canada', 'Cuba', 'Costa Rica', 'Panama','India', 'Turkey', 'Iran', 'Indonesia', 'Philippines', 'Japan', 'Israel', 'Malaysia', 'Thailand', 'Vietnam', 'Iraq', 'Bangladesh', 'Pakistan', 'Brazil', 'Argentina', 'Colombia', 'Peru', 'Chile', 'Bolivia', 'Uruguay', 'Paraguay', 'Venezuela', 'South Africa', 'Morocco', 'Tunisia', 'Ethiopia', 'Libya', 'Egypt', 'Kenya', 'Zambia', 'Algeria', 'Botswana', 'Nigeria', 'Zimbabwe','Australia', 'Fiji', 'Papua New Guinea', 'New Caledonia', 'New Zealand']
continents = ['Asia','Europe','North America','South America','Oceania','Africa']
file = open('main_stats.txt','w')

# Declaring tokens
tokens = ('BEGINTABLE','OPENROW','CLOSEROW','OPENDATA',
          'OPENNOBR','CLOSENOBR','CLOSEDATA','CONTENT',
          'OPENTHEAD','CLOSETHEAD','GARBAGE')
t_ignore = '\t'

############## TOKENIZATION RULES ###############
def t_BEGINTABLE(t):
    r'<div.class="tab-pane.".id="nav-yesterday".role="tabpanel".aria-labelledby="nav-yesterday-tab">'
    return t

def t_OPENROW(t):
    r'<tr[^>]*>'
    return t

def t_CLOSEROW(t):
    r'</tr[^>]*>'
    return t

def t_OPENDATA(t):
    r'<td[^>]*>'
    return t

def t_CLOSEDATA(t):
    r'</td>'
    return t

def t_OPENNOBR(t):
    r'<nobr>'
    return t

def t_CLOSENOBR(t):
    r'</nobr>'
    return t

def t_CONTENT(t):
    r'[a-zA-Z0-9+-,.\/]+(\s[a-zA-Z0-9+-,.\/]+)*'
    return t

def t_OPENTHEAD(t):
    r'<thead>'
    return t

def t_CLOSETHEAD(t):
    r'</thead>'
    return t

def t_GARBAGE(t):
    r'<[^>]*>'
    return t

def t_error(t):
    t.lexer.skip(1)

############# GRAMMAR RULES ###############
def p_start(p):
    '''start : BEGINTABLE dump OPENTHEAD dump CLOSETHEAD GARBAGE handlerow'''

def p_dump(p):
    '''dump : GARBAGE dump
            | CONTENT dump
            | OPENROW dump
            | CLOSEROW dump
            | OPENNOBR dump
            | CLOSENOBR dump
            | empty'''

def p_reduntant(p):
    '''reduntant : OPENDATA reduntant
                 | CONTENT reduntant
                 | CLOSEDATA reduntant
                 | GARBAGE reduntant
                 | empty'''
def p_empty(p):
    '''empty :'''
    pass

def p_handlerow(p):
    '''handlerow : OPENROW handlecontent CLOSEROW handlerow
                 | empty'''

def p_handlecontent(p):
    '''handlecontent : datacell datacell datacell datacell datacell datacell datacell datacell datacell datacell datacell datacell datacell datacell reduntant'''

    if p[2] != 'reject':
        line = '\t'.join(p[2:15])
        file.write(line + '\n')

def p_datacell(p):
    '''datacell : OPENDATA CLOSEDATA
                | OPENDATA CONTENT CLOSEDATA
                | OPENDATA CONTENT CONTENT CLOSEDATA
                | OPENDATA OPENNOBR CLOSENOBR CLOSEDATA
                | OPENDATA OPENNOBR CONTENT CLOSENOBR CLOSEDATA
                | OPENDATA GARBAGE CONTENT GARBAGE CLOSEDATA
                | OPENDATA GARBAGE CONTENT CONTENT GARBAGE CLOSEDATA
                | OPENDATA GARBAGE CONTENT CONTENT CONTENT GARBAGE CLOSEDATA'''
    if len(p) == 3:
        p[0] = 'N/A'
    elif len(p) == 4:
        p[0] = p[2]
    elif len(p) == 5:
        p[0] = 'reject'
    elif len(p) == 6:
        p[0] = p[3]
    elif len(p) == 7:
        p[0] = '-'.join(p[3:5])
    elif len(p) == 8:
        if p[3] == 'R':
            p[0] = 'Reunion'
        elif p[3] == 'Cura':
            p[0] = 'Curacao'

def p_error(p):
    pass



#################### FUNCTIONS FOR CREATING DIRECTORIES AND DOWNLOADING WEBPAGES ###################
# Reads from the text file 'worldometers_countrylist.txt'
def make_dict():
    with open('worldometers_countrylist.txt','r') as fp:
        file_contents = fp.readlines()

    continent_dict = {}  # For storing countries by continents
    
    # Continent is key and the countries are appended as values
    for content in file_contents:
        content = content.rstrip('\n')
        if not content or content[0] == '-':
            continue
        elif content[-1] == ':':
            continent = content[0:-1]
            continent_dict[continent] = []
        else:
            continent_dict[continent].append(content)
    # print(continent_dict)
    return continent_dict

# Downloads the webpages
def webpage_download(link, page_name):
    req = Request(link, headers ={'User-Agent':'Mozilla/5.0'})
    webpage = urlopen(req).read()
    mydata = webpage.decode("utf8")
    f = open(page_name+'.html', 'w', encoding="utf-8")
    f.write(mydata)
    f.close()

# Calls the webpage_download to get all the webpages
def download_indi_page(continent_dict):
    # Creating a sub directory for storing the webpages continent wise
    curr_dir = os.getcwd()
    new_dir = os.path.join(curr_dir,'webpages')
    if not os.path.exists(new_dir):
        os.mkdir(new_dir)

    link = 'https://www.worldometers.info/coronavirus/'   # The main page
    os.chdir(new_dir)
    webpage_download(link, 'main_webpage')

    for continent,countries in continent_dict.items():
        conti_dir = os.path.join(new_dir,continent)
        
        if not os.path.exists(conti_dir):
            os.mkdir(conti_dir)
        os.chdir(conti_dir)

        for country in countries:
            if country == 'USA':
                cpy_country = 'US'
            cpy_country = country  # Making a copy
            cpy_country = cpy_country.replace(' ','-')
            cpy_country = cpy_country.lower()
            cpy_country = 'country/'+cpy_country+'/'
            webpage_download(link+cpy_country, country)
        print(f'{continent} all websites fetching done...',flush=True)
        os.chdir('..')  # Back to webpages directory
    
    os.chdir('..') # Back to root directory (curr_dir)


################################ MAIN FUNCTION ##################################
def main():
    continent_dict = make_dict()

    # Downloading individual pages for each country given in the text file
    # download_indi_page(continent_dict)

    # Fetching the yesterday details from the table
    curr_dir = os.getcwd()
    filepath = os.path.join(curr_dir,'webpages','main_webpage.html')
    file_obj = open(filepath, 'r', encoding='utf-8')
    data = file_obj.read()

    # 1.Tokenizing
    print('Starting Tokenizing...')
    lexer = lex.lex()
    lexer.input(data)
    print('Tokenizing done...')
    file_obj.close()

    # 2.Parsing
    print('Starting parsing...')
    parser = yacc.yacc()
    parser.parse(data)
    print('Parsing Done...')
    file.close()
    sub_dir_name = 'Stats'
    file_name = 'main_stats.txt'
    if not os.path.exists(sub_dir_name):
        os.mkdir(sub_dir_name)
    curr_path = os.path.join(os.getcwd(), file_name)
    new_path = os.path.join(os.getcwd(), sub_dir_name, file_name)
    os.rename(curr_path,new_path)



main()
