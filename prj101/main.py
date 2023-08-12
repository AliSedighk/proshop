import tkinter
import userAction
import productAction




def login():
    global session
    user=txt_user.get()
    pas=txt_pass.get()
    result=userAction.user_login(user, pas)
    if result:
        lbl_msg.configure(text="welcome to your account!",fg="green")
        session=result
        txt_user.delete(0,"end")
        txt_pass.delete(0,"end")
        btn_login.configure(state="disabled")
        btn_logout.configure(state="active")
        btn_shop.configure(state="active")
        btn_cart.configure(state="active")
    else:
        lbl_msg.configure(text="wrong username or pass!",fg="red")

def submit():
    def register():
        user=txt_user.get()
        pas=txt_pass.get()
        addr=txt_addr.get()
        result,errorMSG=userAction.user_submit(user, pas, addr)
        if result:
            lbl_msg.configure(text="submit done",fg="green")
            txt_user.delete(0,"end")
            txt_pass.delete(0,"end")
            txt_addr.delete(0,"end")
            btn_submit.configure(state="disabled")
        else:
            lbl_msg.configure(text=errorMSG,fg="red")
        
    win_submit=tkinter.Toplevel()  
    win_submit.title("Submit panel")
    win_submit.geometry("300x400")
    
    lbl_user=tkinter.Label(win_submit,text="Username: ")
    lbl_user.pack()
    txt_user=tkinter.Entry(win_submit)
    txt_user.pack()

    lbl_pass=tkinter.Label(win_submit,text="Password: ")
    lbl_pass.pack()
    txt_pass=tkinter.Entry(win_submit)
    txt_pass.pack()
    
    lbl_addr=tkinter.Label(win_submit,text="Address: ")
    lbl_addr.pack()
    txt_addr=tkinter.Entry(win_submit)
    txt_addr.pack()
    
    lbl_msg=tkinter.Label(win_submit,text="")
    lbl_msg.pack()
    
    btn_submit=tkinter.Button(win_submit,text="Submit",command=register)
    btn_submit.pack()
    
    
    
    win_submit.mainloop()

def logout():
    global session
    session=False
    btn_login.configure(state="active")
    btn_logout.configure(state="disabled")
    btn_shop.configure(state="disabled")
    btn_cart.configure(state="disabled")
    lbl_msg.configure(text="you are logged out now!",fg="green")

def shop():
    def buy():
        global session
        pid=txt_id.get()
        qnt=txt_qnt.get()
        result,msg=productAction.shopValidate(pid, qnt)
        if not result:
            lbl_msg.configure(text=msg,fg="red")
            return
        productAction.savetocart(session,pid,qnt)
        productAction.updateqnt(pid,qnt)
        lstbx.delete(0,"end")
        products=productAction.getAllProducts()
        for product in products:
            text=f"id:{product[0]},   Name:{product[1]},   Price:{product[2]},   Quantity:{product[3]}"
            lstbx.insert("end", text)
        
        lbl_msg.configure(text="saved to your cart",fg="green")
        txt_id.delete(0,"end")
        txt_qnt.delete(0,"end")
        
    win_shop=tkinter.Toplevel(win)
    win_shop.title("shop panel")
    win_shop.geometry("400x300")
    
    products=productAction.getAllProducts()
    
    
    lstbx=tkinter.Listbox(win_shop,width=60)
    lstbx.pack()
    
    for product in products:
        text=f"id:{product[0]},   Name:{product[1]},   Price:{product[2]},   Quantity:{product[3]}"
        lstbx.insert("end", text)
    
    lbl_id=tkinter.Label(win_shop,text="Product id:")
    lbl_id.pack()
    
    txt_id=tkinter.Entry(win_shop)
    txt_id.pack()
    
    lbl_qnt=tkinter.Label(win_shop,text="quantity:")
    lbl_qnt.pack()
    
    txt_qnt=tkinter.Entry(win_shop)
    txt_qnt.pack()
    
    lbl_msg=tkinter.Label(win_shop,text="")
    lbl_msg.pack()
    
    btn_buy=tkinter.Button(win_shop,text="Buy",command=buy)
    btn_buy.pack()
    
    
    
    win_shop.mainloop()

def mycart():
    global session
    
    win_cart=tkinter.Toplevel(win)
    win_cart.title("cart panel")
    win_cart.geometry("400x300")
    
    lstbx=tkinter.Listbox(win_cart,width=60)
    lstbx.pack()
    
    result=productAction.getUserCart(session)
    for product in result:
        text=f"Name:{product[1]},   Quantity:{product[0]},   Total Price:{product[0]*product[2]}"
        lstbx.insert("end", text)
    
    
    win_cart.mainloop()
    
#-------------------admin panel----------------------

win_admin = tkinter.Toplevel(win)
win_admin.title('admin Panel')
win_admin.geometry('300x300')

lbl_add_btn = tkinter.Label(win_admin, text='Add New Products')
lbl_add_btn.pack()
btn_add_product = tkinter.Button(win_admin, text='Add Product', command=add_product)
btn_add_product.pack()

lbl_line1 = tkinter.Label(win_admin, text='')
lbl_line1.pack()

lbl_qnt_add = tkinter.Label(win_admin, text='Product Quantity De/Increment')
lbl_qnt_add.pack()
btn_inde = tkinter.Button(win_admin, text='De/Increase Quantities', command=deincrement)
btn_inde.pack()

lbl_line2 = tkinter.Label(win_admin, text='')
lbl_line2.pack()

lbl_user_mngr = tkinter.Label(win_admin, text='User Manager')
lbl_user_mngr.pack()
btn_user_manager = tkinter.Button(win_admin, text='User Manager', command=user_manager)
btn_user_manager.pack()

win_admin.mainloop()
    
# ------------------ Main ---------------------------
session=False

win=tkinter.Tk()
win.title("SHOP PROJECT")
win.geometry("300x300")

lbl_user=tkinter.Label(win,text="Username: ")
lbl_user.pack()
txt_user=tkinter.Entry(win)
txt_user.pack()

lbl_pass=tkinter.Label(win,text="Password: ")
lbl_pass.pack()
txt_pass=tkinter.Entry(win)
txt_pass.pack()

lbl_msg=tkinter.Label(win,text="")
lbl_msg.pack()

btn_login=tkinter.Button(win,text="Login",command=login)
btn_login.pack()

btn_submit=tkinter.Button(win,text="Submit",command=submit)
btn_submit.pack()

btn_logout=tkinter.Button(win,text="Logout",state="disabled", command=logout)
btn_logout.pack()

btn_shop=tkinter.Button(win,text="Shop",state="disabled", command=shop)
btn_shop.pack()

btn_cart=tkinter.Button(win,text="my cart",state="disabled", command=mycart)
btn_cart.pack()

btn_admin = tkinter.Button(win, text='Admin Panel', state='disabled', command=admin)
btn_admin.pack()

win.mainloop()













