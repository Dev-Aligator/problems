
class Solution():
    def __init__(self):
        path = input()
        print(self.simplifyPath(path))
    def simplifyPath(self, path:str) -> str:
        sim_path = ""
        dirc = []
        current = ""
        ori_path = list(path)
        while ori_path:
            if ori_path[0] != "/":
                current += ori_path[0]
                ori_path.pop(0)
            else:
                while ori_path and ori_path[0] == "/":
                    ori_path.pop(0)
                if current == "/.":
                    pass
                elif current == "/..":
                    dirc.pop()
                else:
                    dirc.append(current)
                current = "/"
        if current != "/":
            dirc.append(current)
        for di in dirc:
            sim_path += di
        return sim_path if sim_path != "" else "/"
Solution()
            
            

            
