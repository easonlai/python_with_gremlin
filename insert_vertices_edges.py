from gremlin_python.driver import client, serializer

endpoint = "PLEASE_ENTER_YOUR_OWN_AZURE_COSMOS_GREMLIN_DB_NAME.gremlin.cosmosdb.azure.com"
graph_database = "recipes-database"
graph_collection = "recipes-graph"
primary_access_key = "PLEASE_ENTER_YOUR_OWN_AZURE_COSMOS_GREMLIN_DB_PRIMARY_ACCESS_KEY"

_gremlin_cleanup_graph = "g.V().drop()"

_gremlin_insert_vertices = [
    "g.addV('recipe').property('id', 'Egg Fired Rice').property('style', 'Chinese').property('type', 'firedRice')",
    "g.addV('recipe').property('id', 'Yang Chow Fried Rice').property('style', 'Chinese').property('type', 'firedRice')",
    "g.addV('recipe').property('id', 'Western Fried Rice').property('style', 'Chinese').property('type', 'firedRice')",
    "g.addV('recipe').property('id', 'Egg Sandwich').property('style', 'Chinese').property('type', 'sandwich')",
    "g.addV('recipe').property('id', 'Luncheon Meat & Egg Sandwich').property('style', 'Chinese').property('type', 'sandwich')",
    "g.addV('recipe').property('id', 'Tomato & Egg Sandwich').property('style', 'Chinese').property('type', 'sandwich')",
    "g.addV('ingredient').property('id', 'Egg').property('type', 'ingredient')",
    "g.addV('ingredient').property('id', 'Cold Rice').property('type', 'ingredient')",
    "g.addV('ingredient').property('id', 'Oil').property('type', 'ingredient')",
    "g.addV('ingredient').property('id', 'Soy Sauce').property('type', 'ingredient')",
    "g.addV('ingredient').property('id', 'Green Onion Diced').property('type', 'ingredient')",
    "g.addV('ingredient').property('id', 'Salt').property('type', 'ingredient')",
    "g.addV('ingredient').property('id', 'Sugar').property('type', 'ingredient')",
    "g.addV('ingredient').property('id', 'Char Siu Diced').property('type', 'ingredient')",
    "g.addV('ingredient').property('id', 'Shrimp').property('type', 'ingredient')",
    "g.addV('ingredient').property('id', 'Sausage Diced').property('type', 'ingredient')",
    "g.addV('ingredient').property('id', 'Green Pea').property('type', 'ingredient')",
    "g.addV('ingredient').property('id', 'Corn').property('type', 'ingredient')",
    "g.addV('ingredient').property('id', 'Ketchup').property('type', 'ingredient')",
    "g.addV('ingredient').property('id', 'White Bread').property('type', 'ingredient')",
    "g.addV('ingredient').property('id', 'Luncheon Meat Slice').property('type', 'ingredient')",
    "g.addV('ingredient').property('id', 'Tomato Slice').property('type', 'ingredient')",
]

