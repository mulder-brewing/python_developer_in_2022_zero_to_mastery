import datetime
from array import array
from collections import Counter, defaultdict, OrderedDict

# Counter creates a dictionary counting the occurrences
li = [1, 2, 3, 4, 5, 6, 7, 7]
print(Counter(li))

sentence = 'blah blah blah thinking about python'
print(Counter(sentence))

# defaultdict gives a default value for key that doesn't exist
dictionary = defaultdict(lambda: 'does not exist', {'a': 1, 'b': 2})
print(dictionary['a'])
print(dictionary['c'])

# Ordered Dictionary is only equal if order is the same
d1 = OrderedDict()
d1['a'] = 1
d1['b'] = 2

d2 = OrderedDict()
d2['b'] = 2
d2['a'] = 1

print(d1 == d2)

d1 = {}
d1['a'] = 1
d1['b'] = 2

d2 = {}
d2['b'] = 2
d2['a'] = 1

print(d1 == d2)

# datetime
print(datetime.date.today())

# array
arr = array('i', [1, 2, 3])
print(arr[0])
