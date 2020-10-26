import turtle

class AmongUs:
	def __init__(self, color, count):
		self.color = color
		self.c = count
	
	def set_pos(self):
		if self.c == 1:
			t.up()
			t.goto(-300, -80)
			t.down()
		else:
			t.up()
			t.goto(150, -80)
			t.down()

	def draw_body(self):
		self.set_pos()

		t.fillcolor(self.color)
		t.begin_fill()
		
		# Left Leg
		t.right(90)
		t.forward(40)
		t.left(180)
		t.circle(30, -180)
		t.right(180)
		
		# Left part
		t.forward(200)
		t.left(180)

		# Head
		t.circle(85, -145)

		# Stomach
		t.right(15)
		t.circle(500, -29)

		# Right leg
		t.circle(30, -180)
		t.right(170)
		t.forward(35)

		# hip
		t.right(90)
		t.forward(10)
		t.backward(70)

		# Fill color
		t.end_fill()
	
	def goggles(self):
		# Move the oen to it's position
		if self.c == 1:
			t.up()
			t.setpos(-280, 110)
			t.down()
		else:
			t.up()
			t.setpos(170, 110)
			t.down()

		# Set color
		t.fillcolor("#f2f6f3")
		t.begin_fill()

		# Draw Goggles
		t.forward(85)
		t.left(180)
		t.circle(37, -180)
		t.left(-180)
		t.forward(80)
		t.left(180)
		t.circle(38, -160)
		t.left(-180)
		t.forward(4)

		# Fill color
		t.end_fill()
	
	def bag(self):
		# Set pos
		if self.c == 1:
			t.up()
			t.setpos(-362, -80)
			t.down()
		else:
			t.up()
			t.setpos(88,-80)
			t.down()

		# Set color
		t.fillcolor(self.color)
		t.begin_fill()

		# Draw bag
		t.left(150)
		t.forward(15)
		t.left(180)
		t.circle(30, -60)
		t.right(200)
		t.forward(100)
		t.left(180)
		t.circle(30, -60)
		t.left(-210)
		t.forward(25)

		# Fill color
		t.end_fill()
	
	def make(self):
		self.draw_body()
		self.goggles()
		self.bag()
	
# Class to Draw the message
class DrawMessage():
	def __init__(self, count):
		self.c = count
		self.font_size = 10
		self.f_text = "One among three is a Impostor.\nI am not the Impostor."
		self.s_text = "Nor am I"
		t.pensize(2)
	
	def goto_pos(self, x, y):
		t.up()
		t.setpos(x, y)
		t.down()
	
	def draw_cloud(self):
		if self.c == 1:
			# First circle
			self.goto_pos(-220, 180)
			t.circle(5, 360)
			# Second circle
			self.goto_pos(-200, 200)
			t.circle(10, 360)
			# Third circle
			self.goto_pos(-200, 240)
			t.forward(200)
			t.circle(35, 180)
			t.forward(200)
			t.circle(35, 180)
		else:
			# First circle
			self.goto_pos(230, 180)
			t.circle(5, 360)
			# Second circle
			self.goto_pos(250, 200)
			t.circle(10, 360)
			# Third circle
			self.goto_pos(250, 240)
			t.forward(100)
			t.circle(35, 180)
			t.forward(100)
			t.circle(35, 180)
	
	def write_text(self):
		if self.c == 1:
			self.goto_pos(t.pos()[0] - 20, t.pos()[1] + 15)
			t.write(self.f_text, font=("verdana", self.font_size, "bold"))
		else:
			self.goto_pos(t.pos()[0], t.pos()[1] + 20)
			t.write(self.s_text, font=("verdana", self.font_size + 1, "bold"))
	
	def bottom_text(self):
		self.goto_pos(-280, -300)
		t.write("You act sus. You are the Impostor...", font=("helvetica", 20, "bold"))
	
	def make(self):
		self.draw_cloud()
		self.write_text()
		if self.c == 2:
			self.bottom_text()
	


# Dont worry much about the code below this. Looks a bit messy because i have made it easy and customizable to user

if __name__ == "__main__":
	col1 = "red"
	col2 = "blue"
	t = turtle.Turtle()
	wn = turtle.Screen()
	wn.title("Among Us meme")
	t.pensize(5)
	
	au1 = AmongUs(col1, 1)
	au2 = AmongUs(col2, 2)
	au1.make()
	au2.make()

	dm1 = DrawMessage(1)
	dm2 = DrawMessage(2)
	dm1.make()
	dm2.make()

	turtle.done()
