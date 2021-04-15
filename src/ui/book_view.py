from tkinter import Tk, ttk, constants
from functions.cookbookapp_functions import cookbookapp_functions


class BookView:
    def __init__(self, root, handle_logout, handle_new_recipe, handle_recipe):
        self._root = root
        self._frame = None
        self._handle_logout = handle_logout
        self._handle_new_recipe = handle_new_recipe
        self._handle_recipe = handle_recipe
        cookbookapp_functions.no_chosen_recipe()

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _handler_logout(self):
        cookbookapp_functions.log_out()
        self._handle_logout()

    def _initialize_book_name_label(self):
        user = cookbookapp_functions.current_user()[1]

        book_name_label = ttk.Label(
            master=self._frame, text=f"{user}'s cookbook")

        book_name_label.grid(row=0, column=0, columnspan=2, sticky=(
            constants.E, constants.W), padx=5, pady=15)

    def _handler_recipe(self, recipe_name):
        cookbookapp_functions.set_chosen_recipe(recipe_name)
        self._handle_recipe()

    def _initialize_recipe_buttons(self):
        recipes = cookbookapp_functions.users_recipes()

        if recipes is not None:

            for i in range(len(recipes)):
                recipe = recipes[i]

                recipe_button = ttk.Button(
                    master=self._frame,
                    text=recipe[2],
                    command=lambda recipe_name=recipe[2]: self._handler_recipe(
                        recipe_name)
                )
                recipe_button.grid(row=2+i, column=0, columnspan=4,
                                   sticky=(constants.E, constants.W), padx=5, pady=5)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        self._initialize_book_name_label()

        new_recipe_button = ttk.Button(
            master=self._frame,
            text="New recipe",
            command=self._handle_new_recipe
        )

        logout_button = ttk.Button(
            master=self._frame,
            text="Log out",
            command=self._handler_logout
        )

        new_recipe_button.grid(row=1, column=0, columnspan=2,
                               sticky=(constants.W), padx=5, pady=5)
        logout_button.grid(row=1, column=1, columnspan=2,
                           sticky=(constants.E), padx=5, pady=5)

        self._initialize_recipe_buttons()

        self._frame.grid_columnconfigure(0, weight=1, minsize=100)

        self._frame.pack()
