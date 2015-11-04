#!/usr/local/bin/python3
import cgi
print("Content-type: text/html")

form = cgi.FieldStorage()

print('''
<html>
    <head>
      <title>CSI CGI</title>
    </head>
    <body>
''')

print("<p>Form</p>")
print("<pre>")
for key in form.keys():
    value = form.getvalue(str(key))
    print(key)
    print(value)
    print("\n")
print("</pre>")

print('''
    </body>
</html>
''')
