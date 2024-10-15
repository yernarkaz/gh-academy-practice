package assignments.university;

import java.util.List;
import java.util.ArrayList;
import java.util.HashMap;

public class Course {
    String name;
    String description;
    Integer credits;
    HashMap<Student, Grade> grades;
    List<Student> students;
    
    public Course(String name, String description, Integer credits) {
        this.name = name;
        this.description = description;
        this.credits = credits;
        this.students = new ArrayList<>(10);
        this.grades = new HashMap<>(10);
    }

    public String getName() {
        return name;
    }

    public String getDescription() {
        return description;
    }

    public Integer getCredits() {
        return credits;
    }

    public List<Student> getStudents() {
        return students;
    }

    public HashMap<Student, Grade> getGrades() {
        return grades;
    }

    public void addStudent(Student student) {
        students.add(student);
    }

    public void assignGrade(Student student, Grade grade) {
        grades.put(student, grade);
    }
}