from tkinter import Tk, ttk, constants
from functions.cookbookapp_functions import cookbookapp_functions

class LoginView:
    def __init__(self, root, handle_login, handle_signin):
        self._root = root
        self._frame = None
        self._handle_login = handle_login
        self._handle_signin = handle_signin
        self._username_entry = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize_username_entry(self):
        username_label = ttk.Label(master=self._frame, text="Username:")
        self._username_entry = ttk.Entry(master=self._frame)

        username_label.grid(row=1, column=0, sticky=(constants.E, constants.W), padx=5, pady=15)
        self._username_entry.grid(row=1, column=1, sticky=(constants.E, constants.W), padx=5, pady=15)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        login_button = ttk.Button(
            master=self._frame, 
            text="Log in",
            command=self._check_login

        )
        signin_button = ttk.Button(
            master=self._frame, 
            text="Sign in",
            command=self._handle_signin
        )

        self._initialize_username_entry()
        
        login_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)
        signin_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

        self._frame.grid_columnconfigure(0, weight=1, minsize=100)

    def _check_login(self):
        username_data = str(self._username_entry.get())

        if cookbookapp_functions.log_in(username_data):
            self._handle_login()
        else:
            pass