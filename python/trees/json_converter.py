def tree_to_json(node):
    """
    Convert a tree data structure to a JSON-compatible format.

    Args:
        node (dict): The root node.

    Returns:
        dict: A dictionary representing the tree.
    """
    if not node:
        return {}

    result = {
        str(node['label_id']): {
            "label": node['label'],
            "children": []
        }
    }

    for child in node['children']:
        child_dict = tree_to_json(child)
        result[str(node['label_id'])]["children"].append(child_dict)

    return result
