#!/usr/local/bin/python3
import cgi
print("Content-type: text/html")

import header

print('''
        <h1>Resources</h1>
        <ul><a href="python.py">Python</ul>
        <ul><a href="linux.py">Linux</ul>
''')

import footer
