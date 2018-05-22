import os

d = os.path.dirname(os.path.abspath(__file__))

def dfs_showdir(path, depth):
    if depth == 0:
        print("root:[" + path + "]")

    for item in os.listdir(path):
        if item[0] != '.' and (os.path.isdir(os.path.join(path, item)) or item[-2:] == 'py' or item[-4:] == 'html'):
            print("|      " * depth + "+--" + item)

            newitem = path +'/'+ item
            if os.path.isdir(newitem):
                dfs_showdir(newitem, depth +1)

dfs_showdir(d, 0)