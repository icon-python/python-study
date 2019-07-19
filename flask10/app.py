import os

from flask import Flask, request, render_template

from helpers.forms import RegisterForm

app = Flask(__name__)
print(os.urandom(24))
app.config['SECRET_KEY'] = os.urandom(24)


@app.route('/')
def hello_world():
    # 验证
    return 'Hello World!'

class OBJ:
    phone = 'yuze'
    pwd = '123'
    confirm_pwd = '234'

@app.route('/register', methods=['GET', 'POST'])
def register():
    # obj = OBJ()
    b = request.json
    form = RegisterForm(request.json)
    if request.method == 'GET':
        return render_template('register.html',form=form)
    # post, 验证表单内容
    # form = RegisterForm(request.form)
    a = form.validate()

    if form.validate():
        print(form.data)
        return 'success'
    return f'error: {form.errors}'



if __name__ == '__main__':
    app.run()
