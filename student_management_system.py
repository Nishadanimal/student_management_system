import requests

import matplotlib.pyplot as plt

from tkinter import *

from tkinter.messagebox import *

from tkinter.scrolledtext import *

from sqlite3 import *

import bs4


try:

    end_point = "https://ipinfo.io/"

    res = requests.get(end_point)

    print(res)

    data = res.json()

    city_name = data['city']

    a1 = "http://api.openweathermap.org/data/2.5/weather?units=metric"

    a2 = "&appid=" + "c6e315d09197cec231495138183954bd"

    a3 = "&q=" + city_name

    website_address = a1 + a2 + a3

    res = requests.get(website_address)

    data = res.json()

    data_main = data['main']

    temp = data_main['temp']

    web_address = "https://www.brainyquote.com/quotes/aristotle_397610"

    res = requests.get(web_address)

    data = bs4.BeautifulSoup(res.text, "html.parser")

    info = data.find("img", {"class": "bqPhotoFullDesktop"})

    quote = info['alt']


except Exception as e:

    print("issue ", e)


conn = None

try:

    con = connect("student.db")

    cursor = con.cursor()

    sql = "create table student (rollno int primary key,name text,marks int)"

    cursor.execute(sql)

except Exception as e:

    pass

finally:

    if conn is not None:

        con.close()


def f1():

    root.withdraw()

    adding.deiconify()

    rollentry.delete(0, END)

    nameentry.delete(0, END)

    marksentry.delete(0, END)


def f2():

    adding.withdraw()

    root.deiconify()


def f3():

    viewdata.delete(1.0, END)

    root.withdraw()

    viewing.deiconify()

    con = None

    try:

        con = connect("student.db")

        sql = "select * from student"

        cursor = con.cursor()

        cursor.execute(sql)

        data = cursor.fetchall()

        msg = ""

        for d in data:

            msg = msg + " Rno: " + \
                str(d[0]) + " Name: " + str(d[1]) + \
                " Marks: " + str(d[2]) + "\n"

        viewdata.insert(INSERT, msg)

    except Exception as e:

        showerror("Failure", "selection issue" + str(e))

    finally:

        if con is not None:

            con.close()


def f4():

    viewing.withdraw()

    root.deiconify()


def f5():

    update.withdraw()

    root.deiconify()


def f6():

    root.withdraw()

    update.deiconify()

    updateentry.delete(0, END)

    updateentryname.delete(0, END)

    updateentrymarks.delete(0, END)


def f7():

    root.withdraw()

    delete.deiconify()


def f8():

    delete.withdraw()

    root.deiconify()


def f9():

    con = None

    if (len(rollentry.get()) == 0):

        showerror("Failure", "Roll number cannot be empty")

        rollentry.delete(0, END)

    elif (rollentry.get()).isalpha():

        showerror("Failure", "Roll number cannot be alphabet")

        rollentry.delete(0, END)

    elif int(rollentry.get()) < 0:

        showerror("Failure", "Roll number cannot be Negative")

        rollentry.delete(0, END)

    elif int(rollentry.get()) == 0:

        showerror("Failure", "Roll number cannot be Zero")

        rollentry.delete(0, END)

    elif (len(nameentry.get()) == 0):

        showerror("Failure", "Name cannot be empty")

        nameentry.delete(0, END)

    elif (len(nameentry.get()) < 2):

        showerror("Failure", "Name Should contain minimum two characters ")

        nameentry.delete(0, END)

    elif (nameentry.get()).isdigit():

        showerror("Failure", "Name cannot contain a digit")

        nameentry.delete(0, END)

    elif len(marksentry.get()) == 0:

        showerror("Failure", "Marks cannot be empty")

        marksentry.delete(0, END)

    elif (marksentry.get()).isalpha():

        showerror("Failure", "Marks cannot be alphabet")

        marksentry.delete(0, END)

    elif int(marksentry.get()) < 0 or int(marksentry.get()) > 100:

        showerror("Failure", "Marks range should be within 0 to 100")

        marksentry.delete(0, END)

    else:

        try:

            con = connect("student.db")

            cursor = con.cursor()

            sql = "insert into student values('%d','%s','%d')"

            rno = int(rollentry.get())

            name = nameentry.get()

            marks = int(marksentry.get())

            con.execute(sql % (rno, name, marks))

            con.commit()

            showinfo("Success", "Record Added")

        except Exception as e:

            showerror("Failure", "insertion issue "+str(e))

        finally:

            if con is not None:

                con.close()

        rollentry.delete(0, END)

        nameentry.delete(0, END)

        marksentry.delete(0, END)


