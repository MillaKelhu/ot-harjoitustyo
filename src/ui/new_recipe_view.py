from tkinter import Tk, ttk, constants, Text, Scrollbar

class NewRecipeView:
    def __init__(self, root, handle_new_recipe):
        self._root = root
        self._frame = None
        self._handle_new_recipe = handle_new_recipe
        self._name_entry = None
        self._instructions_text = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize_name_field(self):
        name_label = ttk.Label(master=self._frame, text="Name:")
        self._name_entry = ttk.Entry(master=self._frame)

        name_label.grid(row=1, column=0, sticky=(constants.E, constants.W), padx=5, pady=15)
        self._name_entry.grid(row=1, column=1, sticky=(constants.E, constants.W), padx=5, pady=15)

    def _initialize_instructions_field(self):
        instructions_label = ttk.Label(master=self._frame, text="Ingredients:")
        self._instructions_text = Text(master=self._frame)

        instructions_label.grid(row=2, column=0, sticky=(constants.E, constants.W), padx=5, pady=5)
        self._instructions_text.grid(row=3, rowspan=10, column=0, columnspan=2, sticky=(constants.E, constants.W), padx=5, pady=5)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        create_new_recipe_button = ttk.Button(
            master=self._frame, 
            text="Create new recipe",
            command=self._check_entries
        )

        self._initialize_name_field()

        self._initialize_instructions_field()

        create_new_recipe_button.grid(row=14, column=0, columnspan=2, padx=5, pady=5)

        self._frame.grid_columnconfigure(0, weight=1, minsize=100)

    def _check_entries(self):
        name_data = self._name_entry.get()
        instructions_data = self._instructions_text.get(1.0, "end")

        if len(name_data) > 0 and len(instructions_data) > 0:
            self._handle_new_recipe()
        else:
            pass
