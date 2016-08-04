# filename:     lec13_trees
# author:       dan.smith.me@gmail.com
# date:         01/08/2016
# version:      1.0
# =====================================================================================================================

class binary_tree(object):
    def __init__(self, value):
        self.value = value
        self.left_branch = None
        self.right_branch = None
        self.parent = None

    def set_left_branch(self, node):
        self.left_branch = node

    def set_right_branch(self, node):
        self.right_branch = node

    def set_parent(self, parent):
        self.parent = parent

    # Other methods ...
    def get_value(self):
        return self.value

    def get_left_branch(self):
        return self.left_branch

    def get_right_branch(self):
        return self.right_branch

    def get_parent(self):
        return self.parent

    def __str__(self):
        return self.value


# # Constructing an example tree
# n5 = binary_tree(5)
# n2 = binary_tree(2)
# n1 = binary_tree(1)
# n4 = binary_tree(4)
# n8 = binary_tree(8)
# n6 = binary_tree(6)
# n7 = binary_tree(7)
#
# n5.set_left_branch(n2)
# n2.set_parent(n5)
# n5.set_right_branch(n8)
# n8.set_parent(n5)
# n2.set_left_branch(n1)
# n1.set_parent(n2)
# n2.set_right_branch(n4)
# n4.set_parent(n2)
# n8.set_left_branch(n6)
# n6.set_parent(n8)
# n6.set_right_branch(n7)
# n7.set_parent(n6)


# DFS of binary tree
def dfs_binary(root, fcn):
    stack = [root]
    while len(stack) > 0:
        if fcn(stack[0]):
            return True
        else:
            temp = stack.pop(0)
            if temp.get_right_branch():
                stack.insert(0, temp.get_right_branch())
            if temp.get_left_branch():
                stack.insert(0, temp.get_left_branch())
    return False

# DFS of binary tree
def bfs_binary(root, fcn):
    queue = [root]
    while len(queue) > 0:
        if fcn(queue[0]):
            return True
        else:
            temp = queue.pop(0)
            if temp.get_left_branch():
                queue.append(temp.get_left_branch())
            if temp.get_right_branch():
                queue.append(temp.get_right_branch())
    return False


# Ordered Search
def dfs_binary_ordered(root, fcn, ltFcn):
    stack = [root]
    while len(stack) > 0:
        if fcn(stack[0]):
            return True
        elif ltFcn(stack[0]):
            temp = stack.pop(0)
            if temp.get_left_branch():
                stack.insert(0, temp.get_left_branch())
        else:
            if temp.get_right_branch():
                stack.insert(0, temp.get_right_branch())
    return False


# Decision Trees
def build_d_tree(sofar, todo):
    if len(todo) == 0:
        return binary_tree(sofar)
    else:
        withelt = build_d_tree(sofar + [todo[0]], todo[1:])
        withoutelt = build_d_tree(sofar, todo[1:])
        here = binary_tree(sofar)
        here.set_left_branch(withelt)
        here.set_right_branch(withoutelt)
        return here


def dfs_d_tree(root, value_fcn, constraint_fcn):
    stack = [root]
    best = None
    visited = 0
    while len(stack) > 0:
        visited += 1
        if constraint_fcn(stack[0].get_value()):
            if best == None:
                best = stack[0]
            elif value_fcn(stack[0].get_value()) > value_fcn(best.get_value()):
                best = stack[0]
            temp = stack[0]
            if temp.get_right_branch():
                stack.insert(0, temp.get_right_branch())
            if temp.get_left_branch():
                stack.insert(0, temp.get_left_branch())
        else:
            stack.pop(0)
    print 'visited', visited
    return best

a = [6, 3]
b = [7, 2]
c = [8, 4]
d = [9, 5]

tree_test = build_d_tree([], [a, b, c, d])


def sum_values(lst):
    vals = [e[0] for e in lst]
    return sum(vals)


def weights_below10(lst):
    wts = [e[1] for e in lst]
    return sum(wts) <= 10

print(dfs_d_tree(tree_test, sum_values, weights_below10))

