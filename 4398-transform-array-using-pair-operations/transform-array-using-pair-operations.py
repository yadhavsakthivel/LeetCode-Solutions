class Solution(object):
    def canTransform(self, source, target):
        if sum(source)==sum(target):
            return True
        else:
            return False
        