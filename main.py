import tkinter
from tkinter import *
from tkinter import ttk
from tkcalendar import Calendar
from tkcalendar import DateEntry
import datetime
import webbrowser
from ttkthemes import ThemedTk
import sqlite3
import smtplib

connection = sqlite3.connect("database.db")

connection.execute('''CREATE TABLE IF NOT EXISTS ASSIGNMENTS
                    (DESC TEXT,
                    TYPE TEXT,
                    CLASS TEXT,
                   DATE TEXT);''')
#print("Table created")

main = ThemedTk(theme="black")
main.title('Student Life Planner v0.1')
main.geometry('900x800')
tabControl = ttk.Notebook(main)

imgAssignment = PhotoImage(file="assignmenticon.gif")
imgSettings = PhotoImage(file="settingicon.gif")
imgBS = PhotoImage(file="brightspacelogo-md.png")

tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)
tab3 = ttk.Frame(tabControl)
tab4 = ttk.Frame(tabControl)
tab5 = ttk.Frame(tabControl)


tabControl.add(tab1, text='Main', image=imgAssignment,)
tabControl.add(tab2, text='Add/Edit Classes')
tabControl.add(tab3, text='Calender')
tabControl.add(tab4, text='Mail')
tabControl.add(tab5, text='Settings', image=imgSettings)
tabControl.pack(expand=5, fill="both")

# ---------------- Database Contents ------------------------------------
#def database():



# ---------------- TAB 1 Contents ------------------------------------

# -----------------------------------------------------------
# Program Name Label
# -----------------------------------------------------------
header = ttk.Label(tab1, text='Assignments', font=("TkMenuFont", 23, 'underline italic'))
header.grid(row=0, column=0)

# -----------------------------------------------------------
# Assignment Description Label
# -----------------------------------------------------------
assignmentDesc = ttk.Label(tab1, text='Description', font=("TkMenuFont", 12, 'bold'))
assignmentDesc.grid(row=1, column=0)

# -----------------------------------------------------------
# Type of Assignment Label
# -----------------------------------------------------------
assignmentType = ttk.Label(tab1, text='Type', font=("TkMenuFont", 12, 'bold'))
assignmentType.grid(row=1, column=2)

# -----------------------------------------------------------
# Class Selection Label
# -----------------------------------------------------------
whatClass = ttk.Label(tab1, text='Class', font=("TkMenuFont", 12, 'bold'))
whatClass.grid(row=1, column=4)

dueDate = ttk.Label(tab1, text='Due Date', font=("TkMenuFont", 12, 'bold'))
dueDate.grid(row=1, column=6)

separator = ttk.Separator(tab1, orient='horizontal')
separator.grid(row=2, column=0)

# -----------------------------------------------------------
# Assignment Description Entry
# -----------------------------------------------------------
assignmentEnt = Entry(tab1, width=40)
assignmentEnt.grid(row=3, column=0, padx=10, pady=5)

# -----------------------------------------------------------
# Type of Assignment Drop down menu
# -----------------------------------------------------------
TypeOptions = ["Homework", "Lab", "Paper", "Discussion", "Project", "Quiz", "Presentation", "Exam", "Midterm", "Final"]
SelectedType = StringVar()

assignmentType = ttk.Combobox(tab1, textvariable=SelectedType)
assignmentType['values'] = ("Homework", "Lab", "Paper", "Discussion", "Project", "Quiz", "Presentation", "Exam", "Midterm", "Final")
assignmentType.grid(row=3, column=2, padx=10, pady=5)

# -----------------------------------------------------------
# Assignment for class selection Entry
# -----------------------------------------------------------
forClass = ttk.Combobox(tab1)
forClass.grid(row=3, column=4, padx=10, pady=5)

# -----------------------------------------------------------
# Due Date Selection w/Calender
# -----------------------------------------------------------
sel = StringVar()

cal = DateEntry(tab1, selectmode='day', textvariable=sel)
cal.grid(row=3, column=6, padx=20)

# -----------------------------------------------------------
# Add Assignment Button
# -----------------------------------------------------------
addAss = Button(tab1, borderwidth=1, bg='grey', text='Add Assignment', font=("TkMenuFont", 13, 'bold'))
addAss.grid(row=4,column=0)

#def add_assign():


# -----------------------------------------------------------
# Open Bright space
# -----------------------------------------------------------
def openBS():
    new = 1
    url = "https://brightspace.uakron.edu/d2l/home"
    webbrowser.open(url, new=new)


openBrightS = Button(tab1, text="Brightspace", image=imgBS, font=("TkMenuFont", 10, 'bold underline'), command=lambda: openBS())
openBrightS.grid(row=8, column=0, sticky='sw')

# -----------------------------------------------------------
# Assignment listbox
# -----------------------------------------------------------
assignmentlistHeader = Label(tab1, text='Assignment list:', font=("TkMenuFont", 12, 'bold'))
assignmentlistHeader.grid(row=6, column=0, sticky='w')

assignmentList = Listbox(tab1, width=100, height=20)
assignmentList.grid(row=7, column=0,columnspan=7, sticky='w')

# ----------------- TAB 2 CONTENTS -------------------------------

header2 = ttk.Label(tab2, text='CLASSES', font=("TkMenuFont", 23, 'underline'))
header2.grid(row=0, column=0)

# -----------------------------------------------------------
# Class List Widget
# -----------------------------------------------------------

classList = Listbox(tab2, width=30, height=15, relief='solid', borderwidth=3)
classList.grid(row=4, column=0,columnspan=3, sticky='w')



# ----------------- TAB 3 CONTENTS -------------------------------
cal = Calendar(tab3, selectmode='none', year=2022, month=5, day=25)
cal.grid(row=0, column=0)

# ----------------- EMAIL TAB CONTENTS -------------------------------

def send_message():
    address_info = address.get()
    email_body_info = email_body.get()
    print(address_info,email_body_info)
    sender_email = "rileyholschuh@gmail.com"
    sender_password = "pebbleS05"
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, sender_password)
    print("Login successful")
    server.sendmail(sender_email, address_info, email_body_info)
    print("Message sent")
    address_entry.delete(0, END)
    email_body_entry.delete(0, END)


address_field = Label(tab4, text="Recipient Address :")
address_field.grid(row=0, column=0)
email_body_field = Label(tab4, text="Message :")
email_body_field.grid(row=3, column=0)

address = StringVar()
email_body = StringVar()


address_entry = Entry(tab4, textvariable=address, width=30)
address_entry.grid(row=1, column=0)
email_body_entry = Entry(tab4, textvariable=email_body, width=50)
email_body_entry.grid(row=4, column=0)

emailButton = Button(tab4, text="Send Message", command=send_message, width="30", height="2", bg="grey")
emailButton.grid(row=6, column=0)

def openOutlook():
    new = 1
    url = "https://outlook.office.com/mail/"
    webbrowser.open(url, new=new)

emailButtonO = Button(tab4, text="Outlook", width="30", height="2", bg="grey", command=lambda :openOutlook())
emailButtonO.grid(row=6, column=0)




main.mainloop()
