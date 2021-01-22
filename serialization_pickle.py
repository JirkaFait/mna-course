import pickle
friends1 = {"Jirka": [20, "Karvina", 125458], "Pavel": [24, "Ostrava", 458747]}
friends2 = {"Karel": [20, "Karvina", 125458], "Tonda": [24, "Ostrava", 458747]}
friends = (friends1, friends2)

with open('friends.dat', 'wb') as f:
    pickle.dump(friends, f)

with open('friends.dat', 'rb') as f:
    obj = pickle.load(f)
    print(type(obj))
    print(obj)
