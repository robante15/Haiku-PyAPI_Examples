#API Docs: https://www.haiku-os.org/docs/api/classBStringView.html

from Be import *

class Window(BWindow):
	def __init__(self):
		BWindow.__init__(self, BRect(100, 100, 350, 250), "BStringView Example", B_TITLED_WINDOW_LOOK, B_NORMAL_WINDOW_FEEL, B_NOT_RESIZABLE | B_QUIT_ON_WINDOW_CLOSE)
		self.panel = BView(self.Bounds(), "panel", 8, 20000000)
		self.label = BStringView(BRect(40, 30, 200, 50), "label", "Match It")
		self.panel.AddChild(self.label, None)
		self.AddChild(self.panel, None)

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
