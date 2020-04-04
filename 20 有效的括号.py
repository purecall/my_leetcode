class Solution:
    def isValid(self, s: str) -> bool:
        dic = {'{': '}', '[': ']', '(': ')','#':'#'}
        stack = ['#'] # 预留一个元素，否则stack.pop()会失败
        for c in s:
            if c in dic:
                stack.append(c)
            elif dic[stack.pop()] != c: # 在dic中也预留了'#':'#'
                return False
        return len(stack) == 1