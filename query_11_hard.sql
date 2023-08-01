SELECT students.name AS student_name, teachers.name AS teacher_name, AVG(grades.grade) AS average_grade
FROM students
JOIN grades ON students.id = grades.student_id
JOIN subjects ON grades.subject_id = subjects.id
JOIN teachers ON subjects.teacher_id = teachers.id
WHERE students.name = 'Amber Smith' AND teachers.name = 'Debra Nixon'
GROUP BY students.name, teachers.name;
