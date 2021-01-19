'''
The 1st version of the Python tokenizer from
Reis's Compilers book. Original version can be 
found from his software package and this 
verison is simply for reinvention-sake.
'''

import sys # cmd line args

class Token:
    ''' The only class the tokenizer needs to realize
        are tokens, which consist of the literal lexeme
        , token type, and other properties for errors
    '''
    def __init__(self, line, column, category, lexeme):
        self.line = line # source program line number
        self.column = column # the column/index within the line
        self.category = category # token type 
        self.lexeme = lexeme # the literal string

''' Global variables '''
trace = True
source = ''     # The whole source program
sourceindex = 0 # the index for source 
line = 0        # the actual line
column = 0      # the character index within a line
tokenlist = []  # list holding ALL tokens; for parser
prevchar = '\n' # '\n' signal start of new line
blankline = True # False if line is not blank

''' Token Categories '''
EOF           = 0      # end of file
PRINT         = 1      # 'print' keyword
UNSIGNEDINT   = 2      # integer
NAME          = 3      # identifier that is not a keyword
ASSIGNOP      = 4      # '=' assignment operator
LEFTPAREN     = 5      # '('
RIGHTPAREN    = 6      # ')'
PLUS          = 7      # '+'
MINUS         = 8      # '-'
TIMES         = 9      # '*'
NEWLINE       = 10     # newline character
ERROR         = 11     # if not any of the above, then error

# displayable names for each token category, 
# indice match up with category type
catnames = ['EOF', 'PRINT', 'UNSIGNEDINT', 'NAME', 'ASSIGNOP',
            'LEFTPAREN', 'RIGHTPAREN', 'PLUS', 'MINUS',
            'TIMES', 'NEWLINE','ERROR']

# keywords and their token categories}
keywords = {'print': PRINT}

# one-character tokens and their token categories
smalltokens = {'=':ASSIGNOP, '(':LEFTPAREN, ')':RIGHTPAREN,
               '+':PLUS, '-':MINUS, '*':TIMES, '\n':NEWLINE, '':EOF}

# reads in source program file & calls tokenizer,
# eventually returning with an Exception or a full list of tokens
def main():
    global source # source program
    
    # correct no. of cmd line args
    if (len(sys.argv) == 2): 
        with open(sys.argv[1]) as f:
            source = f.read() # returns the whole file as a string

    else:
        print('Incorrect number of cmd-line args')
        print('format: python tokenizer_1.py <file_name>')
        sys.exit(1)

    # /n for text editors that DON'T end with /n
    # if one is missing, add one 
    if (source[-1] != '\n'):
        source = source + '\n'

    # run the tokenizer
    try:
        tokenizer()
    except RuntimeError as emsg:
        print(emsg)
        sys.exit(1)

def tokenizer():
    '''  Tokenizes tokens in source code and appends them to 'tokenlist' '''
    global token
    curchar = '' 
   
    # tokenize through the whole source program
    while True:
        # skip the white spaces, but not \n
        while (curchar != '\n' and curchar.isspace()):
            curchar = getchar() # get next char 
    
        # create a new token; category & lexeme are tbd
        token = Token(line, column, None, '')

        # Now we tokenize based on the current character we can see 
    
        # case 1: unsigned ints
        if (curchar.isdigit()):
            token.category = UNSIGNEDINT 
            # get the whole string of numbers
            while True:
                token.lexeme += curchar # append
                curchar = getchar()     # update char
                if not curchar.isdigit():   # break if no longer digit
                    break
        
        # case 2: keywords or identifier
        elif (curchar.isalpha() or curchar == '_'): 
            while True:
                token.lexeme += curchar     # append 
                curchar = getchar()         # get next 
                if not (curchar.isanum() or curchar == '_'):
                    break

            # check if lexeme is a keyword or identifier 
            if (token.lexeme in keywords):
                token.category = keywords[token.lexeme] # PRINT
            else:
                token.category = NAME       # else, it's a identifier
            
        # case 3: operators/small tokens
        elif (curchar in smalltokens):
            token.category = smalltokens[curchar] # get category
            token.lexeme = curchar
            curchar = getchar()     # move ot first char after token

        # case 4: not a valid token
        else:
            token.category = ERROR
            token.lexeme = curchar
            raise RuntimeError('Invalid Token')

        # append to tokenlist
        tokenlist.append(token)
        
        if (trace):
            print("%3s %4s  %-14s %s" % (str(token.line),
                str(token.column), catnames[token.category], token.lexeme))
        
        if (token.category == EOF): # end of tokenizing
            break

def getchar():
    ''' returns the next character in the source program and
        adjusts 'line' and 'column' globals if needed.
        It also returns '' when EOF & ' ' for blankline 
    '''
    global sourceindex, column, line, prevchar, blankline

    # if we're starting a new line, then we must update the global 
    # properties for where we are in source program

    # if the prevchar is a \n, then we must be a new line,
    # but we'll check for blank line soon
    if (prevchar == '\n'): # saying that we've seen a new line
        line += 1
        column = 0
        blankline = True # first assume that we've reached a blank line

    # check if we're at end of source
    if (sourceindex >= len(source)):
        column = 1
        prevchar = ''
        return '' # empty string signals EOF

    # get c
    c = source[sourceindex]
    sourceindex += 1
    column += 1
    # if 'c' is NOT a whitespace, then it must not be a blank line
    if (c.isspace() == False):
        blankline = False
    prevchar = c        # update prevchar 

    # if at end of blank line (just 1 \n), return space instead
    if (c == '\n' and blankline):
        return ' '
    else: 
        return c        # return character to tokenizer()

main()
