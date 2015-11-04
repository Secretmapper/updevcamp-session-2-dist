#!/usr/local/bin/python3
import cgi
print("Content-type: text/html")

print('''
<!DOCTYPE html>
<html>
<head>
    <title>Web</title>
</head>
    <body>
        <h1>Web</h1>
        <ul><a href="setup.py">Setup</ul>
        <ul><a href="mvc.py">MVC</ul>
    </body>
</html>
''')
