from typing import List, Dict, Optional, Union, Tuple


# 1. Add type hints to this function that processes student grades
def calculate_grade_statistics(grades, student_name):
    """
    Calculate statistics for a student's grades.
    Should accept a list of numbers and a student name.
    Returns a tuple of (average_grade, passing_status, letter_grade)
    """
    if not grades:
        return (0.0, False, 'F')

    average = sum(grades) / len(grades)
    passing = average >= 60

    if average >= 90:
        letter = 'A'
    elif average >= 80:
        letter = 'B'
    elif average >= 70:
        letter = 'C'
    elif average >= 60:
        letter = 'D'
    else:
        letter = 'F'

    return (average, passing, letter)


# 2. Add type hints to this function that processes student records
def update_student_record(current_data, new_grades, new_attendance):
    """
    Updates a student's record with new grades and attendance.
    current_data should be a dictionary with 'grades' and 'attendance' keys
    new_grades should be a list of numbers
    new_attendance should be a list of booleans
    Returns the updated record dictionary
    """
    if not current_data:
        current_data = {'grades': [], 'attendance': []}

    current_data['grades'].extend(new_grades)
    current_data['attendance'].extend(new_attendance)

    return current_data


# 3. Add type hints to this function that finds students by grade
def find_students_by_grade(students, min_grade, max_grade):
    """
    Finds all students with average grades in the specified range.
    students should be a dictionary of student_id -> list of grades
    min_grade and max_grade should be numbers
    Returns a list of student IDs
    """
    matching_students = []

    for student_id, grades in students.items():
        if not grades:
            continue
        average = sum(grades) / len(grades)
        if min_grade <= average <= max_grade:
            matching_students.append(student_id)

    return matching_students
