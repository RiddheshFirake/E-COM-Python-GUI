from tkinter import Tk, Label, Entry, Frame, Button, messagebox,filedialog
import mysql.connector
from tkinter import Tk, Label, Entry, Frame, PhotoImage, Canvas, Button
from PIL import ImageTk
from tkinter.ttk import *
from tkinter import *
from mysql.connector import Error
from PIL import Image, ImageTk
from tkinter import StringVar
import csv




# ******************************************(START)***********************************************

# from tkinter import Tk, Label, Entry, Frame, PhotoImage, Canvas, Button
# import tkinter as tk
def open_Alogin_window():
    root.destroy()  
    Auth_A()
    # import Authentication
    # Authentication.main()

def open_Ulogin_window():
    root.destroy()
    Auth_U()



   

root = Tk()
root.title('Storm-Z mainpage')
root.geometry("1080x520+45+20")
root.resizable(True, True)

    
image_path = "Storm-Z_logo-removebg-preview.png"
image = PhotoImage(file=image_path)

canvas = Canvas(root, width=1000, height=600, highlightthickness=0)
canvas.create_image(370, 5, anchor="n", image=image)
canvas.pack(side="left")

admin_login = Button(root, text="Login as ADMIN ->", font=("Arial", 20, "bold"), bg="#00A9FF", fg="white", bd=4,command=open_Alogin_window)
                                
admin_login.place(relx=0.62,rely=0.29)

user_login = Button(root, text="Login as USER ->", font=("Arial", 20, "bold"), bg="#00A9FF", fg="white", bd=4,
                                command=open_Ulogin_window)
user_login.place(relx=0.62,rely=0.49)





# ******************************************(AUTHENTICATOR)***********************************************


def authenticate_user(username, password):
    try:
        cursor = db_connection.cursor()

        query = "SELECT password FROM User WHERE username = %s"
        cursor.execute(query, (username,))
        print(username)
        # set_username(username)
        result = cursor.fetchone()

        # Check if the username exists and compare the passwords
        if result and result[0] == password:
            return True
        else:
            return False

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return False

    finally:
        cursor.close()


def authenticate_Admin(username, password):
    try:
        cursor = db_connection.cursor()

        query = "SELECT Password FROM Admin WHERE AdminName = %s"
        cursor.execute(query, (username,))
        print(username)
        # set_username(username)
        result = cursor.fetchone()

        # Check if the username exists and compare the passwords
        if result and result[0] == password:
            return True
        else:
            return False

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return False

    finally:
        cursor.close()


def login_clicked():
    entered_username = Lusername_entry.get()
    entered_password = Lpassword_entry.get()

    # Authenticate the user
    if authenticate_user(entered_username, entered_password):
        messagebox.showinfo("Login Successful", "Welcome, " + entered_username + "!")
        set_username(entered_username)
        Authentication_root.destroy()
        Homepg()
    else:
        messagebox.showerror("Login Failed", "Invalid username or password. Please try again.")

def login_clicked_A():
    entered_username = Lusername_entry.get()
    entered_password = Lpassword_entry.get()

    # Authenticate the user
    if authenticate_Admin(entered_username, entered_password):
        messagebox.showinfo("Login Successful", "Welcome, " + entered_username + "!")
        set_username(entered_username)
        Authentication_root.destroy()
        # import vipul_wala_homepg_code
        AdminPg()
    else:
        messagebox.showerror("Login Failed", "Invalid username or password. Please try again.")

def open_signup_window():
    Authentication_root.destroy()  # Close the current window if needed
    # Importing SignUp module and calling its main function
    signup()
    # import signup
    #Yusignup.main()

def open_Asignup_window():
    Authentication_root.destroy()  # Close the current window if needed
    # Importing SignUp module and calling its main function
    Asignup()


def set_username(username):
    global L_username
    L_username = username
    #print("Im inside set_username in auth L_username:",L_username)     working





# Establish a connection to your MySQL database
# Replace 'your_database', 'your_username', 'your_password' with your actual values
db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="pass@123",
    database="StormZ"
)
def Auth_U():
    global Authentication_root,Lusername_entry,Lpassword_entry,c,image
    # GUI setup
    Authentication_root = Tk()
    Authentication_root.title('Storm-Z Login')
    Authentication_root.geometry("1450x720+45+20")
    Authentication_root.resizable(True, True)

    # ... (Rest of your GUI setup)
    image_path = "Storm-Z_logo-removebg-preview.png"
    image = PhotoImage(file=image_path)
    c=PhotoImage(file="Loginsubmit_button.png")

    canvas = Canvas(Authentication_root, width=1000, height=600, highlightthickness=0)
    canvas.create_image(170, 45, anchor="nw", image=image)
    canvas.pack(side="left")

    username_label = Label(Authentication_root, text="Unleash the Power Within,", fg="black", font=("Times 20 italic bold", 20, "bold","italic"))
    username_label.place(relx=0.29, rely=0.61, anchor="center")
    username_label = Label(Authentication_root, text="Your Global Shield for Immunity and Wellness", fg="black", font=("Times 20 italic bold", 20, "bold","italic"))
    username_label.place(relx=0.31, rely=0.69, anchor="center")

    frame = Frame(Authentication_root, width=400, height=400, bg='#046bdc')
    frame.place(relx=0.75, rely=0.5, anchor="center")

    heading = Label(Authentication_root, text="User Login", fg="#046bdc", padx=90, pady=10,bg="yellow", font=("Arial", 25, "bold"))
    heading.place(relx=0.75, rely=0.15, anchor="center")

    username_label = Label(frame, text="Username", fg="black", font=("Microsoft Yahei UI Light", 20, "bold"))
    username_label.place(relx=0.5, rely=0.16, anchor="center")
    Lusername_entry = Entry(frame, width=17, fg="black", border=2, bg="white", font=("Microsoft Yahei UI Light", 23, "bold"))
    Lusername_entry.place(relx=0.5, rely=0.33, anchor="center")

    password_label = Label(frame, text="Enter Password", fg="black", font=("Microsoft Yahei UI Light", 20, "bold"))
    password_label.place(relx=0.5, rely=0.51, anchor="center")
    Lpassword_entry = Entry(frame, width=17, fg="black", border=2, bg="white", show="*", font=("Microsoft Yahei UI Light", 23, "bold"))
    Lpassword_entry.place(relx=0.5, rely=0.68, anchor="center")


    global L_username
    L_username=""





    SubmitButton=Button(frame,image=c,border=0,command=lambda: login_clicked())
    SubmitButton.place(relx=0.5, rely=0.87, anchor="center")





    username_label = Label(Authentication_root, text="Not a user?", fg="black", font=("Times 20 italic bold", 19, "bold"))
    username_label.place(relx=0.75, rely=0.83, anchor="center")
    button = Button(Authentication_root, text='Sign Up',command=open_signup_window,fg="blue",bg="#ffdd53",padx=50,pady=3,font=("Arial", 20, "bold"))
    button.place(relx=0.75, rely=0.91, anchor="center")

    # Create Entry widgets for username and password


    

    
    





    # Create a button that, when clicked, triggers the login logic
    # login_button = Button(frame, text="Login", command=login_clicked, fg="white", bg="#046bdc", padx=50, pady=3, font=("Arial", 20, "bold"))
    # login_button.place(relx=0.5, rely=0.87, anchor="center")



