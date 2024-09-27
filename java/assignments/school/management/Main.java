package assignments.school.management;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        /* create a list of students */
        Student student1 = new Student("John", 20, 1);
        Student student2 = new Student("Jane", 21, 2);
        Student student3 = new Student("Jack", 22, 3);

        /* enroll students in courses */
        List<String> courses = Arrays.asList("Math", "Science", "History");
        student1.enrolledCourses = new ArrayList<>(courses);
        student2.enrolledCourses = new ArrayList<>(courses);
        student3.enrolledCourses = new ArrayList<>(courses);

        /* resign students from courses */
        student1.resignCourses("Math");
        student1.resignCourses("History");
        student3.resignCourses("Science");

        /* set tuition for students */
        student1.setTuition(500);
        System.out.println("Student 1 tuition: " + student1.getTuition());

        student2.setTuition(700);
        System.out.println("Student 2 tuition: " + student2.getTuition());

        student3.setTuition(900);
        System.out.println("Student 3 tuition: " + student3.getTuition());

        /* create a course manager and add students */
        CourseManager courseManager = new CourseManager();
        courseManager.addStudent(student1);
        courseManager.addStudent(student2);
        courseManager.addStudent(student3);

        /* remove one of the students */
        courseManager.removeStudent(student2);

        /* display all students */
        courseManager.displayAllStudents();
    }
}
