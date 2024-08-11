from app import app

@app.route("/")
@app.route("/index")
def index():
    user = {"username": "Andrew"}
    return '''
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Home Page - Blog</title>
    </head>
    <body>
        <h1>Hello, ''' + user["username"] + '''!</h1>
    </body>
</html>
'''