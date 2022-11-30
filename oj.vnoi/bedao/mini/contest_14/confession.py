


class Solution():
    def __init__(self):
        t = int(input())
        test_case = []
        for i in range(t):
            n, k = input().split()
            s = input()
            test_case.append([int(n), int(k), s])
        self.decode(t, test_case) 
    def check(self, mid:str):
        m = int(len(mid)/2)
        count = len(mid) - 1
        for i in range(m):
            if mid[i] != mid[count]:
                return False
            count-=1
        return True
            
    def decode(self, t, test_case:list):
        for T in range(t):
            current = test_case[T]
            s = list(current[2])
            flag = 1
            for i in range(current[1]):
                if s[i] != current[2][-1-i]:
                    if i == current[1] - 1:
                        flag = 0
                        break
                    for j in range(i+1, current[1]):
                        if s[j] == current[2][-i-1]:
                            temp = s[i]
                            s[i] = s[j]
                            s[j] = temp 

                            break 
                        if j == current[1] - 1:
                            flag = 0
                            break
            if flag == 0:
                print("No")
                continue
                
            if self.check(current[2][current[1]:-current[1]]):
                print("Yes")
                print("".join(s))

                
                
                
                    

Solution()
