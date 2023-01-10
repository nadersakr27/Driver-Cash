from tkinter import messagebox
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

# ---------------------------------------------
import sqlite3
data = sqlite3.connect("deriverscash.db")
mycursor  = data.cursor()
mycursor.execute("create table if not exists driveresinfo (name varchar(255) not null,id varchar(14) null,vehicle varchar(20) NULL, phone varchar(11) null);")
data.commit()
data.close()
# -----------------------------------------functions
#اضافة سائق
def addingDriver():
    name = nameEntryvar.get().strip()
    driverID = idEntryvar.get().strip()
    phone = phoneEntryvar.get().strip()
    vehicle = vehicleEntryvar.get().strip()
    if  (name=='')or not(name[0].isalpha()): #name conditions
        if (name==''):
            messagebox.showerror("خطــأ فــي ادخــال اســم الســائــق","برجـاء ادخــال اســم السائــق")
        else :
            messagebox.showerror("خطــأ فــي ادخــال اســم الســائــق","برجـاء ازالــة الارقــام والعلامــات مــن الاســم")
    else :
        if (len(driverID)!= 14  or not((driverID).isdigit()) ) and (driverID!=''): #id conditions
            messagebox.showerror("خطــأ فــي ادخــال رقــم البطــاقــة","برجـاء ادخــال رقــم البطــاقة مكــون من 14 رقــم")
        else:
            if ((len(phone)!=11) or not(phone[0]=='0')or not(phone[1]=='1') or not(phone.isdigit()) )and phone!='': #phone conditions
                messagebox.showerror("خطــأ فــي ادخــال رقــم الهاتــف","برجـاء ادخــال رقــم الهاتــف مكــون من 11 رقــم يبــدء بــ 01")
            else :
                if (len(vehicle)>20) :# vechial conditions
                    messagebox.showerror("خطــأ فــي ادخــال رقــم لوحــة المركبــة","ادخــال لوحــة المركبــة اكبــر مــن الــلازم")
                else:
                    # reset 0 to optinal values
                    if (vehicle==''):
                        vehicle='0'
                    if (driverID==''):
                        driverID ='0'  
                    if (phone==''):
                        phone = '0'
                    #اضافة السائق في قاعدة البيانات
                    data = sqlite3.connect("deriverscash.db")
                    mycursor = data.cursor()
                    # check if there is driver with that name or not
                    checkMultiplableString = f'select name from driveresinfo where name = "{name}"'
                    mycursor.execute(checkMultiplableString)
                    names = mycursor.fetchall()
                    if len(names) >= 1 :
                        # if yes message to tryagin
                        messagebox.showwarning("تكــرار السائــق","يوجــد سائــق بهــذا الاســم")
                    else:
                        print(len(names))
                        stringAddingInfo=f"insert into driveresinfo values('{name}','{driverID}','{vehicle}','{phone}')"
                        # string Make a Table for driver
                        driverTable=f"create table {name} (ty1 INT NULL , ty2 INT NULL ,aprove INT NUll , dis INT NULL) "
                        print(stringAddingInfo)
                        print(driverTable)
                        try:
                            mycursor.execute(stringAddingInfo)
                            mycursor.execute(driverTable)
                            messagebox.showinfo("عمليــة ناجحــة","تــم اضافــة السائــق بنجــاح")
                        except:
                            messagebox.showerror("خطــأ فــي ادخــال البيانــات","برجـاء مراجعــة البيانــات والمحاولــة مــرة أخــري")
                    data.commit()
                    data.close()
# ------------------------------------------
def editingInfo():
    pass
# -------------------------------------------
def deleteDriver() :
    pass
# -------------------------------------------





# -----------------------------------------------
def but():
    print(dateEntry.entry.get())
