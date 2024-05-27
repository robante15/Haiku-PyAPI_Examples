#API Docs: https://www.haiku-os.org/docs/api/classBButton.html
from Be import *

class Window(BWindow):
	def __init__(self):
		BWindow.__init__(self, BRect(100, 100, 350, 250), "BButton Example", B_TITLED_WINDOW_LOOK, B_NORMAL_WINDOW_FEEL, B_QUIT_ON_WINDOW_CLOSE)
		self.panel = BView(self.Bounds(), "panel", 8, 20000000)
		
		self.lbl_test1 = BStringView(BRect(40, 30, 200, 50), "lbl_test", "Hola mundo!")
		self.panel.AddChild(self.lbl_test1, None)

		self.btn_test1 = BButton(BRect(90, 60, 200, 50), "btn_test", "Test button!", BMessage(123))
		self.panel.AddChild(self.btn_test1, None)

		self.AddChild(self.panel, None)
	
	def MessageReceived(self, msg):
		if msg.what == 123:
			self.btn_test1.SetLabel("Button has clicked")
			self.lbl_test1.SetText("Button has clicked")
			print("Hola mundo!")

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
