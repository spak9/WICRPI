'''
@Author Steven Pak
Reis's Writing Intepreters & Compilers 2nd Edition

Ch4 problem 1 solution

Grammar:
    <S> -> 'a' <S> 'b'
    <S> -> 'c'
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

def S():
    if (token == 'a'):
        # consuming would cause another check
        advance()
        S()
        consume('b')
    elif (token == 'c'):
        advance()
    else:
        raise RuntimeError('Expecting an a or c')


# begin the program
main()
