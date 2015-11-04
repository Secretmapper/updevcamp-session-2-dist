#!/usr/local/bin/python3
import cgi
print("Content-type: text/html")

from lib import helpers

print(helpers.render('header', {'title': "Linux"}))
print('''
    <p>Linux</p>
    <p>This is the article for Linux</p>
''')
print(helpers.render('footer'))
