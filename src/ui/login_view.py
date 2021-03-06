from tkinter import Tk, ttk, constants
from functions.cookbookapp_functions import cookbookapp_functions


class InvalidLength(Exception):
    pass


class LoginView:
    """Class that initializes log in -window of ui.
    """

    def __init__(self, root, handle_login, handle_signin):
        """Constructor of class that keeps track of the frame, username- and password entries, error labels, and necessary functions to change the window. 
        Log in -window is initialized in class constructor.

        Args:
            root (Tk): The root in class Tk() that is required to initialize a window.
            handle_login (function): Function _show_book() of class UI.
            handle_signin (function): Function _show_signin() of class UI.
        """

        self._root = root
        self._frame = None
        self._handle_login = handle_login
        self._handle_signin = handle_signin
        self._username_entry = None
        self._password_entry = None
        self._error_label = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize_username_entry(self):
        """Constructs label and entry where the user can input their username.
        """

        username_label = ttk.Label(master=self._frame, text="Username:")
        self._username_entry = ttk.Entry(master=self._frame)

        username_label.grid(row=1, column=0, sticky=(
            constants.E, constants.W), padx=5, pady=15)
        self._username_entry.grid(row=1, column=1, columnspan=2, sticky=(
            constants.E, constants.W), padx=5, pady=15)

    def _initialize_password_entry(self):
        """Constructs label and entry where the user can input their password.
        """

        password_label = ttk.Label(master=self._frame, text="Password:")
        self._password_entry = ttk.Entry(master=self._frame, show="*")

        password_label.grid(row=2, column=0, sticky=(
            constants.E, constants.W), padx=5, pady=15)
        self._password_entry.grid(row=2, column=1, columnspan=2, sticky=(
            constants.E, constants.W), padx=5, pady=15)

    def _initialize(self):
        """Initializes the log in -window with the necessary elements.
        """

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
        self._initialize_password_entry()

        login_button.grid(row=4, column=0, columnspan=3, padx=5, pady=5)
        signin_button.grid(row=5, column=0, columnspan=3, padx=5, pady=5)

        self._hide_error_label()

        self._frame.grid_columnconfigure(0, weight=1, minsize=100)

    def _check_login(self):
        """Uses function log_in() from class CookbookAppFunctions to either change the frame into BookView()
        or display an error label depending on the input the user gave.
        """

        username_data = str(self._username_entry.get())
        password_data = str(self._password_entry.get())

        if cookbookapp_functions.log_in(username_data, password_data):
            self._handle_login()
        else:
            self._show_error_label()

    def _show_error_label(self):
        """Initializes and error label.
        """

        self._error_label = ttk.Label(
            master=self._frame, text="Error: wrong username or password")

        self._error_label.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

    def _hide_error_label(self):
        """Hides an existing error label without destroying it.
        """

        if self._error_label:
            self._error_label.grid_remove()
