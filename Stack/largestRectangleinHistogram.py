from typing import List


class Solution1:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        max_area = 0
        
        for i in range(len(heights)):
            shortest = heights[i]
            area = heights[i]
            for j in range(i+1,len(heights)):
                if shortest > heights[j]:
                    shortest = heights[j]
                area = max(area,((j-i+1)*shortest))
            max_area = max(max_area,area)
        
        return max_area

class Solution2:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        list = []
        for i in range(len(heights)):
            while list and heights[i] < heights[list[-1]]:
                h = heights[list.pop()]
                left = list[-1] if list else -1
                w = i - left - 1
                max_area = max(max_area, w * h)
            list.append(i)
        
        while list:
            h = heights[list.pop()]
            left = list[-1] if list else -1
            w = len(heights) - left - 1
            max_area = max(max_area,h*w)
        
        return max_area

def main():
    heights = [2,1,5,6,2,3]
    result1 = Solution1().largestRectangleArea(heights)
    result2 = Solution2().largestRectangleArea(heights)
    print(f"Solution1:{result1}")
    print(f"Solution2:{result2}")

if __name__ == "__main__":
    main()
