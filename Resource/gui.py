import customtkinter as ctk
from PIL import Image
import settings

class GUI(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.APP_MODE = settings.appearance_mode
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

        # Variables
        self.OPTION = 'dashboard'
        self.SEARCH = ctk.StringVar(value='Search Password')
        self.colour_choose()

        # Window Settings
        self.title('Passwd Manager')
        self.geometry('1280x720')
        self.config(bg=self.BG_COLOUR)
        self.iconbitmap('./Images/logo.ico')
        self.resizable(False, False)

        # Drawing Canvas
        self.canvas = ctk.CTkCanvas(master=self, width=1280, height=720, bg=self.BG_COLOUR)
        self.canvas.create_line(335,0, 335,900, fill=self.HIGHLIGHT_COLOUR_1, width=3)
        self.canvas.pack(expand=True, fill='both')

        # Interface Design
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


    def on_dashboard_click(self, event):
        print('Dashboard')


    def on_my_passwd_click(self, event):
        print('My Passwd')


    def on_settings_click(self, event):
        print('Settings')


    def on_add_click(self, event):
        print('Add Passwd')


    def on_search_click(self, event):
        print('Search')


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
        pass


    def create_my_password(self):
        pass


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
