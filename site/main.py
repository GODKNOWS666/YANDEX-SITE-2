from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/index/<title>')
def index1(title):
    return render_template('base.html', title=title)


@app.route('/training/<lst>')
def training(lst):
    profs = ['Автомеханик', 'Агроинженер', 'Программист', 'Клоун', 'Юрист', 'Каскадер', 'Актер']
    return render_template('base_1.html', list=lst, profs=profs)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port="8080")
