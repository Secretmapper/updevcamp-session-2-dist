#!/usr/local/bin/python3
import cgi
print("Content-type: text/html")

import helpers

print(helpers.render('header', {'title': "UP DevCamp"}))

print('''
    <ul><a href="tracks.py">Tracks</ul>
    <ul><a href="resources.py">Resources</ul>
''')

print(helpers.render('footer'))
