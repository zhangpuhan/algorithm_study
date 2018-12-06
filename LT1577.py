class Solution:
    """
    @param root:
    @return: the sum of leafnode
    """

    def sumLeafNode(self, root):
        # Write your code here

        self.result = 0

        if root is None:
            return 0

        self.dfs(root)

        return self.result

    def dfs(self, node):
        if node.left is None and node.right is None:
            self.result += node.val

        if node.left:
            self.dfs(node.left)

        if node.right:
            self.dfs(node.right)