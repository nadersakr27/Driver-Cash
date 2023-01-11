from tkinter import messagebox
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
# ---------------------------------------------
import sqlite3
data = sqlite3.connect("deriverscash.db")
mycursor  = data.cursor()
mycursor.execute("create table if not exists driveresinfo (name varchar(255) not null,id varchar(14) null,vehicle varchar(20) NULL,phone varchar(11) null);")
data.commit()
data.close()
# ------------------------------------------------
driversnames=[]
title = 'DriverCash'
class Drivercash :
    def __init__(self,win) :
    # first feching data
       
        # -------------------------------------------
        self.title = "DeriverCash"
        self.xpad = 30 
        self.ypad = 30 
        # ---------------------------------
        self.widthOforderFram=  880
        self.heightOforderFram= 350 
        self.xOforderFram= 986.6666
        self.yOforderFram= 420
        # -------------------------------------
        self.widthOfderiverFram= 880 
        self.heightOfderiverFram= 280 
        self.xOfderiverFram= 986.6666
        self.yOfderiverFram= 140
        # ---------------------------------------
        self.widthOffilterFram= 880 
        self.heightOffilterFram= 140 
        self.xOffilterFram= 986.6666
        self.yOffilterFram= 0
        # ---------------------------------------
        self.widthOforderTableFram = 880
        self.heightOforderTableFram = 350
        self.xOforderTableFram= 53.3
        self.yOforderTableFram= 0
        # ----------------------------------------
        self.widthOfpaidTableFram = 880
        self.heightOfpaidTableFram = 140
        self.xOfpaidTableFram= 53.3
        self.yOfpaidTableFram= 350
        # -----------------------------------
        self.widthOfinfoFram = 880
        self.heightOfinfoFram = 280
        self.xOfinfoFram= 53.3
        self.yOfinfoFram= 490
        # -----------------------------------
        
        win.geometry("1920x990+0+0")
        # قسم الطلبات 
        self.ordersFram = ttk.LabelFrame(win,text="  اضـافـة  الطلـبـات  ",width=self.widthOforderFram,height=self.heightOforderFram,relief="ridge",labelanchor='ne')
        # المحتويات
        self.insideFram1 = ttk.Frame(self.ordersFram,width=self.widthOforderFram)
        self.insideFram1.pack(side=TOP)
        # ------------------------
        self.firstTypeEntryvar = ttk.StringVar()
        self.firstTypeEntry = ttk.Entry(self.insideFram1,textvariable=self.firstTypeEntryvar,)
        self.firstTypeEntry.grid(row=0,column=0,padx=self.xpad,pady=self.ypad)
        self.firstTypelabel = ttk.Label(self.insideFram1,text="الخارجــي",)
        self.firstTypelabel.grid(row=0,column=1,pady=self.ypad)
        # ----------------
        self.secondTypeEntryvar = ttk.StringVar()
        self.secondTypeEntry = ttk.Entry(self.insideFram1,textvariable=self.secondTypeEntryvar,)
        self.secondTypeEntry.grid(row=0,column=2,padx=self.xpad,pady=self.ypad)
        self.secondTypelabel = ttk.Label(self.insideFram1,text="الداخلــي",)
        self.secondTypelabel.grid(row=0,column=3,pady=self.ypad)
        # ----------------
        self.apoveEntryvar = ttk.StringVar()
        self.apoveEntry = ttk.Entry(self.insideFram1,bootstyle="success",textvariable=self.apoveEntryvar,)
        self.apoveEntry.grid(row=1,column=0,padx=self.xpad,pady=0)
        self.apovelabel = ttk.Label(self.insideFram1,text="<الحافــز <ج",)
        self.apovelabel.grid(row=1,column=1,pady=0)
        # ----------------
        self.disEntryvar = ttk.StringVar()
        self.disEntry = ttk.Entry(self.insideFram1,bootstyle="danger",textvariable=self.disEntryvar,)
        self.disEntry.grid(row=1,column=2,padx=self.xpad,pady=0)
        self.dislabel = ttk.Label(self.insideFram1,text="<الخصــم <ج",)
        self.dislabel.grid(row=1,column=3,pady=0)
        # ----------------
        self.idEntryvar = ttk.StringVar()
        self.idEntry = ttk.Entry(self.insideFram1,bootstyle="warning",textvariable=self.idEntryvar,)
        self.idEntry.grid(row=2,column=0,padx=self.xpad,pady=self.ypad)
        self.idlabel = ttk.Label(self.insideFram1,text="<المدفــوع <ج",)
        self.idlabel.grid(row=2,column=1,pady=self.ypad)
        # --------------------------
        self.dateEntry = ttk.DateEntry(self.insideFram1)
        # self.dateEntry.entry.state(['readonly'])
        self.dateEntry.configure(width=17)
        self.dateEntry.grid(row=2,column=2,padx=self.xpad,pady=self.ypad)
        self.dateLable = ttk.Label(self.insideFram1,text="التاريــخ",)
        self.dateLable.grid(row=2,column=3,pady=self.ypad)
        # -----------------------------
        self.insideFram2 = ttk.Frame(self.ordersFram,width=self.widthOforderFram,height=50)
        self.insideFram2.pack()
        # ---------------------------------
        self.addOrderButton = ttk.Button(self.insideFram2,text="اضافــة الطلــب",bootstyle = "success")
        self.addOrderButton.configure(width=20)
        self.addOrderButton.place(x = 640,y=30,anchor='center')
        # -----------------------------------
        self.editOrderButton = ttk.Button(self.insideFram2,text="تعديــل")
        self.editOrderButton.configure(width=10)
        self.editOrderButton.place(x = 320,y=30,anchor='center')
        # ------------------------------------
        self.deleteOrderButton = ttk.Button(self.insideFram2,text="حــذف",bootstyle = "danger")
        self.deleteOrderButton.configure(width=10)
        self.deleteOrderButton.place(x = 130,y=30,anchor='center')
        # ------------------------------------
        self.ordersFram.place(x=self.xOforderFram,y=self.yOforderFram,width=self.widthOforderFram,height=self.heightOforderFram)
        # ------------------------------------------------
        # قسم الطلبات 
        self.deriverFram = ttk.LabelFrame(win,text="  اضـافـة  سائــق  ",width=self.widthOforderFram,height=self.heightOforderFram,relief="ridge",labelanchor='ne')
        # المحتويات
        self.insideDriverFrame1 = ttk.Frame(self.deriverFram,width=self.widthOforderFram)
        self.insideDriverFrame1.pack(side=TOP)
        # ------------------------
        self.nameEntryvar = ttk.StringVar()
        self.nameEntry = ttk.Entry(self.insideDriverFrame1,textvariable=self.nameEntryvar,)
        self.nameEntry.grid(row=0,column=2,padx=self.xpad,pady=self.ypad)
        self.namelabel = ttk.Label(self.insideDriverFrame1,text="الاســم",)
        self.namelabel.grid(row=0,column=3,pady=self.ypad)
        # ----------------
        self.idEntryvar = ttk.StringVar()
        self.idEntry = ttk.Entry(self.insideDriverFrame1,textvariable=self.idEntryvar,)
        self.idEntry.grid(row=0,column=0,padx=self.xpad,pady=self.ypad)
        self.idlabel = ttk.Label(self.insideDriverFrame1,text="رقــم البطاقــة",)
        self.idlabel.grid(row=0,column=1,pady=self.ypad)
        # ----------------
        self.phoneEntryvar = ttk.StringVar()
        self.phoneEntry = ttk.Entry(self.insideDriverFrame1,textvariable=self.phoneEntryvar,)
        self.phoneEntry.grid(row=1,column=2,padx=self.xpad,pady=0)
        self.phonelabel = ttk.Label(self.insideDriverFrame1,text="رقــم الهاتــف",)
        self.phonelabel.grid(row=1,column=3,pady=0)
        # ----------------
        self.vehicleEntryvar = ttk.StringVar()
        self.vehicleEntry = ttk.Entry(self.insideDriverFrame1,textvariable=self.vehicleEntryvar,)
        self.vehicleEntry.grid(row=1,column=0,padx=self.xpad,pady=0)
        self.vehiclelabel = ttk.Label(self.insideDriverFrame1,text="لوحــة المــركبــة",)
        self.vehiclelabel.grid(row=1,column=1,pady=0)
        # ---------------------------------------------------------------
        self.insideDeriverFram2 = ttk.Frame(self.deriverFram,width=self.widthOforderFram,height=80)
        self.insideDeriverFram2.pack()
        # ---------------------------------
        self.addOrderButton = ttk.Button(self.insideDeriverFram2,text="اضافــة الســائق",bootstyle = "success",command=self.addingDriver)
        self.addOrderButton.configure(width=20)
        self.addOrderButton.place(x = 640,y=30,anchor='n')
        # -----------------------------------
        self.editOrderButton = ttk.Button(self.insideDeriverFram2,text="تعديــل")
        self.editOrderButton.configure(width=10)
        self.editOrderButton.place(x = 320,y=30,anchor='n')
        # ------------------------------------
        self.deleteOrderButton = ttk.Button(self.insideDeriverFram2,text="حــذف",bootstyle = "danger")
        self.deleteOrderButton.configure(width=10)
        self.deleteOrderButton.place(x = 130,y=30,anchor='n')
        # --------------------------------------
        self.deriverFram.place(x=self.xOfderiverFram,y=self.yOfderiverFram,width=self.widthOfderiverFram,height=self.heightOfderiverFram)
        # ------------------------------------
        # قسم البحث والفلترة
        self.filterFram = ttk.LabelFrame(win,text="  فلتــرة الطلبــات  ",width=self.widthOforderFram,height=self.heightOforderFram,relief="ridge",labelanchor='ne')
        # المحتويات
        self.choicenameVar = ttk.StringVar()
        self.choicename = ttk.Combobox(self.filterFram,state='readonly',textvariable=self.choicenameVar,bootstyle='success')
        self.choicename.config(width=17)
        self.choicenameVar.set("اختـار الســائــق")
        self.choicename.grid(row=0,column=2,padx=self.xpad+28,pady=self.ypad)
        self.fechInfonameComb()
        self.choicename.bind("<<ComboboxSelected>>",self.viewInfoData)
        # -----------------------------------
        self.choicemonthVar = ttk.StringVar()
        self.choicemonth = ttk.Combobox(self.filterFram,state='readonly',textvariable=self.choicemonthVar,)
        self.choicemonth.config(width=17)
        self.choicemonthVar.set("اختـار الشهــر")
        self.choicemonth.grid(row=0,column=1,padx=self.xpad-28,pady=self.ypad)
        # ------------------------------------
        self.choiceyearVar = ttk.StringVar()
        self.choiceyear = ttk.Combobox(self.filterFram,state='readonly',textvariable=self.choiceyearVar,)
        self.choiceyear.config(width=17)
        self.choiceyearVar.set("اختـار السنــة")
        self.choiceyear.grid(row=0,column=0,padx=self.xpad+28,pady=self.ypad)
        # ----------------------------------------------
        self.filterFram.place(x=self.xOffilterFram,y=self.yOffilterFram,width=self.widthOffilterFram,height=self.heightOffilterFram)
        # ----------------------------------------------
        #عرض الداتا
        # 
        # عرض الطلبات 
        self.orderTableFram= ttk.Frame(win)
        # create scrollx,y
        # scrollx = ttk.Scrollbar(self.orderTableFram,orient="horizontal")
        # scrollx.pack(side=BOTTOM,fill=X)
        self.scrolly = ttk.Scrollbar(self.orderTableFram,orient="vertical")
        self.scrolly.pack(side=RIGHT,fill=Y)
        # --------------------------------------------------------
        # create the table
        self.orderTable = ttk.Treeview(self.orderTableFram,columns=("date","ty1","ty2","aprove","dis","tot"),yscrollcommand=self.scrolly.set)
        # config scrollers
        # scrollx.config(command=self.orderTable.xview)
        self.scrolly.config(command=self.orderTable.yview)
        # ------------------------------------
        self.orderTable.heading("date",text="التــاريــخ")
        self.orderTable.heading("ty1",text="الداخلــي")
        self.orderTable.heading("ty2",text="الخارجــي")
        self.orderTable.heading("aprove",text="<الحافــز <ج")
        self.orderTable.heading("dis",text="<الخصــم <ج")
        self.orderTable.heading("tot",text="مجموع اليوم",)
        # -----------------------------------------------------
        self.orderTable.column( "date",width=110,anchor=CENTER)
        self.orderTable.column( "ty1",width=110,anchor=CENTER)
        self.orderTable.column("ty2",width=110,anchor=CENTER)
        self.orderTable.column( "aprove",width=120,anchor=CENTER)
        self.orderTable.column("dis",width=120,anchor=CENTER)
        self.orderTable.column("tot",width=130,anchor=CENTER)
        self.orderTable["show"]="headings"
        self.orderTable.pack(fill=BOTH,expand=2)
        # ---------------------------------
        self.orderTableFram.place(x=self.xOforderTableFram,y=self.yOforderTableFram,width=self.widthOforderTableFram,height=self.heightOforderTableFram)
        # --------------------------------
        # عرض الدفع
        self.paidTableFram= ttk.Frame(win)
        # create scrollxOfpaidtable,y
        # scrollxOfpaidtable = ttk.Scrollbar(self.paidTableFram,orient="horizontal")
        # scrollxOfpaidtable.pack(side=BOTTOM,fill=X)
        self.scrollyofpaidtable = ttk.Scrollbar(self.paidTableFram,orient="vertical")
        self.scrollyofpaidtable.pack(side=RIGHT,fill=Y)
        # --------------------------------------------------------
        # create the table
        self.paidTable = ttk.Treeview(self.paidTableFram,columns=("date","total","self.paid","remind"),yscrollcommand=self.scrollyofpaidtable.set)
        # config scrollers
        # scrollxOfpaidtable.config(command=self.paidTable.xview)
        self.scrollyofpaidtable.config(command=self.paidTable.yview)
        # ------------------------------------
        self.paidTable.heading("date",text="التــاريــخ")
        self.paidTable.heading("total",text="الحساب")
        self.paidTable.heading("self.paid",text="المدفوع")
        self.paidTable.heading("remind",text="المتبقي")
        # -----------------------------------------------------
        self.paidTable.column( "date",width=110,anchor=CENTER)
        self.paidTable.column( "total",width=110,anchor=CENTER)
        self.paidTable.column("self.paid",width=110,anchor=CENTER)
        self.paidTable.column( "remind",width=110,anchor=CENTER)
        self.paidTable["show"]="headings"
        self.paidTable.pack(fill=BOTH,expand=2)
        # ---------------------------------
        self.paidTableFram.place(x=self.xOfpaidTableFram,y=self.yOfpaidTableFram,width=self.widthOfpaidTableFram,height=self.heightOfpaidTableFram)
        # --------------------------------
        # عرض البيانات
        self.infoFram= ttk.Frame(win,relief=RIDGE)
        self.insideframeinfo1 = ttk.Frame(self.infoFram,relief=RIDGE,height=140)
        self.insideframeinfo1.place(x=0,y=0,height=0.5*self.heightOfinfoFram,width=self.widthOfinfoFram)
        self.viewnamevar = ttk.StringVar()
        self.stringname =  ttk.Label(self.insideframeinfo1 ,text=" : الاســم",font=("",15,"bold"))
        self.viewname= ttk.Label(self.insideframeinfo1,text="نادر ناصر صقر " ,font=("",18,"bold"))
        self.stringname.grid(row=1,column=3)
        self.viewname.grid(row=1,column=2,pady=self.ypad,padx=self.xpad+25)
