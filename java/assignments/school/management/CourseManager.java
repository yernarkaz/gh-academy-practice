package assignments.school.management;
import java.util.ArrayList;

public class CourseManager {
    ArrayList<Student> students;

    public CourseManager() {
        this.students = new ArrayList<>(10);
    }

    public CourseManager(ArrayList<Student> students) {
        this.students = students;
    }

    public void addStudent(Student student) {
        this.students.add(student);
    }

    public void removeStudent(Student student) {
        this.students.remove(student);
    }

    public void displayAllStudents() {
        for (Student student : this.students) {
            student.displayDetails();
        }
    }
}
