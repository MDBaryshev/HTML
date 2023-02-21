from flask import Flask

app = Flask(__name__)


@app.route('/')
def page():
    return "<h1>Миссия Колонизация Марса</h1>"


@app.route('/index')
def index():
    return "<h2>И на Марсе будут яблони цвести!</h3>"

@app.route('/promotion')
def promotion():
    return """
            <p>Человечество вырастает из детства.<br>
            Человечеству мала одна планета.<br>
            Мы сделаем обитаемыми безжизненные пока планеты.<br>
            И начнем с Марса!</p>

            <h3>Присоединяйся!<h3>"""


@app.route('/astronaut')
def selection():
    f = open('static/pages/forms.html', encoding='utf-8')
    text = f.read()
    text = text.replace('../', 'static/')
    return text


@app.route('/image_mars')
def image_mars():
        text = """
<!DOCTYPE html>
<html>
<head>
<title>Привет, Марс!</title>
</head>
<body>
<h1>Жди нас, Марс!</h1>
<img src="static/img/MARS.png">
<p>Вот она какая красная планета!</p>
</body>
</html>
"""
        return text



if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')


#http://127.0.0.1:8080/index
#http://127.0.0.1:8080/
