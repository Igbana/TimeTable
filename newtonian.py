from time import sleep
x = 2
y = 0
counter = 1
while True:
	f = (x**3) - (3*x) - 4
	g = (3*(x**2)) - 3
	y = x - (f/g)
	print("\nX",counter)
	print("f =", f)
	print("f' =",g)
	print(y)
	print(x-y)
	x = y
	counter += 1
	sleep(0.2)