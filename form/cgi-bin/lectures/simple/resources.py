#!/usr/local/bin/python3
import cgi
print("Content-type: text/html")

print('''
<!DOCTYPE html>
<html>
<head>
    <title>Resources</title>
</head>
    <body>
        <h1>Resources</h1>
        <ul><a href="python.py">Python</ul>
        <ul><a href="linux.py">Linux</ul>
    </body>
</html>
''')