def f10():

    con = None

    if (len(updateentry.get()) == 0):

        showerror("Failure", "Roll number cannot be empty")

        updateentry.delete(0, END)

    elif (updateentry.get()).isalpha():

        showerror("Failure", "Roll number cannot be alphabet")

        updateentry.delete(0, END)

    elif int(updateentry.get()) <= 0:

        showerror("Failure", "Roll number cannot be Negative")

        updateentry.delete(0, END)

    elif int(updateentry.get()) == 0:

        showerror("Failure", "Roll number cannot be Zero")

        updateentry.delete(0, END)

    elif (len(updateentryname.get()) == 0):

        showerror("Failure", "Name cannot be empty")

        updateentryname.delete(0, END)

    elif (len(updateentryname.get()) < 2):

        showerror("Failure", "Name Should contain minimum two characters ")

        updateentryname.delete(0, END)

    elif (updateentryname.get()).isdigit():

        showerror("Failure", "Name cannot contain a digit")

        updateentryname.delete(0, END)

    elif (len(updateentrymarks.get()) == 0):

        showerror("Failure", "Marks cannot be empty")

        updateentrymarks.delete(0, END)

    elif (updateentrymarks.get()).isalpha():

        showerror("Failure", "Marks cannot be alphabet")

        updateentrymarks.delete(0, END)

    elif int(updateentrymarks.get()) < 0 or int(updateentrymarks.get()) > 100:

        showerror("Failure", "Marks range should be within 0 to 100")

        updateentrymarks.delete(0, END)

    else:

        try:

            con = connect("student.db")

            print("connectedd")

            sql = "update student set name = '%s' , marks='%d' where rollno = '%d'"

            cursor = con.cursor()

            rno = int(updateentry.get())

            name = updateentryname.get()

            marks = int(updateentrymarks.get())

            cursor.execute(sql % (name, marks, rno))

            if cursor.rowcount > 0:

                showinfo("Success", "record updated")

                con.commit()

            else:

                showerror("Failure", "record does not exists")

        except Exception as e:

            print("insertion issue", e)

            con.rollback()

        finally:

            if con is not None:

                con.close()

        updateentry.delete(0, END)

        updateentryname.delete(0, END)

        updateentrymarks.delete(0, END)


def f11():

    con = None

    if (len(deleteentry.get()) == 0):

        showerror("Failure", "Roll Number cannot be empty")

    elif (deleteentry.get()).isalpha():

        showerror("Failure", "Roll Number cannot be alphabet")

        deleteentry.delete(0, END)

    elif (int(deleteentry.get()) < 0):

        showerror("Failure", "Roll Number cannot be negative")

        deleteentry.delete(0, END)

    else:

        try:

            con = connect("student.db")

            sql = "delete from student where rollno = '%d'"

            cursor = con.cursor()

            rno = int(deleteentry.get())

            cursor.execute(sql % (rno))

            if cursor.rowcount > 0:

                showinfo("Success", "Record deleted")

                con.commit()

            else:

                showerror("Failure", "Record does not exists")

        except Exception as e:

            print("insertion issue", e)

            con.rollback()

        finally:

            if con is not None:

                con.close()

            deleteentry.delete(0, END)


def f20():

    con = None

    try:

        con = connect("student.db")

        sql1 = "select * from student"

        cursor = con.cursor()

        cursor.execute(sql1)

        data = cursor.fetchall()

        i = 0

        list3 = []

        list4 = []

        list5 = []

        for d in data:

            list10 = list(data[i])

            list20 = list10[2]

            list30 = list10[1]

            list40 = list10[0]

            list4.append(list20)

            list3.append(list30)

            list5.append(list40)

            i = i+1

    except Exception as e:

        print("insertion issue", e)

        con.rollback()

    finally:

        if con is not None:

            con.close()

    plt.bar(list3, list4)

    plt.title("Batch Information")

    plt.xlabel("Names")

    plt.ylim(top=100)

    plt.ylabel("Marks")

    plt.show()


root = Tk()

root.title("S.M.S")

root.geometry("550x600+450+100")

root.configure(bg='white smoke')


addbtn = Button(root, bg='yellow', text="Add", width=20,
                font=('arial', 20, 'bold'), command=f1)

viewbtn = Button(root, bg='yellow', text="View", width=20,
                 font=('arial', 20, 'bold'), command=f3)

updatebtn = Button(root, bg='yellow', text="Update", width=20,
                   font=('arial', 20, 'bold'), command=f6)

deletebtn = Button(root, bg='yellow', text="Delete", width=20,
                   font=('arial', 20, 'bold'), command=f7)

chartsbtn = Button(root, bg='yellow', text="Charts", width=20,
                   font=('arial', 20, 'bold'), command=f20)


loclabel = Label(root, text="Location:", font=('arial', 20, 'bold'),
                 width=31, height=1, borderwidth=1, relief="solid", anchor=NW)

loc1label = Label(root, text=city_name, font=(
    'arial', 20, 'bold'), relief="solid", bd=0)

