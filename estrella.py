import turtle
t = turtle.Pen()
def dibujar(x):
	for i in range (0,x):
		t.forward(100)
		t.left(360/x*2)
puntas=int(input("Ingrese numero (impar): "))
while((puntas%2)==0 or puntas<3):
	puntas=int(input("Ingrese numero (impar): "))
dibujar(puntas) 
turtle.getscreen()._root.mainloop()