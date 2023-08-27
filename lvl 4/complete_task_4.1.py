import sqlite3 as sq

list_of_students = [
    [221, 'Sofia', 1],
    [222, 'Adam', 2],
    [223, 'Lisa', 3],
    [224, 'Ignat', 4]
]

def on_startup():
    sql_start()


def sql_start():
    global base_connect, cur
    base_connect = sq.connect("/Users/idim/PycharmProjects/project_01/lvl_4/teachers1.db")
    cur = base_connect.cursor()
    if base_connect:
        # pass
        print('Data base connected Ok!')
    base_connect.execute(
        'CREATE TABLE IF NOT EXISTS students (student_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, student_name TEXT, school_id INTEGER)')
    base_connect.commit()


def sql_add_student(data):  # Добавить студенат в базу
    cur.execute('INSERT INTO students (student_id, student_name, school_id) VALUES (?,?,?)', tuple(data))
    base_connect.commit()


def sql_read_student(number):  # Выввести инфу по студенту по его ID
    ret = cur.execute('SELECT * FROM students where student_id =?', [number]).fetchone()
    print(f'ID Студента: {ret[0]}\nИмя студента: {ret[1]}\nID школы: {ret[2]}')
    base_connect.commit()


def read_all_students():  # Выввести инфу по всем студентам
    ret = cur.execute('SELECT * FROM students').fetchall()
    for _ in ret:
        print(f'ID Студента: {_[0]}\nИмя студента: {_[1]}\nID школы: {_[2]}\n\n')


def get_student_by_student(number):  # Выввести инфу по студенту по его ID JOIN инфу по школе
    ret = cur.execute('SELECT * FROM students '
                      'JOIN School ON School.School_id = students.school_id '
                      'WHERE student_id =?', [number]).fetchone()
    print(f'ID Студента: {ret[0]}\nИмя студента: {ret[1]}\nID школы: {ret[2]}\nНазвание школы: {ret[4]}\n'
          f'Количество мест: {ret[5]}')
    base_connect.commit()


def get_student_with_teacher(number):  # Выввести инфу по студенту по его ID JOIN инфу по учиталям в данной школе
    ret = cur.execute('SELECT * FROM students '
                      'JOIN Teacher ON Teacher.School_id = students.school_id '
                      'WHERE student_id =?', [number]).fetchall()
    print(f'ID Студента: {ret[0][0]}\nИмя студента: {ret[0][1]}\nID школы: {ret[0][2]}\n')
    for _ in range(len(ret)):
        print(f'ID Учителя: {ret[_][3]}\n'
              f'Имя учителя: {ret[_][4]}\n'
              f'Должность учителя: {ret[_][7]}\n')
    base_connect.commit()


def get_student_by_school(number):  # Выввести инфу по студенту по ID школы JOIN инфу по школе
    ret = cur.execute('SELECT * FROM students '
                      'JOIN School ON School.School_id = students.school_id '
                      'WHERE School.School_id =?', [number]).fetchall()
    for _ in ret:
        print(f'ID Студента: {_[0]}\nИмя студента: {_[1]}\nID школы: {_[2]}\nНазвание школы: {_[4]}\n')
    base_connect.commit()


def sql_delete_student(data):  # Удалить студента из базы
    cur.execute('DELETE FROM students WHERE student_name == ?', (data,))
    base_connect.commit()

