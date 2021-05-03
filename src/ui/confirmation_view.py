from tkinter import Tk, ttk, Toplevel
from functions.cookbookapp_functions import cookbookapp_functions


class ConfirmationWindow:
    """Class that initializes a toplevel window to confirm deletion of a recipe.
    """

    def __init__(self, handle_return):
        """Constructor of class that keeps track of frame and necessary function to return to book window.

        Args:
            handle_return (function): Function _show_book() of class UI.
        """

        self._frame = Toplevel()
        self._frame.title("")
        self._handle_return = handle_return

        self._initialize()

    def show(self):
        self._frame.deiconify()

    def destroy(self):
        self._frame.destroy()

    def _hide_confirmation_window(self):
        """Hides the confirmation window without deleting it.
        """

        self._frame.withdraw()

    def _handle_delete(self):
        """Switches window to BookView() after deletion of recipe.
        """

        cookbookapp_functions.delete_chosen_recipe()
        self._handle_return()

    def _initilize_message(self):
        """Constructs a label for confirmation window.
        """

        message_label = ttk.Label(
            self._frame, text="Are you sure you want to delete this recipe?")

        message_label.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

    def _initialize(self):
        """Initializes the window with necessary elements.
        """

        cancel_button = ttk.Button(
            master=self._frame,
            text="Cancel",
            command=self._hide_confirmation_window
        )

        delete_button = ttk.Button(
            master=self._frame,
            text="Delete",
            command=self._handle_delete
        )

        self._initilize_message()

        cancel_button.grid(row=1, column=0, padx=5, pady=5)
        delete_button.grid(row=1, column=1, padx=5, pady=5)
