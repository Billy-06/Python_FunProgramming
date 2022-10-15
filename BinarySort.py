def inOrderWalk(x):
    if x is not None:
        inOrderWalk(x.left)
        print(x.key)
        inOrderWalk(x.right)