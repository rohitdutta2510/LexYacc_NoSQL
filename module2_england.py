import ply.lex as lex
import ply.yacc as yacc
from urllib.request import Request, urlopen

# Defining Tokens
tokens = ('BEGIN', 'END', 'OPENH3', 'CLOSEH3', 'OPENLI', 'CLOSELI', 'GARBAGE', 'CONTENT')
t_ignore = '\t'

# Tokenizer Rules
def t_BEGIN(t):
    r'<span.class="mw-headline".id="Timeline">Timeline</span>'
    return t

def t_END(t):
    r'<span.class="mw-headline".id="Notes">Notes</span> | <span.class="mw-headline".id="See_also">See.also</span> | <span.class="mw-headline".id="References">References</span> | <span.class="mw-headline".id="External_links">External.links</span>'
    return t

def t_OPENH3(t):
    r'<h3[^>]*>'
    return t

def t_CLOSEH3(t):
    r'</h3[^>]*>'
    return t

def t_OPENLI(t):
    r'<li[^>]*>'
    return t

def t_CLOSELI(t):
    r'</li[^>]*>'
    return t

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

def p_summary(p):
    '''summary : BEGIN CONTENT handletext
    '''

def p_handletext(p):
    '''handletext : handleheader handleli handletext
                  | empty 
    '''

def p_handleheader(p):
    '''handleheader : OPENH3 CONTENT CONTENT CLOSEH3
    '''
    global data
    if p[2] != 'edit' and p[2] != 'citation needed':
        data.append('\n' + p[2])

def p_handleli(p):
    '''handleli : OPENLI addnewline handlecontent handleli CLOSELI handleli
                | OPENLI addnewline handlecontent handleli CLOSELI CONTENT handleli
                | OPENLI addnewline handlecontent CLOSELI handleli
                | empty
    '''

def p_addnewline(p):
    '''addnewline : empty
    '''
    data.append('\n')

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

    return mydata

def parseHTML(doc):
    # file_obj = open('temp.html','r',encoding="utf-8")
    # doc = file_obj.read()
    lexer = lex.lex()
    lexer.input(doc)

    # f=open('t.txt','w',encoding="utf-8")
    # for tok in lexer:
    #     w = str(tok) + '\n'
    #     f.write(w)
    # f.close

    parser = yacc.yacc()
    parser.parse(doc)
    # file_obj.close()


def writeFile(filename):
    global data
    path = './worldwide_country/' + filename
    f=open(path,'w',encoding="utf-8")
    text = ' '.join(data)
    f.write(text)
    f.close

# driver function
def main():
    global data
    hyperlinks = ['https://en.wikipedia.org/wiki/Timeline_of_the_COVID-19_pandemic_in_England_(January%E2%80%93June_2020)',
                  'https://en.wikipedia.org/wiki/Timeline_of_the_COVID-19_pandemic_in_England_(July%E2%80%93December_2020)'
                ]
    
    filename = ['England_January_June_2020.txt','England_July_December_2020.txt',]

    for idx in range(len(hyperlinks)):
        wiki = getWikiPage(hyperlinks[idx])
        parseHTML(wiki)
        writeFile(filename[idx])
        data = []

    
if __name__ == '__main__':
    main()
    # parseHTML()
    # writeFile('temp.txt')