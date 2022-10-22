# Binary Node conttain the left pointer, right pointer, and the parent pointer
# 

class BinaryNode:
    def __init__(self, item):
        self.item = item
        self.left = None
        self.right = None
        self.parent = None
        # self.subtree_update()

    # Treaversal Order
    def subtree_iter(self):
        # the node and its descendants
        if self.left: yield from self.left.subtree_iter()
        yield self
        if self.right: yield from self.right.subtree_iter()

    # Tree Navigation
    def subtree_first(self):
        if self.left: return self.left.subtree_first()
        else: return self

    def subtree_last(self):
        if self.right: return self.right.subtree_last()
        else: return self

    def successor(self):
        if self.right: return self.right.subtree_first()

        while self.parent and (self is self.parent.right):
            self = self.parent
        
        return self.parent

    def predecessor(self):
        if self.left: return self.left.subtree_last()

        while self.parent and (self is self.parent.left):
            self = self.parent

        return self.parent

    # if there's no left child put the node there
    def subtree_insert_before(self, node):
        if self.left:
            self = self.left.subtree_last()
            self.right, node.parent = node, self
        else:
            self.left, node.parent = node, self


    # if there's no right child put the node there
    def subtree_insert_after(self, node):
        if self.right:
            self = self.right.subtree_first()
            self.left, node.parent = node, self
        else:
            self.right, node.parent = node, self
        

    def subtree_delete(self):
        # Check if the node has children (either left or right)
        if self.left or self.right:
            # if there's a left child we'll remove the predecessor
            if self.left: deleted = self.predecessor()
            # if there's a left child we'll remove the successor
            else: deleted = self.successor()

            self.item, deleted.item = deleted.item, self.item
            return deleted.subtree_delete()

        if self.parent:
            if self.parent.left is self: self.parent.left = None
            else: self.parent.right = None
            # self.parent.maintain()

        return self