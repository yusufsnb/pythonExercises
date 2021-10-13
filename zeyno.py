a = 1
b = -2
c = -4
delta = b**2 - 4*a*c
x1 = (-b + delta**0.5)/2*a
x2 = (-b - delta**0.5)/2*a

print(x1, x2)

#print(m**2 - ((x1+x2)/x1 * x2)*m + 1/(x1*x2))

print("m**2 {}m {}".format((round((x1+x2)/(x1 * x2), 2)), 1/round((x1*x2), 2)))
