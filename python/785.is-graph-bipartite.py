#
# @lc app=leetcode id=785 lang=python3
#
# [785] Is Graph Bipartite?
#

# @lc code=start
class Solution:
    def isBipartite(self, graph: list[list[int]]) -> bool:
        color: dict[str, list[int]] = {"white": [], "black": []}

        def getColor(node: int) -> str:
            return "white" if node in color["white"] else "black"

        for nodeIndex in range(len(graph)):
            pass

        return True


# @lc code=end
