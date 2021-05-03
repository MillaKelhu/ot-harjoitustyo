from tkinter import Tk, ttk, constants, Text, Scrollbar
from functions.cookbookapp_functions import cookbookapp_functions


class ModifyRecipeView:
    """Class that initializes a window to modify a recipe.
    """

    def __init__(self, root, handle_return):
        """Constructor of class that keeps track of the frame, necessary function to return to the recipe -window, 
        values of entries for recipe instructions and currently displayed recipe as a tuple.
        The window is initialized in class constructor.

        Args:
            root (Tk): The root in class Tk() that is required to initialize a window.
            handle_return (function): Function _show_recipe() of class UI.
        """

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
        """Constructs a label containing the name of variable _recipe.
        """

        name_label = ttk.Label(master=self._frame, text=self._recipe[2])

        name_label.grid(row=0, column=0, columnspan=2, sticky=(
            constants.E, constants.W), padx=5, pady=15)

    def _initialize_new_instructions_field(self):
        """Constructs a label and entry where the user can input new instructions. 
        The entry is not empty, but contains the old instructions so the user can decide whether to just modify or delete them completely.
        """

        instructions_label = ttk.Label(
            master=self._frame, text="New instructions:")
        self._new_instructions_text = Text(master=self._frame)

        self._new_instructions_text.insert(1.0, self._recipe[3])

        instructions_label.grid(row=1, column=0, sticky=(
            constants.E, constants.W), padx=5, pady=5)
        self._new_instructions_text.grid(row=2, rowspan=10, column=0, columnspan=2, sticky=(
            constants.E, constants.W), padx=5, pady=5)

    def _initialize(self):
        """Initializes the window with necessary elements.
        """

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
        """Checks the length of input and and uses function modify_chosen_recipe() from class CookbookAppFunctions to either change the window to RecipeView()
        or display an error label (latter not yet implemented).
        """

        new_instructions_data = self._new_instructions_text.get(1.0, "end")

        if len(new_instructions_data) > 0:
            cookbookapp_functions.modify_chosen_recipe(new_instructions_data)
            self._handle_return()
        else:
            pass
