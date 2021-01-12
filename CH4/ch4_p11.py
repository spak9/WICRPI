'''
@Author Steven Pak
Reis's Writing Intepreters and Compilers 2nd edition

ch4 p11

The current grammar of:
    <S> -> <S> 'a'
    <S> -> 'b'
doesn't work well with top-down parsers because
of left-recursion. 

The new grammar is:
    <S> -> 'b' <T>
    <T> -> 'a' <T> | lambda
'''
