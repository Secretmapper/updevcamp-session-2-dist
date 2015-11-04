#!/usr/local/bin/python3
import cgi
print("Content-type: text/html")

import helpers

print(helpers.renderHeader({'title': "Tracks"}))

print('''
    <ul><a href="web.py">Web</ul>
''')

print(helpers.renderFooter())
