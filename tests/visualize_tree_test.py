import pickle

from path_reference import get_tree_pkl_path
from raptor import Node, Tree
from tests.visualize_core import visualize_tree_structure


def load_tree(path):
    """Load the tree from a pickled file."""
    with open(path, "rb") as file:
        tree_object = pickle.load(file)
    return tree_object


# Load the tree from the pickled file
file_path = get_tree_pkl_path()
tree = load_tree(file_path)

# Now create a new root Node on top of all root nodes
root_node = Node(
    text="Root Node",  # You can replace this with an appropriate text for the root node
    index=-1,
    children=list(map(lambda x: x.index, tree.root_nodes.values())),
    embeddings=[]
)

visualize_tree_structure(root_node, tree)
