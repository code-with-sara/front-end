from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

# Sample in-memory database
students = [
    {"id": 1, "name": "Alice", "age": 22},
    {"id": 2, "name": "Bob", "age": 25}
]

# 📌 Route to serve HTML frontend
@app.route('/')
def index():
    return render_template('index.html')

# 📌 GET: Retrieve all students
@app.route('/students', methods=['GET'])
def get_students():
    return jsonify(students)

# POST: Add a new student
@app.route('/students', methods=['POST'])
def add_student():
    data = request.json
    new_student = {"id": len(students) + 1, "name": data["name"], "age": data["age"]}
    students.append(new_student)
    return jsonify(new_student), 201

#PUT: Update an existing student
@app.route('/students/<int:id>', methods=['PUT'])
def update_student(id):
    student = next((s for s in students if s["id"] == id), None)
    if not student:
        return jsonify({"error": "Student not found"}), 404
    data = request.json
    student["name"] = data.get("name", student["name"])
    student["age"] = data.get("age", student["age"])
    return jsonify(student)

# DELETE: Remove a student
@app.route('/students/<int:id>', methods=['DELETE'])
def delete_student(id):
    global students
    students = [s for s in students if s["id"] != id]
    return jsonify({"message": "Student deleted"}), 200

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True, port = 5001)
