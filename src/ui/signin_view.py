from tkinter import Tk, ttk, constants
from functions.cookbookapp_functions import cookbookapp_functions


class SigninView:
    def __init__(self, root, handle_create_new_user):
        self._root = root
        self._frame = None
        self._handle_create_new_user = handle_create_new_user
        self._new_username_entry = None
        self._password_entry = None
        self._error_label = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize_new_user_entry(self):
        new_username_label = ttk.Label(
            master=self._frame, text="New username:")
        self._new_username_entry = ttk.Entry(master=self._frame)

        new_username_label.grid(row=1, column=0, sticky=(
            constants.E, constants.W), padx=5, pady=15)
        self._new_username_entry.grid(row=1, column=1, sticky=(
            constants.E, constants.W), padx=5, pady=15)

    def _initialize_password_entry(self):
        password_label = ttk.Label(master=self._frame, text="Password:")
        self._password_entry = ttk.Entry(master=self._frame, show="*")

        password_label.grid(row=2, column=0, sticky=(
            constants.E, constants.W), padx=5, pady=15)
        self._password_entry.grid(row=2, column=1, sticky=(
            constants.E, constants.W), padx=5, pady=15)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        self._new_user_button = ttk.Button(
            master=self._frame,
            text="Create new user",
            command=self._check_new_username
        )

        self._initialize_new_user_entry()
        self._initialize_password_entry()

        self._new_user_button.grid(
            row=3, column=0, columnspan=2, padx=5, pady=5)

        self._hide_error_label()

        self._frame.grid_columnconfigure(0, weight=1, minsize=100)

    def _check_new_username(self):
        new_username_data = self._new_username_entry.get()
        password_data = str(self._password_entry.get())

        if len(new_username_data) > 0:
            if len(password_data) > 0:
                if cookbookapp_functions.sign_in(new_username_data, password_data):
                    self._handle_create_new_user()
                else:
                    self._show_error_label("Error: username is taken")
            else:
                self._show_error_label("Error: password must be longer")
        else:
            self._show_error_label("Error: username must be longer")

    def _show_error_label(self, message):

        self._hide_error_label()

        self._error_label = ttk.Label(master=self._frame, text=message)

        self._error_label.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

    def _hide_error_label(self):
        if self._error_label:
            self._error_label.grid_remove()
