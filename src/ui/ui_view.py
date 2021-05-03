from tkinter import Tk, ttk, constants, Toplevel
from ui.login_view import LoginView
from ui.signin_view import SigninView
from ui.book_view import BookView
from ui.new_recipe_view import NewRecipeView
from ui.recipe_view import RecipeView
from ui.modify_recipe_view import ModifyRecipeView
from ui.confirmation_view import ConfirmationWindow


class UI:
    """Class that oversees all components of the ui.
    """

    def __init__(self, root):
        """COnstructor of class that keeps track of the main frame (variable _frame) and toplevel frame (variable _topframe).

        Args:
            root (Tk): The root in class Tk() that is required to initialize a window.
        """

        self._root = root
        self._frame = None
        self._topframe = None

    def start(self):
        """The function is executed to start the app. First window show to the user is the log in -window.
        """

        self._show_login()

    def _destroy_current(self):
        """Destroys current frame and sets variable _frame as None.
        """

        if self._frame:
            self._frame.destroy()

        self._frame = None

    def _destroy_current_top(self):
        """Destroys current toplevel frame and sets variable _topframe as None.
        """

        if self._topframe:
            self._topframe.destroy()

        self._topframe = None

    def _show_login(self):
        """Sets variable _frame as LoginView().
        """

        self._destroy_current()
        self._destroy_current_top()

        self._frame = LoginView(
            self._root,
            self._show_book,
            self._show_signin
        )

        self._frame.pack()

    def _show_signin(self):
        """Sets variable _frame as SigninView().
        """

        self._destroy_current()
        self._destroy_current_top()

        self._frame = SigninView(
            self._root,
            self._show_login
        )

        self._frame.pack()

    def _show_book(self):
        """Sets variable _frame as BookView.
        """

        self._destroy_current()
        self._destroy_current_top()

        self._frame = BookView(
            self._root,
            self._show_login,
            self._show_new_recipe,
            self._show_recipe
        )

        self._frame.pack()

    def _show_new_recipe(self):
        """Sets variable _frame as NewRecipeView()
        """

        self._destroy_current()
        self._destroy_current_top()

        self._frame = NewRecipeView(
            self._root,
            self._show_book
        )

        self._frame.pack()

    def _show_recipe(self):
        """Sets variable _frame as RecipeView().
        """

        self._destroy_current()
        self._destroy_current_top()

        self._frame = RecipeView(
            self._root,
            self._show_book,
            self._show_modify_recipe,
            self._show_confirmation_window
        )

        self._frame.pack()

    def _show_modify_recipe(self):
        """Sets variable _frame ad ModifyRecipeView().
        """

        self._destroy_current()
        self._destroy_current_top()

        self._frame = ModifyRecipeView(
            self._root,
            self._show_recipe
        )

        self._frame.pack()

    def _show_confirmation_window(self):
        """Sets variable _topframe as ConfirmationWindow().
        """

        self._destroy_current_top()

        self._topframe = ConfirmationWindow(
            self._show_book
        )

        self._topframe.show()
