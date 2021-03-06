'''
@Author Steven Pak
Reis's Writing Intepreters & Compilers 2nd Edition

Ch4 problem 4 solution

Grammar:
    <S> -> <A><B><C>
    <A> -> 'a' 
    <A> -> '' 
    <B> -> 'b'
    <B> -> ''
    <C> -> 'c'
    <C> -> ''
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
    
    if (token != ''):
        print('Garbage following <S>-string')
    else:
        print('pass')
    
def S():
    # Only 1 <S> production
    if (token in ['a', 'b', 'c']):
        A()
        B()
        C()
    else:
        raise RuntimeError('Expecting a, b, or c')

def A():
    # 1st production
    if (token == 'a'):
        advance()
    
    # 2nd production that is lambda, therefore
    # the current token is already on the next 
    # production's token
    elif (token in ['b', 'c', '']):
        pass
    else: 
        raise RuntimeError('Expecting a or lambda')

def B():
    if (token == 'b'):
        advance()
    elif (token in ['c', '']):
        pass
    else:
        raise RuntimeError('Expecting b or lambda')

def C():
    if (token == 'c'):
        advance()
    elif (token == ''):
        pass
    else:
        raise RuntimeError('Expecting c or lambda')

main()

