class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def create_large_binary_tree(depth):
    """Create a binary tree of a given depth."""
    def create_node(level, index):
        if level > depth:
            return None
        value = (2 ** (level - 1)) + index
        left = create_node(level + 1, 2 * index)
        right = create_node(level + 1, 2 * index + 1)
        return TreeNode(value, left, right)
    
    return create_node(1, 1)

def print_tree(node, level=0, prefix="Root: "):
    """Print the binary tree structure."""
    if node is not None:
        print(" " * (level * 4) + prefix + str(node.value))
        if node.left is not None or node.right is not None:
            if node.left is not None:
                print_tree(node.left, level + 1, "L--- ")
            else:
                print(" " * ((level + 1) * 4) + "L--- None")
            if node.right is not None:
                print_tree(node.right, level + 1, "R--- ")
            else:
                print(" " * ((level + 1) * 4) + "R--- None")

# Example usage
if __name__ == "__main__":
    depth = 15  # Depth of the binary tree
    tree = create_large_binary_tree(depth)
    print("Binary Tree Structure:")
    print_tree(tree)
