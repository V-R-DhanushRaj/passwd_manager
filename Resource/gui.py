import customtkinter as tk
import settings

class GUI(tk.CTk):
    def __init__(self):
        super().__init__()
        self.app_mode = settings.appearance_mode
        tk.set_appearance_mode(self.app_mode)

        # Variables
        self.OPTION = 'dashboard'
        self.colour_choose()

        # Window Settings
        self.title('Passwd Manager')
        self.geometry('1280x720')
        self.config(bg=self.BG_COLOUR)
        self.resizable(False, False)

        # Drawing Canvas
        self.canvas = tk.CTkCanvas(master=self, width=1280, height=720, bg=self.BG_COLOUR)
        self.canvas.create_line(335,0, 335,900, fill=self.HIGHLIGHT_COLOUR_1, width=3)
        self.canvas.pack(expand=True, fill='both')

        # Side Bar Title
        self.side_bar_title = tk.CTkLabel(master=self, text='Passwd Manager', text_color=self.FONT_COLOUR_1,
                                          font=('Inter', 24, 'bold'), bg_color=self.BG_COLOUR)
        self.side_bar_title.place(x=27, y=20)

        # Side Bar Option
        self.dashboard = tk.CTkFrame(master=self, width=235, height=40, corner_radius=10, bg_color=self.BG_COLOUR, fg_color=self.HIGHLIGHT_COLOUR_1,)
        self.dashboard_text = tk.CTkLabel(master=self.dashboard, text='Dashboard', text_color=self.FONT_COLOUR_1,
                                          font=('Inter', 16, 'bold'))
        self.dashboard_text.place(x=50, y=6)
        self.dashboard.place(x=17, y=90)

        self.my_passwd = tk.CTkFrame(master=self, width=235, height=40, corner_radius=10, bg_color=self.BG_COLOUR, fg_color=self.BG_COLOUR)
        self.my_passwd_text = tk.CTkLabel(master=self.my_passwd, text='My Passwords', text_color=self.FONT_COLOUR_1,
                                          font=('Inter', 16, 'bold'))
        self.my_passwd_text.place(x=50, y=6)
        self.my_passwd.place(x=17, y=135)

        self.settings = tk.CTkFrame(master=self, width=235, height=40, corner_radius=10, bg_color=self.BG_COLOUR, fg_color=self.BG_COLOUR)
        self.settings_text = tk.CTkLabel(master=self.settings, text='Settings', text_color=self.FONT_COLOUR_1,
                                          font=('Inter', 16, 'bold'), bg_color=self.BG_COLOUR)
        self.settings_text.place(x=50, y=6)
        self.settings.place(x=17, y=650)


    def colour_choose(self):
        if self.app_mode == 'light':
            self.BG_COLOUR = '#ffffff'
            self.HIGHLIGHT_COLOUR_1 = '#eeeeef'
            self.HIGHLIGHT_COLOUR_2 = '#cecece'
            self.BUTTON_COLOUR_1 = '#000000'
            self.FONT_COLOUR_1 = '#000000'
            self.FONT_COLOUR_2 = '#ffffff'
        elif self.app_mode == 'dark':
            self.BG_COLOUR = 'ffffff'  # change later for all
            self.HIGHLIGHT_COLOUR_1 = 'eeeeef'
            self.HIGHLIGHT_COLOUR_2 = 'cecece'
            self.BUTTON_COLOUR_1 = '000000'
            self.FONT_COLOUR_1 = '000000'
            self.FONT_COLOUR_2 = 'ffffff'

gui = GUI()
gui.mainloop()