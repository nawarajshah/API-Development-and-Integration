from flask import Flask, jsonify

app = Flask(__name__)


students = [
    {"roll_no": 1, "name": "John Doe", "age": 18, "grade": "12th grade"},
    {"roll_no": 2, "name": "Ram Sharma", "age": 17, "grade": "11th grade"},
    {"roll_no": 3, "name": "Sita Giri", "age": 16, "grade": "10th grade"},

]


@app.route("/students", methods=["GET"])
def get_students():
    return jsonify({"students": students})


@app.route("/students/<int:roll_no>", methods=["GET"])
def get_student(roll_no):
    for student in students:
        if student['roll_no'] == roll_no:
            return jsonify(student)
    return jsonify({"message": "student not found"})


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
