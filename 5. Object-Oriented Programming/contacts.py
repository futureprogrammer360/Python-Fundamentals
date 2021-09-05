class Contact:
    """Contact class"""

    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

    def __repr__(self):
        return self.name + " - " + self.email + " - " + self.phone


class Community:
    """Community class"""

    def __init__(self, name):
        self.name = name
        self.contacts = []

    def __repr__(self):
        string = "Community " + self.name + ":\n"
        for contact in self.contacts:
            string += "  " + str(contact) + "\n"
        return string

    def add(self, new_contact):
        """Add new contact to community"""
        self.contacts.append(new_contact)
        print(str(new_contact) + " added to " + self.name)

    def remove(self, name=None, email=None, phone=None):
        """Remove contact from community"""
        for contact in self.contacts:
            if (contact.name == name) or (contact.email == email) or (contact.phone == phone):
                self.contacts.pop(self.contacts.index(contact))
                print(str(contact) + " removed from " + self.name)
                return contact
        print("No matching contact found.")

    def get(self, name=None, email=None, phone=None):
        """Get contact by name, email, or phone"""
        for contact in self.contacts:
            if (contact.name == name) or (contact.email == email) or (contact.phone == phone):
                return contact
        print("No matching contact found.")


if __name__ == "__main__":
    community1 = Community("Somewhere")
    community1.add(Contact("Brandy Simmerman", "archaeopteryx@overdilution.co.uk", "123456789"))
    community1.add(Contact("Maurice Doukas", "panplegia@calicut.co.uk", "61651651651"))
    community1.add(Contact("Ramonita Difillippo", "onycha@canadite.com", "89794162121"))
    community1.add(Contact("Shari Schwarzenberg", "creesh@apotheoses.org", "1289498413"))
    print()
    print(community1)
    community1.remove(name="Maurice Doukas")
    community1.remove(phone="89794162121")
    community1.remove(email="Non existent email address")
    print()
    print(community1)
