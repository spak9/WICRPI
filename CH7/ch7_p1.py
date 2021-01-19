'''
    The following error is that 'a =' expects a <factor> but gets a 
    NEWLINE

    The following error with 'printf(3)' is that when tokenizing, it views
    'printf' as a name, but Reis is using it as function, even a C function
    which shouldn't be recognized as such, therefore it will expect as ASSIGNOP 
    following a NAME token.

    The following error with 'print(3))' won't work from first glance because 
    nothing in our grammar supports unbalanced parentheses. The error the parser
    gets is 'Expecting NEWLINE'
'''
