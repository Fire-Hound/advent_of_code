class Tree:
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.children = {}
        self.value = []

    def get(self, pointer):
        copy = pointer.copy()
        node = self
        for path in copy:
            if node.name == path:
                continue
            elif path in node.children:
                node = node.children[path]
            else:
                node.children[path] = Tree(path, node)
                node = node.children[path]
        return node

    def __str__(self):
        return f"Tree({self.name}, {self.value}, {self.children})"

    def __repr__(self):
        return self.__str__()


def is_command(line):
    return line.startswith("$ ")


def get_all_nodes(tree):
    nodes = []
    traversed = []
    node = tree
    while node:
        for child in node.children:
            nodes.append(node.children[child])
        traversed.append(node)
        if len(nodes) == 0:
            break
        node = nodes.pop(-1)
    return traversed


def get_all_values(_node):
    node = _node
    values = []
    nodes = []
    while node:
        values.extend(node.value)
        for child in node.children:
            nodes.append(node.children[child])
        if len(nodes) == 0:
            break
        node = nodes.pop(-1)
    return values


def part1(tree):
    nodes = get_all_nodes(tree)
    total = 0
    for node in nodes:
        values = get_all_values(node)
        node_size = sum([int(value[0]) for value in values])
        if node_size <= 100000:
            total += node_size
    print(total)


def part2(tree):
    root_size = sum([int(value[0]) for value in get_all_values(tree)])

    unused_space = 70000000 - root_size
    space_needed = 30000000 - unused_space

    nodes = get_all_nodes(tree)
    sizes = {}

    for node in nodes:
        values = get_all_values(node)
        node_size = sum([int(value[0]) for value in values])
        if node_size >= space_needed:
            sizes[node.name] = node_size

    print(min(sizes.values()))


if __name__ == "__main__":
    filename = "input.txt"
    with open(filename) as f:
        console = f.read().split("\n")

    tree = Tree("/")
    pointer = []
    for line in console:
        if is_command(line):
            tokens = line.split(" ")
            if tokens[1] == "cd":
                if tokens[2] == "..":
                    pointer = pointer[:-1]
                else:
                    pointer.append(tokens[2])
        else:
            output = line.split(" ")
            node = tree.get(pointer)
            if output[0] == "dir":
                node.children[output[1]] = Tree(output[1], node)
            else:
                node.value.append(output)
    part1(tree)
    part2(tree)
