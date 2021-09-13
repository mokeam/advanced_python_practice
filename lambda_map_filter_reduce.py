from functools import reduce

# lambda arguments: expression
add10 = lambda x: x + 10
print(add10(5))

mult = lambda x,y: x * y
print(mult(3,4))

points_2D = [(1,2), (15,1), (5,-1), (10,4)]
points_2D_sorted = sorted(points_2D, key=lambda x: x[1])
print(points_2D)
print(points_2D_sorted)

# map(func, seq)
a = [1, 2, 3, 4, 5, 6]
b = map(lambda x: x * 2, a)
print(a)
print(list(b))


# filter(func,seq)
b = filter(lambda x: x % 2 == 0, a)
print(list(b))

# reduce(func, seq)
mult_a = reduce(lambda x,y: x * y, a)
print(mult_a)