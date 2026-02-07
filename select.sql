-- create a table
CREATE TABLE students (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL,age INTEGER,
  grade TEXT,  
  favarite_subject TEXT NOT NULL
);
-- insert some values
INSERT INTO students VALUES (1, 'Ryan', 22,'A','Maths');
INSERT INTO students VALUES (2, 'Joanna',16,'B','Arabic');
-- fetch some values
SELECT * FROM students;