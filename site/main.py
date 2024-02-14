from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index1():
    return render_template('index.html', title='Домашняя страница')


if __name__ == "__main__":
    app.run(host="127.0.0.1", port="8080")