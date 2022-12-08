from gremlin_python.driver import client, serializer
import csv
from pathlib import Path

recipe_file_path = "./data/recipe.csv"
recipe_file = open(recipe_file_path,"r")
recipe_data = list(csv.reader(recipe_file, delimiter=","))
recipe_file.close()
recipe_file_name = Path(recipe_file_path).stem
_gremlin_insert_recipe_vertices = []

ingredient_file_path = "./data/ingredient.csv"
ingredient_file = open(ingredient_file_path,"r")
ingredient_data = list(csv.reader(ingredient_file, delimiter=","))
ingredient_file.close()
ingredient_file_name = Path(ingredient_file_path).stem
_gremlin_insert_ingredient_vertices = []

requires_file_path = "./data/requires.csv"
requires_file = open(requires_file_path,"r")
requires_data = list(csv.reader(requires_file, delimiter=","))
requires_file.close()
requires_file_name = Path(requires_file_path).stem
_gremlin_insert_requires_edges = []

endpoint = "PLEASE_ENTER_YOUR_OWN_AZURE_COSMOS_GREMLIN_DB_NAME.gremlin.cosmosdb.azure.com"
graph_database = "recipes-database"
graph_collection = "recipes-graph"
primary_access_key = "PLEASE_ENTER_YOUR_OWN_AZURE_COSMOS_GREMLIN_DB_PRIMARY_ACCESS_KEY"

for recipe in recipe_data:
    recipe_vertex = ("g.addV('"+recipe_file_name+"').property('id', '"+recipe[1]+"').property('style', '"
    +recipe[2]+"').property('type', '"+recipe[3]+"'),")
    _gremlin_insert_recipe_vertices.append(recipe_vertex)

for ingredient in ingredient_data:
    ingredient_vertex = "g.addV('"+ingredient_file_name+"').property('id', '"+ingredient[1]+"').property('type', '"+ingredient[2]+"'),"
    _gremlin_insert_ingredient_vertices.append(ingredient_vertex)

for requires in requires_data:
    requires_edge = "g.V('"+requires[0]+"').addE('"+requires[1]+"').to(g.V('"+requires[2]+\
    "')).property('weight',"+requires[3]+").property('quantity',"+requires[4]+"),"
    print(requires_edge)
    _gremlin_insert_requires_edges.append(requires_edge)

_gremlin_cleanup_graph = "g.V().drop()"

def cleanup_graph(client_connection):
    print("\n> {0}".format(_gremlin_cleanup_graph))
    callback = client_connection.submitAsync(_gremlin_cleanup_graph)
    if callback.result() is not None:
        callback.result().all().result() 
    print("Graph DB has been cleaned up.")

def insert_recipe_vertices(client_connection):
    for vertex in _gremlin_insert_recipe_vertices:
        print("\n> {0}".format(vertex))
        callback = client_connection.submitAsync(vertex)
        if callback.result() is not None:
            print("Inserted this vertex:\n{0}".format(callback.result().one()))
        else:
            print("Something went wrong with this query: {0}".format(vertex))

def insert_ingredient_vertices(client_connection):
    for vertex in _gremlin_insert_ingredient_vertices:
        print("\n> {0}".format(vertex))
        callback = client_connection.submitAsync(vertex)
        if callback.result() is not None:
            print("Inserted this vertex:\n{0}".format(callback.result().one()))
        else:
            print("Something went wrong with this query: {0}".format(vertex))

def insert_requires_edges(client_connection):
    for edge in _gremlin_insert_requires_edges:
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
    insert_recipe_vertices(client_connection)
    insert_ingredient_vertices(client_connection)

    # Insert Edges
    insert_requires_edges(client_connection)

    print('Finished!')

    # Close the client connection
    client_connection.close()

if __name__ == '__main__':
    run()
