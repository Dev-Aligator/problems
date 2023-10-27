class Solution:
    def sumGame(self, num:str) -> bool:
        n = len(num) // 2

        num_list = [ 9 if ch == "?" else 2 * int(ch) for ch in num]

        return sum(num_list[:n]) != sum(num_list[n:])

print(Solution().sumGame("?0?91172275656701?361205452?62??99?9??4478?7967373994600735??4?079246???5827572?81087461?089"))

            
            
