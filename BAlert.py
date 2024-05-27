#API Docs: https://www.haiku-os.org/docs/api/classBAlert.html

from Be import *

class Window(BWindow):
	def __init__(self):
		BWindow.__init__(self, BRect(100, 100, 350, 250), "BAlert Example", B_TITLED_WINDOW_LOOK, B_NORMAL_WINDOW_FEEL, B_QUIT_ON_WINDOW_CLOSE)
		self.panel = BView(self.Bounds(), "panel", 8, 20000000)

		self.btn_test1 = BButton(BRect(90, 60, 200, 50), "btn_test", "Test button!", BMessage(123))
		self.panel.AddChild(self.btn_test1, None)

		self.AddChild(self.panel, None)
	
	def MessageReceived(self, msg):
		if msg.what == 123:
			ask = BAlert('BAlert Test', 'Message with information', 'Button1','Button2', 'Button3', B_WIDTH_AS_USUAL, B_OFFSET_SPACING,B_INFO_ALERT)
			ask.Go()

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
