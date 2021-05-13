from tkinter import Tk, ttk, constants
from functions.cookbookapp_functions import cookbookapp_functions


class BookView:
    """Class that initializes cookbook -window of ui.
    """

    def __init__(self, root, handle_logout, handle_new_recipe, handle_recipe):
        """Constructor of class that keeps track of frame and necessary functions to change window.
        Cookbook -window is initialized in class constructor.

        Args:
            root (Tk): The root in class Tk() that is required to initialize a window.
            handle_logout (function): Function _show_login() of class UI.
            handle_new_recipe (function): Function _show_new_recipe() of class UI.
            handle_recipe (function): Function _show_recipe() of class UI.
        """

        self._root = root
        self._frame = None
        self._handle_logout = handle_logout
        self._handle_new_recipe = handle_new_recipe
        self._handle_recipe = handle_recipe
        self._search_entry = None
        self._buttons = []
        cookbookapp_functions.no_chosen_recipe()

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _handler_logout(self):
        """Switches window to Log in -window after logging out.
        """

        cookbookapp_functions.log_out()
        self._handle_logout()

    def _initialize_book_name_label(self):
        """Constructs the name of the cookbook according to who is logged in.
        """

        user = cookbookapp_functions.current_user()[1]

        book_name_label = ttk.Label(
            master=self._frame, text=f"{user}'s cookbook")

        book_name_label.grid(row=0, column=0, columnspan=2, sticky=(
            constants.E, constants.W), padx=5, pady=15)

    def _initialize_search_entry(self):
        self._search_entry = ttk.Entry(master=self._frame)

        search_button = ttk.Button(
            master=self._frame,
            text="Search",
            command=self._handler_search
        )

        self._search_entry.grid(row=2, column=0, columnspan=2, sticky=(
            constants.E, constants.W), padx=5, pady=15)
        search_button.grid(row=2, column=2, sticky=(
            constants.E, constants.W), padx=5, pady=15)

    def _handler_recipe(self, recipe_name):
        """Switches window to recipe window according to the chosen recipe.

        Args:
            recipe_name (string): The name of the recipe.
        """

        cookbookapp_functions.set_chosen_recipe(recipe_name)
        self._handle_recipe()

    def _handler_search(self):
        self._destroy_recipe_buttons()

        keyword = str(self._search_entry.get())

        self._initialize_recipe_buttons(keyword)

    def _initialize_recipe_buttons(self, keyword=None):
        """Constructs buttons that display a recipe's name. 
        The buttons have the function to set the variable _chosen_recipe in class CookbookAppFunctions,
        and change the view into RecipeView().
        """

        recipes = cookbookapp_functions.users_recipes(keyword)

        if recipes is not None:

            for i in range(len(recipes)):
                recipe = recipes[i]

                recipe_button = ttk.Button(
                    master=self._frame,
                    text=recipe[2],
                    command=lambda recipe_name=recipe[2]: self._handler_recipe(
                        recipe_name)
                )
                recipe_button.grid(row=3+i, column=0, columnspan=4,
                                   sticky=(constants.E, constants.W), padx=5, pady=5)
                
                self._buttons.append(recipe_button)

    def _destroy_recipe_buttons(self):
        for button in self._buttons:
            button.destroy()
        
        self._buttons = []

    def _initialize(self):
        """Initializes the cookbook -window with necessary elements.
        """

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

        self._initialize_search_entry()

        self._initialize_recipe_buttons()

        self._frame.grid_columnconfigure(0, weight=1, minsize=100)

        self._frame.pack()