_gremlin_insert_edges = [
    "g.V('Egg Fired Rice').addE('requires').to(g.V('Egg')).property('weight',1).property('quantity',3)",
    "g.V('Egg Fired Rice').addE('requires').to(g.V('Cold Rice')).property('weight',1).property('quantity',2)",
    "g.V('Egg Fired Rice').addE('requires').to(g.V('Oil')).property('weight',1).property('quantity',1)",
    "g.V('Egg Fired Rice').addE('requires').to(g.V('Soy Sauce')).property('weight',1).property('quantity',1)",
    "g.V('Egg Fired Rice').addE('requires').to(g.V('Green Onion Diced')).property('weight',0.5).property('quantity',15)",
    "g.V('Egg Fired Rice').addE('requires').to(g.V('Salt')).property('weight',0.5).property('quantity',1)",
    "g.V('Egg Fired Rice').addE('requires').to(g.V('Sugar')).property('weight',0.5).property('quantity',1)",
    "g.V('Yang Chow Fried Rice').addE('requires').to(g.V('Egg')).property('weight',1).property('quantity',2)",
    "g.V('Yang Chow Fried Rice').addE('requires').to(g.V('Cold Rice')).property('weight',1).property('quantity',2)",
    "g.V('Yang Chow Fried Rice').addE('requires').to(g.V('Oil')).property('weight',1).property('quantity',1)",
    "g.V('Yang Chow Fried Rice').addE('requires').to(g.V('Soy Sauce')).property('weight',1).property('quantity',1)",
    "g.V('Yang Chow Fried Rice').addE('requires').to(g.V('Green Onion Diced')).property('weight',0.5).property('quantity',15)",
    "g.V('Yang Chow Fried Rice').addE('requires').to(g.V('Salt')).property('weight',0.5).property('quantity',1)",
    "g.V('Yang Chow Fried Rice').addE('requires').to(g.V('Sugar')).property('weight',0.5).property('quantity',1)",
    "g.V('Yang Chow Fried Rice').addE('requires').to(g.V('Char Siu Diced')).property('weight',1).property('quantity',15)",
    "g.V('Yang Chow Fried Rice').addE('requires').to(g.V('Shrimp')).property('weight',1).property('quantity',8)",
    "g.V('Western Fried Rice').addE('requires').to(g.V('Egg')).property('weight',1).property('quantity',2)",
    "g.V('Western Fried Rice').addE('requires').to(g.V('Cold Rice')).property('weight',1).property('quantity',2)",
    "g.V('Western Fried Rice').addE('requires').to(g.V('Oil')).property('weight',1).property('quantity',1)",
    "g.V('Western Fried Rice').addE('requires').to(g.V('Green Onion Diced')).property('weight',0.5).property('quantity',15)",
    "g.V('Western Fried Rice').addE('requires').to(g.V('Salt')).property('weight',0.5).property('quantity',1)",
    "g.V('Western Fried Rice').addE('requires').to(g.V('Sugar')).property('weight',0.5).property('quantity',1)",
    "g.V('Western Fried Rice').addE('requires').to(g.V('Sausage Diced')).property('weight',1).property('quantity',15)",
    "g.V('Western Fried Rice').addE('requires').to(g.V('Green Pea')).property('weight',1).property('quantity',10)",
    "g.V('Western Fried Rice').addE('requires').to(g.V('Corn')).property('weight',0.5).property('quantity',10)",
    "g.V('Western Fried Rice').addE('requires').to(g.V('Ketchup')).property('weight',1).property('quantity',3)",
    "g.V('Egg Sandwich').addE('requires').to(g.V('White Bread')).property('weight',1).property('quantity',2)",
    "g.V('Egg Sandwich').addE('requires').to(g.V('Egg')).property('weight',1).property('quantity',2)",
    "g.V('Egg Sandwich').addE('requires').to(g.V('Oil')).property('weight',1).property('quantity',1)",
    "g.V('Egg Sandwich').addE('requires').to(g.V('Salt')).property('weight',1).property('quantity',1)",
    "g.V('Luncheon Meat & Egg Sandwich').addE('requires').to(g.V('White Bread')).property('weight',1).property('quantity',2)",
    "g.V('Luncheon Meat & Egg Sandwich').addE('requires').to(g.V('Egg')).property('weight',1).property('quantity',2)",
    "g.V('Luncheon Meat & Egg Sandwich').addE('requires').to(g.V('Oil')).property('weight',1).property('quantity',1)",
    "g.V('Luncheon Meat & Egg Sandwich').addE('requires').to(g.V('Salt')).property('weight',0.5).property('quantity',1)",
    "g.V('Luncheon Meat & Egg Sandwich').addE('requires').to(g.V('Luncheon Meat Slice')).property('weight',1).property('quantity',2)",
    "g.V('Tomato & Egg Sandwich').addE('requires').to(g.V('White Bread')).property('weight',1).property('quantity',2)",
    "g.V('Tomato & Egg Sandwich').addE('requires').to(g.V('Egg')).property('weight',1).property('quantity',2)",
    "g.V('Tomato & Egg Sandwich').addE('requires').to(g.V('Oil')).property('weight',1).property('quantity',1)",
    "g.V('Tomato & Egg Sandwich').addE('requires').to(g.V('Salt')).property('weight',1).property('quantity',1)",
    "g.V('Tomato & Egg Sandwich').addE('requires').to(g.V('Tomato Slice')).property('weight',1).property('quantity',4)",
]

def cleanup_graph(client_connection):
    print("\n> {0}".format(_gremlin_cleanup_graph))
    callback = client_connection.submitAsync(_gremlin_cleanup_graph)
    if callback.result() is not None:
        callback.result().all().result() 
    print("Graph DB has been cleaned up.")

def insert_vertices(client_connection):
    for vertex in _gremlin_insert_vertices:
        print("\n> {0}".format(vertex))
        callback = client_connection.submitAsync(vertex)
        if callback.result() is not None:
            print("Inserted this vertex:\n{0}".format(callback.result().one()))
        else:
            print("Something went wrong with this query: {0}".format(vertex))

def insert_edges(client_connection):
    for edge in _gremlin_insert_edges:
        callback = client_connection.submitAsync(edge)
        if callback.result() is not None:
            print("Inserted this edge:\n{0}".format(callback.result().one()))
        else:
            print("Something went wrong with this query:\n{0}".format(edge))

def run():
    # Client Initialization
    print("Initializing Gremlin Python Client.")
    client_connection = client.Client(
        "wss://" + endpoint + ":443/", "g",
        username="/dbs/" + graph_database + "/colls/" + graph_collection,
        password=primary_access_key,
        message_serializer=serializer.GraphSONSerializersV2d0()
    )
    print("Gremlin Python Client Initialized.")

    # Purge Graph Database
    cleanup_graph(client_connection)

    # Insert Vertices
    insert_vertices(client_connection)

    # Insert Edges
    insert_edges(client_connection)

    print('Finished!')

    # Close the client connection
    client_connection.close()

if __name__ == '__main__':
    run()