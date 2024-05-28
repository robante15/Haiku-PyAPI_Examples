# API Docs: https://www.haiku-os.org/docs/api/classBStringView.html

from Be import *

FRAME_LEFT = 10.0


class Window(BWindow):
    def __init__(self):
        # Create a window
        BWindow.__init__(self,
                         # Set the frame of the window (left, top, right, bottom)
                         BRect(100, 100, 450, 275),
                         "Triangle Area Example",  # Set the title of the window
                         B_TITLED_WINDOW_LOOK,  # Set the look of the window
                         B_NORMAL_WINDOW_FEEL,  # Set the feel of the window
                         # Set the flags of the window (not resizable and quit on close)
                         B_QUIT_ON_WINDOW_CLOSE)

        # Create a panel to hold the label
        self.panel = BView(self.Bounds(), "panel", 8, 20000000)

        # Create a label (BStringView)
        text_title = "Area of a Triangle"

        title_width = BFont().StringWidth(text_title)  # Get the width of the text
        window_width = self.Frame().Width()  # Get the width of the window
        # Calculate the x position of the label
        title_left = (window_width - title_width) / 2
        title_right = title_left + title_width  # Calculate the right side of the label

        self.lbl_test = BStringView(BRect(title_left, 10, title_right, 30),  # Set the frame of the label
                                    "lbl_test",  # Set the name of the label
                                    text_title)  # Set the text of the label

        # Create a text control (BTextControl)
        self.txt_base = BTextControl(
            # Set the frame of the text control
            BRect(10, 40, window_width - 10, 60),
            "txt_base",  # Set the name of the text control
            "Base",  # Set the label of the text control
            "",  # Set the initial text of the text control
            None)  # Set the message to be sent when the text control is changed

        # Create a text control (BTextControl)
        self.txt_height = BTextControl(
            # Set the frame of the text control
            BRect(10, 70, window_width - 10, 90),
            "txt_height",  # Set the name of the text control
            "Height",  # Set the label of the text control
            "",  # Set the initial text of the text control
            None)  # Set the message to be sent when the text control is changed

        # Create a button (BButton)
        self.btn_calculate = BButton(
            # Set the frame of the button
            BRect(10, 100, window_width - 10, 120),
            "btn_calculate",  # Set the name of the button
            "Calculate",  # Set the label of the button
            # Set the message to be sent when the button is clicked
            BMessage(123))

        # Create a label (BStringView) to display the result
        self.lbl_result = BStringView(
            # Set the frame of the label
            BRect(10, 130, window_width - 10, 150),
            "lbl_result",  # Set the name of the label
            "")

        self.panel.AddChild(self.lbl_test, None)  # Add the label to the panel
        # Add the text control to the panel
        self.panel.AddChild(self.txt_base, None)
        # Add the text control to the panel
        self.panel.AddChild(self.txt_height, None)
        # Add the button to the panel
        self.panel.AddChild(self.btn_calculate, None)
        # Add the label to the panel
        self.panel.AddChild(self.lbl_result, None)

        self.AddChild(self.panel, None)  # Add the panel to the window

        # Handle the message sent by the button
    def MessageReceived(self, msg):
        # Check if the message is the one sent by the button
        if msg.what == 123:
            # Get the text from the text controls
            base = float(self.txt_base.Text())
            height = float(self.txt_height.Text())
            # Calculate the area of the triangle
            area = 0.5 * base * height
            # Display the area in a message box
            result = "Area: " + str(area)
            print(result)
            result_width = BFont().StringWidth(result)

            # TODO: Calculate the x position of the label for centering
            self.lbl_result.SetText(result)


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