def Auth_A():
    global Authentication_root,Lusername_entry,Lpassword_entry,c,image
    # GUI setup
    Authentication_root = Tk()
    Authentication_root.title('Storm-Z Login')
    Authentication_root.geometry("1450x720+45+20")
    Authentication_root.resizable(True, True)

    # ... (Rest of your GUI setup)
    image_path = "Storm-Z_logo-removebg-preview.png"
    image = PhotoImage(file=image_path)
    c=PhotoImage(file="Loginsubmit_button.png")

    canvas = Canvas(Authentication_root, width=1000, height=600, highlightthickness=0)
    canvas.create_image(170, 45, anchor="nw", image=image)
    canvas.pack(side="left")

    username_label = Label(Authentication_root, text="Unleash the Power Within,", fg="black", font=("Times 20 italic bold", 20, "bold","italic"))
    username_label.place(relx=0.29, rely=0.61, anchor="center")
    username_label = Label(Authentication_root, text="Your Global Shield for Immunity and Wellness", fg="black", font=("Times 20 italic bold", 20, "bold","italic"))
    username_label.place(relx=0.31, rely=0.69, anchor="center")

    frame = Frame(Authentication_root, width=400, height=400, bg='#046bdc')
    frame.place(relx=0.75, rely=0.5, anchor="center")

    heading = Label(Authentication_root, text="Admin Login", fg="#046bdc", padx=90, pady=10,bg="yellow", font=("Arial", 25, "bold"))
    heading.place(relx=0.75, rely=0.15, anchor="center")

    username_label = Label(frame, text="Admin name", fg="black", font=("Microsoft Yahei UI Light", 20, "bold"))
    username_label.place(relx=0.5, rely=0.16, anchor="center")
    Lusername_entry = Entry(frame, width=17, fg="black", border=2, bg="white", font=("Microsoft Yahei UI Light", 23, "bold"))
    Lusername_entry.place(relx=0.5, rely=0.33, anchor="center")

    password_label = Label(frame, text="Enter Password", fg="black", font=("Microsoft Yahei UI Light", 20, "bold"))
    password_label.place(relx=0.5, rely=0.51, anchor="center")
    Lpassword_entry = Entry(frame, width=17, fg="black", border=2, bg="white", show="*", font=("Microsoft Yahei UI Light", 23, "bold"))
    Lpassword_entry.place(relx=0.5, rely=0.68, anchor="center")


    global L_username
    L_username=""





    SubmitButton=Button(frame,image=c,border=0,command=lambda: login_clicked_A())
    SubmitButton.place(relx=0.5, rely=0.87, anchor="center")





    username_label = Label(Authentication_root, text="Not a user?", fg="black", font=("Times 20 italic bold", 19, "bold"))
    username_label.place(relx=0.75, rely=0.83, anchor="center")
    button = Button(Authentication_root, text='Sign Up',command=open_Asignup_window,fg="blue",bg="#ffdd53",padx=50,pady=3,font=("Arial", 20, "bold"))
    button.place(relx=0.75, rely=0.91, anchor="center")

    # Create Entry widgets for username and password







    # Create a button that, when clicked, triggers the login logic
    # login_button = Button(frame, text="Login", command=login_clicked, fg="white", bg="#046bdc", padx=50, pady=3, font=("Arial", 20, "bold"))
    # login_button.place(relx=0.5, rely=0.87, anchor="center")





# ******************************************(SIGNUP)***********************************************





def HomePage():
    #from Admin_Page import S_username,S_password,S_repassword
    sign_root.destroy()  # Close the current window if needed
    import HomePage
    HomePage.insert_data()



def open_login_window():
    sign_root.destroy()  # Close the current window if needed
    # Importing SignUp module and calling its main function
    import login
    login.main()



flag=0

def insert_data():
    global flag,Username
    Username=Susername_entry.get()
    Password=Spassword_entry.get()
    RePassword=Spassword_rentry.get()
    Gender=gender.get()
    Products='0'
    TotalProductPrice='69'

    StormZ_db=mysql.connector.connect(host="localhost",user="root",password="pass@123",database="StormZ")
    StormZ_db_cursor=StormZ_db.cursor()
    print(Password)
    print(RePassword)
    if Username!='' and Password!='' and TotalProductPrice!='' and Gender!='' and Products!='' and Password==RePassword:
        flag=0
        StormZ_db_cursor.execute("INSERT INTO User (Username, Password, Gender, Products, TotalProductPrice) VALUES (%s, %s, %s, %s, %s)",
            (Username, Password, Gender, Products, TotalProductPrice))
        StormZ_db_cursor.execute("commit")
        #lastid = StormZ_db_cursor.lastrowid
        messagebox.showinfo("Information", "Employee inserted successfully...")
        set_username(Username)
    else:
        flag=1
        messagebox.showinfo("Information", "It didnt got inserted into DataBase due to some error!\nMaybe Because you entered Password Wrong!")
 
    #Username.delete(0, END)
    #Password.delete(0, END)
    #Username.focus_set()

def Ainsert_data():
    global flag,Username
    Username=ASusername_entry.get()
    Password=ASpassword_entry.get()
    RePassword=ASpassword_rentry.get()
    # Gender=gender.get()
    # Products='0'
    # TotalProductPrice='69'

    StormZ_db=mysql.connector.connect(host="localhost",user="root",password="pass@123",database="StormZ")
    StormZ_db_cursor=StormZ_db.cursor()
    print(Password)
    print(RePassword)
    if Username!='' and Password!='' and Password==RePassword:
        flag=0
        StormZ_db_cursor.execute("INSERT INTO Admin (AdminName, Password) VALUES (%s, %s)",
            (Username, Password))
        StormZ_db_cursor.execute("commit")
        #lastid = StormZ_db_cursor.lastrowid
        messagebox.showinfo("Information", "Admin inserted successfully...")
        # set_username(Username)
    else:
        flag=1
        messagebox.showinfo("Information", "It didnt got inserted into DataBase due to some error!\nMaybe Because you entered Password Wrong!")
 
    #Username.delete(0, END)
    #Password.delete(0, END)
    #Username.focus_set()



def Multiple_functions():
    insert_data()
    if flag==0:
        sign_root.destroy()
        # import vipul_wala_homepg_code
        Homepg()
    else:
        insert_data()

def AMultiple_functions():
    Ainsert_data()
    if flag==0:
        sign_root.destroy()
        AdminPg()
    else:
        Ainsert_data()


def set_username(username):
    global S_username
    S_username = username




    

def back_to_logU():
    sign_root.destroy() 
    Auth_U()



