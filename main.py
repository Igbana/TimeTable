#TimeTable app
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.card import MDCard
from kivy.properties import NumericProperty, BooleanProperty
from kivy.lang import Builder

class Field(FloatLayout):
	def add_widget(self, widget, *args, **kwargs):
		widget.pos_hint = {'x':0, 'y':0}
		super().add_widget(widget)

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
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		for i in range(10):
			self.ids.grid.add_widget(Field())
	
class MainApp(MDApp):
	def build(self):
		return TableScreen()
		
MainApp().run()