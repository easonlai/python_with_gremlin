# Python with Azure Cosmos DB for Apache Gremlin

This is a demo repo demonstrating how to use Python to interact with [Azure Cosmos DB for Apache Gremlin](https://learn.microsoft.com/en-us/azure/cosmos-db/gremlin/introduction). I prepared a sample dataset of recipes and corresponding ingredients to illustrate their graph relationship. It contains 6 recipes and 16 ingredients.

Each of the recipes & ingredients represents the vertex (aka node). Vertexes are connected via edges representing the relationships (requires). And each vertex and edge has its corresponding property for more descriptive details.

I used "id" in the vertex property to store the recipe's name and ingredient for easier illustration. In the edge property, I used "weight" to illustrate whether or not the ingredient must be required. And used the "quantity" property to illustrate the amount required, e.g., ".property('quantity',3)" of 'Egg' represents 3 eggs are required; ".property('quantity',2)" of 'Cold Rice' represents the 2 cups of cold rice are required; "property('quantity',1)" of 'Soy Sauce' or 'Salt' or 'Sugar' represents 1 tablespoon is required.

Content:
* data/ingredient.csv <-- CSV file for storing the ingredient (vertexes).
* data/recipe.csv <-- CSV file for storing the recipe (vertexes).
* data/requires.csv <-- CSV file for storing the relationship between the recipe and ingredient (edges).
* [insert_vertices_edges_2.py](https://github.com/easonlai/python_with_gremlin/blob/main/insert_vertices_edges_2.py) <-- Version 2 of the Python script to read vertexes and edges CSV data file and insert it into Azure Cosmos DB for Apache Gremlin.
* [insert_vertices_edges.py](https://github.com/easonlai/python_with_gremlin/blob/main/insert_vertices_edges.py) <-- Version 1 of the Python script that hardcodes vertexes and edges to insert into Azure Cosmos DB for Apache Gremlin.
* [graph_query.ipynb](https://github.com/easonlai/python_with_gremlin/blob/main/graph_query.ipynb) <-- Sample Notebook to perform interactive Gremlin query over Azure Cosmos DB for Apache Gremlin.

![alt text](https://github.com/easonlai/python_with_gremlin/blob/main/git-images/git-image-1.png)

Enjoy!

