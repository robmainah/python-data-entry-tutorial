from tkinter import *
from tkinter import ttk
from tkinter import messagebox


window = Tk()
window.title("Data Entry form")


def enter_data():
    if terms_status_var.get() != "Accepted":
        return messagebox.showwarning(title="Error", message="You have not selected the terms")

    first_name = first_name_entry.get()
    last_name = last_name_entry.get()

    if not first_name or not last_name:
        return messagebox.showwarning(title="Error", message="Firstname and Lastname is required")

    title = title_combobox.get()
    age = age_spinbox.get()
    nationality = nationality_combobox.get()
    number_courses = number_courses_spinbox.get()
    num_semesters = num_semesters_spinbox.get()
    registered_check = reg_status_var.get()

    data = [first_name, last_name, title, age, nationality, num_semesters, number_courses, registered_check]


    print(first_name, last_name, title, age,
          nationality, number_courses, num_semesters,
          registered_check)


frame = Frame(window)
frame.pack()

user_info_frame = LabelFrame(frame, text="User Information")
user_info_frame.grid(row=0, column=0, padx=20, pady=20)

first_name = Label(user_info_frame, text="First Name")
first_name.grid(row=0, column=0)

last_name = Label(user_info_frame, text="Last Name")
last_name.grid(row=0, column=1)

first_name_entry = Entry(user_info_frame)
first_name_entry.grid(row=1, column=0)

last_name_entry = Entry(user_info_frame)
last_name_entry.grid(row=1, column=1)

title = Label(user_info_frame, text="Title")
title.grid(row=0, column=2)

title_combobox = ttk.Combobox(user_info_frame, values=["", "Mr.", "Mrs.", "Dr."])
title_combobox.grid(row=1, column=2)

age = Label(user_info_frame, text="Age")
age.grid(row=2, column=0)

age_spinbox = Spinbox(user_info_frame, from_=18, to=110)
age_spinbox.grid(row=3, column=0)

nationality = Label(user_info_frame, text="Nationality")
nationality.grid(row=2, column=1)

nationality_combobox = ttk.Combobox(user_info_frame, values=["Kenyan", "Ugandan", "American"])
nationality_combobox.grid(row=3, column=1)

for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

course_frame = LabelFrame(frame, text="Courses Details")
course_frame.grid(row=1, column=0, sticky="news", padx=20, pady=20)

registered = Label(course_frame, text="Registration status")
registered.grid(row=0, column=0)

reg_status_var = StringVar(value="Not Reegistered")
registered_check = Checkbutton(course_frame, text="Currently Registered", variable=reg_status_var, onvalue='Registered', offvalue='Not Registered')
registered_check.grid(row=1, column=0)

number_courses = Label(course_frame, text="# Completed courses")
number_courses.grid(row=0, column=1)

number_courses_spinbox = Spinbox(course_frame, from_=0, to='infinity')
number_courses_spinbox.grid(row=1, column=1)

num_semesters = Label(course_frame, text="# of Semesters")
num_semesters.grid(row=0, column=2)
num_semesters_spinbox = Spinbox(course_frame, from_=0, to="infinity")
num_semesters_spinbox.grid(row=1, column=2)

for widget in course_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

terms_frame = LabelFrame(frame, text="Terms & Condtions")
terms_frame.grid(row=2, column=0, sticky="news", padx=20, pady=20)

terms_status_var = StringVar(value="Not accepted")
terms_checkbox = Checkbutton(terms_frame, text="I accept the terms and conditions", variable=terms_status_var, onvalue="Accepted", offvalue="Not accepted")
terms_checkbox.grid(row=0, column=0)

button = Button(frame, text="Enter Data", command=enter_data)
button.grid(row=3, column=0, sticky="news", padx=20, pady=20)

window.mainloop()