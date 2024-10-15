package assignments.university;

import java.util.List;

public class Main {
    public static void main(String[] args) {
        // Create a new department
        Department department = new Department("Computer Science");

        // Create professors
        Professor professor1 = new FullTimeProfessor("John Doe", 100000L, department);
        Professor professor2 = new AdjunctProfessor("Jane Doe", 5000L, department);

        // Add professors to the department 
        department.addProfessor(professor1.name, professor1);
        department.addProfessor(professor2.name, professor2);

        // Create courses
        Course course1 = new Course("CS101", "Introduction to Computer Science", 3);
        Course course2 = new Course("CS102", "Data Structures", 3);

        // Add courses to the department
        department.addCourse(course1.name, course1);
        department.addCourse(course2.name, course2);

        // Assign professors to courses
        professor1.teachCourse(course1);
        professor2.teachCourse(course2);

        // Create students
        Student student1 = new Student("Alice", 123L);
        Student student2 = new Student("Bob", 456L);
        Student student3 = new Student("Charlie", 789L);
        Student student4 = new Student("David", 101L);

        // Register students for courses
        student1.enrollInCourse(course1);
        student2.enrollInCourse(course1);
        student3.enrollInCourse(course2);
        student4.enrollInCourse(course2);

        // Assign grades to students
        professor1.gradeStudent(student4, course2, new Grade(90));
        professor2.gradeStudent(student1, course1, new Grade(85));
        professor2.gradeStudent(student2, course1, new Grade(90));
        professor1.gradeStudent(student3, course2, new Grade(95));

        // View a list of student's grade report
        Professor professor = professor1;
        System.out.println("Department: " + department.getName());
        System.out.println("Professor: " + professor.getName());
        for (Course course: professor.getCourses()) {
            System.out.println("Teaching: " + course.getName());
            List<Student> students = course.getStudents();
            System.out.println("Students: " + String.join(", ", students.stream().map(Student::getName).toArray(String[]::new)));
            for (Student student: students) {
                Grade grade = course.getGrades().get(student);
                System.out.println("Grade report for: " + student.getName());
                System.out.println(" - " + course.getName() + ": " + grade.getScore());
            }
            System.out.println();
        }
    }
}
