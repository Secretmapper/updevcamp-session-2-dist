#!/usr/local/bin/python3
import cgi
import os

form = cgi.FieldStorage()

print("Content-type: text/html")

# print out our head
print('''
<!DOCTYPE html>
<html lang="en">
<head>
  <title></title>
  <link rel="stylesheet" href="/pure.css">
</head>
<body>''')

# if we have the name and class in our parameters,
# then we know it's a successful form
if('name' in form and 'class' in form):
    print("<p>Right Form</p>")
    print("<pre>")
    for key in form.keys():
        value = form.getvalue(str(key))
        print(key)
        print(value)
        print("\n")
    print("</pre>")
else: #else
    warning = ''
    if os.environ['REQUEST_METHOD'] == 'POST':
        # let's set a warning if we have a post request
        # and have no form input
        warning = '<div class="warning">Your form is invalid!</div>'
    print('''
      <h1>Class Registration</h1>
      <div>''', warning, '''
      <form action="crs3.py" method="POST" class="pure-form pure-form-stacked">
        <label>Name</label>
        <input type="text" name="name"/>
        <label>Class</label>
        <select name="class">
          <option value=""></option>
          <option value="CS 11">CS 11</option>
          <option value="CS 21">CS 21</option>
          <option value="CS 32">CS 32</option>
        </select>
        <input type="submit" value="Go" class="pure-button pure-button-primary"/>
      </form>
    ''')

#print our our 'footer'
print('''
</body>
</html>
''')
