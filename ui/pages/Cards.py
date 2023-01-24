import customtkinter, getpass
from PIL import ImageTk, Image
from customtkinter import *

from classes import TKMore

TkMore = TKMore.TKMore()


class CardsMain:
    def __init__(self, main):
        self.name_text = None
        self.name_field = None
        self.name_container = None
        self.main_screen = main
        main.heading.set_text('Flashcards Dashboard')
        self.container = TkMore.container_main(main.container, main)
        self.container.propagate(False)
        self.container.configure(width=(main.container.winfo_width() * 0.8), height=main.container.winfo_height() * 0.8)
        self.container.pack(side=TOP, pady=(main.container.winfo_height() * 0.05, 0))

        self.main_screen.add_items_to_list(self.container)

        res = self.main_screen.main_screen.LOGIN.get_flashcards()
        self.result = customtkinter.CTkLabel(master=self.container, text=res[1])
        if res[0]:
            if res[1]:
                pass
            else:
                self.result.configure(text='You currently dont have any flashcards.')
        else:
            self.result.configure(text=f'Error: {res[1]}')
        self.result.pack()
        self.create_card_button = TkMore.button_purple(self.container, 'Create Flashcard')
        self.create_card_button.pack()
        self.create_card_button.configure(command=self.func_create_card)
        self.main_screen.add_items_to_list(self.result, self.create_card_button)

    def func_create_card(self):
        self.main_screen.delete_item_list()
        self.container = TkMore.container_main(self.main_screen.container, self.main_screen)
        self.container.propagate(False)
        self.container.configure(width=(self.main_screen.container.winfo_width() * 0.8),
                                 height=self.main_screen.container.winfo_height() * 0.8)
        self.container.pack(side=TOP, pady=(self.main_screen.container.winfo_height() * 0.05, 0))

        self.details_container = customtkinter.CTkFrame(master=self.container,
                                                        width=self.main_screen.main_screen.screensize[0] * 0.3,
                                                        height=self.main_screen.main_screen.screensize[1] * 0.1)

        self.details_container.pack(side=TOP, pady=(self.main_screen.main_screen.screensize[1] * 0.1, 0))
        self.details_container.propagate(False)
        self.name_text = customtkinter.CTkLabel(master=self.details_container,
                                                text='Name: ', text_font=('FredokaOne 13 bold'))
        self.name_field = customtkinter.CTkEntry(master=self.details_container)
        self.name_text.pack(side=LEFT)
        self.name_field.pack(side=RIGHT, padx=(0, 30))

        self.details_container2 = customtkinter.CTkFrame(master=self.container,
                                                        width=self.main_screen.main_screen.screensize[0] * 0.3,
                                                        height=self.main_screen.main_screen.screensize[1] * 0.1)

        self.details_container2.pack(side=TOP, pady=(self.main_screen.main_screen.screensize[1] * 0.01, 0))
        self.details_container2.propagate(False)

        self.desc_text = customtkinter.CTkLabel(master=self.details_container2,
                                                text='Description: ', text_font=('FredokaOne 13 bold'))
        self.desc_field = customtkinter.CTkEntry(master=self.details_container2)
        self.desc_text.pack(side=LEFT)
        self.desc_field.pack(side=RIGHT, padx=(0, 30))
        self.create_button = TkMore.button_purple(self.container, 'Create Set')
        self.create_button.configure(command=self.create)
        self.create_button.pack(side=TOP)
        self.main_screen.add_items_to_list(self.create_button, self.name_field, self.name_text, self.details_container,
                                           self.container)

    def create(self):
        res = self.create_set()
        if res[0] == True:
            self.main_screen.change_page('cards')
        else:
            self.main_screen.delete_item_list()
            self.result = customtkinter.CTkLabel(master=self.container, text=res[1])
            self.result.pack()
            self.main_screen.add_items_to_list(self.result)

    def create_set(self):
        user_id = self.main_screen.main_screen.LOGIN.user_id
        name: str = self.name_field.get()
        desc: str = self.desc_field.get()
        namea = True
        desca = True

        if not name or not len(name) <= 20:
            for letter in name:
                if not letter.isalpha() and not letter.isnumeric():
                    namea = False

        if namea and desca:
            return True, self.main_screen.main_screen.DB.create_set(user_id, name, desc)
        elif not namea:
            return False, "The name is invalid. Please make sure it's between 0 and 20 in length."
        else:
            return False, "The description is invalid."
