from tkinter import Tk, ttk, constants, Text, Scrollbar
from functions.cookbookapp_functions import cookbookapp_functions


class ModifyRecipeView:
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

    def _initialize_recipe_name(self):
        name_label = ttk.Label(master=self._frame, text=self._recipe[2])

        name_label.grid(row=0, column=0, columnspan=2, sticky=(
            constants.E, constants.W), padx=5, pady=15)

    def _initialize_new_instructions_field(self):
        instructions_label = ttk.Label(
            master=self._frame, text="New instructions:")
        self._new_instructions_text = Text(master=self._frame)

        self._new_instructions_text.insert(1.0, self._recipe[3])

        instructions_label.grid(row=1, column=0, sticky=(
            constants.E, constants.W), padx=5, pady=5)
        self._new_instructions_text.grid(row=2, rowspan=10, column=0, columnspan=2, sticky=(
            constants.E, constants.W), padx=5, pady=5)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        save_modified_button = ttk.Button(
            master=self._frame,
            text="Save modified recipe",
            command=self._save_new_instructions
        )

        return_without_saving_button = ttk.Button(
            master=self._frame,
            text="Return without saving",
            command=self._handle_return
        )

        self._initialize_recipe_name()

        self._initialize_new_instructions_field()

        save_modified_button.grid(
            row=13, column=0, columnspan=2, sticky=(constants.W), padx=5, pady=5)

        return_without_saving_button.grid(
            row=13, column=1, columnspan=2, sticky=(constants.E), padx=5, pady=5)

    def _save_new_instructions(self):
        new_instructions_data = self._new_instructions_text.get(1.0, "end")

        if len(new_instructions_data) > 0:
            cookbookapp_functions.modify_chosen_recipe(new_instructions_data)
            self._handle_return()
        else:
            pass
