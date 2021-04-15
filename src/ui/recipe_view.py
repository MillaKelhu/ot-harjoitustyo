from tkinter import Tk, ttk, constants
from functions.cookbookapp_functions import cookbookapp_functions

class RecipeView:
    def __init__(self, root, handle_return):
        self._root = root
        self._frame = None
        self._handle_return = handle_return
        self._recipe = cookbookapp_functions.get_chosen_recipe()

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize_recipe(self):
        name_label = ttk.Label(master=self._frame, text=self._recipe[2])
        instructions_label = ttk.Label(master=self._frame, text=self._recipe[3])

        name_label.grid(row=0, column=0, columnspan=2, sticky=(constants.E, constants.W), padx=5, pady=15)
        instructions_label.grid(row=1, column=0, columnspan=2, sticky=(constants.E, constants.W), padx=5, pady=15)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        return_button = ttk.Button(
            master=self._frame, 
            text="Return",
            command=self._handle_return
        )

        self._initialize_recipe()

        return_button.grid(row=2, column=0, columnspan=2, sticky=(constants.E, constants.W), padx=5, pady=5)