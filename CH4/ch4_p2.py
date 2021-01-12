'''
@Author Steven Pak
Reis's Writing Intepreters & Compilers 2nd Edition

Ch4 problem 2 solution

Grammar:
    <S> -> 'a' <B> 'd'
    <B> -> ('b' 'b')* [c]
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
    consume('a')
    B()
    consume('d')

def B():
    # pairs of b's
    while (token == 'b'):
        advance()
        consume('b')

    # optional 'c'
    if (token == 'c'):
        advance()

main()
