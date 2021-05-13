from tkinter import Tk, ttk, constants, Text, Scrollbar
from functions.cookbookapp_functions import cookbookapp_functions


class NewRecipeView:
    """Class that initializes a window to add a new recipe.
    """

    def __init__(self, root, handle_return):
        """Constructor of class that keeps track of the frame, necessary function to return to the cookbook -window, 
        and values of entries for recipe name and instructions.
        The window is initialized in class constructor.

        Args:
            root (Tk): The root in class Tk() that is required to initialize a window.
            handle_return (function): Function _show_book() of class UI.
        """

        self._root = root
        self._frame = None
        self._handle_return = handle_return
        self._name_entry = None
        self._instructions_text = None
        self._error_label = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize_name_field(self):
        """Constructs a label and entry where the user is required to input recipe name.
        """

        name_label = ttk.Label(master=self._frame, text="Name:")
        self._name_entry = ttk.Entry(master=self._frame)

        name_label.grid(row=1, column=0, sticky=(constants.W), padx=5, pady=15)
        self._name_entry.grid(row=1, column=1, padx=5, pady=15)

    def _initialize_instructions_field(self):
        """Constructs a label and entry where the user is required to input instructions for the recipe.
        """

        instructions_label = ttk.Label(
            master=self._frame, text="Instructions:")
        self._instructions_text = Text(master=self._frame)

        instructions_label.grid(row=2, column=0, sticky=(
            constants.E, constants.W), padx=5, pady=5)
        self._instructions_text.grid(row=3, rowspan=10, column=0, columnspan=2, sticky=(
            constants.E, constants.W), padx=5, pady=5)

    def _initialize(self):
        """Initializes the window with necessary elements.
        """

        self._frame = ttk.Frame(master=self._root)

        create_new_recipe_button = ttk.Button(
            master=self._frame,
            text="Create new recipe",
            command=self._check_entries
        )

        return_without_saving_button = ttk.Button(
            master=self._frame,
            text="Return without saving",
            command=self._handle_return
        )

        self._initialize_name_field()

        self._initialize_instructions_field()

        create_new_recipe_button.grid(
            row=15, column=0, columnspan=2, sticky=(constants.W), padx=5, pady=5)

        return_without_saving_button.grid(
            row=15, column=1, columnspan=2, sticky=(constants.E), padx=5, pady=5)

        self._frame.grid_columnconfigure(0, weight=1, minsize=100)

    def _check_entries(self):
        """Checks the length of input and and uses function add_recipes() from class CookbookAppFunctions to either change the window to BookView()
        or display an error label.
        """

        name_data = self._name_entry.get()
        instructions_data = self._instructions_text.get(1.0, "end")

        if 0 < len(name_data) < 100:
            if 0 < len(instructions_data) < 5001:
                cookbookapp_functions.add_recipes(name_data, instructions_data)
                self._handle_return()
            else:
                self._show_error_label("Error: instructions must be 1-5000 characters long")
        else:
            self._show_error_label("Error: name must be 1-99 characters long")

    def _show_error_label(self, message):
        """Initializes an error label. As there can be several error labels, the function first hides any error labels that already exist.

        Args:
            message (string): A message of the error label.
        """

        self._hide_error_label()

        self._error_label = ttk.Label(master=self._frame, text=message)

        self._error_label.grid(row=14, column=0, columnspan=2, padx=5, pady=5)

    def _hide_error_label(self):
        """Hides an existing error label without destroying it.
        """

        if self._error_label:
            self._error_label.grid_remove()
