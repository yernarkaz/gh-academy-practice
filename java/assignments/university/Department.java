package assignments.university;

import java.util.HashMap;


public class Department {
    String name;
    HashMap<String, Professor> professors;
    HashMap<String, Course> courses;

    public Department(String name) {
        this.name = name;
        this.professors = new HashMap<>(10);
        this.courses = new HashMap<>(10);
    }

    public String getName() {
        return this.name;
    }

    public HashMap<String, Professor> getProfessors() {
        return this.professors;
    }

    public HashMap<String, Course> getCourses() {
        return this.courses;
    }

    public void addProfessor(String name, Professor professor) {
        this.professors.put(name, professor);
    }

    public void addCourse(String name, Course course) {
        this.courses.put(name, course);
    }
}