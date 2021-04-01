class TreeNode:
    def __init__(self, data, key=int):
        self.data = data
        self.key = key
        self.left = None
        self.right = None


class PrioQueue:
    def __init__(self, key=int):
        self.root = None
        self.key = key

    def getEmpty(self):
        return self.root == None
    empty = property(getEmpty)

    def add(self, data):
        element = TreeNode(data)
        # Classic add í Binary tree
        if self.root == None:
            # Ef tré er tómt
            self.root = element
            return 0
        else:
            head = self.root
            while True:
                # Finna réttan stað og setja node þar
                if self.key(element.data) <= self.key(head.data):
                    if head.left == None:
                        head.left = element
                        return 0
                    else:
                        head = head.left
                else:
                    if head.right == None:
                        head.right = element
                        return 0
                    else:
                        head = head.right

    def pop(self):
        # TODO error Handling

        head = self.root
        last = None
        while head.left != None:
            last = head
            head = head.left

        if last == None:
            self.root = head.right
        else:
            last.left = head.right
        data = head.data
        del head
        return data


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x+other.x, self.y+other.y)

    def BoundsCheck(self, bounds):
        return 0 <= self.x and self.x < bounds[0] and 0 <= self.y and self.y < bounds[1]

    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


def CountList(L):
    counted = {}
    for x in L:
        if x in counted.keys():
            counted[x] += 1
        else:
            counted[x] = 1
    return counted
