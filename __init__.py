from collections import deque

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def fetch_nodes(node):
    # Stage 1: Fetch nodes - Traverse to get nodes
    if node is None:
        return []
    # Traverse left subtree, root, then right subtree
    return fetch_nodes(node.left) + [node] + fetch_nodes(node.right)

def process_nodes(nodes):
    # Stage 2: Process nodes - Example processing: print node values
    for node in nodes:
        print(f"Processing node with value: {node.value}")

def post_process_results(results):
    # Stage 3: Post-process - Collect results (for this example, just return them)
    return results

def pipeline_in_order_traversal(root):
    # Pipeline: Fetch -> Process -> Post-process
    nodes = fetch_nodes(root)
    process_nodes(nodes)
    return post_process_results(nodes)

# Example usage:
if __name__ == "__main__":
    # Create a sample binary tree
    #       4
    #      / \
    #     2   6
    #    / \ / \
    #   1  3 5  7

    tree = TreeNode(4)
    tree.left = TreeNode(2)
    tree.right = TreeNode(6)
    tree.left.left = TreeNode(1)
    tree.left.right = TreeNode(3)
    tree.right.left = TreeNode(5)
    tree.right.right = TreeNode(7)

    # Execute pipelined in-order traversal
    pipeline_in_order_traversal(tree)
