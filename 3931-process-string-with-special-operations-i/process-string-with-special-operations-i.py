class Solution(object):
    def processStr(self, s):
        result=[]
        for ch in s:
            if ch.islower():
                result.append(ch)
            if ch=='*':
                if result:
                    result.pop()
            if ch=='#':
                result=result+result
            if ch=="%":
                result.reverse()

        return ''.join(result)
        