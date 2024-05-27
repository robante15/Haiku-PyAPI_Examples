# API Docs: https://www.haiku-os.org/docs/api/classBTextControl.html

from Be import *


class Window(BWindow):
    def __init__(self):
        # Create a window
        BWindow.__init__(self,
                         # Set the frame of the window
                         BRect(100, 100, 350, 250),
                         "BTextControl Example",  # Set the title of the window
                         B_TITLED_WINDOW_LOOK,  # Set the look of the window
                         B_NORMAL_WINDOW_FEEL,  # Set the feel of the window
                         B_QUIT_ON_WINDOW_CLOSE)  # Set the flags of the window

        # Create a panel to hold the text control
        self.panel = BView(self.Bounds(), "panel", 8, 20000000)

        # Create a text control (BTextControl)
        self.txt_test = BTextControl(
            BRect(40, 30, 200, 50),  # Set the frame of the text control
            "txt_test",  # Set the name of the text control
            "Text input",  # Set the label of the text control
            "",  # Set the initial text of the text control
            None)  # Set the message to be sent when the text control is changed

        # Add the text control to the panel
        self.panel.AddChild(self.txt_test, None)

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

        # Handle the message sent by the text control
    def MessageReceived(self, msg):
        if msg.what == 123:
            # Print the text input to the console
            print("Input text:" + self.txt_test.Text())


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
