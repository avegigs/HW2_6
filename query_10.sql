SELECT DISTINCT subjects.name, teachers.name
FROM subjects
JOIN teachers ON subjects.teacher_id = teachers.id
JOIN grades ON subjects.id = grades.subject_id
JOIN students ON grades.student_id = students.id
WHERE students.name = 'Victor Miller' AND teachers.name = 'Marie Moore';
