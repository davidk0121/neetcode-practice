class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(cur):
            if not cur: return None
            temp = cur.left
            cur.left = dfs(cur.right)
            cur.right = dfs(temp)

            return cur
        return dfs(root)