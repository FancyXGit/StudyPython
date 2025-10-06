from trees import *


def print_leaves_sum(tree, so_far=0):
    so_far = so_far + get_label(tree)
    if is_leaf(tree):
        print(so_far)
    else:
        for branch in get_branches(tree):
            print_leaves_sum(branch, so_far)


def main():
    numbers = tree(3, [tree(4), tree(5, [tree(6)])])
    print_tree(numbers)
    print_leaves_sum(numbers)


if __name__ == "__main__":
    main()