def signup():
    global sign_root,Susername_entry,Spassword_entry,Spassword_rentry,image
    sign_root = Tk()
    sign_root.title('Storm-Z Signup')
    sign_root.geometry("1450x720+45+20")
    # sign_root.config(bg="#ffffff")
    sign_root.resizable(True, True)
    # sign_root = Toplevel()


    image_path = "Storm-Z_logo-removebg-preview.png"
    image = PhotoImage(file=image_path)
    button1=PhotoImage(file="Signupsubmit_button.png")

    canvas = Canvas(sign_root, width=1000, height=600, highlightthickness=0)
    canvas.create_image(170, 45, anchor="nw", image=image)
    canvas.pack(side="left")

    username_label = Label(sign_root, text="Unleash the Power Within,", fg="black", font=("Times 20 italic bold", 20, "bold","italic"))
    username_label.place(relx=0.29, rely=0.61, anchor="center")
    username_label = Label(sign_root, text="Your Global Shield for Immunity and Wellness", fg="black", font=("Times 20 italic bold", 20, "bold","italic"))
    username_label.place(relx=0.31, rely=0.69, anchor="center")

    frame = Frame(sign_root, width=400, height=500, bg='#046bdc')
    frame.place(relx=0.75, rely=0.5, anchor="center")

    heading = Label(sign_root, text="User Sign Up", fg="#046bdc", padx=90, pady=10,bg="yellow", font=("Arial", 25, "bold"))
    heading.place(relx=0.75, rely=0.08, anchor="center")

    username_label = Label(frame, text="Enter Username", fg="black", font=("Microsoft Yahei UI Light", 20, "bold"))
    username_label.place(relx=0.1, rely=0.08, anchor="w")
    Susername_entry = Entry(frame, width=17, fg="black", border=2, bg="white", font=("Microsoft Yahei UI Light", 23, "bold"))
    Susername_entry.place(relx=0.1, rely=0.19, anchor="w")

    password_label = Label(frame, text="Enter new Password", fg="black", font=("Microsoft Yahei UI Light", 20, "bold"))
    password_label.place(relx=0.1, rely=0.32, anchor="w")
    Spassword_entry = Entry(frame, width=17, fg="black", border=2, bg="white", show="*",font=("Microsoft Yahei UI Light", 23, "bold"))
    Spassword_entry.place(relx=0.1, rely=0.43, anchor="w")

    repassword_label = Label(frame, text="Re-enter your Password", fg="black", font=("Microsoft Yahei UI Light", 20, "bold"))
    repassword_label.place(relx=0.1, rely=0.57, anchor="w")
    Spassword_rentry = Entry(frame, width=17, fg="black", border=2, bg="white", show="*",font=("Microsoft Yahei UI Light", 23, "bold"))
    Spassword_rentry.place(relx=0.1, rely=0.68, anchor="w")


    global gender
    gender_label = Label(frame, text="Select your Gender", fg="black", font=("Microsoft Yahei UI Light", 20, "bold"))
    gender_label.place(relx=0.1, rely=0.81, anchor="w")
    gender = StringVar()
    Radiobutton(frame, text="Male", variable=gender, value="Male", font=("Arial", 19)).place(relx=0.35, rely=0.92, anchor="e")
    Radiobutton(frame, text="Female", variable=gender, value="Female" ,font=("Arial", 19)).place(relx=0.4, rely=0.92, anchor="w")

    # SubmitButton=Button(frame,image=button
    # nter")

    button = Button(sign_root, text='Submit',command=Multiple_functions,fg="blue",bg="#ffdd53",padx=50,pady=3,font=("Arial", 20, "bold"))
    button.place(relx=0.75, rely=0.91, anchor="center")

    BackToLogin_btn = Button(sign_root, text="Back to Login page", font=("Arial", 12, "bold"), bg="#ffa500", fg="white", bd=6, width=20,     command=back_to_logU)
    BackToLogin_btn.place(relx=0.17, rely=0.1, anchor="se")  


    # global S_username
    # global S_password

    # username = username_entry.get()



    S_username=username_entry.get()





    S_password=password_entry.get()
    S_repassword=password_rentry.get()






    # def run_sign_root():
    #     sign_root.mainloop()

    # if __name__ == "__main__":
    #     run_sign_root()



def back_to_logA():
    sign_root.destroy() 
    Auth_A()

def Asignup():
    global sign_root,ASusername_entry,ASpassword_entry,ASpassword_rentry,image
    sign_root = Tk()
    sign_root.title('Storm-Z Signup')
    sign_root.geometry("1450x720+45+20")
    # sign_root.config(bg="#ffffff")
    sign_root.resizable(True, True)
    # sign_root = Toplevel()


    image_path = "Storm-Z_logo-removebg-preview.png"
    image = PhotoImage(file=image_path)
    button1=PhotoImage(file="Signupsubmit_button.png")

    canvas = Canvas(sign_root, width=1000, height=600, highlightthickness=0)
    canvas.create_image(170, 45, anchor="nw", image=image)
    canvas.pack(side="left")

    username_label = Label(sign_root, text="Unleash the Power Within,", fg="black", font=("Times 20 italic bold", 20, "bold","italic"))
    username_label.place(relx=0.29, rely=0.61, anchor="center")
    username_label = Label(sign_root, text="Your Global Shield for Immunity and Wellness", fg="black", font=("Times 20 italic bold", 20, "bold","italic"))
    username_label.place(relx=0.31, rely=0.69, anchor="center")

    frame = Frame(sign_root, width=400, height=500, bg='#046bdc')
    frame.place(relx=0.75, rely=0.5, anchor="center")

    heading = Label(sign_root, text="User Sign Up", fg="#046bdc", padx=90, pady=10,bg="yellow", font=("Arial", 25, "bold"))
    heading.place(relx=0.75, rely=0.08, anchor="center")

    username_label = Label(frame, text="Enter Admin", fg="black", font=("Microsoft Yahei UI Light", 20, "bold"))
    username_label.place(relx=0.1, rely=0.08, anchor="w")
    ASusername_entry = Entry(frame, width=17, fg="black", border=2, bg="white", font=("Microsoft Yahei UI Light", 23, "bold"))
    ASusername_entry.place(relx=0.1, rely=0.19, anchor="w")

    password_label = Label(frame, text="Enter new Password", fg="black", font=("Microsoft Yahei UI Light", 20, "bold"))
    password_label.place(relx=0.1, rely=0.32, anchor="w")
    ASpassword_entry = Entry(frame, width=17, fg="black", border=2, bg="white", show="*",font=("Microsoft Yahei UI Light", 23, "bold"))
    ASpassword_entry.place(relx=0.1, rely=0.43, anchor="w")

    repassword_label = Label(frame, text="Re-enter your Password", fg="black", font=("Microsoft Yahei UI Light", 20, "bold"))
    repassword_label.place(relx=0.1, rely=0.57, anchor="w")
    ASpassword_rentry = Entry(frame, width=17, fg="black", border=2, bg="white", show="*",font=("Microsoft Yahei UI Light", 23, "bold"))
    ASpassword_rentry.place(relx=0.1, rely=0.68, anchor="w")


    # global gender
    # gender_label = Label(frame, text="Select your Gender", fg="black", font=("Microsoft Yahei UI Light", 20, "bold"))
    # gender_label.place(relx=0.1, rely=0.81, anchor="w")
    # gender = Tk.StringVar()
    # Radiobutton(frame, text="Male", variable=gender, value="Male", font=("Arial", 19)).place(relx=0.35, rely=0.92, anchor="e")
    # Radiobutton(frame, text="Female", variable=gender, value="Female" ,font=("Arial", 19)).place(relx=0.4, rely=0.92, anchor="w")



    # global S_username
    # global S_password

    # username = username_entry.get()



    # S_username=username_entry.get()





    # S_password=password_entry.get()
    # S_repassword=password_rentry.get()





    # SubmitButton=Button(frame,image=button1, border=0)
    # SubmitButton.place(relx=0.5, rely=0.92, anchor="center")

    button = Button(sign_root, text='Submit',command=AMultiple_functions,fg="blue",bg="#ffdd53",padx=50,pady=3,font=("Arial", 20, "bold"))
    button.place(relx=0.75, rely=0.758, anchor="center")


    BackToLogin_btn = Button(sign_root, text="Back to Login page", font=("Arial", 12, "bold"), bg="#ffa500", fg="white", bd=6, width=20,     command=back_to_logA)
    BackToLogin_btn.place(relx=0.17, rely=0.1, anchor="se")  

    # def run_sign_root():
    #     sign_root.mainloop()

    # if __name__ == "__main__":
    #     run_sign_root()