# ---------------------------------------------------------------------------
        self.viewidvar = ttk.StringVar()
        self.stringid =  ttk.Label(self.insideframeinfo1 ,text=": رقــم البطاقــة",font=("",15,"bold"))
        self.viewid= ttk.Label(self.insideframeinfo1,text="30106291100454" ,font=("",18,"bold"))
        self.stringid.grid(row=1,column=1)
        self.viewid.grid(row=1,column=0,pady=self.ypad+20,padx=self.xpad+25) 
# ---------------------------------------------------------------------
        self.insideframeinfo2 = ttk.Frame(self.infoFram,relief=RIDGE)
        self.insideframeinfo2.place(x=0,y=0.5*self.heightOfinfoFram,height=0.5*self.heightOfinfoFram,width=self.widthOfinfoFram)
        self.viewphonevar = ttk.StringVar()
        self.stringphone =  ttk.Label(self.insideframeinfo2 ,text=" : رقــم الهاتــف",font=("",15,"bold"))
        self.viewphone= ttk.Label(self.insideframeinfo2,text="01288235749" ,font=("",18,"bold"))
        self.stringphone.grid(row=1,column=3)
        self.viewphone.grid(row=1,column=2,pady=self.ypad,padx=self.xpad+25)
# ---------------------------------------------------------------------------
        self.viewvehiclevar = ttk.StringVar()
        self.stringvehicle =  ttk.Label(self.insideframeinfo2 ,text=" : رقــم المركبة",font=("",15,"bold"))
        self.viewvehicle= ttk.Label(self.insideframeinfo2,text="1051س م ص" ,font=("",18,"bold"))
        self.stringvehicle.grid(row=1,column=1)
        self.viewvehicle.grid(row=1,column=0,pady=self.ypad+20,padx=self.xpad+25) 
