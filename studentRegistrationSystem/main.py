import tkinter as tk
import tkinter.ttk as ttk

root = tk.Tk()
root.geometry("500x600")
root.title("Student System")

student_data = [
    ['1', 'Robert', 'robert@gmail.com', 'Python'],
    ['2', 'Maina', 'maina@gmail.com', 'C++']
]


def load_student_data():
    for item in record_table.get_children():
        record_table.delete(item)

    for key in range(len(student_data)):
        record_table.insert(parent='', index='end', text='', iid=str(key), values=student_data[key])


def add_student_data(id, name, email, course):
    name = name.title()
    course = course.title()

    student_data.append([id, name, email, course])

    load_student_data()
    clear_student_data()


def put_student_in_entry(index):
    student_id.delete(0, tk.END)
    student_name.delete(0, tk.END)
    student_email.delete(0, tk.END)
    student_course.delete(0, tk.END)

    student_id.insert(0, student_data[index][0])
    student_name.insert(0, student_data[index][1])
    student_email.insert(0, student_data[index][2])
    student_course.insert(0, student_data[index][3])


def update_student_data(id, name, email, course, index):
    student_data[index] = [id, name, email, course]
    load_student_data()
    clear_student_data()


def delete_student_data(index):
    del student_data[index]
    load_student_data()
    clear_student_data()


def clear_student_data():
    student_id.delete(0, tk.END)
    student_name.delete(0, tk.END)
    student_email.delete(0, tk.END)
    student_course.delete(0, tk.END)

    load_student_data()


head_frame = tk.Frame(root)
head_frame.pack(pady=10)
head_frame.pack_propagate(False)
head_frame.configure(width=400, height=300)

heading_lb = tk.Label(head_frame, text="Student Registration System", font=('Bold', 13), bg='red')
heading_lb.pack(fill=tk.X, pady=5)

student_id_lb = tk.Label(head_frame, text="Student ID:", font=('Bold', 10))
student_id_lb.place(x=0, y=50)
student_id = tk.Entry(head_frame, font=('Bold', 10))
student_id.place(x=110, y=50, width=180)

student_name_lb = tk.Label(head_frame, text="Student Name:", font=('Bold', 10))
student_name_lb.place(x=0, y=100)
student_name = tk.Entry(head_frame, font=('Bold', 10))
student_name.place(x=110, y=100, width=180)

student_email_lb = tk.Label(head_frame, text="Student Email:", font=('Bold', 10))
student_email_lb.place(x=0, y=150)
student_email = tk.Entry(head_frame, font=('Bold', 10))
student_email.place(x=110, y=150, width=180)

student_course_lb = tk.Label(head_frame, text="Student Course:", font=('Bold', 10))
student_course_lb.place(x=0, y=200)
student_course = tk.Entry(head_frame, font=('Bold', 10))
student_course.place(x=110, y=200, width=180)

register = tk.Button(head_frame, text="Register", font=('Bold', 12), pady=5,
                     command=lambda: add_student_data(
                         student_id.get(),
                         student_name.get(),
                         student_email.get(),
                         student_course.get()
                     ))
register.place(x=0, y=250)

update = tk.Button(head_frame, text="Update", font=('Bold', 12), pady=5,
                   command=lambda: update_student_data(
                        student_id.get(),
                        student_name.get(),
                        student_email.get(),
                        student_course.get(),
                       index=int(record_table.selection()[0])
                   ))
update.place(x=85, y=250)

delete= tk.Button(head_frame, text="Delete", font=('Bold', 12), pady=5,
                  command=lambda: delete_student_data(int(record_table.selection()[0])))
delete.place(x=165, y=250)

clear = tk.Button(head_frame, text="Clear", font=('Bold', 12), pady=5,
                  command=lambda: clear_student_data())
clear.place(x=235, y=250)

search_bar_frame = tk.Frame(root)
search_bar_frame.pack(pady=5)
search_bar_frame.pack_propagate(False)
search_bar_frame.configure(width=400, height=50)

search_lb = tk.Label(search_bar_frame, text="Search student by ID", font=('Bold', 10))
search_lb.pack(anchor=tk.W)

search_entry = tk.Entry(search_bar_frame, font=('Bold', 10))
search_entry.pack(anchor=tk.W)

record_frame = tk.Frame(root)
record_frame.pack(pady=10)
record_frame.pack_propagate(False)
record_frame.configure(width=400, height=200)

record_lb = tk.Label(record_frame, text="Select student to update or delete", bg='red', font=('Bold', 13))
record_lb.pack(fill=tk.X)

record_table = ttk.Treeview(record_frame)
record_table.pack(fill=tk.X, pady=5)

record_table.bind('<<TreeviewSelect>>', lambda e: put_student_in_entry(
    int(record_table.selection()[0])))

record_table['column'] = ['Id', 'Name', 'Email', 'Course']

record_table.column('#0', anchor=tk.W, width=0, stretch=tk.NO)
record_table.column('Id', anchor=tk.W, width=50)
record_table.column('Name', anchor=tk.W, width=100)
record_table.column('Email', anchor=tk.W, width=120)
record_table.column('Course', anchor=tk.W, width=160)

record_table.heading('Id', text='Id', anchor=tk.W)
record_table.heading('Name', text='Name', anchor=tk.W)
record_table.heading('Email', text='Email', anchor=tk.W)
record_table.heading('Course', text='Course', anchor=tk.W)

load_student_data()
root.mainloop()