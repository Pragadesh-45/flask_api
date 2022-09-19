from flask import Flask, jsonify

app = Flask(__name__)

students = [{
    'name': "Fathima",
    'id': "1",
    'class': "1A1",
    'subject': "Environmental Science" },
    {
    'name': "Vijay",
    'id': "2",
    'class': "4A2",
    'subject': "Science" },
    {
    'name': "Antony",
    'id': "3",
    'class': "12A1",
    'subject': "Computer Science" }]


@app.route('/')
def index():
    return "Welcome to the Index page"

if __name__ == "__main__":
    app.run(debug=True)

