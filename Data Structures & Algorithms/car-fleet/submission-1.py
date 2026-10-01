class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        d = {}
        for i in range(len(position)):
            d[position[i]] = speed[i]
        
        # sorted dictionary at this point
        cars = sorted(d.items(), reverse=True)
        stack = []
        for car in cars:
            time = (target-car[0]) / car[1]
            if not stack or time > stack[-1]:
                stack.append(time)
        return len(stack)

            