#!/usr/local/bin/python3
import cgi
print("Content-type: text/html")

import header

print('''
    <h1>Tracks</h1>
    <ul><a href="tracks.py">Tracks</ul>
    <ul><a href="resources.py">Resources</ul>
''')

import footer