# ******************************************(V_HOMEPAGE)***********************************************

# from tkinter import *
# import tkinter as tk
# from tkinter import messagebox

# import mysql.connector
# from decouple import config

# from Admin_Page import admin_root
# from signup import S_username
# #from login import L_username

global product_id,action_type

def create_connection():
    """Create a connection to the MySQL database."""
    try:
        connection = mysql.connector.connect(
            host="localhost",user="root",password="pass@123",database="StormZ"
        )
        # 'root@localhost', 'Star-Viper'

        return connection
    except Error as e:
        messagebox.showerror("Error", f"Error connecting to the database: {e}")
        return None

def add_to_cart(product_name, total_price):
    connection = create_connection()
    if connection:
        try:
            with connection.cursor() as cursor:
                # Assuming 'selected_products' is your table for the shopping cart
                cursor.execute("INSERT INTO selected_products (product_name, product_price) VALUES (%s, %s)", (product_name, total_price))
            connection.commit()
            messagebox.showinfo("Information", "Product added to cart successfully...")
        except Error as e:
            connection.rollback()
            messagebox.showerror("Error", f"Error adding product to the database: {e}")
        finally:
            connection.close()

# def add_to_cart_and_track(ProductName):
#     add_to_cart(ProductName)
#     selected_products.append(ProductName)

#     # Add the selected product to the database
#     connection = create_connection()
#     if connection:
#         try:
#             with connection.cursor() as cursor:
#                 cursor.execute("INSERT INTO selected_products (product_id) VALUES (%s)", (ProductName,))
#             connection.commit()
#         except Error as e:
#             connection.rollback()
#             messagebox.showerror("Error", f"Error adding product to the database: {e}")
#         finally:
#             connection.close()

def delete_from_cart(delete_no):
    if delete_no in selected_products:
        selected_products.remove(delete_no)
        messagebox.showinfo("Delete Product !", f"Product {delete_no} is Deleted from the list")

        # Remove the selected product from the database
        connection = create_connection()
        if connection:
            try:
                with connection.cursor() as cursor:
                    cursor.execute("DELETE FROM selected_products WHERE product_id = %s", (delete_no,))
                connection.commit()
            except Error as e:
                connection.rollback()
                messagebox.showerror("Error", f"Error deleting product from the database: {e}")
            finally:
                connection.close()
    else:
        messagebox.showinfo("Cannot find the product !", "Please first enter the product in order to delete it")

def clear_list():
    messagebox.showinfo("Clear List", "Shopping cart cleared.")

    # Clear the selected products list and remove all records from the database
    selected_products.clear()
    connection = create_connection()
    if connection:
        try:
            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM selected_products")
            connection.commit()
        except Error as e:
            connection.rollback()
            messagebox.showerror("Error", f"Error clearing the database: {e}")
        finally:
            connection.close()

def show_selected_products():
    connection = create_connection()
    if connection:
        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM selected_products")
                result = cursor.fetchall()
                selected_products_from_db = [row[0] for row in result]

            messagebox.showinfo("Selected Products", f"Selected products: {', '.join(map(str, selected_products_from_db))}")
        except Error as e:
            messagebox.showerror("Error", f"Error fetching selected products from the database: {e}")
        finally:
            connection.close()
# ... (your existing code)

def log_action(product_id, action_type):
    """Log the action (add or delete) in the database."""
    connection = create_connection()
    if connection:
        try:
            with connection.cursor() as cursor:
                cursor.execute("INSERT INTO selected_products (product_id, action_type) VALUES (%s, %s)",
                               (product_id, action_type))
            connection.commit()
        except Error as e:
            connection.rollback()
            messagebox.showerror("Error", f"Error logging action in the database: {e}")
        finally:
            connection.close()

# def add_to_cart_and_track(ProductName):
#     add_to_cart(ProductName)
#     selected_products.append(ProductName)
#     log_action(ProductName, 'add')

def delete_from_cart(delete_no):
    if delete_no in selected_products:
        selected_products.remove(delete_no)
        messagebox.showinfo("Delete Product !", f"Product {delete_no} is Deleted from the list")
        # log_action(delete_no, 'delete')
        # Remove the selected product from the database
        connection = create_connection()
        if connection:
            try:
                with connection.cursor() as cursor:
                    cursor.execute("DELETE FROM selected_products WHERE product_id = %s AND action_type = 'add'",
                                   (delete_no,))
                connection.commit()
            except Error as e:
                connection.rollback()
                messagebox.showerror("Error", f"Error deleting product from the database: {e}")
            finally:
                connection.close()
    else:
        messagebox.showinfo("Cannot find the product !", "Please first enter the product in order to delete it")

# homepg.mainloop()Riddhesh

# def add_to_cart(ProductName):
#     messagebox.showinfo("Add to Cart", f"Product {ProductName} added to cart.")


def clear_list():
    selected_products.clear()
    connection = create_connection()
    if connection:
        try:
            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM selected_products")
            connection.commit()
        except Error as e:
            connection.rollback()
            messagebox.showerror("Error", f"Error clearing the database: {e}")
        finally:
            connection.close()
    messagebox.showinfo("Clear List", "Shopping cart cleared.")

def show_selected_products(selected_products):
    messagebox.showinfo("Selected Products", f"Selected products: {', '.join(map(str, selected_products))}")


def update_user_data(user, total_product_price,Sum):
    try:
        StormZ_db = mysql.connector.connect(
            host="localhost", user="root", password="pass@123", database="StormZ"
        )
        StormZ_db_cursor = StormZ_db.cursor()
        products =(Sum)
        print(user)
        print(total_product_price)
        print(Sum)

        # Assuming the table name is 'User' and it has columns 'TotalProductPrice' and 'Products'
        update_query = (
            "UPDATE User SET TotalProductPrice=%s, Products=%s WHERE Username=%s"
        )
        data = (total_product_price, products, user)

        StormZ_db_cursor.execute(update_query, data)
        StormZ_db.commit()

        messagebox.showinfo("Update Successful", "User data updated successfully.")

    except mysql.connector.Error as err:
        messagebox.showerror(
            "Error", f"Error updating user data: {err}"
        )

    finally:
        StormZ_db_cursor.close()
        StormZ_db.close()

