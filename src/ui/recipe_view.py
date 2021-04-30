from tkinter import Tk, ttk, constants, Toplevel
from functions.cookbookapp_functions import cookbookapp_functions
from ui.confirmation_view import ConfirmationWindow


class RecipeView:
    def __init__(self, root, handle_return, handle_modify, handle_delete):
        self._root = root
        self._frame = None
        self._handle_return = handle_return
        self._handle_modify = handle_modify
        self._handle_delete = handle_delete
        self._recipe = cookbookapp_functions.get_chosen_recipe()

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize_recipe(self):
        name_label = ttk.Label(master=self._frame, text=self._recipe[2])
        instructions_label = ttk.Label(
            master=self._frame, text=self._recipe[3])

        name_label.grid(row=0, column=0, columnspan=3, sticky=(
            constants.E, constants.W), padx=5, pady=15)
        instructions_label.grid(row=1, column=0, columnspan=3, sticky=(
            constants.E, constants.W), padx=5, pady=15)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        return_button = ttk.Button(
            master=self._frame,
            text="Return",
            command=self._handle_return
        )

        modify_button = ttk.Button(
            master=self._frame,
            text="Modify recipe",
            command=self._handle_modify
        )

        delete_button = ttk.Button(
            master=self._frame,
            text="Delete recipe",
            command=self._handle_delete
        )

        self._initialize_recipe()

        return_button.grid(
            row=14, column=0, columnspan=1, sticky=(constants.W), padx=5, pady=5)
        modify_button.grid(
            row=14, column=1, columnspan=1, padx=5, pady=5)
        delete_button.grid(
            row=14, column=2, columnspan=1,sticky=(constants.E), padx=5, pady=5)

    