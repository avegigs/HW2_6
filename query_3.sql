SELECT subjects.name, AVG(grades.grade) as average_grade
FROM subjects
JOIN grades ON subjects.id = grades.subject_id
GROUP BY subjects.id;