# SZFruits_image = None
# SZChoco_image = None
# SZDfruit_image = None
# SZSpices_image = None
# def load_images():
#     global SZFruits_image, SZChoco_image, SZDfruit_image, SZSpices_image

#     # Load and resize images
#     SZFruits_image = Image.open("Masala_prod.jpg").resize((260, 210))
#     SZChoco_image = Image.open("StormZ_fruits.jpeg").resize((248, 210))
#     SZDfruit_image = Image.open("Chocolate_prod.png").resize((260, 200))
#     SZSpices_image = Image.open("DryFruit_prod.jpg").resize((248, 200))

#     # Convert images to PhotoImage objects
#     SZFruits_image = ImageTk.PhotoImage(SZFruits_image)
#     SZChoco_image = ImageTk.PhotoImage(SZChoco_image)
#     SZDfruit_image = ImageTk.PhotoImage(SZDfruit_image)
#     SZSpices_image = ImageTk.PhotoImage(SZSpices_image)


selected_products = []

def count_products_in_cart():
    global Funky,Dazzling,Spice,Choco
    Funky = 0
    Dazzling = 0     
    Spice = 0    
    Choco = 0 
    for i in selected_products:
            

        if i == 'Funky Fruits Fusion':
            Funky = Funky + 1
        elif i == 'Dazzling Dryfruit Delight':
            Dazzling = Dazzling + 1
        elif i == 'Spice Spectacle Elixir':
            Spice = Spice + 1
        elif i == 'Choco-Charm Craze' :
            Choco = Choco + 1
    sum=Funky+Dazzling+Choco+Spice
    if S_username!="":
        print("\n\nInside hompg and above update user data func S_username:",S_username)
        update_user_data(S_username,TotalProductPrice,sum)
    else:
        from Authentication import L_username
        print("\n\nInside hompg L_username:",L_username)
        update_user_data(L_username,TotalProductPrice,sum)

    print(Funky)
    print(Dazzling)
    print(Spice)
    print(Choco)
    homepg.destroy()


def add_to_cart_and_track(ProductName,ProductPrice):
    global TotalProductPrice
    
    TotalProductPrice = ProductPrice + TotalProductPrice
    add_to_cart(ProductName,ProductPrice)
    selected_products.append(ProductName)
    # if 'admin_root' in globals():
    #     admin_root.destroy()
    # add_to_cart_and_track(ProductName)
    # log_action(product_id, action_type)
    

def delete_from_cart(delete_no):
    if delete_no in selected_products:
        selected_products.remove(delete_no)
        messagebox.showinfo("Delete Product !",f"Product {delete_no} is Deleted from the list")

    else:
        messagebox.showinfo("Cannot find the product !","Please first enter the product in order to delete it")

#  blue color scheme
# background_color = "#ADD8E6"  # Light Blue
# button_color = "#1E90FF"  # Dodger Blue
# canvas_color = "#B0DAFF"  # Sky Blue x lightblue
def navigate_to(section):
    # Add logic to navigate to different sections based on the button clicked
    if section == "Home":
        # Add logic for Home page
        print("Navigate to Home")
    elif section == "Products":
        # Add logic for Products page
        print("Navigate to Products")
    elif section == "About Us":
        # Add logic for About Us page
        print("Navigate to About Us")

# Function to create a navbar button
# def create_navbar_button(text, command, x_position):
#     button = Button(homepg, text=text, font=("Arial", 10, "bold"), bg="#1640D6", fg="white",padx=120, bd=4, command=command)
#     button.place(relx=x_position, rely=0.01,)
    
# Create navbar buttons
def create_navbar_button(frame, text, command):
    button = Button(frame, text=text, font=("Arial", 10, "bold"), bg="#1640D6", fg="white", padx=20, pady=5, bd=4, command=command)
    button.pack(side=LEFT, padx=20)







def load_images():
    global SZFruits_image, SZChoco_image, SZDfruit_image, SZSpices_image

    # Load and resize images
    SZFruits_image = Image.open("fruits.jpg").resize((260, 210))
    SZChoco_image = Image.open("StormZ_fruits.jpeg").resize((248, 210))
    SZDfruit_image = Image.open("Chocolate_prod.png").resize((260, 200))
    SZSpices_image = Image.open("DryFruit_prod.jpg").resize((248, 200))

    # Convert images to PhotoImage objects
    
    SZFruits_image = ImageTk.PhotoImage(SZFruits_image)
    SZChoco_image = ImageTk.PhotoImage(SZChoco_image)
    SZDfruit_image = ImageTk.PhotoImage(SZDfruit_image)
    SZSpices_image = ImageTk.PhotoImage(SZSpices_image)

    canvas_homepg.create_image(120, 219, anchor=NW, image=SZFruits_image)
    canvas_homepg.create_image(440, 219, anchor=NW, image=SZChoco_image)
    canvas_homepg.create_image(760, 219, anchor=NW, image=SZDfruit_image)
    canvas_homepg.create_image(1080, 219, anchor=NW, image=SZSpices_image)

#load_images()



# ... (other functions)
TotalProductPrice=0

def add_to_cart_and_track(ProductName, ProductPrice):
    global TotalProductPrice

    TotalProductPrice = ProductPrice + TotalProductPrice
    add_to_cart(ProductName, ProductPrice)
    selected_products.append(ProductName)

    # Load images before creating buttons
    # Update images on canvas
    canvas_homepg.create_image(120, 219, anchor=NW, image=SZFruits_image)
    canvas_homepg.create_image(440, 219, anchor=NW, image=SZChoco_image)
    canvas_homepg.create_image(760, 219, anchor=NW, image=SZDfruit_image)
    canvas_homepg.create_image(1080, 219, anchor=NW, image=SZSpices_image)



def open_aboutus_window():
    homepg.destroy()  
    import aboutus
    #aboutus.main() 



