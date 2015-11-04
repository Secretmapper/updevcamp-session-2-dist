def render(data):
    print('''
        <form action="index.py" method="POST">
        <p>PAGE IS INVALID''' + str(data.get('invalid')) + '''</p>
            NAME:<input type="text" name="name"><br>
            URL: <input type="text" name="url">
            <input type="submit">
        </form>
    ''')
