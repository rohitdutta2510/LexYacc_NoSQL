import ply.lex as lex
import ply.yacc as yacc
import os

############################# FOR FINDING ACTIVE CASES #############################

tokens = ('BEGINTABLE','CLOSEDATA','CONTENT')
t_ignore = '\t'

date = []  # For keeping tally of daily deaths dates
count = [] # For keeping tally of daily deaths count

############### TOKEN RULES ################
def t_BEGINTABLE(t):
    r'text:.\'Active.Cases\'|name:.\'Currently.Infected\'|text:.\'\(Number.of.Infected.People\)\''
    return t

def t_CLOSEDATA(t):
    r'yAxis:.{|name:.\'3-day.moving.average\'|],'
    return t

def t_CONTENT(t):
   r'categories:.\[[^\]]*\]|data:.\[[^\]]*\]'
   return t

def t_error(t):
    t.lexer.skip(1)

############### GRAMMAR RULES #############
def p_start(p):
    '''start : collectdate collectcount'''

def p_collectdate(p):
    '''collectdate : BEGINTABLE CONTENT CLOSEDATA
                   | BEGINTABLE BEGINTABLE CONTENT CLOSEDATA'''
    global date
    # Dates are coming up
    if p[1] == "text: 'Active Cases'" or p[1] == "text: '(Number of Infected People)'":
        if len(p) == 4:
            content = p[2]  # This contains some unnecassary text, thus cleaning it
        elif len(p) == 5:
            content = p[3]
        content = content[len('categories: ['):-1]
        date = [element.strip('"') for element in content.split('\",\"')]

def p_collectcount(p):
    '''collectcount : BEGINTABLE CONTENT CLOSEDATA
                    | CONTENT BEGINTABLE CONTENT CLOSEDATA'''
    global count
    # Count with respect to the dates are handled here
    if len(p) == 4:
        if p[1] == "name: 'Currently Infected'":
            content = p[2]   # This contains some unnecessary text, thus cleaning it
            content = content[len('data: ['):-1]
            count = content.split(',')
            count = ['0' if val == 'null' else val for val in count]
    elif len(p) == 5:
        if p[2] == "name: 'Currently Infected'":
            content = p[3]
            content = content[len('data: ['):-1]
            count = content.split(',')
            count = ['0' if val == 'null' else val for val in count]

def p_error(p):
    pass

############### MAIN FUNCTION ##############
if __name__ == "__main__":
    root_dir = os.getcwd()
    webpage_dir = os.path.join(root_dir,'webpages')  # Going to the webpages folder

    for continent_folder in os.listdir(webpage_dir): #Going folder by folder
        if continent_folder == 'main_webpage.html':
            continue
        else:
            continent_path = os.path.join(webpage_dir,continent_folder)
            if os.path.isdir(continent_path):
                print(f'Continent : {continent_folder} starting')
                # Going country by country in a continent
                for country_file in os.listdir(continent_path):
                    html_file_path = os.path.join(continent_path,country_file) # HTML file path
                    file_obj = open(html_file_path, 'r', encoding='utf-8')
                    data = file_obj.read()
                        
                    # Tokenizing
                    lexer = lex.lex()
                    lexer.input(data)
                    print(f'{country_file} tokenizing done...')

                    # Parsing
                    parser = yacc.yacc()
                    parser.parse(data)
                    print(f'{country_file} parsing done...')
                    file_obj.close()
                    
                    # Writing the contents into a file named {country name}_active_cases.txt in Stats folder
                    if len(count) != 0:
                        stats_dir = os.path.join(root_dir,'Stats')
                        os.chdir(stats_dir)  # Going to Stats
                        fp = open(country_file[:-5]+'_active_cases.txt','w')
                        for i in range(len(date)):
                            # tab separated date and count
                            fp.write(date[i] + '\t' + count[i] + '\n')
                        fp.close()
                        os.chdir('..')  # Coming back from Stats
                        count = []
                        date = []

                print(f'Continent : {continent_folder} done...\n')       


################################### END OF MODULE 1 PART 1 #########################################