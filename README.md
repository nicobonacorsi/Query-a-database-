# Query-a-database-

One of the mechanisms used to store and manage large quantities of 
data is databases. There are many types of databases, but the one that
has revolutionized the sector is the database organized according to
the relational model theorized by Codd half a century ago. According
to this model, the data are arranged in tables in direct relation, to
optimize memory requirements, promote data consistency and minimize
errors.

We need to design a set of functions that implements a simple
relational database for a training school, with four tables, namely
students, teachers, courses, and exams.The
tables are implemented as lists of dictionaries (see, for example, the
file small_students.json) and have the following structures:
   - students: keys stud_code, stud_name, stud_surname, stud_email
   - teachers: keys teach_code, teach_name, teach_surname, teach_email
   - courses: keys course_code, course_name, teach_code
   - exams: keys exam_code, course_code, stud_code, date, grade.
The relationship between the tables implies that each row in each of
the tables have a reference to another table: an exam (exam_code)
corresponds to a grade given by the teacher (teach_code) to a student
(stud_code) for having taken an exam of a given course (course_code)
in a certain date. Every student can have taken several exams. Every
teacher can be responsible for several courses. However, exactly
one teacher is responsible for every course. We must realize some functions to query databases of different sizes.
Then, every function always requires a 'dbsize' string type parameter, which can assume the values 'small,' 'medium,' and 'large.'
The functions are:

    - student_average(stud_code, dbsize), which receives the code of
      a student and returns the average of the grades of the exams
      taken by the student.

    - course_average(course_code, dbsize), which receives the code of
      a course and returns the average grade of the exams for that
      course, taken by all students.

    - teacher_average(teach_code, dbsize), which receives the code of
      a teacher and returns the average grade for all the exams taken
      in all of the teacher's courses.

    - top_students(dbisze), which returns the list of the 'stud_code's
      of those students with an average of taken exams, greater than
      or equal to 28. The stud_codes are sorted in descending order by
      average grade and, in case of a tie, in lexicographic order by
      the student's last name and first name, finally the stud_code
      in ascending order.

    - print_recorded_exams(stud_code, fileout, dbsize), which receives a
      stud_code of a student and saves in fileout the list of the exams
      taken by that student. The rows are sorted in ascending
      order by date of exam taken and, in case of the same date, by
      alphabetical order of the exam names. The file has an initial line
      with the text
"Exams taken by student <stud_surname> <stud_name>, student number <stud_code>",
      while the following lines have the following structure:
"<course_name>\t<date>\t<grade>",
      where the fields are aligned with the longest course name (i.e. all
      dates and grades are vertically aligned). The function returns the
      number of exams taken by the student.

    - print_top_students(fileout, dbsize), which saves in fileout a
      row for each student with an average grade greater than or equal
      to 28. The rows in the file are in descending order by average
      grade and, in case of a tie, in lexicographic order by the
      student's last name and first name.
      The rows in the file have the following structure:
"<stud_surname> <names>\t<average>",
      where the average values are vertically aligned for all rows. The
      function returns the number of rows saved in the file.

    - print_exam_record(exam_code, fileout, dbsize), which receives an
      exam_code of an exam and saves in fileout the information about that
      exam, using the following formula
"The student <stud_surname> <stud_name>, student number <stud_code>, took on <date> the <course_name> exam with the teacher <teach_surname> <teach_name> with grade <grade>."
      The function returns the exam grade associated with the exam_code
      received as input.
