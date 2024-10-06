package assignments.contactlist;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;

public class ContactList {
    ArrayList<Contact> contacts;
    HashMap<String, String> lookup_name;
    HashMap<String, String> lookup_email;

    public ContactList() {
        this.contacts = new ArrayList<>();
        this.lookup_name = new HashMap<>();
        this.lookup_email = new HashMap<>();
    } 
    
    public void addContact(Contact contact) {
        this.contacts.add(contact);
        this.lookup_name.put(contact.name, contact.phoneNumber);
        this.lookup_email.put(contact.email, contact.phoneNumber);
    }

    public void removeContact(Contact contact) {
        if (this.lookup_name.containsKey(contact.name)) {
            this.contacts.remove(contact);
            this.lookup_name.remove(contact.name);
            this.lookup_email.remove(contact.email);
        } else {
            System.out.println("Contact not found to remove.");
            System.out.println();
        }
    }

    public void searchContactByName(String name) {
        System.out.println("Search by name:");
        if (this.lookup_name.containsKey(name)) {
            System.out.println("Name: " + name);
            System.out.println("Phone Number: " + this.lookup_name.get(name));
            System.out.println();
        } else {
            System.out.println("Contact not found.");
        }
        System.out.println();
    }

    public void searchContactByEmail(String email) {
        System.out.println("Search by email:");
        if (this.lookup_email.containsKey(email)) {
            System.out.println("Email: " + email);
            System.out.println("Phone Number: " + this.lookup_email.get(email));
            System.out.println();
        } else {
            System.out.println("Contact not found.");
        }
        System.out.println();
    }

    public void updateContactByName(String name, String phoneNumber) {
        if (this.lookup_name.containsKey(name)) {
            this.lookup_name.put(name, phoneNumber);
            System.out.println("Contact updated successfully.");
        } else {
            System.out.println("Contact not found.");
        }
        System.out.println();
    }

    private String extractDomainFromEmail(String email) {
        String[] parts = email.split("@");
        if (parts.length == 2) {
            return parts[1];
        }
        return "";
    }

    public void displayUniqueDomains() {
        HashSet<String> domains = new HashSet<>();
        for (Contact contact : this.contacts) {
            String domain = extractDomainFromEmail(contact.email);
            domains.add(domain);
        }
        for (String domain : domains) {
            System.out.println(domain);
        }
    }

    public void displayAllContacts() {
        this.contacts.sort((contact1, contact2) -> contact1.name.compareTo(contact2.name));
        for (Contact contact : this.contacts) {
            System.out.println("Name: " + contact.name);
            System.out.println("Phone Number: " + contact.phoneNumber);
            System.out.println("Email: " + contact.email);
            System.out.println();
        }
    }
}
