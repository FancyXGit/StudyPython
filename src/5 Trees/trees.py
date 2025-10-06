def get_branches(tree):
    return tree[1:]


def get_label(tree):
    return tree[0]


def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    else:
        for branch in get_branches(tree):
            if not is_tree(branch):
                return False
        return True


def is_leaf(tree):
    if get_branches(tree) == []:
        return True
    return False


def tree(label, branches=[]):
    for branch in branches:
        assert is_tree(branch)
    return [label] + branches


def count_leaves(tree):
    branches = get_branches(tree)
    if branches == [] and is_tree(tree):
        return 1
    branch_leaves = [count_leaves(branch) for branch in branches]
    return sum(branch_leaves)


def get_leaves(tree):
    if is_leaf(tree):
        return [get_label(tree)]
    return [leaf for branch in get_branches(tree) for leaf in get_leaves(branch)]


def print_tree(tree, indent=0):
    print(" " * indent + str(get_label(tree)))
    branches = get_branches(tree)
    for branch in branches:
        print_tree(branch, indent + 1)


def make_fibonacci_tree(deepth, para1=1, para2=1):
    prev_tree_1 = tree(para1)
    prev_tree_2 = tree(para2)
    next_tree = []
    for i in range(deepth):
        next_tree = tree(
            get_label(prev_tree_1) + get_label(prev_tree_2), [prev_tree_1, prev_tree_2]
        )
        prev_tree_1, prev_tree_2 = prev_tree_2, next_tree
    return next_tree


def main():
    tree1 = tree(10, [tree(2)])
    print(tree1)
    print(count_leaves(tree1))

    tree2 = make_fibonacci_tree(4, 0, 1)
    print(tree2)  # 1 1 2 3 5 8 13
    print(count_leaves(tree2))
    print(get_leaves(tree2))
    print_tree(tree2)


if __name__ == "__main__":
    main()
