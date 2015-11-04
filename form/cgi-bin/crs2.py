#!/usr/local/bin/python3
import cgi

print("Content-type: text/html")

print('''
<!DOCTYPE html>
<html lang="en">
<head>
  <title></title>
  <link rel="stylesheet" href="/pure.css">
</head>
<body>
  <h1>Class Registration</h1>
  <form action="register2.py" method="POST" class="pure-form pure-form-stacked">
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
</body>
</html>
''')
