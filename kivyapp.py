
import kivy
from kivy.app import App
from kivy.uix.label import Label

kivy.require('2.1.0')
# Defining a class
class homeworktracker(App):

    # Function that returns
    # the root widget
    def build(self):

        # Label with text Hello World is
        # returned as root widget
        return Label(text ="Hello World !")


# Here our class is initialized
# and its run() method is called.
# This initializes and starts
# our Kivy application.
homeworktracker().run()
