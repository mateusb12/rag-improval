from openai_setup import setup_openai_key
from raptor import RetrievalAugmentation
import networkx as nx
from pyvis.network import Network


def tree_to_graph(tree):
    G = nx.DiGraph()

    # Add all nodes first
    for node_id, node in tree.all_nodes.items():
        # Shorten the displayed text
        short_text = (node.text[:40] + '...') if len(node.text) > 40 else node.text

        # Add node with short text and full text as title for tooltip
        G.add_node(node_id, label=short_text, title=node.text)
        print(f"Added node {node_id}: {short_text}")

    # Add edges after all nodes have been added to ensure all references are valid
    for node_id, node in tree.all_nodes.items():
        if hasattr(node, 'children') and isinstance(node.children, set) and node.children:
            print(f"Node {node_id} has children: {node.children}")
            for child_id in node.children:
                if child_id in G.nodes:
                    G.add_edge(node_id, child_id)
                    print(f"Added edge from {node_id} to {child_id}")
                else:
                    print(f"Warning: Child node {child_id} not found in graph nodes")

    return G


def main():
    setup_openai_key()

    # Load the tree from the saved path
    save_path = "demo/cinderella"

    # Assuming `RetrievalAugmentation` can load the tree directly
    ra = RetrievalAugmentation(tree=save_path)

    # Print the entire tree structure for debugging
    def print_tree_structure(tree):
        for node_id, node in tree.all_nodes.items():
            print(f"Node {node_id}: {node.text}")
            if hasattr(node, 'children') and isinstance(node.children, set):
                print(f"  Children: {node.children}")
            else:
                print("  No children")

    print_tree_structure(ra.tree)

    # Convert the tree to a NetworkX graph
    graph = tree_to_graph(ra.tree)

    # Create a Pyvis Network object
    net = Network(notebook=True, width="100%", height="750px", bgcolor="#222222", font_color="white")

    # Load the NetworkX graph into the Pyvis Network object
    net.from_nx(graph)

    # Display the interactive network in the Jupyter notebook cell
    net.show("demo/cinderella_tree.html")

    print("Interactive tree visualization displayed in the Jupyter notebook.")


if __name__ == "__main__":
    main()
