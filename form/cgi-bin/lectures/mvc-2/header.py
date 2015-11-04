def render(data):
    return '''
            <html>
                <head>
                  <title>''' + data.get('title') + '''</title>
                </head>
                <body>
                    <h1>''' + data.get('title') + '''</h1>
            '''
