package assignments.university;

public class FullTimeProfessor extends Professor {

    public FullTimeProfessor(String name, Long salary, Department department) {
        super(name, salary, department);
    }

    @Override
    public Long calculateSalary() {
        return salary;
    }

    @Override
    public String toString() {
        return "Professor : " + name + " (Full-time)";
    }
}
