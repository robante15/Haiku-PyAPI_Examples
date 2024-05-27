#API Docs: https://www.haiku-os.org/docs/api/classBCheckBox.html

from Be import *

class Window(BWindow):
	def __init__(self):
		BWindow.__init__(self, BRect(100, 100, 350, 250), "BCheckBox Example", B_TITLED_WINDOW_LOOK, B_NORMAL_WINDOW_FEEL, B_QUIT_ON_WINDOW_CLOSE)
		
		self.panel = BView(self.Bounds(), "panel", 8, 20000000)
		
		self.chkbox_test = BCheckBox(BRect(10,70,290,90),'chkbox_test','Enable check?',BMessage(123))
		self.panel.AddChild(self.chkbox_test, None)
		
		self.AddChild(self.panel, None)

	def MessageReceived(self, msg):
		if msg.what == 123:
			if self.chkbox_test.Value() == False:
				print("Box unchecked")
			elif self.chkbox_test.Value() == True:
				print("Box is checked")
		
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
