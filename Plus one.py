class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        strings = "".join(map(str,digits))
        summation = str(int(strings) + 1)
        return [int(ch) for ch in summation]

        
