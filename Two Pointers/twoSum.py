class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        a = 0
        b = 0
        f = False

        for i in range(len(numbers)):
            a = i+1 
            for j in range(i+1,len(numbers)):
            
                s = numbers[i] + numbers[j]

                if (s == target):
                    b=j+1
                    f=True 
                    break
                elif( s > target):
                    break
            if (f):
                break
        
        return [a,b]