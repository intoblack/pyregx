#coding=utf-8
#!/usr/bin/env python


regx_dict = {
    'CLEAR_NUM' : '(-|\\+)?\d*\d',
    'CLEAR_WORD' : '[\w\'-_]*[\w\'-_\']',
    'ANY_WORD' : '(.+?)',
    'QQ' : '^\d\d{3,10}$',
    'MAIL' : '\w+([-+.]\w+)*@\w+([-.]\w+)*.\w+([-.]\w+)*',
    'IP' : '\d{1,3}\\.\d{1,3}\\.\d{1,3}\\.\d{1,3}',
    'PHONE' : '^((\d{3,4})|\d{3,4}-)?\d{7,8}$',
    'MOBILE' : '^1\d{10}'
}
