class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = []
        sub_group = list(map(lambda x: sorted(list(x)), strs))
        while len(strs) > 0:
            l = []
            s = sub_group.pop(0)
            st = strs.pop(0)
            l.append(st)
            i = 1
            while i >= 0:
                try:
                    i = sub_group.index(s)
                except ValueError:
                    i = -1
                if i >= 0:
                    st = strs.pop(i)
                    l.append(st)
                    sub_group.pop(i)
            anagram.append(l)
        return anagram