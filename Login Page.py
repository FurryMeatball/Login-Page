import tkinter as tk


window = tk.Tk() #create window
window.geometry("350x350") #set widnow size
label1 = tk.Label(text="Create Account", fg="white", bg="black", width = 200, height = 2) #create title
label1.pack()


label2= tk.Label(text = "Enter Username:") #Label for username entry box
label2.pack(padx=20, pady=3)


entry_username = tk.Entry()#create username entry box
entry_username.pack(padx=20, pady=3)


label3 = tk.Label(text = "Enter Password:") #Label for password entry box
label3.pack(padx=20, pady=3)


entry_password = tk.Entry()
entry_password.pack(padx=20, pady=3)


label4 = tk.Label(text = "Confirm Username:") #Label for username check entry box
label4.pack(padx=20, pady=3)


entry_checkuser = tk.Entry()
entry_checkuser.pack(padx=20, pady=3)


label5 = tk.Label(text = "Confirm Password:") #Label for password check entry box
label5.pack(padx=20, pady=3)


entry_checkpass = tk.Entry()
entry_checkpass.pack(padx=20, pady=3)



def checkCallBack():#command to be excecuted when button is pressed
    username = entry_username.get()
    password = entry_password.get()
    user_check = entry_checkuser.get()
    pass_check = entry_checkpass.get()
    if user_check != username or pass_check != password:
        label6 = tk.Label(text = "Username or password does not match. Try again.", fg = "red")
        label6.pack(padx=20, pady=3)
        entry_username.delete(0, tk.END)#clears all entry boxes if user and pass dont match
        entry_password.delete(0, tk.END)
        entry_checkuser.delete(0, tk.END)
        entry_checkpass.delete(0, tk.END)
    else:
        label7 = tk.Label(text = "Account created successfully", fg = "green")
        label7.pack(padx=20, pady=3)



check_button = tk.Button(text = "Create", command = checkCallBack)
check_button.pack(padx=20, pady=3)




window.mainloop()
