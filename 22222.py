import tkinter as tk
from tkinter import ttk, messagebox

# Global variables
member_name = ""
member_position = ""
job_vacancy = ""
daily_tasks = {}  # Dictionary to store daily tasks for each team

# Function to save data
def save_data():
    global member_name, member_position, job_vacancy
    member_name = member_name_entry.get()
    member_position = member_position_var.get()
    job_vacancy = job_vacancy_entry.get()

    if member_name and job_vacancy:  # Check if name and job vacancy are not empty
        data = [member_name, member_position, job_vacancy]
        tree.insert('', 'end', values=data)
        daily_tasks.setdefault(member_position, {}).setdefault(member_name, [])  # Initialize daily tasks for the new employee
        with open('company_database.txt', 'a') as file:
            file.write(f"Name: {member_name}, Position: {member_position}, Job Vacancy: {job_vacancy}\n")
        member_name_entry.delete(0, tk.END)
        job_vacancy_entry.delete(0, tk.END)
        messagebox.showinfo("Success", "Data saved successfully!")
    else:
        messagebox.showwarning("Incomplete Data", "Please provide both name and job vacancy.")

# Function to delete selected data
def delete_selected_data():
    selected_item = tree.selection()
    if selected_item:
        member_name = tree.item(selected_item, 'values')[0]
        member_position = tree.item(selected_item, 'values')[1]
        tree.delete(selected_item)
        del daily_tasks[member_position][member_name]  # Remove daily tasks for the deleted employee
        if not daily_tasks[member_position]:  # If there are no more employees in the team, delete the team
            del daily_tasks[member_position]
        with open('company_database.txt', 'w') as file:
            for item in tree.get_children():
                data = tree.item(item, 'values')
                file.write(f"Name: {data[0]}, Position: {data[1]}, Job Vacancy: {data[2]}\n")
        messagebox.showinfo("Data Deleted", "Selected data has been deleted!")
    else:
        messagebox.showwarning("No Selection", "Please select a row to delete.")

# Function to view saved data
def view_data():
    try:
        with open('company_database.txt', 'r') as file:
            data = file.readlines()
        if data:
            for item in tree.get_children():
                tree.delete(item)
            for line in data:
                line_data = line.strip().split(', ')
                tree.insert('', 'end', values=line_data)
            messagebox.showinfo("Company Database", "Data loaded successfully!")
        else:
            messagebox.showinfo("No Data", "No data available.")
    except FileNotFoundError:
        messagebox.showinfo("No Data", "No data available.")

# Function to view daily tasks for the selected employee
def view_daily_tasks():
    selected_item = tree.selection()
    if selected_item:
        member_name = tree.item(selected_item, 'values')[0]
        member_position = tree.item(selected_item, 'values')[1]
        tasks = daily_tasks.get(member_position, {}).get(member_name, [])
        tasks_str = "\n".join(tasks)
        messagebox.showinfo(f"Daily Tasks for {member_name} - {member_position}", tasks_str)
    else:
        messagebox.showwarning("No Selection", "Please select an employee to view daily tasks.")

# Function to add daily tasks for the selected employee
def add_daily_task():
    selected_item = tree.selection()
    if selected_item:
        member_name = tree.item(selected_item, 'values')[0]
        member_position = tree.item(selected_item, 'values')[1]
        task = task_entry.get()
        daily_tasks.setdefault(member_position, {}).setdefault(member_name, []).append(task)
        task_entry.delete(0, tk.END)
        messagebox.showinfo("Task Added", "Daily task added successfully!")
    else:
        messagebox.showwarning("No Selection", "Please select an employee to add a daily task.")

# Create a Tkinter window
window = tk.Tk()
window.title("Company Database Management")

# Create a frame for input fields
input_frame = tk.Frame(window)
input_frame.pack(pady=10)

member_name_label = tk.Label(input_frame, text="Name:")
member_name_label.grid(row=0, column=0, padx=5, pady=5)
member_name_entry = tk.Entry(input_frame)
member_name_entry.grid(row=0, column=1, padx=5, pady=5)

member_position_label = tk.Label(input_frame, text="Position:")
member_position_label.grid(row=1, column=0, padx=5, pady=5)
positions = ["CEO", "CFO", "Head Developer", "Head Designer", "Manager", "Employee"]
member_position_var = tk.StringVar(window)
member_position_var.set(positions[0])
position_dropdown = tk.OptionMenu(input_frame, member_position_var, *positions)
position_dropdown.grid(row=1, column=1, padx=5, pady=5)

job_vacancy_label = tk.Label(input_frame, text="Job Vacancy:")
job_vacancy_label.grid(row=2, column=0, padx=5, pady=5)
job_vacancy_entry = tk.Entry(input_frame)
job_vacancy_entry.grid(row=2, column=1, padx=5, pady=5)

# Create a frame for buttons
button_frame = tk.Frame(window)
button_frame.pack(pady=10)

save_button = tk.Button(button_frame, text="Save Data", command=save_data)
save_button.grid(row=0, column=0, padx=5, pady=5)

view_button = tk.Button(button_frame, text="View Data", command=view_data)
view_button.grid(row=0, column=1, padx=5, pady=5)

delete_data_button = tk.Button(button_frame, text="Delete Selected Data", command=delete_selected_data)
delete_data_button.grid(row=0, column=2, padx=5, pady=5)

view_tasks_button = tk.Button(button_frame, text="View Daily Tasks", command=view_daily_tasks)
view_tasks_button.grid(row=0, column=3, padx=5, pady=5)

# Create a frame for daily tasks
daily_tasks_frame = tk.Frame(window)
daily_tasks_frame.pack(pady=10)

task_label = tk.Label(daily_tasks_frame, text="Add Daily Task:")
task_label.grid(row=0, column=0, padx=5, pady=5)
task_entry = tk.Entry(daily_tasks_frame)
task_entry.grid(row=0, column=1, padx=5, pady=5)
add_task_button = tk.Button(daily_tasks_frame, text="Add Task", command=add_daily_task)
add_task_button.grid(row=0, column=2, padx=5, pady=5)

# Create a frame for the treeview
tree_frame = tk.Frame(window)
tree_frame.pack(pady=10)

# Create a treeview for data display
columns = ("Name", "Position", "Job Vacancy")
tree = ttk.Treeview(tree_frame, columns=columns, show='headings', selectmode="browse")

# Configure column headings
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=150, anchor="center")

tree.pack(expand=True, fill='both')

# Start the Tkinter main loop
window.mainloop()
