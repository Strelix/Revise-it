import customtkinter
from customtkinter import LEFT, RIGHT, TOP, BOTTOM

from classes.DB import Database
from classes.Files import Files
from ui.LeftBar import LeftBar
from ui.Main import Main
from ui.Popup import Popup
from ui.TopBar import TopBar

from getpass import getpass
import sys, os

from classes.Login import Login

customtkinter.set_default_color_theme('dark-blue')
customtkinter.set_appearance_mode('dark')


class Window(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.DB = Database()
        self.LOGIN = Login(self.DB)
        self.FILES = Files()

        self.title('Revise.it')
        self.attributes('-fullscreen', True)

        self.screensize = self.winfo_screenwidth(), self.winfo_screenheight()

        self.topbar = TopBar(self)
        self.leftbar = LeftBar(self)

        self.main = Main(self)
        self.popup = Popup(self)

    def load_main(self):
        self.topbar.text = customtkinter.CTkLabel(master=self.topbar.top_bar, text='TEST')
        self.topbar.text.pack()

if __name__ == "__main__":
    ui = Window()

    ui.load_main()
    ui.mainloop()
