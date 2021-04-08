from tkinter import Tk, ttk, constants
from functions.user_functions import UserFunctions

class SigninView:
    def __init__(self, root, handle_new_user):
        self._root = root
        self._frame = None
        self._handle_new_user = handle_new_user
        self._new_username_entry = None
        self._functions = UserFunctions()

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize_new_user_entry(self):
        new_username_label = ttk.Label(master=self._frame, text="New username:")
        self._new_username_entry = ttk.Entry(master=self._frame)

        new_username_label.grid(row=1, column=0, sticky=(constants.E, constants.W), padx=5, pady=15)
        self._new_username_entry.grid(row=1, column=1, sticky=(constants.E, constants.W), padx=5, pady=15)

    def _new_user(self):
        if self._new_username_entry != None:
            username_value = str(self._new_username_entry.get())
        
            self._functions.new_user(username_value)
        
        self._handle_new_user

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        new_user_button = ttk.Button(
            master=self._frame,
            text="Create new user",
            command=self._new_user
        )

        self._initialize_new_user_entry()
        new_user_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

        self._frame.grid_columnconfigure(0, weight=1, minsize=100)

        self._frame.pack()