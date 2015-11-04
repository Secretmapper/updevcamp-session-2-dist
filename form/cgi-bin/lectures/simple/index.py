#!/usr/local/bin/python3
import cgi
print("Content-type: text/html")

print('''
<!DOCTYPE html>
<html>
<head>
    <title>UP DevCamp</title>
</head>
    <body>
        <h1>UP DevCamp</h1>
        <ul><a href="tracks.py">Tracks</ul>
        <ul><a href="resources.py">Resources</ul>
    </body>
</html>
''')
