import json

import mariadb


class Database:
    def __init__(self):
        self.connection: mariadb.connect = None
        try:
            self.connection = mariadb.connect(user='root',
                                              database='revise_it',
                                              password='',
                                              host='localhost')
            print('[SERVER] Database Connected')
        except mariadb.Error as error_message:
            print(f'[SERVER] DataBase Error: {error_message}')
            exit('[SERVER] Database Error')

    def __execute(self, statement):
        try:
            cursor = self.connection.cursor()
            cursor.execute(statement)
            self.connection.commit()
            cursor.close()
        except mariadb.Error as error_message:
            print(f'[SERVER] Database Error: {error_message}')

    def __execute_params(self, statement, *params):
        try:
            cursor = self.connection.cursor()
            cursor.execute(statement, params)
            self.connection.commit()
            cursor.close()
        except mariadb.Error as error_message:
            print(f'[SERVER] Database Error: {error_message}')

    def __get_execute(self, statement):
        try:
            cursor = self.connection.cursor()
            cursor.execute(statement)
            saved = cursor.fetchall()
            cursor.close()
            return saved

        except mariadb.Error as error_message:
            print(f'[SERVER] Database Error: {error_message}')
            return

    def __get_execute_params(self, statement, *params):
        try:
            cursor = self.connection.cursor()
            cursor.execute(statement, params)
            saved = cursor.fetchall()
            cursor.close()
            return saved

        except mariadb.Error as error_message:
            print(f'[SERVER] Database Error: {error_message}')
            return

    def __get_users(self):
        return self.__get_execute('SELECT * FROM users')

    def get_all_users(self):
        return self.__get_users()

    def get_all_cards(self):
        return self.__get_execute('SELECT * FROM flashacrds')

    def append_user(self, username, pin) -> None:
        hashed_pin = pin
        statement = 'INSERT INTO users (username, password) VALUES (?, ?)'
        self.__execute_params(statement, username, pin)

    def get_user_from_name(self, username):
        return self.__get_execute_params('SELECT * FROM users WHERE username = ?', username)

    def get_cards_from_id(self, card_id):
        return self.__get_execute_params('SELECT * FROM flashcards WHERE id = ?', card_id)

    def get_cards_from_user_id(self, user_id):
        return self.__get_execute_params('SELECT * FROM flashcards WHERE user_id = ?', user_id)
