# API Docs: https://www.haiku-os.org/docs/api/classBStringView.html

from Be import *

FRAME_LEFT = 10.0


class Window(BWindow):
    def __init__(self):
        # Create a window
        BWindow.__init__(self,
                         # Set the frame of the window (left, top, right, bottom)
                         BRect(100, 100, 450, 250),
                         "BStringView Centered Example",  # Set the title of the window
                         B_TITLED_WINDOW_LOOK,  # Set the look of the window
                         B_NORMAL_WINDOW_FEEL,  # Set the feel of the window
                         # Set the flags of the window (not resizable and quit on close)
                         B_QUIT_ON_WINDOW_CLOSE)

        # Create a panel to hold the label
        self.panel = BView(self.Bounds(), "panel", 8, 20000000)

        # Create a label (BStringView)
        text = "Example Label"

        text_width = BFont().StringWidth(text)  # Get the width of the text
        window_width = self.Frame().Width()  # Get the width of the window
        # Calculate the x position of the label
        left = (window_width - text_width) / 2
        right = left + text_width  # Calculate the right side of the label

        self.lbl_test = BStringView(BRect(left, 10, right, 30),  # Set the frame of the label
                                    "lbl_test",  # Set the name of the label
                                    text)  # Set the text of the label

        self.panel.AddChild(self.lbl_test, None)  # Add the label to the panel
        self.AddChild(self.panel, None)  # Add the panel to the window


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
