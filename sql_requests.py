create_table_student_request = """
    CREATE TABLE student (
    id SERIAL PRIMARY KEY NOT NULL, 
    name VARCHAR(100) NOT NULL, 
    gpa NUMERIC(10, 2), 
    birth TIMESTAMPTZ)
"""
create_table_course_request = """
    CREATE TABLE course (
    id SERIAL PRIMARY KEY NOT NULL, 
    name VARCHAR(100) NOT NULL)
"""
create_table_student_course_request = """
    CREATE TABLE student_course (
    id SERIAL PRIMARY KEY, 
    student_id INTEGER REFERENCES student(id) NOT NULL, 
    course_id INTEGER REFERENCES course(id) NOT NULL)
"""
get_students_request = """
    SELECT *
    FROM student
    WHERE id IN (
        SELECT student_id
        FROM student_course
        WHERE course_id =:course_id)
"""
create_student_request = """
    INSERT INTO student 
    VALUES (:id, :name, :gpa, :birth)
"""
get_student_course_last_id = """
    SELECT max(id) as last_id
    FROM student_course
"""
assign_student_to_course_request = """
    INSERT INTO student_course
    VALUES (:id, :student_id, :course_id) 
"""
get_student_request = """
    SELECT *
    FROM student
    WHERE id =:student_id
"""
