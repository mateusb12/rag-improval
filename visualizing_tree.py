from openai_setup import setup_openai_key
from raptor import RetrievalAugmentation
import networkx as nx
from pyvis.network import Network

setup_openai_key()


def tree_to_graph(tree, current_depth, max_depth):
    G = nx.DiGraph()

    def add_nodes_edges(node_id, depth):
        if depth > max_depth:
            return
        node = tree.all_nodes[node_id]

        # Shorten the displayed text
        short_text = (node.text[:40] + '...') if len(node.text) > 40 else node.text

        # Add node with short text and full text as title for tooltip
        G.add_node(node_id, label=short_text, title=node.text)
        print(f"Added node {node_id}: {short_text}")

        if hasattr(node, 'children') and node.children:
            for child_id in node.children:
                G.add_edge(node_id, child_id)
                print(f"Added edge from {node_id} to {child_id}")
                add_nodes_edges(child_id, depth + 1)

    add_nodes_edges(0, 1)  # Assuming root node has ID 0
    return G


# Load the tree from the saved path
SAVE_PATH = "demo/cinderella"

# Assuming `RetrievalAugmentation` can load the tree directly
RA = RetrievalAugmentation(tree=SAVE_PATH)

# Set the desired tree depth
TREE_DEPTH = 3

# Convert the tree to a NetworkX graph
G = tree_to_graph(RA.tree, 1, TREE_DEPTH)

# Create a Pyvis Network object
net = Network(notebook=True, width="1000px", height="700px", bgcolor="#222222", font_color="white")

# Load the NetworkX graph into the Pyvis Network object
net.from_nx(G)

# Save and show the interactive HTML file
net.show("demo/cinderella_tree.html")

print("Interactive tree visualization saved as 'demo/cinderella_tree.html'")
