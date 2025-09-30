from flask import Flask, jsonify, request
import uuid

app = Flask(__name__)

students = {}

def find_unique_char(name):
    """Encontra a primeira letra não repetida do nome."""
    char_counts = {}
    for char in name.lower():
        char_counts[char] = char_counts.get(char, 0) + 1

    for char in name.lower():
        if char_counts[char] == 1:
            return char
        
        return '_'
    
def add_unique_char(student):
    """Adiciona a primeira letra não repetida ao objeto do estudante."""
    student_with_char = student.copy()
    student_with_char['first_unique_char'] = find_unique_char(student['name'])
    return student_with_char

@app.route('/students', methods=['POST'])
def add_student():
    """Cadastrar um novo estudante."""
    data = request.get_json()
    if not data or 'name' not in data or 'score' not in data:
        return jsonify({'error': 'Nome e nota são obrigatórios.'}), 400
    
    name = data['name']
    score = data['score']

    try:
        score = float(score)
        if not (0 <= score <= 10):
            return jsonify({'error': 'A nota deve estar entre 0 e 10.'}), 400
    except (ValueError, TypeError):
        return jsonify({'error': 'A nota deve ser um número'}), 400
    
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
    """Retorna lista de todos os estudantes."""
    students_list = [add_unique_char(student) for student in students.values()] 
    return jsonify(students_list), 200

@app.route('/students/<string:student_id>', methods=['GET'])
def get_student(student_id):
    """Retorna dados de um estudante especifico pelo ID"""
    student = students.get(student_id)
    if not student:
        return jsonify({'error': 'Estudante não encontrado'}), 404
    
    return jsonify(add_unique_char(student)), 200

if __name__ == '__main__':
    students['1'] = {'id': '1', 'name': 'Gabriel', 'score': 9.5}
    students['2'] = {'id': '2', 'name': 'Maria', 'score': 7.0}
    students['3'] = {'id': '3', 'name': 'Lucas', 'score': 8.2}

    app.run(debug=True)