from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3
#from PIL import Image
import webbrowser
import tkinter.messagebox


# colors

bgc1 = 'lawngreen'
bgc2 = 'yellowgreen'

bgc1 = 'darkcyan'
bgc2 = 'darkturqoise'

bgc1 = 'mediumorchid'
bgc2 = 'magenta'

bgc1 = 'goldenrod'
bgc2 = 'dark goldenrod'

bgc1 = 'skyblue'
bgc2 = 'steelblue'




root= Tk()
fnt1 = ("Microsoft YaHei UI", 13)
fnt2 = ("arial", 16, "bold")
root.configure(bg=bgc1)


# variable section

img1 = PhotoImage(file = 'ico1.png')
img2 = PhotoImage(file = 'ico2.png')
q = StringVar()
t1 = StringVar()
t2 = StringVar()
t3 = StringVar()
t4 = StringVar()
t5 = StringVar()
t6 = StringVar()
t7 = StringVar()
t8 = StringVar()



def update(rows):
    trv.delete(*trv.get_children())
    for i in rows:
        trv.insert('', 'end', values=i)
    
def search():
    q2 = q.get()
    query = "SELECT * from master WHERE name LIKE '%"+q2+"%' OR add1 LIKE '%"+q2+"%'"
    cursor.execute(query)
    rows = cursor.fetchall()
    update(rows)
    
def search_url():
    url = 'https://services.gst.gov.in/services/searchtp'
    webbrowser.open(url)
    
        
def reset_tree():
    ent.delete(0, END)
    q2 = q.get()
    query = "SELECT * from master WHERE name LIKE '%"+q2+"%' OR add1 LIKE '%"+q2+"%'"
    cursor.execute(query)
    rows = cursor.fetchall()
    update(rows)


def getrow(event):
    rowid = trv.identify_row(event.y)
    item=trv.item(trv.focus())
    t1.set(item['values'][0])
    t2.set(item['values'][2])
    t3.set(item['values'][3])
    t4.set(item['values'][4])
    t5.set(item['values'][5])
    t6.set(item['values'][6])
    t7.set(item['values'][7])
    t8.set(item['values'][8])


def add_customer():
    cust_actual =  cust_gst.get()
    len_gst  = len(cust_actual)

    if len_gst != 0 :
        if len_gst != 15:
            tkinter.messagebox.showerror("Error", "Gst Number seems to be Wrong, please check !!")

    if cust_name.get() == "":
        tkinter.messagebox.showerror("Error", "Empty Customer name")
        return False
    else:
        if messagebox.askyesno("Confirm Add ?", "Are you sure want to Add Customer ?"):
            cursor.execute("INSERT INTO master (name,add1,add2,add3,state,statecode,gstno,type) VALUES (?, ?, ?, ?, ?, ?, ?,?)", (cust_name.get(), cust_add1.get(), cust_add2.get(), cust_add3.get(), state.get(), state_code.get(),cust_gst.get(),"Customer"))
            conn.commit()
#            tkinter.messagebox.showinfo("Success", "Customer saved successfully !!!!")
            search()
    
def update_customer():
    cust_actual =  cust_gst.get()
    cust_upper = cust_actual.upper()
    cust_id =  t1.get()
    len_gst  = len(cust_actual)

    if len_gst != 0 :
        if len_gst != 15:
            tkinter.messagebox.showerror("Error", "Gst Number seems to be Wrong, please check !!")
         
    if cust_name.get() == "":
        tkinter.messagebox.showerror("Error", "Empty Customer name")
        return False
    else:
        if messagebox.askyesno("Confirm Update ?", "Are you sure want to Update Customer ?"):
            query = "UPDATE master SET name = ?, add1 =  ?, add2 =  ?, add3 =  ?,state = ?, statecode=?, gstno=? WHERE id = ?"
            cursor.execute(query,(cust_name.get(), cust_add1.get(), cust_add2.get(), cust_add3.get(), state.get(), state_code.get(),cust_upper, cust_id))
            conn.commit()
            search()
            clear_entryfileds()
            
    
def delete_customer():
    customer_id =  t1.get()
    if customer_id == "":
        tkinter.messagebox.showerror("Error", "Please Select the Ledger you want to delete >< Double Click !!!!")
        return False
    else:
        if messagebox.askyesno("Confirm Delete ?", "Are you sure want to delete Customer ?"):
            query = "DELETE FROM MASTER WHERE id = "+customer_id
            cursor.execute(query)
            conn.commit()
            search()
            clear_entryfileds()

def clear_entryfileds():
    cust_name.delete(0, END)
    cust_add1.delete(0, END)
    cust_add2.delete(0, END)
    cust_add3.delete(0, END)
    state.delete(0,END)
    state_code.delete(0, END)
    cust_gst.delete(0, END)
    
# wrappers             
wrapper1= tk.LabelFrame(root, text = "Customer List", width=400,height=140, bg=bgc1, fg='black')
wrapper3= tk.LabelFrame(root, text = "Customer Data",width=1298,height=340, bg=bgc2, fg="black")
wrapper1.pack(padx=10,pady=20)
wrapper3.pack(padx=10,pady=0)

