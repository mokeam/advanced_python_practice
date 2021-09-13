from collections import Counter, namedtuple, OrderedDict, defaultdict, deque

# Counter
a = "aaaaaaabbbbbccccc"
my_counter = Counter(a)
print(my_counter)
print(my_counter.keys())
print(my_counter.values())
print(my_counter.most_common(2))

# namedtuple
Point = namedtuple('Point','x,y')
pt = Point(1,-4)
print(pt.x,pt.y)

# OrderedDict
ordered_dict = OrderedDict()
ordered_dict['b'] = 2
ordered_dict['c'] = 3
ordered_dict['d'] = 4
ordered_dict['a'] = 1
print(ordered_dict)

# defaultdict
d = defaultdict(int)
d['a'] = 1
d['b'] = 2
print(d['c'])

# deque
d = deque()
d.append(1)
d.append(2)
d.appendleft(3)
print(d)
d.pop()
d.extend([4,8,5])
print(d)