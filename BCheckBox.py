# API Docs: https://www.haiku-os.org/docs/api/classBCheckBox.html

from Be import *


class Window(BWindow):
    def __init__(self):
        # Create a window
        BWindow.__init__(self,
                         # Set the frame of the window
                         BRect(100, 100, 350, 250),
                         "BCheckBox Example",  # Set the title of the window
                         B_TITLED_WINDOW_LOOK,  # Set the look of the window
                         B_NORMAL_WINDOW_FEEL,  # Set the feel of the window
                         B_QUIT_ON_WINDOW_CLOSE)  # Set the flags of the window

        # Create a panel to hold the checkbox
        self.panel = BView(self.Bounds(), "panel", 8, 20000000)

        # Create a checkbox (BCheckBox)
        self.chkbox_test = BCheckBox(
            BRect(10, 70, 290, 90),  # Set the frame of the checkbox
            'chkbox_test',  # Set the name of the checkbox
            'Option to check',  # Set the label of the checkbox
            BMessage(123)) # Set the message to be sent when the checkbox is clicked
        # Add the checkbox to the panel
        self.panel.AddChild(self.chkbox_test, None)

        self.AddChild(self.panel, None)  # Add the panel to the window

        # Handle the message sent by the checkbox
    def MessageReceived(self, msg):
        if msg.what == 123:
            if self.chkbox_test.Value() == False:  # Check if the value of the checkbox is unchecked
                print("Box unchecked")
            elif self.chkbox_test.Value() == True:  # Check if the value of the checkbox is checked
                print("Box is checked")


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
