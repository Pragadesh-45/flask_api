from flask import Flask, jsonify

app = Flask(__name__)


students = [{
    'name': "Fathima",
    'student_id': "1",
    'class': "1A1",
    'subject': "Environmental Science" },
    {
    'name': "Vijay",
    'student_id': "2",
    'class': "4A2",
    'subject': "Science" },
    {
    'name': "Antony",
    'student_id': "3",
    'class': "12A1",
    'subject': "Computer Science" }]


@app.route('/')
def index():
    return "Welcome To Index Page"

@app.route("/students", methods = ['GET'])
def get():
    return jsonify({'Students':students})

@app.route("/students/<int:student_id>", methods = ['GET'])
def get_student(student_id):
    return jsonify({'Student':students[student_id]})

@app.route("/students", methods=['POST'])
def create ():
    student = {
    'name': "Pablo Emilio Escobar Gaviria",
    'student_id': "4",
    'class': "12A1",
    'subject': "Drugs" }

    students.append(student)
    return jsonify({'Created': student})


@app.route("/students/<int:student_id>", methods = ['PUT'])
def student_update(student_id):
    students[student_id]['subject'] = "Biology"
    return jsonify({'student': students[student_id]})

@app.route("/students/<int:student_id>", methods = ['DELETE'])
def delete(student_id):
    students.remove(students[student_id])
    return jsonify({'result': True})


if __name__ == "__main__":
    app.run(debug=True)