def Homepg():
    global homepg,canvas_homepg,SZChoco,SZDfruit,SZFruits,SZSpices
    homepg = Tk()
    homepg.title('Storm-Z Products')
    homepg.geometry("1450x750+45+20")
    # homepg.config(bg="#ffffff")
    homepg.resizable(True, True)
    TotalProductPrice=0


    # canvas_homepg = tk.Canvas(homepg, width=900, height=700, bg='#B0DAFF')
    canvas_homepg = Canvas(homepg, width=1700, height=900, bg='#B0DAFF')
    canvas_homepg.pack()

    # image_path = "Storm-Z_logo-removebg-preview.png"
    # image = PhotoImage(file=image_path)
    # canvas1 = Canvas(homepg, width=900, height=500, highlightthickness=0)
    # canvas1.create_image(170, 45, anchor="n", image=image)
    # canvas1.pack()








    # ... (previous code)

    # Global variables to store PhotoImage objects
    SZFruits_image = None
    SZChoco_image = None
    SZDfruit_image = None
    SZSpices_image = None

    # ... (other functions)



    # Images

    SZChoco = Image.open("StormZ_fruits.jpeg").resize((248, 210))
    SZDfruit = Image.open("Chocolate_prod.png").resize((260, 200))
    SZSpices = Image.open("DryFruit_prod.jpg").resize((248, 200))
    SZFruits = Image.open("Masala_prod.jpg").resize((260, 210))

    SZFruits = ImageTk.PhotoImage(SZFruits)
    SZChoco = ImageTk.PhotoImage(SZChoco)
    SZDfruit = ImageTk.PhotoImage(SZDfruit)
    SZSpices = ImageTk.PhotoImage(SZSpices)

    # Calculate relx and rely based on canvas dimensions
    canvas_width = canvas_homepg.winfo_width()
    canvas_height = canvas_homepg.winfo_height()

    canvas_homepg.create_image(120, 219, anchor=NW, image=SZFruits)
    canvas_homepg.create_image(440, 219, anchor=NW, image=SZChoco)
    canvas_homepg.create_image(760, 219, anchor=NW, image=SZDfruit)
    canvas_homepg.create_image(1080, 219, anchor=NW, image=SZSpices)

    # #Add to cart btns
    # style = ttk.Style()
    # style.configure("Rounded.TButton", padding=10, relief="sunken", background="lightblue", foreground="blue",borderwidth=975)
    # style.map("Rounded.TButton", background=[("active", "darkblue")])













    stylish_button_add1 = Button(canvas_homepg, text="Add to Cart", font=("Arial", 12, "bold"), bg="#00A9FF", fg="white", bd=4,
                                    command=lambda: add_to_cart_and_track("Funky Fruits Fusion",250))

    stylish_button_add1.place(x=190, y=487)

    stylish_button_add2 = Button(canvas_homepg, text="Add to Cart", font=("Arial", 12, "bold"), bg="#00A9FF", fg="white", bd=4,
                                    command=lambda: add_to_cart_and_track("Dazzling Dryfruit Delight",350))
    stylish_button_add2.place(x=510, y=487)

    stylish_button_add3 = Button(canvas_homepg, text="Add to Cart", font=("Arial", 12, "bold"), bg="#00A9FF", fg="white", bd=4,
                                    command=lambda: add_to_cart_and_track("Spice Spectacle Elixir",450))
    stylish_button_add3.place(x=830, y=487)

    stylish_button_add4 = Button(canvas_homepg, text="Add to Cart", font=("Arial", 12, "bold"), bg="#00A9FF", fg="white", bd=4,
                                    command=lambda: add_to_cart_and_track("Choco-Charm Craze",550))
    stylish_button_add4.place(x=1150, y=487)


    # #Delete btns
    stylish_button_add4 = Button(canvas_homepg, text="Delete from Cart", font=("Arial", 12, "bold"), bg="#4E31AA", fg="white", bd=4,
                                    highlightbackground="#1E90FF",  # Border color
                                    highlightcolor="#1E90FF",  # Border color for active state
                                    command=lambda: delete_from_cart("Funky Fruits Fusion"))
    stylish_button_add4.place(x=175, y=536)

    stylish_button_add4 = Button(canvas_homepg, text="Delete from Cart", font=("Arial", 12, "bold"), bg="#4E31AA", fg="white", bd=4,
                                    command=lambda: delete_from_cart("Dazzling Dryfruit Delight"))
    stylish_button_add4.place(x=495, y=536)

    stylish_button_add4 = Button(canvas_homepg, text="Delete from Cart", font=("Arial", 12, "bold"), bg="#4E31AA", fg="white", bd=4,
                                    command=lambda: delete_from_cart("Spice Spectacle Elixir"))
    stylish_button_add4.place(x=815, y=536)

    stylish_button_add4 = Button(canvas_homepg, text="Delete from Cart", font=("Arial", 12, "bold"), bg="#4E31AA", fg="white", bd=4,
                                    command=lambda: delete_from_cart("Choco-Charm Craze"))
    stylish_button_add4.place(x=1135, y=536)

    #Names
    username_label = Label(canvas_homepg, text="WELCOME TO ", bg="#B0DAFF", fg="#11009E", 
                        font=("Arial", 43, "bold"),)

    username_label.place(x=558, y=60)

    # SZLogo = Image.open("Storm-Z_logo-removebg-preview.png").resize((340, 290))
    # SZLogo = ImageTk.PhotoImage(SZLogo)
    # canvas_homepg.create_image(600, 40, anchor=tk.NW, image=SZLogo)



    username_label = Label(canvas_homepg, text="Funky Fruits Fusion",bg="#B0DAFF" ,fg="black", 
                        font=("Times 20 italic bold", 19, "bold","italic"))
    username_label.place(x=130, y=442)

    username_label = Label(canvas_homepg, text="Dazzling Dryfruit Delight",bg="#B0DAFF" ,fg="black", 
                        font=("Times 20 italic bold", 19, "bold","italic"))
    username_label.place(x=420, y=442)

    username_label = Label(canvas_homepg, text="Spice Spectacle Elixir",bg="#B0DAFF" ,fg="black", 
                        font=("Times 20 italic bold", 19, "bold","italic"))
    username_label.place(x=760, y=442)

    username_label = Label(canvas_homepg, text="Choco-Charm Craze",bg="#B0DAFF" ,fg="black", 
                        font=("Times 20 italic bold", 19, "bold","italic"))
    username_label.place(x=1086, y=442)


    #Clear Btn
    stylish_button_delete1 = Button(canvas_homepg, text="Clear List", font=("Arial", 9, "bold"),padx=23,pady=3, bg="RED", fg="white", bd=4,
                                    command=clear_list)
    stylish_button_delete1.place(relx=0.5, rely=0.93, anchor="center")


    #Show Selected Btn
    show_selected_button = Button(canvas_homepg, text="Show Selected Products", font=("Arial", 12, "bold"),padx=29,pady=6, bg="#11009E", fg="white", bd=4,
                                    command=lambda: show_selected_products(selected_products))
    show_selected_button.place(relx=0.5, rely=0.85, anchor="center")

    #DONE BTN
    Proceed_btn = Button(canvas_homepg, text="Proceed", font=("Arial", 12, "bold"), bg="#2ecc71", fg="white", bd=6,width=15,command=lambda: count_products_in_cart())
    Proceed_btn.place(relx=0.85, rely=0.9)

    # Function to handle navbar button clicks

    # Create a frame in the given can
    navbar_frame = Frame(canvas_homepg, bg='#83A2FF', height=50)
    navbar_frame.place(relx=0, rely=0, anchor='nw', width=1700)

    # Create navbar buttons inside the frame
    create_navbar_button(navbar_frame, "Home", lambda: navigate_to("Home"))
    create_navbar_button(navbar_frame, "Products", lambda: navigate_to("Products"))
    create_navbar_button(navbar_frame, "About Us",command=open_aboutus_window)


        
    # def run_homepg():
    #     homepg.mainloop()

    # if __name__ == "__main__":
    #     run_homepg()





# ******************************************(ADMIN PAGE)***********************************************






# import tkinter as tk
# from tkinter import messagebox
# from tkinter import ttk
# from tkinter import *
# import mysql.connector 
# #from vipul_wala_homepg_code import Funky,Dazzling,Spice,Choco
# from signup import S_username,S_password,gender,S_repassword,set_username


