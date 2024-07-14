import pickle #use to store python objects as it is 

def save_dict(dict, name):
  with open(name, "wb") as file:
    pickle.dump(dict, file)


def load_dict(name):
  with open(name, "rb") as file:
    return pickle.load(file)


save_dict({1: 'a', 2: 'b', 3: 'c'}, 'test.pkl')
print(load_dict('test.pkl'))