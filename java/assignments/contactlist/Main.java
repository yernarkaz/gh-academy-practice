package assignments.contactlist;

public class Main {
    public static void main(String[] args) {
        // Create a new ContactList object
        ContactList contactList = new ContactList();

        // Add some contacts to the contact list
        contactList.addContact(new Contact("John Doe", "1234567890", "johndoe@gmail.com"));
        contactList.addContact(new Contact("Jane Doe", "0987654321", "janedoe@yahoo.com"));
        contactList.addContact(new Contact("Black Smith", "1234567890", "blacksmith@abc.com"));
        contactList.addContact(new Contact("White Smith", "0987654321", "whitesmith@gmail.com"));

        // Remove a contact from the contact list
        Contact contactToRemove = contactList.contacts.get(0);
        contactList.removeContact(contactToRemove);

        // Search for a contact in the contact list
        contactList.searchContactByName("John Doe");
        contactList.searchContactByName("Black Smith");
        contactList.searchContactByEmail("whitesmith@gmail.com");

        // Update phone number of a contact in the contact list
        contactList.updateContactByName("Jane Smith", "011235813");

        // Display all contacts in the contact list
        contactList.displayAllContacts();

        // Display unique domains in the contact list
        contactList.displayUniqueDomains();
    }
}
