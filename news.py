import ply.lex as lex
import ply.yacc as yacc

# Defining Tokens
tokens = ('BEGIN', 'END', 'OPENH3', 'CLOSEH3', 'IGNORE', 'GARBAGE', 'CONTENT')
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

def p_start(p):
    '''start : summary'''
    p[0] = p[1]

def p_summary(p):
    '''summary : BEGIN handletext END
    '''
    f=open('news.txt','w',encoding="utf-8")
    text = ' '.join(data)
    f.write(text)
    f.close

def p_handletext(p):
    '''handletext : handleheader handlecontent handletext
                  | empty 
    '''

def p_handleheader(p):
    '''handleheader : OPENH3 CONTENT CLOSEH3'''
    data.append('\n' + p[2] + '\n')

def p_handlecontent(p):
    '''handlecontent : addcontent handlecontent
                     | empty
    '''

def p_addcontent(p):
    '''addcontent : CONTENT'''
    data.append(p[1])

def p_empty(p):
    '''empty :'''
    pass

def p_error(p):
    pass

# driver function
def main():
    file_obj = open('news.html','r',encoding="utf-8")
    data = file_obj.read()
    lexer = lex.lex()
    lexer.input(data)

    # f=open('t.txt','w',encoding="utf-8")
    # for tok in lexer:
    #     w = str(tok) + '\n'
    #     f.write(w)
    # f.close

    parser = yacc.yacc()
    parser.parse(data)
    file_obj.close()

if __name__ == '__main__':
    main()