# t1.py tokenizer
import sys        # sys needed to access cmd line args and sys.exit()

class Token:
   def __init__(self, line, column, category, lexeme):
      self.line = line         # source prog line number of the token
      self.column = column     # source prog col in which token starts
      self.category = category # category of the token
      self.lexeme = lexeme     # token in string form

# global variables
trace = True           # controls token trace
source = ''            # receives entire source program
sourceindex = 0        # index into source
line = 0               # current line number 
column = 0             # current column number
tokenlist = []         # list of tokens created by tokenizer
prevchar = '\n'        # '\n' in prevchar signals start of new line
blankline = True       # reset to False if line is not blank

# constants that represent token categories
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

# displayable names for each token category
catnames = ['EOF', 'PRINT', 'UNSIGNEDINT', 'NAME', 'ASSIGNOP',
            'LEFTPAREN', 'RIGHTPAREN', 'PLUS', 'MINUS',
            'TIMES', 'NEWLINE','ERROR']

# keywords and their token categories}
keywords = {'print': PRINT}

# one-character tokens and their token categories
smalltokens = {'=':ASSIGNOP, '(':LEFTPAREN, ')':RIGHTPAREN,
               '+':PLUS, '-':MINUS, '*':TIMES, '\n':NEWLINE, '':EOF}

# main() reads input file and calls tokenizer()
def main():
   global source

   if len(sys.argv) == 2:   # check if correct number of cmd line args
      try:
         infile = open(sys.argv[1], 'r')
         source = infile.read()  # read source program
      except IOError:
         print('Cannot read input file ' + sys.argv[1])
         sys.exit(1)
   else:
      print('Wrong number of command line arguments')
      print('format: python t1.py <infile>')
      sys.exit(1)

   if source[-1] != '\n':        # add newline to end if missing
      source = source + '\n'

   if trace:                     # for token trace
      print('Line  Col Category       Lexeme\n')

   try:
      tokenizer()                # tokenize source code in source
   except RuntimeError as emsg: 
     # output slash n in place of newline
     lexeme = token.lexeme.replace('\n', '\\n')
     print('\nError on '+ "'" + lexeme + "'" + ' line ' +
        str(token.line) + ' column ' + str(token.column))
     print(emsg) # message from RuntimeError object
     sys.exit(1)       # 1 return code indicates an error has occurred
 
# tokenizer tokenizes tokens in source code and appends them to tokens
def tokenizer():
   global token
   curchar = ' '                 # prime curchar with space

   while True:
      # skip whitespace but not newlines
      while curchar != '\n' and curchar.isspace():
         curchar = getchar() # get next char from source program

      # construct and initialize a new token
      token = Token(line, column, None, '')  

      if curchar.isdigit():            # start of unsigned int?
         token.category = UNSIGNEDINT  # save category of token
         while True:
            token.lexeme += curchar    # append curchar to lexeme
            curchar = getchar()        # get next character
            if not curchar.isdigit():  # break if not a digit
               break

      elif curchar.isalpha() or curchar == '_':   # start of name?
         while True:
            token.lexeme += curchar    # append curchar to lexeme
            curchar = getchar()        # get next character
            # break if not letter, '_', or digit
            if not (curchar.isalnum() or curchar == '_'):
               break

         # determine if lexeme is a keyword or name of variable
         if token.lexeme in keywords:
            token.category = keywords[token.lexeme]
         else:
            token.category = NAME

      elif curchar in smalltokens:
         token.category = smalltokens[curchar]   # get category
         token.lexeme = curchar
         curchar = getchar()       # move to first char after token

      else:                         
         token.category = ERROR    # invalid token 
         token.lexeme = curchar    # save lexeme
         raise RuntimeError('Invalid token')
      
      tokenlist.append(token)      # append token to tokens list
      if trace:                    # display token if trace is True
         print("%3s %4s  %-14s %s" % (str(token.line), 
            str(token.column), catnames[token.category], token.lexeme))

      if token.category == EOF:    # finished tokenizing?
         break

# getchar() gets next char from source and adjusts line and column
def getchar():
   global sourceindex, column, line, prevchar, blankline

   # check if starting a new line
   if prevchar == '\n':    # '\n' signals start of a new line
      line += 1            # increment line number                             
      column = 0           # reset column number
      blankline = True     # initialize blankline

   if sourceindex >= len(source): # at end of source code?
      column = 1                  # set EOF column to 1  
      prevchar = ''               # save current char for next call
      return ''                   # null str signals end of source

   c = source[sourceindex] # get next char in the source program
   sourceindex += 1        # increment sourceindex to next character
   column += 1             # increment column number
   if not c.isspace():     # if c not whitespace then line not blank
      blankline = False    # indicate line not blank
   prevchar = c            # save current char for next call

   # if at end of blank line, return space in place of '\n'
   if c == '\n' and blankline:
      return ' '
   else:
      return c             # return character to tokenizer()

main()                     # call main function

