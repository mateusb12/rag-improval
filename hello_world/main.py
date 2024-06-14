from hello_world.tree import rag_root
from openai_api import query_openai


def recursive_query(node, depth=0):
    if depth > 2:  # Limit the depth for simplicity
        return ""

    response = query_openai(f"{node.prompt}")
    summary = f"{node.name}: {response}\n"

    for child in node.children:
        summary += recursive_query(child, depth + 1)

    return summary


def generate_response(tree_root):
    return recursive_query(tree_root)


if __name__ == "__main__":
    final_response = generate_response(rag_root)
    print(final_response)
