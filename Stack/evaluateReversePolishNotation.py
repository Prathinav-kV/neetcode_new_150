class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        l = []

        for i in tokens:
            
            if i == "+":
                left = int(l.pop())
                right = int(l.pop()) 
                l.append( left + right )
            elif i == "-":
                left = int(l.pop())
                right = int(l.pop())
                l.append(right - left)
            elif i == "*":
                left = int(l.pop())
                right = int(l.pop()) 
                l.append( left * right )
            elif i == "/":
                left = int(l.pop())
                right = int(l.pop())
                l.append(int(right / left))
            else:
                l.append(int(i))
        
        return l[-1]
