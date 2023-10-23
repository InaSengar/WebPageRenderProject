## Render a webpage with Nodes: API Design Exercise
### Installation Instructions
To set up the service, refer to: [Install.md](Install.md)

### Running and Testing the Service
To run the service, execute in terminal: `python main.py`

To test `GET /api/tree`, go to: <a> http://localhost:3001/api/tree </a>

To test `POST /api/tree`, run this curl command (replace parent id and label as necessary):
```
curl -X POST http://localhost:3001/api/tree -H "Content-Type: application/json" -d '{
  "parent": "7",
  "label": "tortoise"
}'
```

### Design Choices
The tree structure utilized in this application is stored in `animal_tree.csv` file. The data is converted to a general 
tree structure in the `k_tree.py` module. A general tree structure was used here to handle the csv contents as it provides 
a more structured and hierarchical representation of the data.

Once the tree structure is created, the next step is to transform it into a JSON format. To facilitate this process, the 
Flask framework is employed on the backend to render the JSON data. This enables the tree structure to be accessible 
through the designated endpoint.

Adding a new node to the tree involves a two-step process. First, the new node is appended to the animal_tree.csv file. 
Afterward, the data tree is reconstructed from the updated CSV file. Upon refreshing the `http://localhost:3001/api/tree` 
endpoint, the newly added node becomes visible within the tree structure.
