# From Reis's Writing Compilers 2nd Edition

# Grammer:
# S -> AC
# A -> ab
# C -> cC
# C -> d

import sys

tokenindex = -1
token = ''

def main():
    try:
        parser()
    except RuntimeError as emsg:
        print(emsg)

def advance():
    global tokenindex, token
    tokenindex += 1 # increment index
    # check if we're at the end of string or given no input string
    if (len(sys.argv) < 2 or tokenindex >= len(sys.argv[1])):
        token = ''; # the end 
    else:
        token = sys.argv[1][tokenindex] # advance to next token (character)

def consume(expected):
    if (expected == token):
        advance()
    else:
        raise RuntimeError(f'Expecting: {expected}')

def parser():
    # prime token with first token 
    advance() 
    S()

    # check if we've finished input string, that is
    # S() will eventually chain all calls to end, therefore
    # if we end up with another token after S(), input doesn't
    # end with 'd'
    if token != '':
        print('Garbage following <S>-string')

def S():
    A()
    C()

def A():
    consume('a')
    consume('b')

def C():
    if (token == 'c'):
        advance()
        C()
    # if we reach 'd' token, then we've come to the end of the grammar and input string
    elif token == 'd':
        advance()
    else:
        raise RuntimeError('Expecting c or d')

main()
