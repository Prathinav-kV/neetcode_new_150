from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []  # pair: [temp, index]

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                res[stackInd] = i - stackInd
            stack.append((t, i))
        return res
    
def main():
    # temperatures = [73,74,75,71,69,72,76,73]
    temperatures = [30,38,30,36,35,40,28]
    result = Solution().dailyTemperatures(temperatures)
    print(result)

if __name__ == "__main__":
    main()
