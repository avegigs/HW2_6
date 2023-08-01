SELECT students.name AS student_name, subjects.name AS subject_name, grades.grade AS last_grade
FROM students
JOIN grades ON students.id = grades.student_id
JOIN subjects ON grades.subject_id = subjects.id
WHERE students.group_id = 1 AND subjects.name = 'quickly'
AND grades.date = (SELECT MAX(date) FROM grades WHERE subject_id = subjects.id AND student_id = students.id);
