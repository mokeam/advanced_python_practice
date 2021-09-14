def foo(a, b, *args, **kwargs):
    print(a,b)
    for arg in args:
        print(arg)
    for key in kwargs:
        print(key, kwargs[key])

if __name__ == '__main__':
    foo(1, 2, 3, 4, 5, six = 6, seven = 7)
    numbers = [1, 2, 3, 4, 5, 6]
    beginning, *middle, last = numbers
    print(beginning)
    print(middle)
    print(last)

    my_tuple = (1, 2, 3)
    my_list = [4, 5, 6]
    new_list = [*my_tuple, *my_list]
    print(new_list)

    dict_a = {"a":1, "b":2}
    dict_b = {"c":3, "d":4}
    my_dict = {**dict_a, **dict_b}
    print(my_dict)