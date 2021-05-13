from tkinter import Tk, ttk, constants
from functions.cookbookapp_functions import cookbookapp_functions


class SigninView:
    """Class that initializes sign in -window of ui.
    """

    def __init__(self, root, handle_return):
        """Constructor of class that keeps track of the frame, new username- and password entries, error labels, and necessary function to change the window.
        Sign in -window is intialized in class constructor.

        Args:
            root (Tk): The root in class Tk() that is required to initialize a window.
            handle_return (function): Function _show_login() of class UI.
        """

        self._root = root
        self._frame = None
        self._handle_return = handle_return
        self._new_username_entry = None
        self._password_entry = None
        self._error_label = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize_new_user_entry(self):
        """Constructs a label and entry where the user can input a username for a new user profile.
        """

        new_username_label = ttk.Label(
            master=self._frame, text="New username:")
        self._new_username_entry = ttk.Entry(master=self._frame)

        new_username_label.grid(row=1, column=0, sticky=(
            constants.E, constants.W), padx=5, pady=15)
        self._new_username_entry.grid(row=1, column=1, sticky=(
            constants.E, constants.W), padx=5, pady=15)

    def _initialize_password_entry(self):
        """Constructs a label and entry where the user can input a password for a new user profile.
        """

        password_label = ttk.Label(master=self._frame, text="Password:")
        self._password_entry = ttk.Entry(master=self._frame, show="*")

        password_label.grid(row=2, column=0, sticky=(
            constants.E, constants.W), padx=5, pady=15)
        self._password_entry.grid(row=2, column=1, sticky=(
            constants.E, constants.W), padx=5, pady=15)

    def _initialize(self):
        """Initializes the sign in -window with the necessary elements.
        """

        self._frame = ttk.Frame(master=self._root)

        self._new_user_button = ttk.Button(
            master=self._frame,
            text="Create new user",
            command=self._check_new_username
        )

        self._cancel_button = ttk.Button(
            master=self._frame,
            text="Cancel",
            command=self._handle_return
        )

        self._initialize_new_user_entry()
        self._initialize_password_entry()

        self._new_user_button.grid(
            row=4, column=0, columnspan=2, padx=5, pady=5)
        self._cancel_button.grid(
            row=5, column=0, columnspan=2, padx=5, pady=5)

        self._hide_error_label()

        self._frame.grid_columnconfigure(0, weight=1, minsize=100)

    def _check_new_username(self):
        """Checks length of input and uses function sign_in() from class CookbookAppFunctions to either change the frame into LoginView()
        or display an error label.
        """

        new_username_data = self._new_username_entry.get()
        password_data = str(self._password_entry.get())

        if 0 < len(new_username_data) < 100:
            if 0 < len(password_data) < 100:
                if cookbookapp_functions.sign_in(new_username_data, password_data):
                    self._handle_return()
                else:
                    self._show_error_label("Error: username is taken")
            else:
                self._show_error_label("Error: password must be 1-99 characters long")
        else:
            self._show_error_label("Error: username must be 1-99 characters long")

    def _show_error_label(self, message):
        """Initializes an error label. As there can be several error labels, the function first hides any error labels that already exist.

        Args:
            message (string): A message of the error label.
        """

        self._hide_error_label()

        self._error_label = ttk.Label(master=self._frame, text=message)

        self._error_label.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

    def _hide_error_label(self):
        """Hides an existing error label without destroying it.
        """

        if self._error_label:
            self._error_label.grid_remove()
