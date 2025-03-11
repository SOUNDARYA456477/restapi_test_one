from flask import Flask, jsonify

app = Flask('__name__')


@app.route('/students-list')
def students_list():
    students=[{
        'student_name': 'std1',
        'age':21,
        "email":'sound@gmail.com'
   },
        {'student_name': 'std2',
        'age':22,
        "email":'sound@gmail.com'
   },
        {'student_name': 'std3',
        'age':23,
        "email":'sound@gmail.com'
   }
]
    return jsonify(students)

if __name__ == '__main__':
    app.run(
        host='127.0.0.1',
        port=5010,
        debug=True
    )