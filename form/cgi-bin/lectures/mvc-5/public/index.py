#!/usr/local/bin/python3
import cgi
print("Content-type: text/html")

## This block of code just sets the dir path
## one level up (so we can access lib and templates
# set package to ..
import sys
import os
PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))
# set package to .. end

from lib import helpers

print(helpers.render('header', {'title': "UP DevCamp"}))

print('''
    <ul><a href="tracks.py">Tracks</ul>
    <ul><a href="resources.py">Resources</ul>
''')

print(helpers.render('footer'))
