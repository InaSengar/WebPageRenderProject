### Data Persistence

A MySQL database will be used to manage the hierarchical tree data for this service.
Specifically, an adjacency list model will be used in order to maintain the relationships between the parent and children nodes.

```
CREATE TABLE category(
        node_id INT AUTO_INCREMENT PRIMARY KEY,
        label VARCHAR(20) NOT NULL,
        parent INT DEFAULT NULL
);
```

SQL statement to create the table:
```
INSERT INTO category VALUES(1,'root',NULL),(2,'ant',1),(3,'bear',1),
        (4,'cat',3),(5,'dog',3),(6,'elephant',5),(7,'frog',1);
```

In the adjacency list model, every entry within the table maintains a reference to its parent node.

```
SELECT * FROM category ORDER BY node_id;
+-------------+----------------------+--------+
| node_id     | label                | parent |
+-------------+----------------------+--------+
|           1 | root                 |   NULL |
|           2 | ant                  |      1 |
|           3 | bear                 |      1 |
|           4 | cat                  |      3 |
|           5 | dog                  |      3 |
|           6 | elephant             |      5 |
|           7 | frog                 |      1 |
+-------------+----------------------+--------+
```

Sample query that would support `GET /api/tree`:
```
# Fetch the tree data from the database
query = "SELECT node_id, label, parent_id FROM category"
```

Sample query that would support `POST /api/tree`:
```
# Insert a new node into the database
query = "INSERT INTO category (label, parent_id) VALUES (%s, %s)"
```