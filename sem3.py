import tkinter as tk
from tkinter import ttk
import random
import string


def generate_passwords(first_name, last_name, dob, color):
    base_passwords = [
        first_name + last_name,
        last_name + first_name,
        first_name + dob,
        last_name + dob,
        color + dob,
        first_name + color,
        last_name + color,
        dob + color,
    ]

    special_characters = "!@#$%^&*"
    passwords = []

    for pwd in base_passwords:
        pwd += ''.join(random.choices(string.ascii_uppercase, k=2))
        pwd += ''.join(random.choices(string.digits, k=2))
        pwd += ''.join(random.choices(special_characters, k=1))
        passwords.append(pwd)

    return passwords


def display_passwords(passwords_frame, passwords):
    for widget in passwords_frame.winfo_children():
        widget.destroy()

    for pwd in passwords:
        pwd_entry = tk.Entry(passwords_frame, font=("Arial", 10), fg="#1a1a1a", bg="#ffcc00",
                             width=35, relief="flat", justify="center")
        pwd_entry.insert(0, pwd)
        pwd_entry.config(state="readonly")
        pwd_entry.pack(anchor="center", padx=5, pady=2)


def on_hover(event):
    event.widget.config(bg="#ffcc00", fg="#1a1a1a")


def on_leave(event):
    event.widget.config(bg="#1a1a1a", fg="#ffcc00")


def main():
    root = tk.Tk()
    root.title("Password Generator")
    root.geometry("950x500")
    root.configure(bg="#1a1a1a")

    header = tk.Label(root, text="Password Generator", font=("Arial", 20, "bold"), fg="#ffcc00", bg="#1a1a1a")
    header.pack(side=tk.TOP, pady=(20, 10))

    main_frame = tk.Frame(root, bg="#333333", bd=2, relief="ridge")
    main_frame.pack(padx=20, pady=10, fill="both", expand=True)

    main_frame.columnconfigure(0, weight=1, uniform="equal")
    main_frame.columnconfigure(1, weight=1, uniform="equal")
    main_frame.rowconfigure(0, weight=1)

    input_frame = tk.Frame(main_frame, bg="#1a1a1a", padx=20, pady=20, bd=1, relief="solid")
    input_frame.grid(row=0, column=0, sticky="nswe", padx=(10, 5), pady=10)

    labels = ["First Name", "Last Name", "Date of Birth (DDMMYY)", "Favorite Color"]
    entries = []

    for i, text in enumerate(labels):
        label = tk.Label(input_frame, text=text, font=("Arial", 11), fg="#ffcc00", bg="#1a1a1a")
        label.grid(row=i, column=0, sticky="e", pady=8)

        entry = tk.Entry(input_frame, font=("Arial", 11), fg="#1a1a1a", bg="#ffcc00", width=25, relief="flat",
                         insertbackground="#1a1a1a")
        entry.grid(row=i, column=1, padx=10, pady=8, ipadx=5, ipady=5)
        entries.append(entry)

    generate_button = tk.Button(input_frame, text="Generate Passwords", font=("Arial", 11, "bold"),
                                fg="#1a1a1a", bg="#ffcc00", relief="flat", cursor="hand2",
                                command=lambda: display_passwords(passwords_frame, generate_passwords(
                                    *(e.get() for e in entries))))
    generate_button.grid(row=len(labels), column=0, columnspan=2, pady=20, ipadx=10, ipady=5)

    generate_button.bind("<Enter>", on_hover)
    generate_button.bind("<Leave>", on_leave)

    passwords_frame = tk.Frame(main_frame, bg="#333333", bd=1, relief="solid", padx=10, pady=10)
    passwords_frame.grid(row=0, column=1, sticky="nswe", padx=(5, 10), pady=10)

    password_label = tk.Label(passwords_frame, text="Generated Passwords", font=("Arial", 12, "bold"),
                              fg="#ffcc00", bg="#333333", pady=5)
    password_label.pack(anchor="center", padx=10, pady=(10, 5))

    footer = tk.Label(root, text="Thank you for using the Password Generator", font=("Arial", 10),
                      fg="#ffcc00", bg="#1a1a1a")
    footer.pack(side=tk.BOTTOM, pady=(10, 20))

    root.mainloop()


if __name__ == "__main__":
    main()