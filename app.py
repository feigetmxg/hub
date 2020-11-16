from flask import Flask, render_template, request
from wtforms import Form, TextAreaField, validators

app = Flask(__name__)


class Mine(Form):
    my_text = TextAreaField('',
                            [validators.DataRequired(),
                             validators.length(min=15)])


@app.route('/')
def index():
    form = Mine(request.form)
    return render_template('index.html', form=form)


@app.route('/results', methods=['POST'])
def results():
    form = Mine(request.form)
    if request.method == 'POST' and form.validate():
        item = request.form['my_text']
        return render_template('results.html',
                               content=item)
    return render_template('index.html', form=form)


if __name__ == '__main__':
    app.run(debug=True,
            host="172.17.4.207",
            port=8888)
