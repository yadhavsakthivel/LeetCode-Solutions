class Solution(object):
    def minQueenMoves(self, source, target):
        sr, sc=source
        tr, tc=target

        if sr==tr and sc==tc:
            return 0
        if sr==tr:
            return 1
        if sc==tc:
            return 1

        if abs(sr-tr)==abs(sc-tc):
            return 1

        return 2