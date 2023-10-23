import yaml
from flask import Flask, request, jsonify
from trees import add_node_to_csv, build_tree_from_csv, is_valid_parent, print_tree, tree_to_json


app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.config['JSON_SORT_KEYS'] = False

with open('config.yaml', 'r') as f:
    cfg = yaml.safe_load(f)

# Read output from the database dump path defined in config.yaml
pth_db_dump = cfg['path_database_dump']

# Initialize data_tree by building the tree from the CSV file
data_tree = build_tree_from_csv(pth_db_dump)


@app.route('/api/tree', methods=['GET'])
def get_tree():
    """
    Get the tree data structure in JSON format.

    Returns:
        JSON: The tree data in the specified format.
    """
    global data_tree

    print_tree(data_tree)

    # Convert the tree to JSON dictionary
    tree_json = tree_to_json(data_tree)

    return jsonify([tree_json])


@app.route('/api/tree', methods=['POST'])
def add_node():
    """
    Add a new node to the tree.

    Reads the parent and label from the POST request, checks if the parent node exists,
    adds a new node to the CSV file, and rebuilds the tree.

    Returns:
        JSON: A success message or an error message.
    """
    global data_tree

    data = request.get_json()
    parent_id = data['parent']
    label = data['label']

    # Check if the parent ID exists in the data tree
    if not is_valid_parent(data_tree, parent_id):
        return jsonify({"error": "Parent node does not exist"}), 400

    # Call the function to add the new node to the CSV file
    add_node_to_csv(pth_db_dump, parent_id, label)

    # Rebuild the tree from the updated CSV file
    data_tree = build_tree_from_csv(pth_db_dump)

    # Return a success response
    return jsonify({"message": "Node added successfully"})


if __name__ == '__main__':
    app.run(host='localhost', port=3001)
