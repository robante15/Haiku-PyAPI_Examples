#API Docs: https://www.haiku-os.org/docs/api/classBRadioButton.html
from Be import *

class Window(BWindow):
	def __init__(self):
		BWindow.__init__(self, BRect(100, 100, 350, 250), "BRadioButton Example", B_TITLED_WINDOW_LOOK, B_NORMAL_WINDOW_FEEL, B_QUIT_ON_WINDOW_CLOSE)
		
		self.panel = BView(self.Bounds(), "panel", 8, 20000000)
		
		self.rbtn_test1 = BRadioButton(BRect(10,70,290,90),'rbtn_test1','Option 1',BMessage(123))
		self.rbtn_test2 = BRadioButton(BRect(10,90,290,90),'rbtn_test2','Option 2',BMessage(321))
		
		self.panel.AddChild(self.rbtn_test1, None)
		self.panel.AddChild(self.rbtn_test2, None)
		
		self.AddChild(self.panel, None)

	def MessageReceived(self, msg):
		if msg.what == 123:
			print("Option 1 Checked")
		elif msg.what == 321:
			print("Option 2 Checked")
		
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
