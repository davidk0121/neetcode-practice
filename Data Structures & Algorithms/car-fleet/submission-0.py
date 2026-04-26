class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [[p, i] for p, i in zip(position, speed)] # make pairs
        pair.sort(reverse = True) # reverse order
        stack = []

        for p, i in pair: 
            stack.append((target - p) / i)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)



