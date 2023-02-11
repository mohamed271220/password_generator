from tkinter import *
import random
from tkinter import messagebox
import json

# import pyperclip

FONT_NAME = "Courier"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    pass_entry.delete(0, 'end')
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    passwoed_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    passwoed_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    passwoed_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = passwoed_letters + passwoed_symbols + passwoed_numbers
    random.shuffle(password_list)

    password = "".join(password_list)
    # ===
    # for char in password_list:
    #     password += char

    print(f"Your password is: {password}")
    pass_entry.insert(0, password)
    # pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get()
    email = email_entry.get()
    password = pass_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        },
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title='oops', message="Please fill your info ")
    else:
        is_ok = messagebox.askokcancel(title=website,
                                       message=f'are you sure you want save this info for your {website} ?')
        if is_ok:
            try:
                with open("data.json", "r") as data_file:
                    # Reading old data
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                # Updating old data with new data
                data.update(new_data)

                with open("data.json", "w") as data_file:
                    # Saving updated data
                    json.dump(data, data_file, indent=4)
            finally:
                website_entry.delete(0, END)
                pass_entry.delete(0, END)


# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = website_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('password generator')
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
lock_pic = PhotoImage(file="logo.png")
canvas.create_image(100, 90, image=lock_pic)
canvas.grid(column=2, row=2)

label_website = Label(text="Website:", font=(FONT_NAME, 19))
label_website.grid(column=1, row=3)
website_entry = Entry(width=35)
website_entry.focus()
website_entry.grid(column=2, row=3)

label_email = Label(text="Email address:", font=(FONT_NAME, 19))
label_email.grid(column=1, row=4)
email_entry = Entry(width=55)
email_entry.insert(0, 'example@gmail.com')
email_entry.grid(column=2, row=4, columnspan=3)

label_pass = Label(text="Password:", font=(FONT_NAME, 19))
label_pass.grid(column=1, row=5)
pass_entry = Entry(width=35)
pass_entry.grid(column=2, row=5)

search_button = Button(text="Search", width=13, command=find_password)
search_button.grid(column=4,row=3)

gen_button = Button(text='Generate Password', command=password_generator)
gen_button.grid(column=4, row=5)

add_button = Button(text='Add', width=45, command=save_password)
add_button.grid(column=2, row=6, columnspan=3)

window.mainloop()
