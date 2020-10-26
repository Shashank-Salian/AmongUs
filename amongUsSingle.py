import turtle

class AmongUs:
	def __init__(self):
		self.color = "red"	# Color of the character
		t.pensize(5)
	
	def set_pos(self):
		t.up()
		t.setpos(-112, -80)
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
		# Move the pen to it's position
		t.up()
		t.setpos(-80, 110)
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
		t.up()
		t.setpos(-173, -80)
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
	
	
	

if __name__ == "__main__":
	t = turtle.Turtle()
	au = AmongUs()
	au.make()
	turtle.done()
