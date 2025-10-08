class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        ans = []  
        for i in range(0, len(s), k):  
            if i + k <= len(s):
                ans.append(s[i:i+k])  
            else:
                string = ""
                while k:
                    if i < len(s):
                        string += s[i]  
                        i += 1
                    else:
                        string += fill  
                    k -= 1
                ans.append(string) 
        return ans
