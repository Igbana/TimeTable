#TimeTable app
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivy.properties import NumericProperty, BooleanProperty
from kivy.lang import Builder


class Field(FloatLayout):
	def add_widget(self, widget, *args, **kwargs):
		widget.pos_hint = {'x':0, 'y':0}
		super().add_widget(widget)
		
class TableLabel(MDLabel):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.halign = 'center'
		self.bold = True

class Bar(MDCard):
	allowance = NumericProperty(40)
	at = NumericProperty()
	resizing = BooleanProperty(False)
	moving = BooleanProperty(False)
	def __init__(self, **kwargs):
		super().__init__(self, **kwargs)
		self.md_bg_color = [0,0,1,1]
		self.size_hint_x = None
		self.width = "200dp"
	def on_touch_down(self, touch):
		#for stretching
		if touch.pos[0] - self.right <= self.allowance and self.right - touch.pos[0] <= self.allowance and self.collide_point(touch.pos[0], touch.pos[1]):
			self.md_bg_color = [0,0,0.9,1]
			self.resizing = True
		elif self.collide_point(touch.pos[0], touch.pos[1]):
			self.moving = True
	def on_touch_move(self, touch):
		if self.resizing:
			if touch.pos[0] > self.x:
				self.width = touch.pos[0] - self.x
		elif self.moving:
			self.pos[0] = touch.pos[0] - self.width/2
			self.pos[1] = touch.pos[1] - self.height/2
	def on_touch_up(self, touch):
		self.md_bg_color = [0,0,1,1]
		self.resizing = False
		self.moving = False
	

class TableScreen(MDScreen):
	tmeVal = NumericProperty()
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.tmeLst = [f"{12 if i%12==0 else i%12}:00{'am' if i//12 == 0 else 'pm'}" for i in range(4, 23)]
		self.days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
		self.tmeVal = len(self.tmeLst)
		for i in range((len(self.days)+1)*(self.tmeVal+1)):
			if i in range(1,self.tmeVal+1):
				self.ids.grid.add_widget(TableLabel(text=self.tmeLst[i-1]))
			elif (i%(self.tmeVal+1) == 0) and i != 0:
				self.ids.grid.add_widget(TableLabel(text = self.days[(i//20)-1]))
			else:
				self.ids.grid.add_widget(Field())
	
class MainApp(MDApp):
	def build(self):
		return TableScreen()
		
MainApp().run()