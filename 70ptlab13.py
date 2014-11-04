#
#         70-100pt - Making a game
#
#########################################


# 70pt - Add buttons for left, right and down that move the player circle
# 100pt - using lab 11 as an example, add in three horizontally scrolling "enemies"



from Tkinter import *
root = Tk()

drawpad = Canvas(root, width=800,height=600, background='white')
player = drawpad.create_oval(390,580,410,600, fill="red")

# enemy
enemy = drawpad.create_oval(50,50,100,100, fill="blue")
# enemys
enemys = drawpad.create_oval(200,200,250,250, fill="green")
# enemyx
enemyx =  drawpad.create_oval(400,400,450,450, fill="orange")


class MyApp:
	def __init__(self, parent):
       	    global drawpad
       	    self.myParent = parent  
       	    self.myContainer1 = Frame(parent)
       	    self.myContainer1.pack()
       	    self.button1 = Button(self.myContainer1)
       	    self.button1.configure(text="up", background= "green")
       	    self.button1.pack(side=LEFT)
       	    self.button1.bind("<Button-1>", self.up)
       	    drawpad.pack(side=BOTTOM)
       	    self.myParent = parent  
       	    self.myContainer2 = Frame(parent)
       	    self.myContainer2.pack()
       	    self.button2 = Button(self.myContainer1)
       	    self.button2.configure(text="right", background= "green")
       	    self.button2.pack(side=LEFT)
       	    self.button2.bind("<Button-1>", self.right)
       	    drawpad.pack(side=BOTTOM)
       	    self.myParent = parent  
       	    self.myContainer3 = Frame(parent)
       	    self.myContainer3.pack()
       	    self.button3 = Button(self.myContainer1)
       	    self.button3.configure(text="left", background= "green")
       	    self.button3.pack(side=LEFT)
       	    self.button3.bind("<Button-1>", self.left)
       	    self.myParent = parent  
       	    self.myContainer4 = Frame(parent)
       	    self.myContainer4.pack()
       	    self.button4 = Button(self.myContainer1)
       	    self.button4.configure(text="down", background= "green")
       	    self.button4.pack(side=LEFT)
       	    self.button4.bind("<Button-1>", self.down)
       	    self.animate()
	
	def animate(self):
	    global drawpad
	    global player
            global enemy
            global enemys
            global enemyx
            drawpad.move(enemyx, 1, 0)
            drawpad.move(enemys, 1, 0)
            drawpad.move(enemy, 1, 0)
            
            
            drawpad.after(10,self.animate) 

	    
	def left(self, event):   
	   global oval
	   global player
	   drawpad.move(player,-20,0)
	    	
	def right(self, event):   
	   global oval
	   global player
	   drawpad.move(player,20,0)
			
	def up(self, event):   
	   global oval
	   global player
	   drawpad.move(player,0,-20)
	
	def down(self, event):   
	   global oval
	   global player
	   
		
myapp = MyApp(root)
root.mainloop()