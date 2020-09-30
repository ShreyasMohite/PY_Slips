





from tkinter import *
import tkinter.messagebox
from tkinter import ttk
import datetime
import slipbackend




class Slip:
    def __init__(self,root):
        self.root=root
        self.root.title("Slip")
        self.root.geometry("500x550")
        self.root.resizable(0,0)
        self.root.iconbitmap("lista.ico")

        

    #=====================================================================

        def on_enter1(e):
            but_save['background']="black"
            but_save['foreground']="cyan"  
        def on_leave1(e):
            but_save['background']="SystemButtonFace"
            but_save['foreground']="SystemButtonText"

            

        def on_enter2(e):
            but_update['background']="black"
            but_update['foreground']="cyan"  
        def on_leave2(e):
            but_update['background']="SystemButtonFace"
            but_update['foreground']="SystemButtonText"



        def on_enter3(e):
            but_delete['background']="black"
            but_delete['foreground']="cyan"  
        def on_leave3(e):
            but_delete['background']="SystemButtonFace"
            but_delete['foreground']="SystemButtonText"


        def on_enter4(e):
            but_view['background']="black"
            but_view['foreground']="cyan"  
        def on_leave4(e):
            but_view['background']="SystemButtonFace"
            but_view['foreground']="SystemButtonText"

            

        def on_enter5(e):
            but_clear['background']="black"
            but_clear['foreground']="cyan"  
        def on_leave5(e):
            but_clear['background']="SystemButtonFace"
            but_clear['foreground']="SystemButtonText"




        #=====================================================

        def reset():
            text.delete(1.0,"end")
            #print(text.get(1.0,"end-1c"))
            #datetime.datetime.now()
            pass

         
        def Add_Data():
            if(len(text.get(1.0,"end-1c")) !=0):
                slipbackend.add_list(datetime.datetime.now(),text.get(1.0,"end-1c"))
                view_Data()


        def view_Data():
            lists.delete(*lists.get_children())
            for rows in slipbackend.view_list():
                lists.insert('',END,values=rows)


        def Update_Data():
            if(len(text.get(1.0,"end-1c"))!=0):
                slipbackend.delete_list(text.get(1.0,"end-1c"))
            if(len(text.get(1.0,"end-1c"))!=0):
                slipbackend.add_list(datetime.datetime.now(),text.get(1.0,"end-1c"))          
                reset()
                view_Data()
        
        
        
        def Delete_Data():           
            slipbackend.delete_list(text.get(1.0,"end-1c"))
            view_Data()



        global lists
        global scrollbar
        global sor
        #global text
        def  place(event):
            reset()
            crow=lists.focus()
            contents=lists.item(crow)
            row=contents['values']       
            text.insert("end",row[2])
            
        

        main_frame=Frame(self.root,width=500,height=550,bd=4,relief="ridge")
        main_frame.place(x=0,y=0)


        top_frame=Frame(main_frame,width=493,height=350,bd=4,relief="ridge",bg="black")
        top_frame.place(x=0,y=0)


        bottom_frame=Frame(main_frame,width=493,height=192,bd=4,relief="ridge")
        bottom_frame.place(x=0,y=350)


    #=====================================================================


        label_frame=LabelFrame(top_frame,width=480,height=342,text="Add Details")
        label_frame.place(x=1,y=0)

        Scol=Scrollbar(label_frame,orient="vertical")
        Scol.grid(column=7,sticky="NS")


        text=Text(label_frame,width=57,height=13,font=('times new roman',12,'bold'),yscrollcommand=Scol.set)
        text.grid(row=0,column=0)
        Scol.config(command=text.yview)

        but_save=Button(main_frame,text="Save",width=7,font=('times new roman',12,'bold'),cursor="hand2",command=Add_Data)
        but_save.place(x=20,y=290)
        but_save.bind("<Enter>",on_enter1)
        but_save.bind("<Leave>",on_leave1)

        but_update=Button(main_frame,text="Update",width=7,font=('times new roman',12,'bold'),cursor="hand2",command=Update_Data)
        but_update.place(x=110,y=290)
        but_update.bind("<Enter>",on_enter2)
        but_update.bind("<Leave>",on_leave2)


        but_delete=Button(main_frame,text="Delete",width=7,font=('times new roman',12,'bold'),cursor="hand2",command=Delete_Data)
        but_delete.place(x=210,y=290)
        but_delete.bind("<Enter>",on_enter3)
        but_delete.bind("<Leave>",on_leave3)

        but_view=Button(main_frame,text="View",width=7,font=('times new roman',12,'bold'),cursor="hand2",command=view_Data)
        but_view.place(x=310,y=290)
        but_view.bind("<Enter>",on_enter4)
        but_view.bind("<Leave>",on_leave4)

        but_clear=Button(main_frame,text="Clear",width=7,font=('times new roman',12,'bold'),cursor="hand2",command=reset)
        but_clear.place(x=400,y=290)
        but_clear.bind("<Enter>",on_enter5)
        but_clear.bind("<Leave>",on_leave5)


#========================================================================================

        scrollbar=Scrollbar(bottom_frame,orient=VERTICAL)

        sor=Scrollbar(bottom_frame,orient=HORIZONTAL)

        lists=tkinter.ttk.Treeview(bottom_frame,columns=("ID","Date","Lists"),height=7)
        
        
        scrollbar.config(command=lists.yview)
        scrollbar.pack(side=RIGHT,fill=Y)
        sor.config(command=lists.xview)
        sor.pack(side=BOTTOM,fill=BOTH)


        lists.heading("ID",text="ID")
        lists.heading("Date",text="Date")
        lists.heading("Lists",text="Lists")

        lists['show']="headings"
        lists.column("ID",width=35,minwidth=10)
        lists.column("Date",width=120,minwidth=40)
        lists.column("Lists",width=310,minwidth=50)

        lists.bind('<ButtonRelease-1>',place)

        lists.pack(side=TOP,fill=X)

        


if __name__ == "__main__":
    root=Tk()
    app=Slip(root)
    root.mainloop()























