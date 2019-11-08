import records

from sql_requests import (
    create_table_student_course_request,
    create_table_course_request,
    create_table_student_request,
    get_students_request,
    create_student_request,
    assign_student_to_course_request,
    get_student_course_last_id,
    get_student_request
)


db = records.Database(database_address)


def create_tables_in_db(db):  # создает таблицы
    db.query(create_table_course_request)
    db.query(create_table_student_request)
    db.query(create_table_student_course_request)


def get_students(db, course_id):  # возвращает студентов определенного курса
    students = db.query(get_students_request, course_id=course_id).as_dict()
    return students


def add_students(db, course_id, students):  # создает студентов и записывает их на курс
    """
    Students format:
        [
            {
                'id': 1,
                'name': 'lol',
                'gpa': Decimal('3.50'),
                'birth': datetime.datetime(2019, 9, 9, 0, 0, tzinfo=psycopg2.tz.FixedOffsetTimezone(offset=180, name=None))
            },
            {
                'id': 2,
                'name': 'kek',
                'gpa': Decimal('4.00'),
                'birth': datetime.datetime(2019, 9, 10, 0, 0, tzinfo=psycopg2.tz.FixedOffsetTimezone(offset=180, name=None))
            }
        ]
    """

    for student in students:
        student_course_last_id = db.query(get_student_course_last_id).first()
        db.query(
            create_student_request,
            id=student["id"],
            name=student["name"],
            gpa=student["gpa"],
            birth=student["birth"],
        )
        db.query(
            assign_student_to_course_request,
            id=student_course_last_id.last_id + 1,
            student_id=student["id"],
            course_id=course_id,
        )


def add_student(db, student):  # просто создает студента
    db.query(
        create_student_request,
        id=student["id"],
        name=student["name"],
        gpa=student["gpa"],
        birth=student["birth"],
    )


def get_student(db, student_id):
    student = db.query(
        get_student_request,
        student_id=student_id
    ).as_dict()
    return student
