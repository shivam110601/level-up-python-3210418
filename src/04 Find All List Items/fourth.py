def index_all(search_list, item):
  index_list = []
  for index, value in enumerate(search_list):
    if item == value:
      print("I---", [index], value)
      index_list.append([index])
    elif isinstance(search_list[index], list):
      print("II---", search_list[index])
      for i in index_all(search_list[index], item):
        print("III---", [index], i)
        index_list.append([index]+i)
        print("IV---", [index]+i)
  return index_list

print(index_all([[[1, 2, 3], 2, [1, 3]], [1, 2, 3]], 2))