# ===========================================
title = "DeriverCash"
# -------------------------------------------
xpad = 30 
ypad = 30 
# ---------------------------------
widthOfOrderFram=  880
heightOfOrderFram= 350 
xOfOrderFram= 986.6666
yOfOrderFram= 420
# -------------------------------------
widthOfderiverFram= 880 
heightOfderiverFram= 280 
xOfderiverFram= 986.6666
yOfderiverFram= 140
# ---------------------------------------
widthOffilterFram= 880 
heightOffilterFram= 140 
xOffilterFram= 986.6666
yOffilterFram= 0
# ---------------------------------------
widthoforderTableFram = 880
heightoforderTableFram = 350
xOfOrderTableFram= 53.3
yOfOrderTableFram= 0
# ----------------------------------------
widthofpaidTableFram = 880
heightofpaidTableFram = 140
xOfpaidTableFram= 53.3
yOfpaidTableFram= 350
# -----------------------------------
widthofinfoFram = 880
heightofinfoFram = 280
xOfinfoFram= 53.3
yOfinfoFram= 490
# -----------------------------------
win = ttk.Window(resizable=(False, False),title=title)
win.geometry("1920x990+0+0")
# قسم الطلبات 
ordersFram = ttk.LabelFrame(win,text="  اضـافـة  الطلـبـات  ",width=widthOfOrderFram,height=heightOfOrderFram,relief="ridge",labelanchor='ne')
# المحتويات
insideFram1 = ttk.Frame(ordersFram,width=widthOfOrderFram)
insideFram1.pack(side=TOP)
# ------------------------
firstTypeEntryvar = ttk.StringVar()
firstTypeEntry = ttk.Entry(insideFram1,textvariable=firstTypeEntryvar,)
firstTypeEntry.grid(row=0,column=0,padx=xpad,pady=ypad)
firstTypelabel = ttk.Label(insideFram1,text="الخارجــي",)
firstTypelabel.grid(row=0,column=1,pady=ypad)
# ----------------
secondTypeEntryvar = ttk.StringVar()
secondTypeEntry = ttk.Entry(insideFram1,textvariable=secondTypeEntryvar,)
secondTypeEntry.grid(row=0,column=2,padx=xpad,pady=ypad)
secondTypelabel = ttk.Label(insideFram1,text="الداخلــي",)
secondTypelabel.grid(row=0,column=3,pady=ypad)
# ----------------
apoveEntryvar = ttk.StringVar()
apoveEntry = ttk.Entry(insideFram1,bootstyle="success",textvariable=apoveEntryvar,)
apoveEntry.grid(row=1,column=0,padx=xpad,pady=0)
apovelabel = ttk.Label(insideFram1,text="<الحافــز <ج",)
apovelabel.grid(row=1,column=1,pady=0)
# ----------------
disEntryvar = ttk.StringVar()
disEntry = ttk.Entry(insideFram1,bootstyle="danger",textvariable=disEntryvar,)
disEntry.grid(row=1,column=2,padx=xpad,pady=0)
dislabel = ttk.Label(insideFram1,text="<الخصــم <ج",)
dislabel.grid(row=1,column=3,pady=0)
# ----------------
paidEntryvar = ttk.StringVar()
paidEntry = ttk.Entry(insideFram1,bootstyle="warning",textvariable=paidEntryvar,)
paidEntry.grid(row=2,column=0,padx=xpad,pady=ypad)
paidlabel = ttk.Label(insideFram1,text="<المدفــوع <ج",)
paidlabel.grid(row=2,column=1,pady=ypad)
# --------------------------
dateEntry = ttk.DateEntry(insideFram1)
# dateEntry.entry.state(['readonly'])
dateEntry.configure(width=17)
dateEntry.grid(row=2,column=2,padx=xpad,pady=ypad)
datelabel = ttk.Label(insideFram1,text="التاريــخ",)
datelabel.grid(row=2,column=3,pady=ypad)
# -----------------------------
insideFram2 = ttk.Frame(ordersFram,width=widthOfOrderFram,height=50)
insideFram2.pack()
# ---------------------------------
addOrderButton = ttk.Button(insideFram2,text="اضافــة الطلــب",bootstyle = "success")
addOrderButton.configure(width=20)
addOrderButton.place(x = 640,y=30,anchor='center')
# -----------------------------------
editOrderButton = ttk.Button(insideFram2,text="تعديــل")
editOrderButton.configure(width=10)
editOrderButton.place(x = 320,y=30,anchor='center')
# ------------------------------------
deleteOrderButton = ttk.Button(insideFram2,text="حــذف",bootstyle = "danger")
deleteOrderButton.configure(width=10)
deleteOrderButton.place(x = 130,y=30,anchor='center')
# ------------------------------------
ordersFram.place(x=xOfOrderFram,y=yOfOrderFram,width=widthOfOrderFram,height=heightOfOrderFram)
# ------------------------------------------------
# قسم الطلبات 
deriverFram = ttk.LabelFrame(win,text="  اضـافـة  سائــق  ",width=widthOfOrderFram,height=heightOfOrderFram,relief="ridge",labelanchor='ne')
# المحتويات
insideDeriverFram1 = ttk.Frame(deriverFram,width=widthOfOrderFram)
insideDeriverFram1.pack(side=TOP)
# ------------------------
nameEntryvar = ttk.StringVar()
nameEntry = ttk.Entry(insideDeriverFram1,textvariable=nameEntryvar,)
nameEntry.grid(row=0,column=2,padx=xpad,pady=ypad)
namelabel = ttk.Label(insideDeriverFram1,text="الاســم",)
namelabel.grid(row=0,column=3,pady=ypad)
# ----------------
idEntryvar = ttk.StringVar()
idEntry = ttk.Entry(insideDeriverFram1,textvariable=idEntryvar,)
idEntry.grid(row=0,column=0,padx=xpad,pady=ypad)
idlabel = ttk.Label(insideDeriverFram1,text="رقــم البطاقــة",)
idlabel.grid(row=0,column=1,pady=ypad)
# ----------------
phoneEntryvar = ttk.StringVar()
phoneEntry = ttk.Entry(insideDeriverFram1,textvariable=phoneEntryvar,)
phoneEntry.grid(row=1,column=2,padx=xpad,pady=0)
phonelabel = ttk.Label(insideDeriverFram1,text="رقــم الهاتــف",)
phonelabel.grid(row=1,column=3,pady=0)
# ----------------
vehicleEntryvar = ttk.StringVar()
vehicleEntry = ttk.Entry(insideDeriverFram1,textvariable=vehicleEntryvar,)
vehicleEntry.grid(row=1,column=0,padx=xpad,pady=0)
vehiclelabel = ttk.Label(insideDeriverFram1,text="لوحــة المــركبــة",)
vehiclelabel.grid(row=1,column=1,pady=0)
# ---------------------------------------------------------------
insideDeriverFram2 = ttk.Frame(deriverFram,width=widthOfOrderFram,height=80)
insideDeriverFram2.pack()
# ---------------------------------
addOrderButton = ttk.Button(insideDeriverFram2,text="اضافــة الســائق",bootstyle = "success",command=addingDriver)
addOrderButton.configure(width=20)
addOrderButton.place(x = 640,y=30,anchor='n')
# -----------------------------------
editOrderButton = ttk.Button(insideDeriverFram2,text="تعديــل")
editOrderButton.configure(width=10)
editOrderButton.place(x = 320,y=30,anchor='n')
# ------------------------------------
deleteOrderButton = ttk.Button(insideDeriverFram2,text="حــذف",bootstyle = "danger")
deleteOrderButton.configure(width=10)
deleteOrderButton.place(x = 130,y=30,anchor='n')
# --------------------------------------
deriverFram.place(x=xOfderiverFram,y=yOfderiverFram,width=widthOfderiverFram,height=heightOfderiverFram)
# ------------------------------------
# قسم البحث والفلترة
filterFram = ttk.LabelFrame(win,text="  فلتــرة الطلبــات  ",width=widthOfOrderFram,height=heightOfOrderFram,relief="ridge",labelanchor='ne')
# المحتويات
choiceNameVar = ttk.StringVar()
choiceName = ttk.Combobox(filterFram,state='readonly',textvariable=choiceNameVar,bootstyle='success')
choiceName.config(width=18)
choiceNameVar.set("اختـار الســائــق")
choiceName.grid(row=0,column=2,padx=xpad,pady=ypad)
# -----------------------------------
choicemonthVar = ttk.StringVar()
choicemonth = ttk.Combobox(filterFram,state='readonly',textvariable=choicemonthVar,)
choicemonth.config(width=18)
choicemonthVar.set("اختـار الشهــر")
choicemonth.grid(row=0,column=1,padx=xpad,pady=ypad)
# ------------------------------------
choiceyearVar = ttk.StringVar()
choiceyear = ttk.Combobox(filterFram,state='readonly',textvariable=choiceyearVar,)
choiceyear.config(width=18)
choiceyearVar.set("اختـار السنــة")
choiceyear.grid(row=0,column=0,padx=xpad,pady=ypad)
# ----------------------------------------------
filterFram.place(x=xOffilterFram,y=yOffilterFram,width=widthOffilterFram,height=heightOffilterFram)
# ----------------------------------------------
#عرض الداتا
# 
# عرض الطلبات 
orderTableFram= ttk.Frame(win)
# create scrollx,y
# scrollx = ttk.Scrollbar(orderTableFram,orient="horizontal")
# scrollx.pack(side=BOTTOM,fill=X)
scrolly = ttk.Scrollbar(orderTableFram,orient="vertical")
scrolly.pack(side=RIGHT,fill=Y)
# --------------------------------------------------------
# create the table
orderTable = ttk.Treeview(orderTableFram,columns=("date","ty1","ty2","aprove","dis","tot"),yscrollcommand=scrolly.set)
# config scrollers
# scrollx.config(command=orderTable.xview)
scrolly.config(command=orderTable.yview)
# ------------------------------------
orderTable.heading("date",text="التــاريــخ")
orderTable.heading("ty1",text="الداخلــي")
orderTable.heading("ty2",text="الخارجــي")
orderTable.heading("aprove",text="<الحافــز <ج")
orderTable.heading("dis",text="<الخصــم <ج")
orderTable.heading("tot",text="مجموع اليوم",)
# -----------------------------------------------------
orderTable.column( "date",width=110,anchor=CENTER)
orderTable.column( "ty1",width=110,anchor=CENTER)
orderTable.column("ty2",width=110,anchor=CENTER)
orderTable.column( "aprove",width=120,anchor=CENTER)
orderTable.column("dis",width=120,anchor=CENTER)
orderTable.column("tot",width=130,anchor=CENTER)
orderTable["show"]="headings"
orderTable.pack(fill=BOTH,expand=2)
# ---------------------------------
orderTableFram.place(x=xOfOrderTableFram,y=yOfOrderTableFram,width=widthoforderTableFram,height=heightoforderTableFram)
# --------------------------------

