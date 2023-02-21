from flask import Flask

app = Flask(__name__)

@app.route('/')
def page():
    return "<h1>Миссия Колонизация Марса</h1>"

@app.route('/index')
def index():
    return "<h1>И на Марсе будут яблони цвести!</h1>"
@app.route('/promotion')
def pages():
    return """<p>Человечество вырастает из детства.
           Человечеству мала одна планета.<br>
           Мы сделаем обитаемыми безжизненные пока планеты.<br>
           И начнем с Марса!<br>
           Присоединяйся!</p>"""

@app.route('/image_mars')
def mars():
    text = '''<!DOCTYPE html>
<html>
<head>
<title>Привет, Марс!</title>
<link rel="stylesheet" type="text/css" href='static/css/style.css'>
</head>
<body>
<h1 id="welcome">Привет, Марс!</h1>
<img src='static/img/m.jpg'>
<div class="mars">
                      А мы тут компонентами Bootstrap балуемся
                    </div>
<p>Welcome to HTML-CSS-JS.com</p>
<p>Online HTML, CSS and JavaScript editor 
with instant preview.</p>
</body>
</html>'''
    return text


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')