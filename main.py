from tkinter import *
import random
from tkinter import messagebox
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
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title='oops', message="Please fill your info ")
    else:
        is_ok = messagebox.askokcancel(title=website,
                                       message=f'are you sure you want save this info for your {website} ?')
        if is_ok:
            with open("file.txt", "a") as f:
                f.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0, 'end')
                email_entry.delete(0, 'end')
                pass_entry.delete(0, 'end')


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
website_entry = Entry(width=55)
website_entry.focus()
website_entry.grid(column=2, row=3, columnspan=3)

label_email = Label(text="Email address:", font=(FONT_NAME, 19))
label_email.grid(column=1, row=4)
email_entry = Entry(width=55)
email_entry.insert(0, 'example@gmail.com')
email_entry.grid(column=2, row=4, columnspan=3)

label_pass = Label(text="Password:", font=(FONT_NAME, 19))
label_pass.grid(column=1, row=5)
pass_entry = Entry(width=35)
pass_entry.grid(column=2, row=5)

gen_button = Button(text='Generate Password', command=password_generator)
gen_button.grid(column=4, row=5)

add_button = Button(text='Add', width=45, command=save_password)
add_button.grid(column=2, row=6, columnspan=3)

window.mainloop()
