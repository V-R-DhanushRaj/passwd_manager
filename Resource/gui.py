import customtkinter as ctk
import tkinter.messagebox
from PIL import Image
import settings, core
import json


class GUI(ctk.CTk):
    def __init__(self):
        with open('./Resource/setting.json') as settings_file:
            data = json.load(settings_file)

        super().__init__()
        self.APP_MODE = data["appearance_mode"]
        ctk.set_appearance_mode(self.APP_MODE)

        # Images
        self.dashboard_img = ctk.CTkImage(light_image=Image.open("./Images/dashboard_light.png"),
                                          dark_image=Image.open('./Images/dashboard_light.png'), size=(30, 30))
        self.my_passwd_img = ctk.CTkImage(light_image=Image.open('./Images/analytics_light.png'),
                                          dark_image=Image.open('./Images/analytics_light.png'), size=(30, 30))
        self.settings_img = ctk.CTkImage(light_image=Image.open('./Images/settings_light.png'),
                                          dark_image=Image.open('./Images/settings_light.png'), size=(30, 30))
        self.search_img = ctk.CTkImage(light_image=Image.open('./Images/search.png'),
                                          dark_image=Image.open('./Images/search.png'), size=(30, 30))
        self.add_img = ctk.CTkImage(light_image=Image.open('./Images/add_light.png'),
                                          dark_image=Image.open('./Images/add_light.png'), size=(25, 25))
        self.welcome_img = ctk.CTkImage(light_image=Image.open('./Images/sign_up.png'),
                                          dark_image=Image.open('./Images/sign_up.png'), size=(620, 680))

        # Variables
        self.OPTION = data["page"]
        self.USERS = data["users"]
        self.SEARCH = ctk.StringVar(value='Search Password')
        self.PASSWORDS = ctk.IntVar(value=data["passwords"])
        self.MAIL_ID = ctk.IntVar(value=data["mail_id"])
        self.SITES_SECURED = ctk.IntVar(value=data["sites_secured"])
        self.colour_choose()

        # Window Settings
        self.title('Passwd Manager')
        self.geometry('1280x720')
        self.config(bg=self.BG_COLOUR)
        self.iconbitmap('./Images/logo.ico')
        self.resizable(False, False)

        # Drawing line
        self.canvas = ctk.CTkCanvas(master=self, width=1280, height=720, bg=self.BG_COLOUR)
        self.canvas.create_line(335, 0, 335, 900, fill=self.HIGHLIGHT_COLOUR_1, width=3)

        # Interface Design
        if self.OPTION == 'sign_up':
            self.create_sign_up()
        else:
            self.create_log_in()
        self.create_sidebar()
        self.create_search_add()
        self.create_dashboard()
        self.create_my_password()

        # Events
        self.dashboard.bind('<Button-1>', self.on_dashboard_click)
        for widget in self.dashboard.winfo_children():
            widget.bind("<Button-1>", self.on_dashboard_click)

        self.my_passwd.bind('<Button-1>', self.on_my_passwd_click)
        for widget in self.my_passwd.winfo_children():
            widget.bind("<Button-1>", self.on_my_passwd_click)

        self.settings.bind('<Button-1>', self.on_settings_click)
        for widget in self.settings.winfo_children():
            widget.bind("<Button-1>", self.on_settings_click)

        self.add.bind('<Button-1>', self.on_add_click)
        for widget in self.add.winfo_children():
            widget.bind("<Button-1>", self.on_add_click)

        self.search_icon.bind('<Button-1>', self.on_search_click)

        # Displaying Tab
        self.OPTION = 'dashboard'
        self.choose_tab()


    def choose_tab(self):
        if self.OPTION == 'sign_up':
            self.canvas.pack_forget()
            self.sign_up.place(x=20, y=20)

        elif self.OPTION == 'log_in':
            self.log_in.place(x=0,y=0)
            self.canvas.pack_forget()

        elif self.OPTION == 'dashboard':
            self.canvas.pack(expand=True, fill='both')
            self.side_bar.place(x=0, y=2)
            self.search_add.place(x=300,y=15)
            self.dashboard_frame.place(x=300, y=85)
            self.my_passwd_frame.place_forget()
            try:
                self.sign_up.place_forget()
            except:
                self.log_in.place_forget()

        elif self.OPTION == 'my_password':
            self.canvas.pack(expand=True, fill='both')
            self.side_bar.place(x=0, y=2)
            self.search_add.place(x=300, y=15)
            self.my_passwd_frame.place(x=300, y=85)
            self.dashboard_frame.place_forget()


    def on_dashboard_click(self, event):
        self.OPTION = 'dashboard'
        self.dashboard.configure(fg_color=self.HIGHLIGHT_COLOUR_1)
        self.my_passwd.configure(fg_color=self.BG_COLOUR)
        self.choose_tab()


    def on_my_passwd_click(self, event):
        self.OPTION = 'my_password'
        self.dashboard.configure(fg_color=self.BG_COLOUR)
        self.my_passwd.configure(fg_color=self.HIGHLIGHT_COLOUR_1)
        self.choose_tab()


    def on_settings_click(self, event):
        print('Settings')


    def on_add_click(self, event):
        self.add_passwd_popup()


    def on_search_click(self, event):
        print('Search')


    def add_passwd(self, web, id, passwd, note_textbox):
        if web.get() == '' or id.get() == '' or passwd.get() == '':
            tkinter.messagebox.showerror('Empty Input', "Don't leave any input empty!")
        else:
            self.add_popup.destroy()
            print(note_textbox.get('1.0', 'end'))
            #core.save_passwd(self.USERNAME, web.get(), id.get(), passwd.get(), note_textbox.g)



    def add_passwd_popup(self):
        self.add_popup = ctk.CTkToplevel(self)
        self.add_popup.geometry('430x620')
        self.add_popup.title('Adding password...')
        self.add_popup.iconbitmap('./Images/logo.ico')
        self.add_popup.configure(fg_color='#444444')
        self.add_popup.resizable(False, False)

        website_name = ctk.StringVar()
        emailid = ctk.StringVar()
        passwd = ctk.StringVar()

        title = ctk.CTkLabel(master=self.add_popup, text='Add Password!', font=('normal', 30, 'bold'), corner_radius=45, fg_color='#808080', text_color='white', width= 380, height=40)
        title.place(x=25, y=30)
        web_title = ctk.CTkLabel(master=self.add_popup, text='Website name: ', font=('normal', 20, 'bold'), text_color='white')
        web_title.place(x=20, y=100)
        web_entry = ctk.CTkEntry(master=self.add_popup, textvariable=website_name, width=230)
        web_entry.place(x=180, y=100)
        mail_title = ctk.CTkLabel(master=self.add_popup, text='Email ID: ', font=('normal', 20, 'bold'), text_color='white')
        mail_title.place(x=20, y=150)
        mail_entry = ctk.CTkEntry(master=self.add_popup, textvariable=emailid, width=230)
        mail_entry.place(x=180, y=150)
        password_title = ctk.CTkLabel(master=self.add_popup, text='Password: ', font=('normal', 20, 'bold'), text_color='white')
        password_title.place(x=20, y=200)
        passwd_entry = ctk.CTkEntry(master=self.add_popup, textvariable=passwd, width=190)
        passwd_entry.place(x=180, y=200)
        rand_passwd = ctk.CTkButton(master=self.add_popup, text='+', width=35, command=lambda: passwd.set(core.generate_password()), fg_color='grey', hover_color='darkgrey')
        rand_passwd.place(x=375, y=200)
        note_title = ctk.CTkLabel(master=self.add_popup, text='NOTE', font=('normal', 20, 'bold'), text_color='white')
        note_title.place(x=20, y=250)
        note_box = ctk.CTkTextbox(master=self.add_popup, width=390, height=200)
        note_box.place(x=20, y=280)

        back_button = ctk.CTkButton(master=self.add_popup, text='Back', width=190, fg_color='grey', hover_color='darkgrey', command=self.add_popup.destroy)
        back_button.place(x=20, y=570)
        add_button = ctk.CTkButton(master=self.add_popup, text='Add Password', width=190, fg_color='grey', hover_color='darkgrey', command=lambda :self.add_passwd(website_name, emailid, passwd, note_box))
        add_button.place(x=220, y=570)







    def new_user(self, username, passwd):
        # Changing setting.json
        file = open('./Resource/setting.json', 'r')
        data = json.load(file)
        file.close()
        data["page"] = "log_in"
        data["users"] = [username]
        file = open('./Resource/setting.json', 'w')
        json.dump(data, file)
        file.close()

        core.gen_secondary_key(username, passwd)
        core.create_file(username)
        self.OPTION = 'dashboard'
        self.choose_tab()


    def varify_user(self, username, password):
        key = core.get_key(username)
        check_key = core.passwd_to_key(password).decode()
        if key == check_key:
            self.OPTION = 'dashboard'
            self.choose_tab()

        else:
            self.log_in.place_forget()
            self.log_in.place(x=0, y=0)
            error_window = tkinter.messagebox.showinfo('Error', "Incorrect Password")


    def create_sign_up(self):
        core.gen_primary_key()
        user_name = ctk.StringVar()
        passwd = ctk.StringVar()

        self.sign_up = ctk.CTkFrame(master=self, bg_color=self.BG_COLOUR, fg_color='#adbc1d',
                                    width=1240, height=680, corner_radius=20)
        welcome_icon = ctk.CTkLabel(master=self.sign_up, text='', image=self.welcome_img)
        welcome_icon.place(x=0, y=0)
        sign_up_text = ctk.CTkLabel(master=self.sign_up, text='Sign Up', text_color=self.BG_COLOUR,
                                    font=('Inter', 50, 'bold'))
        sign_up_text.place(x=850, y=120)
        username_text = ctk.CTkLabel(master=self.sign_up, text='Username: ', font=('Inter', 25, 'normal'))
        username_text.place(x=720, y=300)
        username_entry = ctk.CTkEntry(master=self.sign_up, textvariable=user_name, border_width=0, width=300)
        username_entry.place(x=850, y=302)
        passwd_text = ctk.CTkLabel(master=self.sign_up, text='Password: ', font=('Inter', 25, 'normal'))
        passwd_text.place(x=720, y=350)
        passwd_entry = ctk.CTkEntry(master=self.sign_up, textvariable=passwd, border_width=0, width=300)
        passwd_entry.place(x=850, y=352)
        sign_up_button = ctk.CTkButton(master=self.sign_up, text='SIGN UP', width=432,
                                       command=lambda: self.new_user(user_name.get(), passwd.get()))
        sign_up_button.place(x=720, y=400)


    def create_log_in(self):
        user_name = ctk.StringVar()
        passwd = ctk.StringVar()

        self.log_in = ctk.CTkFrame(master=self, bg_color=self.BG_COLOUR, fg_color=self.BG_COLOUR,
                                   width=1280, height=720)
        login_frame = ctk.CTkFrame(master=self.log_in, bg_color=self.BG_COLOUR, fg_color=self.BG_COLOUR, height=660,
                                   border_color=self.HIGHLIGHT_COLOUR_2, width=1220, border_width=5, corner_radius=30)
        login_frame.place(x=30, y=30)
        title = ctk.CTkLabel(master=self.log_in, bg_color=self.BG_COLOUR, text_color=self.HIGHLIGHT_COLOUR_2,
                             text='Passwd Manager', font=('Inter', 25, 'bold'), width=220)
        title.place(x=80, y=15)
        log_in_title = ctk.CTkLabel(master=self.log_in, text='Log In', font=('Inter', 50, 'bold'))
        log_in_title.place(x=580, y= 200)
        username_text = ctk.CTkLabel(master=self.log_in, text='Username: ', font=('Inter', 25, 'normal'))
        username_text.place(x=450, y=300)
        username_dropdown = ctk.CTkComboBox(master=self.log_in, variable=user_name, width=300, bg_color=self.BG_COLOUR,
                                            fg_color=self.HIGHLIGHT_COLOUR_2, dropdown_fg_color=self.HIGHLIGHT_COLOUR_1,
                                            border_color=self.HIGHLIGHT_COLOUR_2, values=self.USERS,
                                            dropdown_hover_color=self.HIGHLIGHT_COLOUR_1)
        username_dropdown.place(x=580, y=302)
        passwd_text = ctk.CTkLabel(master=self.log_in, text='Password: ', font=('Inter', 25, 'normal'))
        passwd_text.place(x=450, y=350)
        passwd_entry = ctk.CTkEntry(master=self.log_in, textvariable=passwd, border_width=0, width=300,
                                    bg_color=self.BG_COLOUR, fg_color=self.HIGHLIGHT_COLOUR_2)
        passwd_entry.place(x=580, y=352)
        sign_up_button = ctk.CTkButton(master=self.log_in, text='LOG IN', width=432,
                                       command=lambda: self.varify_user(user_name.get(), passwd.get()))
        sign_up_button.place(x=450, y=400)


    def create_sidebar(self):
        # Drawing line
        self.canvas = ctk.CTkCanvas(master=self, width=1280, height=720, bg=self.BG_COLOUR)
        self.canvas.create_line(335, 0, 335, 900, fill=self.HIGHLIGHT_COLOUR_1, width=3)
        self.canvas.pack(expand=True, fill='both')

        self.side_bar = ctk.CTkFrame(master=self, bg_color=self.BG_COLOUR, fg_color=self.BG_COLOUR,
                                     width=250, height=700)
        # Side Bar Title
        side_bar_title = ctk.CTkLabel(master=self.side_bar, text='Passwd Manager', text_color=self.FONT_COLOUR_1,
                                           font=('Inter', 24, 'bold'), bg_color=self.BG_COLOUR)
        side_bar_title.place(x=27, y=18)

        # Side Bar Option
        self.dashboard = ctk.CTkFrame(master=self.side_bar, width=235, height=40, corner_radius=10,
                                      bg_color=self.BG_COLOUR, fg_color=self.HIGHLIGHT_COLOUR_1)
        dashboard_icon = ctk.CTkLabel(master=self.dashboard, text='', image=self.dashboard_img)
        dashboard_icon.place(x=15, y=5)
        dashboard_text = ctk.CTkLabel(master=self.dashboard, text='Dashboard', text_color=self.FONT_COLOUR_1,
                                           font=('Inter', 16, 'bold'))
        dashboard_text.place(x=50, y=6)
        self.dashboard.place(x=17, y=90)

        self.my_passwd = ctk.CTkFrame(master=self.side_bar, width=235, height=40, corner_radius=10,
                                      bg_color=self.BG_COLOUR, fg_color=self.BG_COLOUR)
        my_passwd_icon = ctk.CTkLabel(master=self.my_passwd, text='', image=self.my_passwd_img)
        my_passwd_icon.place(x=15, y=5)
        my_passwd_text = ctk.CTkLabel(master=self.my_passwd, text='My Passwords', text_color=self.FONT_COLOUR_1,
                                           font=('Inter', 16, 'bold'))
        my_passwd_text.place(x=50, y=6)
        self.my_passwd.place(x=17, y=135)

        self.settings = ctk.CTkFrame(master=self.side_bar, width=235, height=40, corner_radius=10,
                                     bg_color=self.BG_COLOUR, fg_color=self.BG_COLOUR)
        settings_icon = ctk.CTkLabel(master=self.settings, text='', image=self.settings_img)
        settings_icon.place(x=15, y=4)
        settings_text = ctk.CTkLabel(master=self.settings, text='Settings', text_color=self.FONT_COLOUR_1,
                                          font=('Inter', 16, 'bold'), bg_color=self.BG_COLOUR)
        settings_text.place(x=50, y=6)
        self.settings.place(x=17, y=650)


    def create_search_add(self):
        # Search
        self.search_add = ctk.CTkFrame(master=self, width=950, height=60,
                                       bg_color=self.BG_COLOUR, fg_color=self.BG_COLOUR)
        search = ctk.CTkFrame(master=self.search_add, width=720, height=52, corner_radius=28,
                                   bg_color=self.BG_COLOUR, fg_color=self.HIGHLIGHT_COLOUR_1)
        search.place(x=2, y=2)
        search_entry = ctk.CTkEntry(master=search, textvariable=self.SEARCH, height=48, width=660,
                                         border_width=0, fg_color=self.HIGHLIGHT_COLOUR_1)
        search_entry.place(x=15, y=2)
        self.search_icon = ctk.CTkLabel(master=search, text='', image=self.search_img)
        self.search_icon.place(x=678, y=9)

        # Add Passwd
        self.add = ctk.CTkFrame(master=self.search_add, width=183, height=40, corner_radius=8,
                                bg_color=self.BG_COLOUR, fg_color=self.BUTTON_COLOUR_1)
        add_text = ctk.CTkLabel(master=self.add, text='Add Password', font=('Inter', 16, 'normal'),
                                text_color=self.FONT_COLOUR_2)
        add_text.place(x=20, y=6)
        add_icon = ctk.CTkLabel(master=self.add, text='', image=self.add_img)
        add_icon.place(x=140,y=6)
        self.add.place(x=750, y=8)


    def create_dashboard(self):
        self.dashboard_frame = ctk.CTkFrame(master=self, width=950, height=620,
                                            bg_color=self.BG_COLOUR, fg_color=self.BG_COLOUR)
        dashboard_title = ctk.CTkLabel(master=self.dashboard_frame, text='My Dashboard', font=('Inter', 34, 'bold'))
        dashboard_title.place(x=2, y=8)

        # Passwords
        dashboard_frame_1_shadow = ctk.CTkFrame(master=self.dashboard_frame, width=300, height=77,
                                                     bg_color=self.BG_COLOUR, fg_color=self.HIGHLIGHT_COLOUR_1)
        dashboard_frame_1_shadow.place(x=5, y=80)
        dashboard_frame_1 = ctk.CTkFrame(master=self.dashboard_frame, width=300, height=77,
                                                     bg_color='transparent', fg_color=self.HIGHLIGHT_COLOUR_2)
        dashboard_frame_1.place(x=10, y=75)
        dash_pass = ctk.CTkLabel(master=dashboard_frame_1, text='Password',
                                      font=('Konkhmer Sleokchher', 16, 'bold'))
        dash_pass.place(x= 150, y=25, anchor='center')
        pass_value = ctk.CTkLabel(master=dashboard_frame_1, textvariable = self.PASSWORDS, text='',
                                      font=('Konkhmer Sleokchher', 16, 'bold'))
        pass_value.place(x = 150, y=50, anchor='center')

        # Mail ID
        dashboard_frame_2_shadow = ctk.CTkFrame(master=self.dashboard_frame, width=300, height=77,
                                                     bg_color=self.BG_COLOUR, fg_color=self.HIGHLIGHT_COLOUR_1)
        dashboard_frame_2_shadow.place(x=320, y=80)
        dashboard_frame_2 = ctk.CTkFrame(master=self.dashboard_frame, width=300, height=77,
                                              bg_color='transparent', fg_color=self.HIGHLIGHT_COLOUR_2)
        dashboard_frame_2.place(x=325, y=75)
        dash_mail = ctk.CTkLabel(master=dashboard_frame_2, text='Mail ID',
                                      font=('Konkhmer Sleokchher', 16, 'bold'))
        dash_mail.place(x=150, y=25, anchor='center')
        mail_value = ctk.CTkLabel(master=dashboard_frame_2, textvariable=self.MAIL_ID, text='',
                                       font=('Konkhmer Sleokchher', 16, 'bold'))
        mail_value.place(x=150, y=50, anchor='center')

        # Sites Secured
        dashboard_frame_3_shadow = ctk.CTkFrame(master=self.dashboard_frame, width=300, height=77,
                                                     bg_color=self.BG_COLOUR, fg_color=self.HIGHLIGHT_COLOUR_1)
        dashboard_frame_3_shadow.place(x=635, y=80)
        dashboard_frame_3 = ctk.CTkFrame(master=self.dashboard_frame, width=300, height=77,
                                              bg_color='transparent', fg_color=self.HIGHLIGHT_COLOUR_2)
        dashboard_frame_3.place(x=640, y=75)
        dash_site = ctk.CTkLabel(master=dashboard_frame_3, text='Sites Secured',
                                      font=('Konkhmer Sleokchher', 16, 'bold'))
        dash_site.place(x=150, y=25, anchor='center')
        site_value = ctk.CTkLabel(master=dashboard_frame_3, textvariable=self.SITES_SECURED, text='',
                                       font=('Konkhmer Sleokchher', 16, 'bold'))
        site_value.place(x=150, y=50, anchor='center')

        # Graph
        dashboard_graph_frame = ctk.CTkFrame(master=self.dashboard_frame, width=938, height=425,
                                                     bg_color=self.BG_COLOUR, fg_color=self.HIGHLIGHT_COLOUR_1)
        dashboard_graph_frame.place(x=5, y=168)


    def create_my_password(self):
        self.my_passwd_frame = ctk.CTkFrame(master=self, width=950, height=620,
                                            bg_color=self.BG_COLOUR, fg_color=self.BG_COLOUR)
        my_passwd_title = ctk.CTkLabel(master=self.my_passwd_frame, text='My Passwords',
                                            font=('Inter', 34, 'bold'))
        my_passwd_title.place(x=2, y=8)
        my_passwd_table_frame = ctk.CTkFrame(master=self.my_passwd_frame, width=938, height=518,
                                                  bg_color=self.BG_COLOUR, fg_color=self.HIGHLIGHT_COLOUR_1)
        my_passwd_table_frame.place(x=5, y=75)


    def colour_choose(self):
        if self.APP_MODE == 'light':
            self.BG_COLOUR = '#ffffff'
            self.HIGHLIGHT_COLOUR_1 = '#eeeeef'
            self.HIGHLIGHT_COLOUR_2 = '#cecece'
            self.BUTTON_COLOUR_1 = '#000000'
            self.FONT_COLOUR_1 = '#000000'
            self.FONT_COLOUR_2 = '#ffffff'
        elif self.APP_MODE == 'dark':
            self.BG_COLOUR = 'ffffff'  # TODO: change later for all
            self.HIGHLIGHT_COLOUR_1 = 'eeeeef'
            self.HIGHLIGHT_COLOUR_2 = 'cecece'
            self.BUTTON_COLOUR_1 = '000000'
            self.FONT_COLOUR_1 = '000000'
            self.FONT_COLOUR_2 = 'ffffff'
