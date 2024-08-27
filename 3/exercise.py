# Node class to define the structure of a tree node
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Function to create the tree structure
def create_tree():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    return root

# Function template for pre-order traversal
def pre_order_traversal(node, result):
    if node:
        # Step 1: Visit the root (Hint: Add the root's value to the result list)
        # Step 2: Traverse the left subtree
        # Step 3: Traverse the right subtree
    return result

# Function template for in-order traversal
def in_order_traversal(node, result):
    if node:
        # Step 1: Traverse the left subtree
        # Step 2: Visit the root (Hint: Add the root's value to the result list)
        # Step 3: Traverse the right subtree
    return result

# Function template for post-order traversal
def post_order_traversal(node, result):
    if node:
        # Step 1: Traverse the left subtree
        # Step 2: Traverse the right subtree
        # Step 3: Visit the root (Hint: Add the root's value to the result list)
    return result

# Function to run and test the traversal methods
def test_traversals():
    root = create_tree()
    pre_order_result = pre_order_traversal(root, [])
    in_order_result = in_order_traversal(root, [])
    post_order_result = post_order_traversal(root, [])

    print("Pre-order Traversal:", pre_order_result)  # Expected Output: [1, 2, 4, 5, 3]
    print("In-order Traversal:", in_order_result)    # Expected Output: [4, 2, 5, 1, 3]
    print("Post-order Traversal:", post_order_result) # Expected Output: [4, 5, 2, 3, 1]

test_traversals()
