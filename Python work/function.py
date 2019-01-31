# Q1
# def hello ():
#     print ("Hello Igor")
# hello()

import matplotlib.pyplot as plot
def f(x):
    y= x+1
    x=1
xs = list(range(-3, 4))
ys = []
for x in xs:
     ys.append(f(x))
plot.plot(xs, ys)
plot.show()