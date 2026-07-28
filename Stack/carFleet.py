from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        stack = []

        drivers = [[p,s] for p,s in zip(position , speed)]
        drivers = sorted(drivers, reverse = True)

        for p,s in drivers:

            time = (target - p)/s
            stack.append(time)

            if len(stack) >= 2 and time <= stack[-2]:
                stack.pop()
        
        return len(stack)
    
def main():
    target = 12
    position = [10,8,0,5,3]
    speed = [2,4,1,1,3]
    solution = Solution().carFleet(target, position, speed)
    print(solution)

if __name__ == "__main__":
    main()
