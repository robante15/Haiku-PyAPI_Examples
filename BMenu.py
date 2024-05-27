# API Docs: https://www.haiku-os.org/docs/api/classBMenu.html
# https://www.haiku-os.org/docs/api/classBMenuBar.html
from Be import *


class Window(BWindow):
    def __init__(self):
        # Create a blank window
        BWindow.__init__(self,
                         # Set the frame of the window (left, top, right, bottom)
                         BRect(100, 100, 400, 250),
                         "BMenu Test",  # Set the title of the window
                         window_type.B_TITLED_WINDOW,  # Set the type of the window
                         B_QUIT_ON_WINDOW_CLOSE)  # Set the flags of the window

        # Create a BMenuBar object that will hold the menu
        menuBarRect = self.Bounds()  # Get the bounds of the window
        menuBarRect.bottom = 20.0  # Set the bottom of the menu bar

        self.menuBar = BMenuBar(menuBarRect, "menuBar")  # Create the menu bar

        # Create a BMenu object that will hold the menu items
        self.menuFile = BMenu("File")
        self.menuHelp = BMenu("Help")

        # Add items to the menu
        self.menuBar.AddItem(self.menuFile)
        self.menuBar.AddItem(self.menuHelp)

        # Create BMenuItems to add to the menu
        self.menuItemOpen = BMenuItem("Open", BMessage(123), 'O')
        self.menuItemClose = BMenuItem("Close", BMessage(321), 'W')

        # Add the menu items to the menu
        self.menuFile.AddItem(self.menuItemOpen)
        self.menuFile.AddItem(self.menuItemClose)

        self.AddChild(self.menuBar, None)  # Add the menu bar to the window

    # Handle the message sent by the button
    def MessageReceived(self, msg):
        if msg.what == 123:
            print("Open")
        elif msg.what == 321:
            self.Quit()  # Close the program


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
