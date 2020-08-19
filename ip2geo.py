
from ip2geotools.databases.noncommercial import DbIpCity
from tkinter import *

mw = Tk()
mw.title("Ip Location Finder")
mw.geometry("450x470")
#mw.resizable(0, 0)
mw.configure(background="#9ccc9c")

# Function for clearing regLbl lgtLbl ltLbl Labels
def clear():
    regLbl.destroy()
    lgtLbl.destroy()
    ltLbl.destroy()
    fBtn['state'] = NORMAL
#    regLbl.grid_forget()
#    lgtLbl.grid_forget()
#    ltLbl.grid_forget()

# Function for finding Data and Displaying them
def find():
    global regLbl
    global city
    global country
    global lgtLbl
    global ltLbl
    try:
        response = DbIpCity.get(ipBox.get(), api_key="free")
        reg = response.region
        city = response.city
        country = response.country
        lgt = response.longitude
        lt = response.latitude
        cc = StringVar()
        cc.set(city+" "+country)
        regLbl = Label(mw, bg="#9ccc9c", textvariable=cc, font=("Ubuntu",20))
        regLbl.grid(row=4, column=0, pady=15)
        lgtLbl = Label(mw, bg="#9ccc9c", text="Longitude: " + str(lgt), font=("Ubuntu",20))
        lgtLbl.grid(row=5, column=0)
        ltLbl = Label(mw, bg="#9ccc9c", text="Latitude: " + str(lt), font=("Ubuntu",20))
        ltLbl.grid(row=6, column=0)
    except:
        regLbl = Label(mw, bg="#9ccc9c", text='Error, try another IP', font=("Ubuntu",20))
        regLbl.grid(row=4, column=0, pady=15)
        lgtLbl = Label(mw, bg="#9ccc9c", text="Longitude: " + "not found ...", font=("Ubuntu",20))
        lgtLbl.grid(row=5, column=0)
        ltLbl = Label(mw, bg="#9ccc9c", text="Latitude: " + "not found ...", font=("Ubuntu",20))
        ltLbl.grid(row=6, column=0)
    fBtn['state'] = DISABLED
    ipBox.delete(0, END)

guidLbl = Label(mw, bg="#9ccc9c", text="Enter IP to Find Location", font=(20))
guidLbl.grid(row=0, column=0, padx=20, pady=25)

ipBox = Entry(mw, borderwidth=15, width=18, relief=FLAT, justify=CENTER, font=("Verdana", 20))
ipBox.grid(row=1, column=0, padx=55)

fBtn = Button(mw, text="Find", bg="#149414", borderwidth=0, width=1, activebackground="#4e5b31", font=("MAD hacker",30), command=find)
fBtn.grid(row=2, column=0, pady=15, ipadx=100)

clrButton = Button(mw, text="Clear Screen", bg="#149414", borderwidth=0, width=2, activebackground="#4e5b31", font=("HACKED",20), command=clear)
clrButton.grid(row=3, column=0, pady=5, ipadx=80)

mw.mainloop()
