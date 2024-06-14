from openai_setup import setup_openai_key
from raptor import RetrievalAugmentation
import networkx as nx
from pyvis.network import Network


def extract_edges(tree):
    edges = []
    for node_index, node in tree.all_nodes.items():
        for child_index in node.children:
            edges.append((node_index, child_index))
    return edges


def tree_to_graph(tree):
    graph = nx.DiGraph()
    edges = extract_edges(tree)

    # Add all nodes first
    for node_id, node in tree.all_nodes.items():
        # Shorten the displayed text for readability
        short_text = (node.text[:20] + '...') if len(node.text) > 20 else node.text
        graph.add_node(node_id, label=short_text)

    # Add edges
    graph.add_edges_from(edges)

    return graph


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
