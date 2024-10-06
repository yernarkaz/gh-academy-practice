package assignments.contactlist;

public class Contact {
    public String name;
    public String phoneNumber;
    public String email;

    public Contact(String name, String phoneNumber, String email) {
        this.name = name;
        this.phoneNumber = phoneNumber;
        this.email = email;
    }

    @Override
    public String toString() {
        return "Name: " + this.name + "\n" 
            + "Phone number: " + this.phoneNumber + "\n"
            + "Email: " + this.email;
    }
}