#functions
# def show():
#     StormZ_db=mysql.connector.connect(host="localhost",user="root",password="pass@123",database="StormZ")
#     StormZ_db_cursor=StormZ_db.cursor()
#     StormZ_db_cursor.execute("SELECT UserId,Username,Password,Gender,Products,TotalProductPrice FROM User")
#     Users=StormZ_db_cursor.fetchall()

#     for i, (UserId,Username,Password,Gender,Products,TotalProductPrice) in enumerate(Users,start=1):
#         Listbox.insert("","end",values=(UserId,Username,Password,Gender,Products,TotalProductPrice))
#         StormZ_db.close()


def delete():
    admin_root.destroy()
    delete_window()
    if del_username_entry.get()=='':
        messagebox.showinfo('Error','Please provide UserId to perform delete operation')
    else:
        # import Delete
        # Delete.delete_user()
        delete_window()


def open_insert_window():
    admin_root.destroy()
    # import insert_window
    insert_window()




def open_update_window():
    admin_root.destroy()
    # import update_window
    update_window()




def export_to_csv():
    file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")], initialdir="C:/")

    if file_path:
        try:
            with open(file_path, 'w', newline='') as csv_file:
                csv_writer = csv.writer(csv_file)
                csv_writer.writerow(['UserId', 'Username', 'Password', 'Gender', 'Products', 'TotalProductPrice'])

                StormZ_db = mysql.connector.connect(host="localhost", user="root", password="pass@123", database="StormZ")
                StormZ_db_cursor = StormZ_db.cursor()
                StormZ_db_cursor.execute("SELECT UserId, Username, Password, Gender, Products, TotalProductPrice FROM User")
                users = StormZ_db_cursor.fetchall()

                for user in users:
                    csv_writer.writerow(user)

                StormZ_db.close()

            messagebox.showinfo("Export Successful", "Data exported to CSV successfully!")
        except Exception as e:
            messagebox.showerror("Export Error", f"An error occurred: {str(e)}")



def AdminPg():
    global admin_root
    # Root Window
    admin_root = Tk()
    admin_root.title('DataBase')
    admin_root.geometry("1200x700")
    admin_root.config(bg="#ffffff")
    admin_root.resizable(True, False)

    # Canvas
    admin_canvas = Canvas(admin_root, width=1200, height=700, bg='lightblue')
    #admin_canvas.configure(highlightcolor='#748CE1',insertbackground='Chocola')
    admin_canvas.pack()

    # Title of the Data
    heading = Label(admin_canvas, text="Customer DataBase", fg="white", bg="#748CE1", font=("Comic Sans MS", 20, "bold"))
    heading.place(relx=0.38, rely=0.05)

    # Adding a border to the label
    heading.config(bd=3.5, relief="solid")

    #making table to show DB


    #delete button
    AdminDelete_btn = Button(admin_canvas, text="Delete", font=("Arial", 12, "bold"), bg="#e74c3c", fg="white", bd=6,width=15,command=delete)
    AdminDelete_btn.place(relx=0.41, rely=0.65)

    #insert btn
    AdminInsert_btn = Button(admin_canvas, text="Insert", font=("Arial", 12, "bold"), bg="#2ecc71", fg="white", bd=6,width=15,command=open_insert_window)
    AdminInsert_btn.place(relx=0.2, rely=0.65)

    #Update btn
    AdminUpdate_btn = Button(admin_canvas, text="Update", font=("Arial", 12, "bold"), bg="#3498db", fg="white", bd=6,width=15,command=open_update_window)
    AdminUpdate_btn.place(relx=0.62, rely=0.65)


    cols=('UserId','Username','Password','Gender','Products','TotalProductPrice')
    Listbox=Treeview(admin_canvas,columns=cols,show='headings')

    for col in cols:
        Listbox.heading(col,text=col)
        Listbox.grid(row=1,column=0,columnspan=2)
        Listbox.place(x=0,y=100)
    StormZ_db=mysql.connector.connect(host="localhost",user="root",password="pass@123",database="StormZ")
    StormZ_db_cursor=StormZ_db.cursor()
    StormZ_db_cursor.execute("SELECT UserId,Username,Password,Gender,Products,TotalProductPrice FROM User")
    Users=StormZ_db_cursor.fetchall()

    for i, (UserId,Username,Password,Gender,Products,TotalProductPrice) in enumerate(Users,start=1):
        Listbox.insert("","end",values=(UserId,Username,Password,Gender,Products,TotalProductPrice))
        StormZ_db.close()
    # show()

    AdminExportCSV_btn = Button(admin_canvas, text="Export to CSV", font=("Arial", 12, "bold"), bg="#f39c12", fg="white",
                                bd=6, width=15, command=export_to_csv)
    AdminExportCSV_btn.place(relx=0.41, rely=0.75)



    # def run_admin_root():
    #     admin_root.mainloop()

    # if __name__ == "__main__":
    #     run_admin_root()



# ******************************************(INSERT_WINDOW)***********************************************






def dbinsert_data():
    global flag
    Username = dbusername_entry.get()
    Password = dbpassword_entry.get()
    RePassword = dbconfirm_password_entry.get()
    Gender = gender_var.get()
    Products='0'
    TotalProductPrice='0'

    StormZ_db=mysql.connector.connect(host="localhost",user="root",password="pass@123",database="StormZ")
    StormZ_db_cursor=StormZ_db.cursor()
    print(Password)
    print(RePassword)
    if Username!='' and Password!='' and TotalProductPrice!='' and Gender!='' and Products!='' and Password==RePassword:
        flag=0
        StormZ_db_cursor.execute("INSERT INTO User (Username, Password, Gender, Products, TotalProductPrice) VALUES (%s, %s, %s, %s, %s)",
            (Username, Password, Gender, Products, TotalProductPrice))
        StormZ_db_cursor.execute("commit")
        #lastid = StormZ_db_cursor.lastrowid
        messagebox.showinfo("Information", "Customer Details inserted successfully...")
        set_username(Username)
        ins_root.destroy()
        # import Admin_Page
        AdminPg()
    else:
        flag=1
        messagebox.showinfo("Information", "It didnt got inserted into DataBase due to some error!\nMaybe Because you entered Password Wrong!")



def insert_window():
    global dbpassword_entry,dbconfirm_password_entry,dbusername_entry,gender_var,ins_root
    # Create the main window
    ins_root = Tk()
    ins_root.title("Data Insertion")

    # Create and place Entry widgets and Labels
    username_label = Label(ins_root, text="Username:")
    username_label.grid(row=0, column=0, padx=10, pady=10)

    dbusername_entry = Entry(ins_root)
    dbusername_entry.grid(row=0, column=1, padx=10, pady=10)

    password_label = Label(ins_root, text="Password:")
    password_label.grid(row=1, column=0, padx=10, pady=10)

    dbpassword_entry = Entry(ins_root, show="*")
    dbpassword_entry.grid(row=1, column=1, padx=10, pady=10)

    confirm_password_label = Label(ins_root, text="Confirm Password:")
    confirm_password_label.grid(row=2, column=0, padx=10, pady=10)

    dbconfirm_password_entry = Entry(ins_root, show="*")
    dbconfirm_password_entry.grid(row=2, column=1, padx=10, pady=10)

    gender_label = Label(ins_root, text="Gender:")
    gender_label.grid(row=3, column=0, padx=10, pady=10)

    gender_var = StringVar()
    gender_var.set("Male")  # Default value
    gender_male_radio = Radiobutton(ins_root, text="Male", variable=gender_var, value="Male")
    gender_male_radio.grid(row=3, column=1, padx=10, pady=10, sticky="w")

    gender_female_radio = Radiobutton(ins_root, text="Female", variable=gender_var, value="Female")
    gender_female_radio.grid(row=3, column=1, padx=10, pady=10, sticky="e")

    # Create and place the Insert button
    insert_button = Button(ins_root, text="Insert", command=dbinsert_data)
    insert_button.grid(row=4, column=0, columnspan=2, pady=20)

    # Start the Tkinter main loop
    root.mainloop()




