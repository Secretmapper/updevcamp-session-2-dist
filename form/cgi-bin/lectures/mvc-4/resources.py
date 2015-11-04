#!/usr/local/bin/python3
import cgi
print("Content-type: text/html")

from lib import helpers

print(helpers.render('header', {'title': "Resources"}))
print('''
    <ul><a href="python.py">Python</ul>
    <ul><a href="linux.py">Linux</ul>
''')
print(helpers.render('footer'))
