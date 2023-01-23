import customtkinter, getpass
from PIL import ImageTk, Image
from customtkinter import LEFT, RIGHT, TOP, BOTTOM

from classes import TKMore

TkMore = TKMore.TKMore()


class CardsMain:
    def __init__(self, main):
        self.main_screen = main
        main.heading.set_text('Flashcards Dashboard')
        self.container = TkMore.container_main(main.container, main)
        self.container.propagate(False)
        self.container.configure(width=main.container.winfo_width() * 0.9, height=main.container.winfo_height() * 0.8)
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
        self.main_screen.add_items_to_list(self.result)

    def func_create_card(self):
        self.main_screen.delete_item_list()
