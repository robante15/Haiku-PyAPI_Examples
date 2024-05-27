#API Docs: https://www.haiku-os.org/docs/api/classBWindow.html
from Be import *

class Window(BWindow):
    def __init__(self):
        BWindow.__init__(self, BRect(100,100,400,250), "Clean Window", window_type.B_TITLED_WINDOW ,  B_QUIT_ON_WINDOW_CLOSE)

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