# ---------------------------------------------------------------------
    
# ---------------------------------------------------------------------
        self.infoFram.place(x=self.xOfinfoFram,y=self.yOfinfoFram,width=self.widthOfinfoFram,height=self.heightOfinfoFram)
        # -----------------------------------------functions
    #اضافة سائق
    def addingDriver(self):
        self.name = self.nameEntryvar.get().strip()
        self.driverID = self.idEntryvar.get().strip()
        self.phone = self.phoneEntryvar.get().strip()
        self.vehicle = self.vehicleEntryvar.get().strip()
        if  (self.name=='')or not(self.name[0].isalpha()): #self.name conditions
            if (self.name==''):
                messagebox.showerror("خطــأ فــي ادخــال اســم الســائــق","برجـاء ادخــال اســم السائــق")
            else :
                messagebox.showerror("خطــأ فــي ادخــال اســم الســائــق","برجـاء ازالــة الارقــام والعلامــات مــن الاســم")
        else :
            if (len(self.driverID)!= 14  or not((self.driverID).isdigit()) ) and (self.driverID!=''): #id conditions
                messagebox.showerror("خطــأ فــي ادخــال رقــم البطــاقــة","برجـاء ادخــال رقــم البطــاقة مكــون من 14 رقــم")
            else:
                if ((len(self.phone)!=11) or not(self.phone[0]=='0')or not(self.phone[1]=='1') or not(self.phone.isdigit()) )and self.phone!='': #self.phone conditions
                    messagebox.showerror("خطــأ فــي ادخــال رقــم الهاتــف","برجـاء ادخــال رقــم الهاتــف مكــون من 11 رقــم يبــدء بــ 01")
                else :
                    if (len(self.vehicle)>20) :# vechial conditions
                        messagebox.showerror("خطــأ فــي ادخــال رقــم لوحــة المركبــة","ادخــال لوحــة المركبــة اكبــر مــن الــلازم")
                    else:
                        # reset 0 to optinal values
                        if (self.vehicle==''):
                            self.vehicle='0'
                        if (self.driverID==''):
                            self.driverID ='0'  
                        if (self.phone==''):
                            self.phone = '0'
                        #اضافة السائق في قاعدة البيانات
                        data = sqlite3.connect("deriverscash.db")
                        mycursor = data.cursor()
                        # check if there is driver with that self.name or not
                        checkMultiplableString = f'select name from driveresinfo where name = "{self.name}"'
                        mycursor.execute(checkMultiplableString)
                        self.names = mycursor.fetchall()
                        if len(self.names) >= 1 :
                            # if yes message to tryagin
                            messagebox.showwarning("تكــرار السائــق","يوجــد سائــق بهــذا الاســم")
                        else:
                            print(len(self.names))
                            stringaddingInfo=f"insert into driveresinfo values('{self.name}','{self.driverID}','{self.vehicle}','{self.phone}')"
                            # string Make a Table for driver
                            driverTable=f"create table {self.name} (ty1 INT NULL , ty2 INT NULL ,aprove INT NUll , dis INT NULL) "
                            print(stringaddingInfo)
                            print(driverTable)
                            try:
                                mycursor.execute(stringaddingInfo)
                                # mycursor.execute(driverTable)
                                # driversnames.append(self.nameEntryvar.get())
                                # self.choicename['values']= driversnames
                                messagebox.showinfo("عمليــة ناجحــة","تــم اضافــة السائــق بنجــاح")
                            except:
                                messagebox.showerror("خطــأ فــي ادخــال البيانــات","برجـاء مراجعــة البيانــات والمحاولــة مــرة أخــري")
                        data.commit()
                        data.close()     
    # ------------------------------------------
    def editingInfo():
        pass
    # -------------------------------------------
    def viewInfoData(self,*args):
        self.viewNamevar.set(self.choicename.get())
    # -------------------------------------------
    def deleteDriver(self) :
        pass
    # -------------------------------------------
    def fechInfonameComb(self,):
        data = sqlite3.connect("deriverscash.db")
        mycursor = data.cursor() 
        stringnames="select name from driveresinfo"
        mycursor.execute(stringnames)
        
        rows = mycursor.fetchall()
        for i in range(len(rows)):
            driversnames.append(rows[i][0])
        data.commit()
        data.close()
        self.choicename['values'] = driversnames
    # ===========================================
if __name__=="__main__":
    win =  ttk.Window(resizable=(False, False),title=title)
    obj = Drivercash(win)
    win.mainloop()
    # -------------------------------------------
