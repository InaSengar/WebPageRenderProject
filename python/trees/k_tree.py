def build_tree_from_csv(csv_file):
    """
    Build a tree data structure from a CSV file.

    Args:
        csv_file (str): The CSV file.

    Returns:
        dict: The root node of the tree data structure.
    """
    with open(csv_file, 'r') as file:
        lines = file.readlines()

    tree_dict = {}

    for line in lines:
        parts = line.strip().split(',')
        label_id, label, parent_id = parts[0], parts[1], parts[2]

        if parent_id == 'NULL':
            root = {'label_id': label_id, 'label': label, 'children': []}
        else:
            node = {'label_id': label_id, 'label': label, 'children': []}
            if parent_id not in tree_dict:
                tree_dict[parent_id] = []
            tree_dict[parent_id].append(node)

    # Function to add children to a parent node
    def add_children(node):
        label_id = node['label_id']
        if label_id in tree_dict:
            node['children'] = tree_dict[label_id]
            for child in node['children']:
                add_children(child)

    add_children(root)
    return root


def add_node_to_csv(csv_file, parent_id, label):
    """
    Add a new node to the CSV file.

    Args:
        csv_file (str): The CSV file.
        parent_id (str): The ID of the parent node.
        label (str): The label of the new node.

    Returns:
        None
    """

    new_id = get_new_id_value(csv_file)

    # Append the new node to the CSV file as a new line
    with open(csv_file, 'a') as file:
        file.write(f'{new_id},{label},{parent_id}\n')


def is_valid_parent(node, parent_id):
    """
    Check if a parent node exists in the tree.

    Args:
        node (dict): The current node.
        parent_id (str): The ID of the parent node.

    Returns:
        bool: True if the parent node exists, False otherwise.
    """
    if node['label_id'] == parent_id:
        return True

    for child in node['children']:
        if is_valid_parent(child, parent_id):
            return True

    return False


def print_tree(node, level=0):
    """
    Print the tree data structure.

    Args:
        node (dict): The current node being examined.
        level (int): The current level of the tree.

    Returns:
        None
    """
    if node:
        print("  " * level + node['label'])
        for child in node['children']:
            print_tree(child, level + 1)


def get_new_id_value(csv_file):
    """
    Create new id for node being added.

    Args:
        csv_file (str): The CSV file.

    Returns:
        int: A new id.
    """
    with open(csv_file, 'r') as file:
        lines = file.readlines()

    global_id_counter = 1
    for line in lines:
        parts = line.strip().split(',')
        if global_id_counter == int(parts[0]):
            global_id_counter += 1

    return global_id_counter
