import re

p = re.compile('[a-z]+')
#print(p.match("::tempo"))
m=p.match(":tempo")
#print(m.group(),m.span() )
print(m)

'''m=p.search("::tempo")
print(m.group(),m.span() )'''

'''import subprocess
result = subprocess.run( ['python','frenchdeck.py'],capture_output=True,text=True)
print(result.stdout)
print(result.stderr)'''

p = re.compile(r'\d+')
m=p.findall('12 drummers 0 drumming, 11 pipers piping, 10 lords a-leaping')
print(m)

def hexrepl(match):
    "返回十进制数字的十六进制字符串"
    value = int(match.group())
    return hex(value)

p = re.compile(r'\d+')
str_done = p.sub(hexrepl, 'Call 65490 for printing, 49152 for user code.')
print(str_done)

print('123')

'''re.sub(r'def\s+([a-zA-Z_][a-zA-Z_0-9]*)\s*\(\s*\):',
    r'static PyObject*\npy_\1(void)\n{',
    'def myfunc():','aba134s')'''

def dashrepl(matchobj):
    if matchobj.group(0) == '-': 
        return ' '
    else: 
        return '-'

print(re.sub('-{1,2}', dashrepl, 'pro----gram-files'))

##%%
from typing import NamedTuple
import re

class Token(NamedTuple):
    type: str
    value: str
    line: int
    column: int

def tokenize(code):
    keywords = {'IF', 'THEN', 'ENDIF', 'FOR', 'NEXT', 'GOSUB', 'RETURN'}
    token_specification = [
        ('NUMBER',   r'\d+(\.\d*)?'),  # Integer or decimal number
        ('ASSIGN',   r':='),           # Assignment operator
        ('END',      r';'),            # Statement terminator
        ('ID',       r'[A-Za-z]+'),    # Identifiers
        ('OP',       r'[+\-*/]'),      # Arithmetic operators
        ('NEWLINE',  r'\n'),           # Line endings
        ('SKIP',     r'[ \t]+'),       # Skip over spaces and tabs
        ('MISMATCH', r'.'),            # Any other character
    ]
    tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specification)
    line_num = 1
    line_start = 0
    for mo in re.finditer(tok_regex, code):
        kind = mo.lastgroup
        value = mo.group()
        column = mo.start() - line_start
        #print('kind="%s";value="%s";column=%d' % (kind,value,column) )
        if kind == 'NUMBER':
            value = float(value) if '.' in value else int(value)
        elif kind == 'ID' and value in keywords:
            kind = value
        elif kind == 'NEWLINE':
            line_start = mo.end()
            line_num += 1
            continue
        elif kind == 'SKIP':
            continue
        elif kind == 'MISMATCH':
            raise RuntimeError(f'{value!r} unexpected on line {line_num}')
        yield Token(kind, value, line_num, column)

statements = '''
    IF quantity THEN
        total := total + price * quantity;
        tax := price * 0.05;
    ENDIF;
'''

for token in tokenize(statements):
    print(token)