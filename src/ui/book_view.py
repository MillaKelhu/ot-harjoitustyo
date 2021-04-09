from tkinter import Tk, ttk, constants

class BookView:
    def __init__(self, root, handle_logout, handle_new_recipe):
        self._root = root
        self._frame = None
        self._handle_logout = handle_logout
        self._handle_new_recipe = handle_new_recipe

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        new_recipe_button = ttk.Button(
            master=self._frame, 
            text="New recipe",
            command=self._handle_new_recipe
        )

        logout_button = ttk.Button(
            master=self._frame,
            text="Log out",
            command=self._handle_logout
        )

        new_recipe_button.grid(row=1, column=0, columnspan=2, padx=5, pady=5)
        logout_button.grid(row=1, column=2, columnspan=2, padx=5, pady=5)

        self._frame.grid_columnconfigure(0, weight=1, minsize=100)

        self._frame.pack()