import customtkinter as ctk
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

        # Drawing Canvas
        self.canvas = ctk.CTkCanvas(master=self, width=1280, height=720, bg=self.BG_COLOUR)

        # Interface Design
        if self.OPTION == 'sign_up':
            self.create_sign_up()
        self.create_dashboard()  # Does not display
        self.create_my_password()  # Does not display

        # Events
        """
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

        self.search_icon.bind('<Button-1>', self.on_search_click)"""

        # Desplaying Tab
        self.choose_tab()


    def choose_tab(self):
        if self.OPTION == 'sign_up':
            self.sign_up.place(x=20, y=20)
        elif self.OPTION == 'log_in':
            pass
        elif self.OPTION == 'dashboard':
            self.create_sidebar()
            self.create_search_add()

            self.dashboard_frame.place(x=300, y=85)
            self.my_passwd_frame.place_forget()
            self.sign_up.place_forget()

        elif self.OPTION == 'my_password':
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
        print('Add Passwd')


    def on_search_click(self, event):
        print('Search')

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

    def create_sign_up(self):
        core.gen_primary_key()
        user_name = ctk.StringVar()
        passwd = ctk.StringVar()

        self.sign_up = ctk.CTkFrame(master=self, bg_color=self.BG_COLOUR, fg_color='#adbc1d', width=1240, height=680, corner_radius=20)
        welcome_icon = ctk.CTkLabel(master=self.sign_up, text='', image=self.welcome_img)
        welcome_icon.place(x=0, y=0)
        sign_up_text = ctk.CTkLabel(master=self.sign_up, text='Sign Up', text_color=self.BG_COLOUR, font=('Inter', 50, 'bold'))
        sign_up_text.place(x=850, y=120)
        username_text = ctk.CTkLabel(master=self.sign_up, text='Username: ', font=('Inter', 25, 'normal'))
        username_text.place(x=720, y=300)
        username_entry = ctk.CTkEntry(master=self.sign_up, textvariable=user_name, border_width=0, width=300)
        username_entry.place(x=850, y=302)
        passwd_text = ctk.CTkLabel(master=self.sign_up, text='Password: ', font=('Inter', 25, 'normal'))
        passwd_text.place(x=720, y=350)
        passwd_entry = ctk.CTkEntry(master=self.sign_up, textvariable=passwd, border_width=0, width=300)
        passwd_entry.place(x=850, y=352)
        sign_up_button = ctk.CTkButton(master=self.sign_up, text='SIGN UP', width=432, command=lambda: self.new_user(user_name.get(), passwd.get()))
        sign_up_button.place(x=720, y=400)

    def create_log_in(self):
        pass

    def create_sidebar(self):
        # Side Bar Title
        self.side_bar_title = ctk.CTkLabel(master=self, text='Passwd Manager', text_color=self.FONT_COLOUR_1,
                                           font=('Inter', 24, 'bold'), bg_color=self.BG_COLOUR)
        self.side_bar_title.place(x=27, y=20)

        # Side Bar Option
        self.dashboard = ctk.CTkFrame(master=self, width=235, height=40, corner_radius=10,
                                      bg_color=self.BG_COLOUR, fg_color=self.HIGHLIGHT_COLOUR_1)
        self.dashboard_icon = ctk.CTkLabel(master=self.dashboard, text='', image=self.dashboard_img)
        self.dashboard_icon.place(x=15, y=5)
        self.dashboard_text = ctk.CTkLabel(master=self.dashboard, text='Dashboard', text_color=self.FONT_COLOUR_1,
                                           font=('Inter', 16, 'bold'))
        self.dashboard_text.place(x=50, y=6)
        self.dashboard.place(x=17, y=90)

        self.my_passwd = ctk.CTkFrame(master=self, width=235, height=40, corner_radius=10,
                                      bg_color=self.BG_COLOUR, fg_color=self.BG_COLOUR)
        self.my_passwd_icon = ctk.CTkLabel(master=self.my_passwd, text='', image=self.my_passwd_img)
        self.my_passwd_icon.place(x=15, y=5)
        self.my_passwd_text = ctk.CTkLabel(master=self.my_passwd, text='My Passwords', text_color=self.FONT_COLOUR_1,
                                           font=('Inter', 16, 'bold'))
        self.my_passwd_text.place(x=50, y=6)
        self.my_passwd.place(x=17, y=135)

        self.settings = ctk.CTkFrame(master=self, width=235, height=40, corner_radius=10,
                                     bg_color=self.BG_COLOUR, fg_color=self.BG_COLOUR)
        self.settings_icon = ctk.CTkLabel(master=self.settings, text='', image=self.settings_img)
        self.settings_icon.place(x=15, y=4)
        self.settings_text = ctk.CTkLabel(master=self.settings, text='Settings', text_color=self.FONT_COLOUR_1,
                                          font=('Inter', 16, 'bold'), bg_color=self.BG_COLOUR)
        self.settings_text.place(x=50, y=6)
        self.settings.place(x=17, y=650)

        # Drawing line
        self.canvas.create_line(335, 0, 335, 900, fill=self.HIGHLIGHT_COLOUR_1, width=3)
        self.canvas.pack(expand=True, fill='both')


    def create_search_add(self):
        # Search
        self.search = ctk.CTkFrame(master=self, width=720, height=52, corner_radius=28,
                                   bg_color=self.BG_COLOUR, fg_color=self.HIGHLIGHT_COLOUR_1)
        self.search.place(x=310, y=18)
        self.search_entry = ctk.CTkEntry(master=self.search, textvariable=self.SEARCH, height=48, width=660,
                                         border_width=0, fg_color=self.HIGHLIGHT_COLOUR_1)
        self.search_entry.place(x=15, y=2)
        self.search_icon = ctk.CTkLabel(master=self.search, text='', image=self.search_img)
        self.search_icon.place(x=678, y=9)

        # Add Passwd
        self.add = ctk.CTkFrame(master=self, width=183, height=40, corner_radius=8,
                                bg_color=self.BG_COLOUR, fg_color=self.BUTTON_COLOUR_1)
        self.add_text = ctk.CTkLabel(master=self.add, text='Add Password', font=('Inter', 16, 'normal'), text_color=self.FONT_COLOUR_2)
        self.add_text.place(x=20, y=6)
        self.add_icon = ctk.CTkLabel(master=self.add, text='', image=self.add_img)
        self.add_icon.place(x=140,y=6)
        self.add.place(x=1075, y=22)


    def create_dashboard(self):
        self.dashboard_frame = ctk.CTkFrame(master=self, width=950, height=620,
                                            bg_color=self.BG_COLOUR, fg_color=self.BG_COLOUR)
        self.dashboard_title = ctk.CTkLabel(master=self.dashboard_frame, text='My Dashboard', font=('Inter', 34, 'bold'))
        self.dashboard_title.place(x=2, y=8)

        # Passwords
        self.dashboard_frame_1_shadow = ctk.CTkFrame(master=self.dashboard_frame, width=300, height=77,
                                                     bg_color=self.BG_COLOUR, fg_color=self.HIGHLIGHT_COLOUR_1)
        self.dashboard_frame_1_shadow.place(x=5, y=80)
        self.dashboard_frame_1 = ctk.CTkFrame(master=self.dashboard_frame, width=300, height=77,
                                                     bg_color='transparent', fg_color=self.HIGHLIGHT_COLOUR_2)
        self.dashboard_frame_1.place(x=10, y=75)
        self.dash_pass = ctk.CTkLabel(master=self.dashboard_frame_1, text='Password',
                                      font=('Konkhmer Sleokchher', 16, 'bold'))
        self.dash_pass.place(x= 150, y=25, anchor='center')
        self.pass_value = ctk.CTkLabel(master=self.dashboard_frame_1, textvariable = self.PASSWORDS, text='',
                                      font=('Konkhmer Sleokchher', 16, 'bold'))
        self.pass_value.place(x = 150, y=50, anchor='center')

        # Mail ID
        self.dashboard_frame_2_shadow = ctk.CTkFrame(master=self.dashboard_frame, width=300, height=77,
                                                     bg_color=self.BG_COLOUR, fg_color=self.HIGHLIGHT_COLOUR_1)
        self.dashboard_frame_2_shadow.place(x=320, y=80)
        self.dashboard_frame_2 = ctk.CTkFrame(master=self.dashboard_frame, width=300, height=77,
                                              bg_color='transparent', fg_color=self.HIGHLIGHT_COLOUR_2)
        self.dashboard_frame_2.place(x=325, y=75)
        self.dash_mail = ctk.CTkLabel(master=self.dashboard_frame_2, text='Mail ID',
                                      font=('Konkhmer Sleokchher', 16, 'bold'))
        self.dash_mail.place(x=150, y=25, anchor='center')
        self.mail_value = ctk.CTkLabel(master=self.dashboard_frame_2, textvariable=self.MAIL_ID, text='',
                                       font=('Konkhmer Sleokchher', 16, 'bold'))
        self.mail_value.place(x=150, y=50, anchor='center')

        # Sites Secured
        self.dashboard_frame_3_shadow = ctk.CTkFrame(master=self.dashboard_frame, width=300, height=77,
                                                     bg_color=self.BG_COLOUR, fg_color=self.HIGHLIGHT_COLOUR_1)
        self.dashboard_frame_3_shadow.place(x=635, y=80)
        self.dashboard_frame_3 = ctk.CTkFrame(master=self.dashboard_frame, width=300, height=77,
                                              bg_color='transparent', fg_color=self.HIGHLIGHT_COLOUR_2)
        self.dashboard_frame_3.place(x=640, y=75)
        self.dash_site = ctk.CTkLabel(master=self.dashboard_frame_3, text='Sites Secured',
                                      font=('Konkhmer Sleokchher', 16, 'bold'))
        self.dash_site.place(x=150, y=25, anchor='center')
        self.site_value = ctk.CTkLabel(master=self.dashboard_frame_3, textvariable=self.SITES_SECURED, text='',
                                       font=('Konkhmer Sleokchher', 16, 'bold'))
        self.site_value.place(x=150, y=50, anchor='center')

        # Graph
        self.dashboard_graph_frame = ctk.CTkFrame(master=self.dashboard_frame, width=938, height=425,
                                                     bg_color=self.BG_COLOUR, fg_color=self.HIGHLIGHT_COLOUR_1)
        self.dashboard_graph_frame.place(x=5, y=168)


    def create_my_password(self):
        self.my_passwd_frame = ctk.CTkFrame(master=self, width=950, height=620,
                                            bg_color=self.BG_COLOUR, fg_color=self.BG_COLOUR)
        self.my_passwd_title = ctk.CTkLabel(master=self.my_passwd_frame, text='My Passwords',
                                            font=('Inter', 34, 'bold'))
        self.my_passwd_title.place(x=2, y=8)
        self.my_passwd_table_frame = ctk.CTkFrame(master=self.my_passwd_frame, width=938, height=518,
                                                  bg_color=self.BG_COLOUR, fg_color=self.HIGHLIGHT_COLOUR_1)
        self.my_passwd_table_frame.place(x=5, y=75)


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
