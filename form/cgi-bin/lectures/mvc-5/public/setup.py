#!/usr/local/bin/python3
import cgi
print("Content-type: text/html")

import sys
import os
PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))


from lib import helpers

print(helpers.render('header', {'title': "Setup"}))
print('''
        <p>Web Setup</p>
        <p>This is the article for Web Setup</p>
''')
print(helpers.render('footer'))
