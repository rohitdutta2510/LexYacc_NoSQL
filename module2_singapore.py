import ply.lex as lex
import ply.yacc as yacc
from urllib.request import Request, urlopen

# Defining Tokens
tokens = ('BEGIN', 'END', 'OPENH2', 'CLOSEH2', 'OPENH3', 'CLOSEH3', 'OPENTABLE', 'CLOSETABLE', 
          'OPENBOLD', 'CLOSEBOLD', 'GARBAGE', 'CONTENT')
t_ignore = '\t'

# Tokenizer Rules
def t_BEGIN(t):
    r'<h2[^>]*>'
    return t

def t_END(t):
    r'<span.class="mw-headline".id="Notes">Notes</span> | <span.class="mw-headline".id="See_also">See.also</span> | <span.class="mw-headline".id="References">References</span> | <span.class="mw-headline".id="External_links">External.links</span>'
    return t

def t_OPENH2(t):
    r'<h2[^>]*>'
    return t

def t_CLOSEH2(t):
    r'</h2[^>]*>'
    return t

def t_OPENH3(t):
    r'<h3[^>]*>'
    return t

def t_CLOSEH3(t):
    r'</h3[^>]*>'
    return t

def t_OPENTABLE(t):
    r'<table[^>]*>'
    return t

def t_CLOSETABLE(t):
    r'</table[^>]*>'
    return t

def t_OPENBOLD(t):
    r'<b[^>]*>'
    return t

def t_CLOSEBOLD(t):
    r'</b[^>]*>'
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
    '''summary : BEGIN CONTENT CONTENT CLOSEH2 handletext summary
               | empty
    '''

def p_handletext(p):
    '''handletext : handleheader OPENTABLE skiptag CLOSETABLE handletext
                  | OPENTABLE skiptag CLOSETABLE handletext
                  | handlebold handlecontent handletext
                  | empty 
    '''

def p_handlebold(p):
    '''handlebold : OPENBOLD CONTENT CLOSEBOLD
    '''
    global data
    if p[2] != 'edit' and p[2] != 'citation needed':
        data.append('\n' + p[2] + '\n')

def p_handleheader(p):
    '''handleheader : OPENH3 CONTENT CONTENT CLOSEH3
    '''
    global data
    if p[2] != 'edit' and p[2] != 'citation needed':
        data.append('\n' + p[2])


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

def p_skiptag(p):
    '''skiptag : CONTENT skiptag
                | OPENBOLD skiptag
                | CLOSEBOLD skiptag
                | empty
    '''

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
    hyperlinks = ['https://en.wikipedia.org/wiki/Timeline_of_the_COVID-19_pandemic_in_Singapore_(2020)',
                  'https://en.wikipedia.org/wiki/Timeline_of_the_COVID-19_pandemic_in_Singapore_(2021)',
                  'https://en.wikipedia.org/wiki/Timeline_of_the_COVID-19_pandemic_in_Singapore_(2022)'
                ]
    
    filename = ['Singapore_2020.txt','Singapore_2021.txt', 'Singapore_2022.txt']

    for idx in range(len(hyperlinks)):
        wiki = getWikiPage(hyperlinks[idx])
        parseHTML(wiki)
        writeFile(filename[idx])
        data = []

    
if __name__ == '__main__':
    main()
    # parseHTML()
    # writeFile('temp.txt')