# عرض الدفع
paidTableFram= ttk.Frame(win)
# create scrollxofpaidtable,y
# scrollxofpaidtable = ttk.Scrollbar(paidTableFram,orient="horizontal")
# scrollxofpaidtable.pack(side=BOTTOM,fill=X)
scrollyofpaidtable = ttk.Scrollbar(paidTableFram,orient="vertical")
scrollyofpaidtable.pack(side=RIGHT,fill=Y)
# --------------------------------------------------------
# create the table
paidTable = ttk.Treeview(paidTableFram,columns=("date","total","paid","remind"),yscrollcommand=scrollyofpaidtable.set)
# config scrollers
# scrollxofpaidtable.config(command=paidTable.xview)
scrollyofpaidtable.config(command=paidTable.yview)
# ------------------------------------
paidTable.heading("date",text="التــاريــخ")
paidTable.heading("total",text="الحساب")
paidTable.heading("paid",text="المدفوع")
paidTable.heading("remind",text="المتبقي")
# -----------------------------------------------------
paidTable.column( "date",width=110,anchor=CENTER)
paidTable.column( "total",width=110,anchor=CENTER)
paidTable.column("paid",width=110,anchor=CENTER)
paidTable.column( "remind",width=110,anchor=CENTER)
paidTable["show"]="headings"
paidTable.pack(fill=BOTH,expand=2)
# ---------------------------------
paidTableFram.place(x=xOfpaidTableFram,y=yOfpaidTableFram,width=widthofpaidTableFram,height=heightofpaidTableFram)
# --------------------------------


# عرض البيانات
infoFram= ttk.Frame(win,relief=RIDGE)

infoFram.place(x=xOfinfoFram,y=yOfinfoFram,width=widthofinfoFram,height=heightofinfoFram)
# --------------------------------






win.mainloop()
