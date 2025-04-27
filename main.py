import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title('Passwd Manager')
logo_pic = tk.PhotoImage(file='Images/logo.png')
window.iconphoto(False, logo_pic)
window.geometry('1000x500')

main_label = ttk.Label(master=window, text='Passwd Manager', font=('Arial', 25, 'bold'))
main_label.pack()

dashboard_button = ttk.Button(master=window, text='Dashboard')
dashboard_button.pack()

my_passwd_button = ttk.Button(master=window, text='My Passwords')
my_passwd_button.pack()


window.mainloop()
