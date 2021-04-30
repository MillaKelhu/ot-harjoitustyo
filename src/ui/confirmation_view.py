from tkinter import Tk, ttk, Toplevel
from functions.cookbookapp_functions import cookbookapp_functions

class ConfirmationWindow:
    def __init__(self, handle_return):
        self._frame = Toplevel()
        self._frame.title("")
        self._handle_return = handle_return

        self._initialize()

    def show(self):
        self._frame.deiconify()

    def destroy(self):
        self._frame.destroy()

    def _hide_confirmation_window(self):
        self._frame.withdraw()

    def _handle_delete(self):
        cookbookapp_functions.delete_chosen_recipe()
        self._handle_return()

    def _initilize_message(self):
        message_label = ttk.Label(self._frame, text="Are you sure you want to delete this recipe?")

        message_label.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

    def _initialize(self):
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