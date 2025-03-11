from flask import Flask, jsonify

app = Flask(__name__)  


students = [
    {'id': 1, 'name': 'dev', 'age': '19', 'dept': 'kssem'},
    {'id': 2, 'name': 'dev', 'age': '19', 'dept': 'kssem'},
    {'id': 3, 'name': 'dev', 'age': '19', 'dept': 'kssem'}
]

@app.route('/students-list', methods=['GET'])
def students_list():
    return jsonify(students)

@app.route('/students-list/<int:student_id>', methods=['GET'])  
def get_student_by_id(student_id):
   
    student = next((s for s in students if s['id'] == student_id), None)

    if student:
        return jsonify(student)
    else:
        return jsonify({'error': 'Student not found'}), 404  

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005, debug=True)