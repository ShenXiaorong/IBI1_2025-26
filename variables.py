a=5.08 #population of Scotland in millions in 2004
b=5.33 #population of Scotland in millions in 2014
c=5.55 #population of Scotland in millions in 2024
d=b-a #population change from 2004 to 2014
e=c-b #population change from 2014 to 2024
if d>e:
    print("	d>e,population	growth	is decelerating.")
elif d<e:
    print("	d<e,population	growth	is accelerating.")
else:
    print("	d=e,population	growth	is constant.")
# d is larger than e, population	growth	is decelerating.
X=True
Y=False
W=X or Y 
print("W=" + str(W)) 
# Truth table for W (X or Y)
# --------------------------
# X      | Y      | W (X or Y)
# --------------------------
# True   | True   | True
# True   | False  | True  # Result for the given X/Y values in this practical :W is True
# False  | True   | True
# False  | False  | False
# --------------------------


