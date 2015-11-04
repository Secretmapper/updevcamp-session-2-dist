#!/usr/local/bin/python3
import cgi
print("Content-type: text/html")

from lib import helpers

print(helpers.render('header', {'title': "Tracks"}))
print('''
    <ul><a href="web.py">Web</ul>
''')
print(helpers.render('footer'))