# ******************************************(DELETE_WINDOW)***********************************************




# import tkinter as tk
# from tkinter import messagebox
# import mysql.connector 


def delete_user():
    username = del_username_entry.get()
    if username:
        StormZ_db=mysql.connector.connect(host="localhost",user="root",password="pass@123",database="StormZ")
        StormZ_db_cursor=StormZ_db.cursor()
        try:
            StormZ_db_cursor.execute("DELETE FROM User WHERE Username = '"+username+"'")
            StormZ_db_cursor.execute("COMMIT")
            del_root.destroy()
            # import Admin_Page
            # Admin_Page.mainloop()
            
        except Exception as e:
            messagebox.showerror("Error",e)
        finally:
            messagebox.showinfo("Delete User", f"Deleting user: {username}")
            StormZ_db.close()
            
        AdminPg()
    else:
        messagebox.showerror("Error", "Please enter a username.")


def delete_window():
    global del_username_entry,del_root
    # Create the main window
    del_root = Tk()



    del_root.title("User Deletion Page")
    del_root.geometry("300x300")

    # Create and place Entry widget for username
    username_label = Label(del_root, text="Username:")
    username_label.pack(pady=10)

    del_username_entry = Entry(del_root, font=("Arial", 12))
    del_username_entry.pack(pady=10)

    # Create and place the Delete button
    delete_button = Button(del_root, text="Delete", command=delete_user, font=("Arial", 12), bg="red", fg="white")
    delete_button.pack(pady=20)

    # Start the Tkinter main loop
    del_root.mainloop()







# ******************************************(UPDATE_WINDOW)***********************************************


# import tkinter as tk
# from tkinter import messagebox
# import mysql.connector

def update_data():
    username = UP_username_entry.get()
    password=UP_password_entry.get()

    if not username:
        messagebox.showerror("Error", "Please enter a username")
        return

    try:
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="pass@123",  
            database="StormZ"
        )

        cursor = db.cursor()

        update_query = "UPDATE User SET Password = %s WHERE username = %s"
        cursor.execute(update_query, (password,username,))

        # Commit changes and close the connection
        db.commit()
        db.close()

        messagebox.showinfo("Success", f"Data updated successfully for Username: {username}")
        update_root.destroy()
        # import Admin_Page
        AdminPg()

    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Database Error: {err}")




def update_window():
    global UP_username_entry,UP_password_entry,update_root
    update_root = Tk()
    update_root.title("Data Update")

    username_label = Label(update_root, text="Enter Username:")
    username_label.grid(row=0, column=0, padx=10, pady=10)

    UP_username_entry = Entry(update_root)
    UP_username_entry.grid(row=0, column=1, padx=10, pady=10)

    username_label = Label(update_root, text="Enter New Password:")
    username_label.grid(row=1, column=0, padx=10, pady=10)

    UP_password_entry = Entry(update_root)
    UP_password_entry.grid(row=1, column=1, padx=10, pady=10)

    # Create and place the Update button
    update_button = Button(update_root, text="Update", command=update_data)
    update_button.grid(row=2, column=0, columnspan=2, pady=20)

    # Start the Tkinter main loop
    update_root.mainloop()


# **********************************************(ABOUTUS)*************************************************


from tkinter import Tk, Label, Entry, Frame, Canvas
import tkinter as tk
from PIL import Image, ImageTk



def set_opacity(widget, alpha):
    img = original_aboutus_image.copy()
    img.putalpha(int(255 * alpha))
    new_photo = ImageTk.PhotoImage(img)
    widget.configure(image=new_photo)
    widget.image = new_photo  # Keep a reference to avoid garbage collection

def show_username_label(event):
    abusername_label.place_configure(relx=0.25, rely=0.66, anchor="center") 
    set_opacity(aboutus_image_label, 0.3)

def hide_username_label(event):
    abusername_label.place_forget()
    set_opacity(aboutus_image_label, 1.0)



def about_us():
    global aboutus_image_label,original_aboutus_image,abusername_label
    about_us_root = Tk()
    about_us_root.title('Storm-Z Login')
    about_us_root.geometry("1450x720+45+20")
    about_us_root.resizable(True, True)
    about_us_root.config(bg="#B0DAFF")

    frame = Frame(about_us_root, width=700, height=400, bg='#046bdc')
    frame.place(relx=0.70, rely=0.6, anchor="center")

    heading = Label(about_us_root, text="About Us", fg="#046bdc",padx=90, pady=10,bg="#F4CE14", font=("Arial", 29, "bold"))
    heading.place(relx=0.5, rely=0.1, anchor="center")

    abusername_label = Label(frame, text="Trustworthy Brand \nCertified by top scientists globally\nGood for both physical and mental well-being\nStrengthens your immune and digestion system\nHigh-quality at an affordable price", fg="black",bg='#046bdc', font=("Microsoft Yahei UI Light", 21, "bold"))
    abusername_label.place(relx=0.5, rely=0.35, anchor="center")

    password_label = Label(frame, text="**Now available in 4 different flavours**", fg="black",bg='#046bdc',font=("Microsoft Yahei UI Light", 25, "bold"))
    password_label.place(relx=0.5, rely=0.78, anchor="center")

    team= Label(about_us_root, text="Our Team", fg="black", bg="#B0DAFF",font=("Times 20 italic bold", 26, "bold","italic"))
    team.place(relx=0.25, rely=0.25, anchor="center")

    features = Label(about_us_root, text="Our Features :", fg="black",bg="#B0DAFF", font=("Times 20 italic bold",26, "bold","italic"))
    features.place(relx=0.7, rely=0.25, anchor="center")

    # hover effect

    # root = tk.Tk()

    aboutus_path = "StormZ_aboutus.jpg"
    original_aboutus_image = Image.open(aboutus_path).resize((500, 400))
    aboutus_photo = ImageTk.PhotoImage(original_aboutus_image)

    aboutus_image_label = tk.Label(about_us_root, image=aboutus_photo)
    aboutus_image_label.place(relx=0.25, height=400, width=500, rely=0.6, anchor="center")

    username_label = Label(about_us_root, text="Vipul Mhatre\nRiddhesh Firake\nParth Mehta\nUthkrushta Mathur", fg="black",
                        font=("Times 20 italic bold", 21, "bold", "italic"))
    username_label.place_forget()

    aboutus_image_label.bind("<Enter>", show_username_label)
    aboutus_image_label.bind("<Leave>", hide_username_label)



    about_us_root.mainloop()




root.mainloop()