templabel = Label(root, text="Temp: ", font=(
    'arial', 20, 'bold'), relief="solid", bd=0)

temp1label = Label(root, text=temp, font=(
    'arial', 20, 'bold'), relief="solid", bd=0)

quotelabel = Label(root, text="QOTD:", font=('arial', 20, 'bold'),
                   width=31, height=1, borderwidth=1, relief="solid", anchor=NW)

quote1label = Label(root, text=quote, font=(
    'arial', 17, 'bold'), relief="solid", bd=0)


addbtn.pack(pady=10)

viewbtn.pack(pady=10)

updatebtn.pack(pady=10)

deletebtn.pack(pady=10)

chartsbtn.pack(pady=10)


loclabel.place(x=5, y=450)

loc1label.place(x=135, y=451)

templabel.place(x=350, y=451)

temp1label.place(x=440, y=451)

quotelabel.place(x=5, y=530)

quote1label.place(x=97, y=532)


''' Code for Adding a Student  '''


adding = Toplevel(root)

adding.title("Add St.")

adding.geometry("550x600+450+100")

adding.withdraw()

adding.configure(bg='white smoke')


rolllabel = Label(adding, text="Enter Roll Number:",
                  font=('arial', 20, 'bold'))

rollentry = Entry(adding, bd=3, font=('arial', 20, 'bold'))

namelabel = Label(adding, text="Enter Name:",
                  font=('arial', 20, 'bold'))

nameentry = Entry(adding, bd=3, font=('arial', 20, 'bold'))

markslabel = Label(adding, text="Enter Marks:",
                   font=('arial', 20, 'bold'))

marksentry = Entry(adding, bd=3, font=('Comic Sans MS', 20, 'bold'))

save = Button(adding, bg='yellow', text="Save", font=(
    'arial', 20, 'bold'), width=10, command=f9)

back = Button(adding, bg='yellow', text="Back", font=(
    'arial', 20, 'bold'), width=10, command=f2)


rolllabel.pack(pady=10)

rollentry.pack(pady=10)

namelabel.pack(pady=10)

nameentry.pack(pady=10)

markslabel.pack(pady=10)

marksentry.pack(pady=10)

save.pack(pady=10)

back.pack(pady=10)


''' Code for Viewing '''


viewing = Toplevel(root)

viewing.title("View St.")

viewing.geometry("550x600+450+100")

viewing.configure(bg='white smoke')


viewdata = ScrolledText(viewing, width=30, height=12,
                        font=('arial', 20, 'bold'))

viewback = Button(viewing, bg='yellow', text="Back",
                  font=('arial', 20, 'bold'), command=f4)


viewdata.pack(pady=10)

viewback.pack(pady=10)

viewing.withdraw()


''' Code for Updating '''


update = Toplevel(root)

update.title("Update St.")

update.geometry("550x600+450+100")

update.withdraw()

update.configure(bg='white smoke')


updateroll = Label(update, text="Enter Roll Number:",
                   font=('arial', 20, 'bold'))

updateentry = Entry(update, bd=3, font=('arial', 20, 'bold'))

updatename = Label(update, text="Enter Name:",
                   font=('arial', 20, 'bold'))

updateentryname = Entry(update, bd=3, font=('arial', 20, 'bold'))

updatemarks = Label(update, text="Enter Marks:",
                    font=('arial', 20, 'bold'))

updateentrymarks = Entry(update, bd=3, font=('arial', 20, 'bold'))

updatesave = Button(update, bg='yellow', text="Save", font=(
    'arial', 20, 'bold'), width=10, command=f10)

updateback = Button(update, bg='yellow', text="Back", font=(
    'arial', 20, 'bold'), width=10, command=f5)


updateroll.pack(pady=10)

updateentry.pack(pady=10)

updatename.pack(pady=10)

updateentryname.pack(pady=10)

updatemarks.pack(pady=10)

updateentrymarks.pack(pady=10)

updatesave.pack(pady=10)

updateback.pack(pady=10)


''' Code for Deleting '''


delete = Toplevel(root)

delete.title("Delete St.")

delete.geometry("550x600+450+100")

delete.withdraw()

delete.configure(bg='white smoke')


deleteroll = Label(delete, text="Enter Roll Number:",
                   font=('arial', 20, 'bold'))

deleteentry = Entry(delete, bd=3, font=('arial', 20, 'bold'))

deletesave = Button(delete, bg='yellow', text="Delete", font=(
    'arial', 20, 'bold'), width=10, command=f11)

deleteback = Button(delete, bg='yellow', text="Back", font=(
    'arial', 20, 'bold'), width=10, command=f8)


deleteroll.pack(pady=10)

deleteentry.pack(pady=10)

deletesave.pack(pady=10)

deleteback.pack(pady=10)


root.mainloop()
