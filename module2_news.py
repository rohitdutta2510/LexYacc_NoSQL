import ply.lex as lex
import ply.yacc as yacc
from urllib.request import Request, urlopen

# Defining Tokens
tokens = ('BEGIN', 'END', 'OPENH3', 'CLOSEH3', 'OPENH4', 'CLOSEH4', 'IGNORE', 'GARBAGE', 'CONTENT')
t_ignore = '\t'

# Tokenizer Rules
def t_BEGIN(t):
    r'<span.class="mw-headline".id="Pandemic_chronology">Pandemic.chronology</span>'
    return t

def t_END(t):
    r'<span.class="mw-headline".id="Summary">Summary</span>'
    return t

def t_OPENH3(t):
    r'<h3[^>]*>'
    return t

def t_CLOSEH3(t):
    r'</h3[^>]*>'
    return t

def t_OPENH4(t):
    r'<h4[^>]*>'
    return t

def t_CLOSEH4(t):
    r'</h4[^>]*>'
    return t

def t_IGNORE(t):
    r'<figure[^>]*> [A-Za-z0-9,/() \'–.:-]+ </figure[^>]*>'

def t_GARBAGE(t):
    r'<[^>]*> | </[^>]*>'

def t_CONTENT(t):
    r'[A-Za-z0-9,/() \'–.:-]+'
    return t

def t_error(t):
    t.lexer.skip(1)

# Grammar Rules
data = [] 
ignore_num = [str(num) for num in range(1, 101)]   

def p_start(p):
    '''start : summary'''
    p[0] = p[1]

def p_summary(p):
    '''summary : BEGIN handletext END
               | BEGIN CONTENT handletext END
    '''

def p_handletext(p):
    '''handletext : handleheader handlecontent handletext
                  | handleheader handleh4 handlecontent handletext
                  | handleheader handlecontent handleh4 handlecontent handletext
                  | empty 
    '''

def p_handleheader(p):
    '''handleheader : OPENH3 CONTENT CLOSEH3
                    | OPENH3 CONTENT CONTENT CLOSEH3
                    | OPENH4 CONTENT CONTENT CLOSEH4
    '''
    global data
    if p[2] != 'edit':
        data.append('\n' + p[2] + '\n')

def p_handleh4(p):
    '''handleh4 : OPENH4 CONTENT CLOSEH4'''
    global data
    if p[2] != 'edit':
        data.append(p[2])

def p_handlecontent(p):
    '''handlecontent : addcontent handlecontent
                     | empty
    '''

def p_addcontent(p):
    '''addcontent : CONTENT'''
    global data
    global ignore_num

    if p[1] not in ignore_num and p[1] != 'edit':
        data.append(p[1])

def p_empty(p):
    '''empty :'''
    pass

def p_error(p):
    pass

def getWikiPage(hyperlink):
    req = Request(hyperlink, headers ={'User-Agent':'Mozilla/5.0'})
    webpage = urlopen(req).read()
    mydata = webpage.decode("utf8")
    # f=open('temp.html','w',encoding="utf-8")
    # f.write(mydata)
    # f.close
    return mydata

def parseHTML(doc):
    file_obj = open('temp.html','r',encoding="utf-8")
    doc = file_obj.read()
    lexer = lex.lex()
    lexer.input(doc)

    f=open('t.txt','w',encoding="utf-8")
    for tok in lexer:
        w = str(tok) + '\n'
        f.write(w)
    f.close

    parser = yacc.yacc()
    parser.parse(doc)
    # file_obj.close()


def writeFile(filename):
    global data
    path = './worldwide_news/' + filename
    f=open(path,'w',encoding="utf-8")
    text = ' '.join(data)
    f.write(text)
    f.close

# driver function
def main():
    years = [2020, 2021, 2022, 2023, 2024]
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    global data
    
    for year in years:
        if year not in [2023, 2024]:
            for month in months:
                filename = str(year) + '_' + month + '.txt'
                hyperlink = 'https://en.wikipedia.org/wiki/Timeline_of_the_COVID-19_pandemic_in_' + month + '_' + str(year)
                wiki = getWikiPage(hyperlink)
                parseHTML(wiki)
                writeFile(filename)
                data = []
        else:
            filename = str(year) + '.txt'
            hyperlink = 'https://en.wikipedia.org/wiki/Timeline_of_the_COVID-19_pandemic_in_' +  str(year)
            wiki = getWikiPage(hyperlink)
            parseHTML(wiki)
            writeFile(filename)
            data = []

    
if __name__ == '__main__':
    # main()
    parseHTML()
    writeFile('temp.txt')