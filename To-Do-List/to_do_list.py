import tkinter
from tkinter import *
import mysql.connector
from mysql.connector import Error
from tkinter import messagebox

root = Tk()
root.title("To-Do-List")
root.geometry("400x750+400+100")
root.resizable(False, False)

# Function to establish a database connection
def create_connection():
    connection = None
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='tododb',
            user='root',
            password='Mysql@123'
        )
        if connection.is_connected():
            print("Connected to MySQL database")
        else:
            print("Failed to connect to MySQL database")
    except Error as e:
        print(f"Error: {e}")
    return connection

task_list = []

def addTask(event=None):
    task_description = task_entry.get()
    task_entry.delete(0, END)

    if task_description:
        try:
            addTaskToDB(task_description)
            task_list.append(task_description)
            listbox.insert(END, task_description)
        except Error as e:
            print(f"Error: {e}")
            messagebox.showerror("Error", "Failed to add task to the database.")

def addTaskToDB(task_description):
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            insert_query = "INSERT INTO todo (TASK, COMPLETED) VALUES (%s, %s)"
            task_data = (task_description, 0)
            cursor.execute(insert_query, task_data)
            connection.commit()
            print("Task added to the database")
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            connection.close()

def deleteTaskFromDB(task):
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            delete_query = "DELETE FROM todo WHERE TASK = %s"
            task_data = (task,)
            cursor.execute(delete_query, task_data)
            connection.commit()
            print("Task deleted from the database")
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            connection.close()

def deleteTask():
    selected_item_index = listbox.curselection()
    if selected_item_index:
        task_index = selected_item_index[0]
        task_description = listbox.get(task_index)
        try:
            deleteTaskFromDB(task_description)
            listbox.delete(task_index)
        except Error as e:
            print(f"Error: {e}")
            messagebox.showerror("Error", "Failed to delete task from the database.")

            
#icon
Image_icon=PhotoImage(file="To-Do-List/Image/task.png")
root.iconphoto(False, Image_icon)

#topbar
TopImage=PhotoImage(file="To-Do-List/Image/topbar.png")
Label(root, image=TopImage).pack()

noteImage=PhotoImage(file="To-Do-List/Image/task.png")
Label(root, image=noteImage, bg="#32405b").place(x=90, y=20)

heading=Label(root, text="TASK LIST", font="Times 20 bold", fg="white", bg="#32405b")
heading.place(x=120, y=20)

canvas = Canvas(root, width=400, height=750)
canvas.pack

#main
frame=Frame(root, width=500, height=50, bg="white")
frame.place(x=0, y=120)

task=StringVar()
task_entry=Entry(frame, width=35, font="arial 20", bd=0)
task_entry.place(x=10, y=7)
task_entry.focus()
task_entry.bind("<Return>", addTask)

button=Button(frame, text="ADD", font="TIMES 20 bold", command=addTask, width=6, bg="navy", fg="white", bd=1)
button.place(x=300, y=0)


# Listbox
frame1=Frame(root, bd=3, width=1200, height=800, bg="white")
frame1.place(x=0, y=180)

listbox=Listbox(frame1, font='Times 20 bold', width=60, height=20, bg="white", fg="blue", cursor="hand2", selectbackground="black")
listbox.pack(side=LEFT, fill=BOTH, padx=2)

scrollbar=Scrollbar(frame1)
scrollbar.pack(side=RIGHT, fill=BOTH)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)



def updateTaskStatusInDB(task_description, completed_status):
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            update_query = "UPDATE todo SET COMPLETED = %s WHERE TASK = %s"
            task_data = (completed_status, task_description)
            cursor.execute(update_query, task_data)
            connection.commit()
            print("Task completion status updated in the database")

            # Apply strikeout effect in the listbox
            selected_item_index = listbox.curselection()
            if selected_item_index:
                task_index = selected_item_index[0]
                if completed_status == 1:
                    # Draw a line over the completed task to simulate strikeout effect
                    canvas.create_line(10, task_index * 40 + 20, 390, task_index * 40 + 20, fill="red", width=2, tags="strikeout_line")
                    listbox.itemconfig(task_index, {'bg':'light green'})
                else:
                    # If task is not completed, remove the strikeout effect
                    canvas.delete("strikeout_line")
                    listbox.itemconfig(task_index, {'bg':'white'})
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            connection.close()

def markTaskAsCompleted():
    selected_item_index = listbox.curselection()
    if selected_item_index:
        task_index = selected_item_index[0]
        task_description = listbox.get(task_index)
        updateTaskStatusInDB(task_description, 1)  # 1 represents completed task
        # Draw a line over the completed task to simulate strikeout effect
        canvas.create_line(10, task_index * 40 + 20, 390, task_index * 40 + 20, fill="red", width=2)
        listbox.itemconfig(task_index, {'bg':'red'})

def populatelistboxFromDB():
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            select_query = "SELECT TASK, COMPLETED FROM todo"
            cursor.execute(select_query)
            tasks = cursor.fetchall()
            for index, task in enumerate(tasks):
                task_description = task[0]
                completed = task[1]
                listbox.insert(END, task_description)
                if completed == 1:
                    # Draw a line over the completed task to simulate strikeout effect
                    canvas.create_line(10, index * 40 + 20, 390, index * 40 + 20, fill="red", width=2)
                    listbox.itemconfig(index, {'bg':'light green'})
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            connection.close()


# Function is called to populate tasks from the database to the listbox
populatelistboxFromDB()

#delete
Delete_icon=PhotoImage(file="To-Do-List/Image/delete.png")
Button(root, image=Delete_icon, bd=0, command=deleteTask).pack(side=BOTTOM, pady=13)

Mark_icon=PhotoImage(file="To-Do-List/Image/blue-tick.png")
Button(root, image=Mark_icon, bd=0, command=lambda:updateTaskStatusInDB(listbox.get(ANCHOR),1)).place(x=100, y=680)

root.mainloop()
