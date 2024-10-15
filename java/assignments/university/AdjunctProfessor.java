package assignments.university;

public class AdjunctProfessor extends Professor {

    public AdjunctProfessor(String name, Long salary, Department department) {
        super(name, salary, department);
    }

    @Override
    public Long calculateSalary() {
        return salary * this.courses.size();
    }

    @Override
    public String toString() {
        return "Professor : " + name + " (Part-time)";
    }
}
