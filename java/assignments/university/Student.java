package assignments.university;

import java.util.List;
import java.util.ArrayList;

public class Student {
    String name;
    Long id;
    List<Course> courses;

    public Student(String name, Long id) {
        this.name = name;
        this.id = id;

        this.courses = new ArrayList<>(10);
    }

    public String getName() {
        return name;
    }

    public Long getId() {
        return id;
    }

    public List<Course> getCourses() {
        return courses;
    }

    public void enrollInCourse(Course course) {
        this.courses.add(course);
        course.addStudent(this);
    }
}
