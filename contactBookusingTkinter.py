import tkinter as tk
from tkinter import messagebox

class ContactBook(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Contact Book")
        self.geometry("400x300")

        self.contacts = []

        self.create_widgets()

    def create_widgets(self):
        # Create a frame to hold all the widgets
        frame = tk.Frame(self, borderwidth=2, relief="groove", highlightbackground="maroon")
        frame.pack(expand=True, fill="both", padx=10, pady=(10, 0))  # Adjusting vertical padding

        self.label_name = tk.Label(frame, text="Name:")
        self.label_name.pack(pady=5)

        self.entry_name = tk.Entry(frame)
        self.entry_name.pack(pady=5)

        self.label_phone = tk.Label(frame, text="Phone:")
        self.label_phone.pack(pady=5)

        self.entry_phone = tk.Entry(frame)
        self.entry_phone.pack(pady=5)

        self.label_email = tk.Label(frame, text="Email:")
        self.label_email.pack(pady=5)

        self.entry_email = tk.Entry(frame)
        self.entry_email.pack(pady=5)

        self.label_address = tk.Label(frame, text="Address:")
        self.label_address.pack(pady=5)

        self.entry_address = tk.Entry(frame)
        self.entry_address.pack(pady=5)

        self.button_add = tk.Button(frame, text="Add Contact", command=self.add_contact)
        self.button_add.pack(pady=5)

        self.button_view = tk.Button(frame, text="View Contacts", command=self.view_contacts)
        self.button_view.pack(pady=5)

        self.label_search = tk.Label(frame, text="Search:")
        self.label_search.pack(pady=5)

        self.entry_search = tk.Entry(frame)
        self.entry_search.pack(pady=5)

        # Change the color of the "Search" button to maroon
        self.button_search = tk.Button(frame, text="Search", command=self.search_contact, bg="maroon", fg="white")
        self.button_search.pack(pady=5)

    def add_contact(self):
        name = self.entry_name.get()
        phone = self.entry_phone.get()
        email = self.entry_email.get()
        address = self.entry_address.get()

        if name and phone:
            contact = {
                "name": name,
                "phone": phone,
                "email": email,
                "address": address
            }
            self.contacts.append(contact)
            messagebox.showinfo("Success", "Contact added successfully!")
            self.clear_entries()
        else:
            messagebox.showerror("Error", "Name and phone number are required fields.")

    def view_contacts(self):
        if self.contacts:
            contact_list = "\n".join([f"{contact['name']}: {contact['phone']}" for contact in self.contacts])
            messagebox.showinfo("Contacts", contact_list)
        else:
            messagebox.showinfo("Contacts", "No contacts available.")

    def search_contact(self):
        query = self.entry_search.get().lower()
        if query:
            search_results = [contact for contact in self.contacts if query in contact['name'].lower() or query in contact['phone']]
            if search_results:
                search_list = "\n".join([f"{contact['name']}: {contact['phone']}" for contact in search_results])
                messagebox.showinfo("Search Results", search_list)
            else:
                messagebox.showinfo("Search Results", "No matching contacts found.")
        else:
            messagebox.showerror("Error", "Please enter a search query.")

    def clear_entries(self):
        self.entry_name.delete(0, tk.END)
        self.entry_phone.delete(0, tk.END)
        self.entry_email.delete(0, tk.END)
        self.entry_address.delete(0, tk.END)

if __name__ == "__main__":
    app = ContactBook()
    app.mainloop()
