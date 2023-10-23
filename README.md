## API Design: Render, Manage, Manipulate Trees on Webpage

This service manages and manipulates trees.
Within the Python directory, there is a README.md with the following information:
1. How to set up this service
2. How to run this service
3. Design choices made along the way

## The Problem

A new web application is being built. The application renders and stores a tree of data.

Animals, an example of a tree:

```
1: root
    2: ant
    3: bear
        4: cat
        5: dog
            6: elephant
    7: frog
```

The format is a simple unique numeric id and alphanumeric label eg, `id: label`. Indentation indicates a child relationship. So, `1: root` has the children `2: ant, 3: bear, 7: frog`.

&nbsp;
## API Details

For the sake of this project, I've persisted data in memory and simple files.

The service runs on, `http://localhost:3001/api/<end-point>` and the following end point has been made available.
<br><br>

---
<br>

### 1. `GET /api/tree` returns the entire tree - in the following format:

```
[
    {
        "<id>": {
            "label": "<first item>",
            "children": [
                {
                    "<id>": {
                        "label": "<another item>",
                        "children": [] // empty children
                    }
                },
                {
                    "<id>": {
                        "label": "<another item>",
                        "children": [ ...<any children>... ]
                    }
                }
            ]
        }
    }
]
```

#### Part 1

The route has been added, and I'm returning the data structure that represents the animals example above.

<br><br>

---
<br>

### 2. `POST /api/tree/` with the payload of the format:

```
{
    "parent": "<id>",
    "label": "<label>"
}
```

Will cause a node to be added to the end of a list of children, a new unique id will be assigned by the service.

#### Part 2

The route has been implemented, and a `GET /api/tree` request returns the updated tree.
<br><br>

---

<br>

### 3. Data persistance

I've documented the queries, methods, and decisions I would make if implementing. 
<br><br>

#### Part 3

I've designed a data schema for a database of my choice that would support the tree data above. It's been added to a `database.md` file.

I've also written sample queries / code that would support the two routes that are detailed above.
