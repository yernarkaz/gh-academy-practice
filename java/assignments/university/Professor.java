package assignments.university;

import java.util.ArrayList;
import java.util.List;

public abstract class Professor implements Teach, Evaluate {
    String name;
    Long salary;
    Department department;
    List<Course> courses;

    public Professor(String name, Long salary, Department department) {
        this.name = name;
        this.salary = salary;
        this.department = department;
        this.courses = new ArrayList<>(10);
    }

    public String getName() {
        return name;
    }

    public Long getSalary() {
        return salary;
    }

    public Department getDepartment() {
        return department;
    }

    public List<Course> getCourses() {
        return courses;
    }

    public void setDepartment(Department department) {
        this.department = department;
    }

    public void setName(String name) {
        this.name = name;
    }

    public void setSalary(Long salary) {
        this.salary = salary;
    }

    public void teachCourse(Course course) {
        courses.add(course);
    }
    public abstract Long calculateSalary();

    @Override
    public String conductLecture() {
        StringBuilder sb = new StringBuilder();
        for (Course course : this.getCourses()) {
            sb.append("Teaching: ").append(course).append(",");
        }
        return sb.toString();
    }

    @Override
    public void gradeStudent(Student student, Course course, Grade grade) {
        course.assignGrade(student, grade);
    }
}