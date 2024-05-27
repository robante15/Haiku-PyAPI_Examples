# API Docs: https://www.haiku-os.org/docs/api/classBRadioButton.html
from Be import *


class Window(BWindow):
    def __init__(self):
        # Create a window
        BWindow.__init__(self,
                         # Set the frame of the window
                         BRect(100, 100, 350, 250),
                         "BRadioButton Example",  # Set the title of the window
                         B_TITLED_WINDOW_LOOK,  # Set the look of the window
                         B_NORMAL_WINDOW_FEEL,  # Set the feel of the window
                         B_QUIT_ON_WINDOW_CLOSE)  # Set the flags of the window

        # Create a panel to hold the radio buttons
        self.panel = BView(self.Bounds(), "panel", 8, 20000000)

        # Create the first radio button (BRadioButton)
        self.rbtn_test1 = BRadioButton(
            BRect(10, 70, 290, 90),  # Set the frame of the radio button
            'rbtn_test1',  # Set the name of the radio button
            'Option 1',  # Set the label of the radio button
            # Set the message to be sent when the radio button is clicked
            BMessage(123))

        # Create the second radio button (BRadioButton)
        self.rbtn_test2 = BRadioButton(
            BRect(10, 90, 290, 90),  # Set the frame of the radio button
            'rbtn_test2',  # Set the name of the radio button
            'Option 2',  # Set the label of the radio button
            # Set the message to be sent when the radio button is clicked
            BMessage(321))

        # Add the first radio button to the panel
        self.panel.AddChild(self.rbtn_test1, None)
        # Add the second radio button to the panel
        self.panel.AddChild(self.rbtn_test2, None)

        self.AddChild(self.panel, None)  # Add the panel to the window

        # Handle the message sent by the radio buttons
    def MessageReceived(self, msg):
        if msg.what == 123:  # Check if the message is the one sent by the first radio button
            print("Option 1 Checked")
        elif msg.what == 321:  # Check if the message is the one sent by the second radio button
            print("Option 2 Checked")


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
