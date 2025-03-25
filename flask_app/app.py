from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return '<p>Hello, Wordld!</p>'
    elif request.method == 'POST':
        pass


if __name__ == '__main__':
    app.run(debug=True)