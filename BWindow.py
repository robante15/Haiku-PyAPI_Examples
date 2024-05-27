# API Docs: https://www.haiku-os.org/docs/api/classBWindow.html
from Be import *


class Window(BWindow):
    def __init__(self):
        # Create a blank window
        BWindow.__init__(self,
                         # Set the frame of the window (left, top, right, bottom)
                         BRect(100, 100, 400, 250),
                         "Clean Window",  # Set the title of the window
                         window_type.B_TITLED_WINDOW,  # Set the type of the window
                         B_QUIT_ON_WINDOW_CLOSE)  # Set the flags of the window


# Create a class that inherits from BApplication
class App(BApplication):
    def __init__(self):
        BApplication.__init__(self, "application/x-python")

    def ReadyToRun(self):
        self.window = Window()
        self.window.Show()


def main():
    global be_app
    be_app = App()
    be_app.Run()
    print('Ran')


if __name__ == "__main__":
    main()