# CONNECTION STRING FOR TRIEVIEW
conn = sqlite3.connect('fas.db')
conn.execute('CREATE TABLE if not exists users (id INTEGER PRIMARY KEY, type TEXT, name TEXT, add1 TEXT, add2 TEXT, add3 TEXT,state TEXT,statecode INTEGER, gstno TEXT,code INTEGER, balance INTEGER)')
cursor = conn.cursor()


#  tree view
trv =  ttk.Treeview(wrapper1, columns=(1,2,3,4,5,6,7,8,9,10,11), show="headings",height="8")
trv.heading(1, text= "ID")
trv.heading(2, text= "Group")
trv.heading(3, text= "Customer Name")
trv.heading(4, text= "Address      ")
trv.heading(5, text= "Address      ")
trv.heading(6, text= "Address      ")
trv.heading(7, text= "State   ")
trv.heading(8, text= "Code    ")
trv.heading(9, text= "GST Number   ")
trv.heading(10, text= "Code     ")
trv.heading(11, text= "Balance  ")

# double click event
trv.bind('<Double 1>',getrow)

# Set the width of the TreeView widget
trv.column(0, width=10)
trv.column(1, width=20)
trv.column(2, width=80)
trv.column(3, width=200)
trv.column(4, width=200)
trv.column(5, width=200)
trv.column(6, width=200)
trv.column(7, width=100)
trv.column(8, width=50)
trv.column(9, width=110)
trv.column(10, width=80)
trv.column(11, width=50)

yscrollbar = ttk.Scrollbar(wrapper1, orient="vertical",command=trv.yview)
yscrollbar.pack(side=RIGHT, fill = "y")
trv.configure(yscrollcommand=yscrollbar.set)
trv.pack()                

query = "SELECT * from master"
cursor.execute(query)
rows=cursor.fetchall()

# Edit menu
cust_lbl = tk.Label(wrapper3, text= "Name of Customer :", font =  fnt1, bg=bgc2, fg="Black")
cust_lbl.place(x=26, y=8)
cust_name = tk.Entry(wrapper3, width=50,font =  fnt1,textvariable=t2)
cust_name.place(x=220, y=10)

cust_lbl1 = tk.Label(wrapper3, text= "Address :", font =  fnt1, bg=bgc2, fg="Black")
cust_lbl1.place(x=114, y=45)
cust_add1 = tk.Entry(wrapper3, width=50,font =  fnt1,textvariable=t3)
cust_add1.place(x=220, y=50)

cust_add2 = tk.Entry(wrapper3, width=50,font =  fnt1,textvariable=t4)
cust_add2.place(x=220, y=90)

cust_add3 = tk.Entry(wrapper3, width=50,font =  fnt1,textvariable=t5)
cust_add3.place(x=220, y=130)

cust_lbl2 = tk.Label(wrapper3, text= "State :", font =  fnt1, bg=bgc2, fg="Black")
cust_lbl2.place(x=139, y=170)
cust_lbl3 = tk.Label(wrapper3, text= "Code :", font =  fnt1, bg=bgc2, fg="Black")
cust_lbl3.place(x=535, y=170)

cust_lbl3 = tk.Label(wrapper3, text= "GST Number :", font =  fnt1, bg=bgc2, fg="Black")
cust_lbl3.place(x=75, y=210)

state = tk.Entry(wrapper3, width=30,font =  fnt1, textvariable=t6)
state.place(x=220, y=170)

state_code = tk.Entry(wrapper3, width=11,font =  fnt1, textvariable=t7)
state_code.place(x=610, y=170)

cust_gst = tk.Entry(wrapper3, width=25,font =  fnt1, textvariable=t8)
cust_gst.place(x=220, y=210)
#cust_name.insert(0, "Enter your name")


# button 
btn_chk =  tk.Button(wrapper3, text = "Search Taxpayer URL",  width=15,height=1, cursor="hand2", bg = 'grey', command=search_url)
btn_chk.place(x=480, y=212)

btn_add =  tk.Button(wrapper3, text = "Add New", font = fnt1, cursor="hand2", width=10,bg="green",command=add_customer)
btn_add.place(x=220, y=260)

btn_update =  tk.Button(wrapper3, text = "Update", font = fnt1, cursor="hand2", width=10,bg="light Blue",command=update_customer)
btn_update.place(x=350, y=260)

btn_delete =  tk.Button(wrapper3, text = "Delete", font = fnt1, cursor="hand2", width=10,bg="red",command=delete_customer)
btn_delete.place(x=480, y=260)

btn_clear =  tk.Button(wrapper3, text = "Clear texts", font = fnt1, cursor="hand2", width=10,bg="yellow",command=clear_entryfileds)
btn_clear.place(x=610, y=260)

# search section in wrapper 2
lbl = Label(wrapper1, text= "Search",bg=bgc1, fg="Black")
lbl.pack(side=tk.LEFT, padx=10, pady=22)
ent = Entry(wrapper1, textvariable=q,font=fnt1)
ent.pack(side=tk.LEFT, padx=6)
btn = Button(wrapper1, text= "Filter",command=search, bg="light blue",font = fnt1, cursor="hand2")
btn.pack(side=tk.LEFT, padx=6)
btn_clear = Button(wrapper1, text= "Reset Tree View",command=reset_tree,bg="light grey", fg="Black",font = fnt1, cursor="hand2")
btn_clear.pack(side=tk.LEFT, padx=6)


root.title("My Application - Customer")
root.geometry("1350x750")
update(rows)

root.mainloop()


