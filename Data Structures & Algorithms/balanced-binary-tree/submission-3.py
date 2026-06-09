class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(cur):
            if not cur: return [True, 0]
            left = dfs(cur.left)
            right = dfs(cur.right)

            balanced = (abs(left[1] - right[1]) <= 1) and left[0] and right[0] 
            return [balanced, 1 + max(left[1], right[1])]
        return dfs(root)[0]