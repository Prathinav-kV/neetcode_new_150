class Solution:
    def search(self, nums: list[int], target: int) -> int:
        start = 0
        end = len(nums)-1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        return -1


def main():
    nums = [1, 2, 3, 4, 5]
    target = 3
    solution = Solution()
    result = solution.search(nums, target)
    print(result)

if __name__ == "__main__":
    main()
