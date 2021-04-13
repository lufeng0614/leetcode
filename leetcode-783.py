class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        rootValList = []
        def reverse(root):
            if root:
                reverse(root.left)
                rootValList.append(root.val)
                reverse(root.right)
        reverse(root)
        return min([rootValList[i+1] - rootValList[i] for i in range(len(rootValList) - 1)])
