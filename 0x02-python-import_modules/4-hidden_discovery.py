#!/usr/bin/python3

if __name__ != "__main__":
    exit()
if __name__ == "__main__":
    """print all names defined by hidden_4 module."""
    import hidden_4

for name in dir(hidden_4):
    if name[0:2] != "__"
    print(name)
