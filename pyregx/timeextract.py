# coding=utf-8
#!/usr/bin/env python

import re
import sys
import time
reload(sys)
sys.setdefaultencoding('utf-8')


REGX_ARRY = [('year', '(今|明|后|大后|大前|前)年'),
             ('today', ur'(今|明|后|昨|前|大前|大后)(天|日)'),
             ('pa_m', '((上|下|中)午|(早|晚)上)(?!([0-9]{1}|([1]{1}[0-2]{1}))点)'), ]


now_day = time.time()

WORD_EXTRACT_REGX = ur'|'.join(ur'(?P<%s>%s)' % (pair[0], pair[1]) for pair in REGX_ARRY)
WORD_EXTRACT = re.compile(WORD_EXTRACT_REGX, re.U | re.IGNORECASE).finditer



for i in WORD_EXTRACT("前年的今天，上午10点我去公司了".decode('utf-8')):
    print i.groupdict()
