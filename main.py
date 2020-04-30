from tkinter import *



class APP:
    def __init__(self):
        #data
        self.countries=[]
        self.criterias=[]

        self.window=Tk()
        self.window.geometry("800x550")
        self.window.config(bg="gray")
        Label(self.window,text="Coronavirus Data Analysis Tool",bg="red",font=["Arial",13],fg="white").pack(fill=BOTH)
        #image frame
        image_frame=Frame(self.window)
        image_frame.pack()

        # image canvas
        self.canvas = Canvas(image_frame, bg='gray', width=750, height=300, scrollregion=(0, 0, 2000,2000))

        #horizontal bar
        hbar = Scrollbar(image_frame, orient=HORIZONTAL)
        hbar.pack(side=BOTTOM, fill=X)
        hbar.config(command=self.canvas.xview)
        #vertical bar
        vbar = Scrollbar(image_frame, orient=VERTICAL)
        vbar.pack(side=RIGHT, fill=Y)
        vbar.config(command=self.canvas.yview)
        #vbar hbar command configs
        self.canvas.config(xscrollcommand=hbar.set, yscrollcommand=vbar.set)
        self.canvas.pack()


        # 2 buttons frame
        upload_buttons_frame = Frame(self.window,bg="gray")
        upload_buttons_frame.pack(ipady=10)
        # 2 buttons
        Button(upload_buttons_frame, text="Upload Country Data").pack(side="left",padx=30)
        Button(upload_buttons_frame, text="Upload Test Statistics").pack(side="left",padx=30)

        #bottom frame for main components
        bottom_frame=Frame(self.window,bg="gray")
        bottom_frame.pack(fill=BOTH)

        #left bottom panel
        left_bot_panel=Frame(bottom_frame,bg="gray",borderwidth=1)
        left_bot_panel.pack(side="left",padx=20,pady=10,ipadx=10,ipady=10)
        #compoennts of left bottom panel
        Label(left_bot_panel,text="Sort Countries:").pack(pady=10)
        Button(left_bot_panel,text="Sort by name").pack(pady=8)
        Button(left_bot_panel,text="Sort by total case").pack()
        #countries label
        Label(bottom_frame,fg="black",bg="gray",text="Countries:",font=["Helvetica",9]).pack(padx=7,side="left")

        #scrollable listbox left (Countries)
        scrollbar = Scrollbar(bottom_frame)
        self.countries_listbox = Listbox(bottom_frame,selectmode="multiple",exportselection=0)
        self.countries_listbox.propagate(False)
        self.countries_listbox.pack(side="left",pady=5)
        scrollbar.pack(side="left", fill=Y,pady=5)
        #debug

        self.countries_listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.countries_listbox.yview)

        # criterias label
        Label(bottom_frame, fg="black", bg="gray", text="Criterias::", font=["Helvetica", 9]).pack(padx=7, side="left")

        #scrollable listbox right (Criterias)
        scrollbar = Scrollbar(bottom_frame)
        self.criterias_listbox = Listbox(bottom_frame,selectmode="multiple",exportselection=0)
        self.criterias_listbox.propagate(False)
        self.criterias_listbox.pack(side="left",pady=5)
        scrollbar.pack(side="left", fill=Y,pady=5)

        # attach listbox to scrollbar
        self.criterias_listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.criterias_listbox.yview)

        # right bottom panel
        right_bot_panel = Frame(bottom_frame, bg="gray", borderwidth=1)
        right_bot_panel.pack(side="left", padx=20, pady=10, ipadx=10, ipady=10)
        # compoennts of left bottom panel
        Label(right_bot_panel, text="Analyse Data:").pack(pady=10)
        Button(right_bot_panel, text="Cluster Countries").pack(pady=8)
        Button(right_bot_panel, text="Cluster Criterias").pack()

        

        self.window.mainloop()

APP()
