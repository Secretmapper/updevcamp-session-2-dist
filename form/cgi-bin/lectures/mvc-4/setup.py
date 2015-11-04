#!/usr/local/bin/python3
import cgi
print("Content-type: text/html")

from lib import helpers

print(helpers.render('header', {'title': "Setup"}))
print('''
        <p>Web Setup</p>
        <p>This is the article for Web Setup</p>
''')
print(helpers.render('footer'))
