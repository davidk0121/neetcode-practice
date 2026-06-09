
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxD = 0
        def dfs(cur):
            if not cur: return 0
            left = dfs(cur.left)
            right = dfs(cur.right) 
            self.maxD = max(self.maxD, left + right)
            return 1 + max(left, right)    

        dfs(root)
        return self.maxD
