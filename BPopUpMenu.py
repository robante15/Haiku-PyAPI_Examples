# API Docs: https://www.haiku-os.org/docs/api/classBPopUpMenu.html
# https://www.haiku-os.org/docs/api/classBMenuField.html

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

        # First, create a BPopUpMenu object
        self.bpmenu = BPopUpMenu("Select an option")

        # Create a BMenuField object that will display the menu (One reason the menu field label exists is to provide the user with information regarding the purpose of the menu field’s pop-up menu.)
        self.bmfield_test = BMenuField(
            BRect(30.0, 25.0, 250.0, 50.0),  # Set the frame of the menu field
            "bmfield_test",  # Set the name of the menu field
            "Pick a color",  # Set the label of the menu field
            self.bpmenu)  # Set the menu to be displayed in the menu field

        # Add items to the menu
        self.bpmenu.AddItem(BMenuItem("Option A", BMessage(123), 'A'))
        self.bpmenu.AddItem(BMenuItem("Option B", BMessage(321), 'B'))
        self.bpmenu.AddItem(BMenuItem("Option C", BMessage(231), 'C'))

        # Set the divider of the menu field (The divider is the line that separates the label from the menu field’s pop-up menu.)
        labelWidth = self.bmfield_test.StringWidth(
            self.bmfield_test.Label())  # Get the width of the label
        LABEL_MARGIN = 5.0  # Set the margin between the label and the divider
        self.bmfield_test.SetDivider(
            labelWidth + LABEL_MARGIN)  # Set the divider

        # Add the menu field to the panel
        self.panel.AddChild(self.bmfield_test, None)

        self.AddChild(self.panel, None)  # Add the panel to the window

    # Handle the message sent by the button
    def MessageReceived(self, msg):
        if msg.what == 123:  # Check if the message is the one sent by the first BMenuItem
            print("Option A Checked")
        elif msg.what == 321:  # Check if the message is the one sent by the second BMenuItem
            print("Option B Checked")
        elif msg.what == 231:  # Check if the message is the one sent by the third BMenuItem
            print("Option C Checked")


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
