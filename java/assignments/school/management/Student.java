package assignments.school.management;
import assignments.school.Person;
import java.util.ArrayList;

public class Student extends Person {
    int studentId;

    public int getStudentId() {
        return studentId;
    }
    ArrayList<String> enrolledCourses;
    double tuition;

    public Student(String name, int age, int studentId) {
        super(name, age);
        this.studentId = studentId;
    }

    public void enrollCourses(ArrayList<String> courses) {
        this.enrolledCourses = courses;
    }

    public void enrollCourses(String course) {
        this.enrolledCourses.add(course);
    }

    public void resignCourses(String course) {
        this.enrolledCourses.remove(course);
    }

    public double getTuition() {
        return this.tuition;
    }

    public void setTuition(double tuition) {
        this.tuition = tuition * this.enrolledCourses.size();
    }
}
