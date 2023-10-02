from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_output.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)

    password = "".join(password_list)
    password_output.insert(0, password)
    pyperclip.copy(password)  # It automatically copies the password to the clipboard
                              # when you click the generate password button

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_docs():
    username = username_input.get()
    website_name = website_input.get()
    user_password = password_output.get()

    if len(username) == 0 or len(user_password) == 0:
        messagebox.showinfo(title="Ooops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website_name,
                                       message=f"These are the details entered: \nWebsite Name: {website_name} "
                                               f"\nEmail: {username} \nPassword: {user_password} \nIs it OK to save? ")
        if is_ok:
            with open("passwords.txt", "a") as file:
                file.write(f"{website_name}  |  {username}  |  {user_password}\n")
                website_input.delete(0, END)
                password_output.delete(0, END)




# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Image
canvas = Canvas(width=250, height=200)
img = PhotoImage(file="logo.png")
canvas.create_image(125, 100, image=img)
canvas.grid(row=0, column=1)

# Labels
website_text = Label(text="Website:")
website_text.grid(row=1, column=0)

username_text = Label(text="Email/Username:")
username_text.grid(row=2, column=0)

password_text = Label(text="Password:")
password_text.grid(row=3, column=0)

# Entries
website_input = Entry(width=41)
website_input.grid(row=1, column=1, columnspan=2)
website_input.focus()

username_input = Entry(width=41)
username_input.grid(row=2, column=1, columnspan=2)
username_input.insert(0, "serhan@gmail.com")  # default value for starting the program when you use usually same mail

password_output = Entry(width=25)
password_output.grid(row=3, column=1)

# Buttons
generate_button = Button(text="Generate Password", width=12, command=generate_password)
generate_button.grid(row=3, column=2)

add_button = Button(text="add", width=40, command=save_docs)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
