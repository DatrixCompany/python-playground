from flask import Flask
app = Flask(__name__)
print(app)


@app.route('/')
def hello_world():
    return 'Hello, World!!!!'


@app.route('/ya')
def helloo_world():
    return 'yaaaa Hello, World!!!!'


@app.route('/ya/<name>')
def helloo_worlds(name):
    return f'yaaaa Hello, {name}!!!!'

# export FLASK_APP=server/first.py
# run command: flask run
