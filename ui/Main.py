import classes.TKMore as TKMoreClass
import customtkinter
from PIL import ImageTk, Image
from ui.pages import Login
from ui.pages import Profile
from ui.pages import Register

from customtkinter import LEFT, RIGHT, TOP, BOTTOM

pages = {
    'default': {
        "login": None,
        "admin": False
    },
    'login': {
        "login": None,
        "admin": False
    },
    'profile': {
        "login": True,
        "admin": False
    },
    'register': {
        "login": False,
        "admin": False
    }
}


class Main:
    def __init__(self, main):
        self.main_screen = main
        # self.

        self.TKMore: Main = TKMoreClass.TKMore()
        self.items: list = []
        self.theme: int = 0

        self.container: object = customtkinter.CTkFrame(master=main, width=main.screensize[0] - 100,
                                                        height=main.screensize[1] - 120,
                                                        corner_radius=20)
        self.container.pack(padx=15, pady=15)
        self.container.pack_propagate(False)

        self.heading: object = customtkinter.CTkLabel(master=self.container, text=' ',
                                                      text_font=('FredokaOne', '15', 'bold'))
        self.heading.pack(side=TOP, pady=15)

    def add_items_to_list(self, *items) -> None:
        try:
            for item in items:
                self.items.append(item)
        except:
            pass

    def delete_item_list(self) -> None:
        return [item.destroy() for item in self.items]

    def change_page(self, page='default', *arguments) -> None:
        page: str = page.lower()

        try:
            if pages[page]:
                pass
        except:
            return self.main_screen.popup.show_popup('Sadly we\'ve had an error loading this page.', 2, 'ERROR', 'red')
        else:
            if pages[page]:
                page_details = pages[page]
                if page_details["login"] == True:
                    if not self.main_screen.LOGIN.logged_in:
                        return self.main_screen.popup.show_popup('Please login to go to this page.', 2, 'ERROR', 'red')
                elif page_details["login"] == False:
                    if self.main_screen.LOGIN.logged_in:
                        return self.main_screen.popup.show_popup('You can\'t view this page while logged in.', 2, 'ERROR', 'red')

                if page_details["admin"]:
                    if not self.main_screen.LOGIN.admin:
                        return self.main_screen.popup.show_popup('This page is restricted to ADMINS.', 2, 'ERROR',
                                                                 'red')

        self.delete_item_list()

        if page == 'default':
            self.heading.set_text('WELCOME!')
        if page == 'register':
            self.register = Register.RegisterMain(self)

        if page == 'login':
            if self.main_screen.LOGIN.logged_in:
                self.change_page('profile')
            else:
                self.login = Login.LoginMain(self)

        if page == 'profile':
            if self.main_screen.LOGIN.logged_in:
                self.profile = Profile.ProfileMain(self)

        if page == 'staff':
            self.staff = Staff.StaffMain(self)

        if page == ' hack':
            self.hack = Hack.HackMain(self)

        if page == 'settings':
            self.settings = Settings.SettingsMain(self)
