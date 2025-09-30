from flask import Flask, jsonify, request
import uuid

app = Flask(__name__)

students = {}

def find_unique_char(name):
    """Find the first not repeated letter in the name."""
    char_counts = {}
    for char in name.lower():
        char_counts[char] = char_counts.get(char, 0) + 1

    for char in name.lower():
        if char_counts[char] == 1:
            return char
        
    return '_'
    
def add_unique_char(student):
    """Add the first not repeated letter to the student object."""
    student_with_char = student.copy()
    student_with_char['first_unique_char'] = find_unique_char(student['name'])
    return student_with_char

@app.route('/students', methods=['POST'])
def add_student():
    """Register new student."""
    data = request.get_json()
    if not data or 'name' not in data or 'score' not in data:
        return jsonify({'error': 'Score and name are mandatoy.'}), 400
    
    name = data['name']
    if not name or not name.strip():
        return jsonify({'error': 'Name cannot be empty.'}), 400
    score = data['score']

    try:
        score = float(score)
        if not (0 <= score <= 10):
            return jsonify({'error': 'Grade must be between 0 and 10.'}), 400
    except (ValueError, TypeError):
        return jsonify({'error': 'Grade must be a number.'}), 400
    
    student_id = str(uuid.uuid4())
    new_student = {
        'id': student_id,
        'name': name,
        'score': score
    }
    students[student_id] = new_student

    return jsonify(new_student), 201

@app.route('/students', methods=['GET'])
def get_all_students():
    """Return a list of all students."""
    students_list = [add_unique_char(student) for student in students.values()] 
    return jsonify(students_list), 200

@app.route('/students/<string:student_id>', methods=['GET'])
def get_student(student_id):
    """Return data from a specific student ID."""
    student = students.get(student_id)
    if not student:
        return jsonify({'error': 'Student not found.'}), 404
    
    return jsonify(add_unique_char(student)), 200

if __name__ == '__main__':
    students['1'] = {'id': '1', 'name': 'Gabriel', 'score': 9.5}
    students['2'] = {'id': '2', 'name': 'Maria', 'score': 7.0}
    students['3'] = {'id': '3', 'name': 'Lucas', 'score': 8.2}

    app.run(debug=True)