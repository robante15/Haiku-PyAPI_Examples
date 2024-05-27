# API Docs: https://www.haiku-os.org/docs/api/classBButton.html
from Be import *


class Window(BWindow):
    def __init__(self):
        # Create a window
        BWindow.__init__(self,
                         BRect(100, 100, 350, 250),
                         "BButton Example",
                         B_TITLED_WINDOW_LOOK,  # Set the look of the window
                         B_NORMAL_WINDOW_FEEL,  # Set the feel of the window
                         B_QUIT_ON_WINDOW_CLOSE)  # Set the flags of the window

        # Create a panel to hold the button
        self.panel = BView(self.Bounds(), "panel", 8, 20000000)

        # Create a label (BStringView)
        self.lbl_test1 = BStringView(
            BRect(40, 30, 200, 50),  # Set the frame of the label
            "lbl_test",  # Set the name of the label
            "Hello world!")  # Set the text of the label
        self.panel.AddChild(self.lbl_test1, None)  # Add the label to the panel

        # Create a button (BButton)
        self.btn_test1 = BButton(
            BRect(90, 60, 200, 50),  # Set the frame of the button
            "btn_test",  # Set the name of the button
            "Test button!",  # Set the label of the button
            # Set the message to be sent when the button is clicked
            BMessage(123))
        # Add the button to the panel
        self.panel.AddChild(self.btn_test1, None)

        self.AddChild(self.panel, None)  # Add the panel to the window

        # Handle the message sent by the button
    def MessageReceived(self, msg):
        # Check if the message is the one sent by the button
        if msg.what == 123:
            # Change the label of the button
            self.btn_test1.SetLabel("Button has clicked")
            # Change the text of the label
            self.lbl_test1.SetText("Button has clicked")
            print("Hello world!")  # Print a message to the console


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
