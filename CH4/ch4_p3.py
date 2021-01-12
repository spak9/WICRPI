'''
@Author Steven Pak
Reis's Writing Intepreters & Compilers 2nd Edition

Ch4 problem 3 solution

Grammar:
    <S> -> 'a'* <B>
    <B> -> 'b'* <C>
    <C> -> 'c'['d'|'e']'f'
'''

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
    
    # check if we're at the end of the string
    if (token != ''):
        print('Garbage within the <S>-string')
    else:
        print('<S>-string valid')
def S():
    # loop while token is 'a'
    while (token == 'a'):
        advance()
    B()

def B():
    # loop while token is 'b'
    while (token == 'b'):
        advance()
    C()

def C():
    consume('c')
    # check between the optional tokens
    if (token == 'd'):
        advance()
    elif (token == 'e'):
        advance()
    consume('f')

main()
