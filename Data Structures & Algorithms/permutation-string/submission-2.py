class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False

        s1Count, s2Count = [0] * 26, [0] * 26

        # count initials
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1

        # match count initials
        matches = 0 
        for i in range(26):
            matches += (1 if s1Count[i] == s2Count[i] else 0)

        # sliding window
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26: return True

            rIndex = ord(s2[r]) - ord('a')
            s2Count[rIndex] += 1
            if s1Count[rIndex] == s2Count[rIndex]:
                matches += 1
            elif s1Count[rIndex] + 1 == s2Count[rIndex]:
                matches -= 1

            lIndex = ord(s2[l]) - ord('a')
            s2Count[lIndex] -= 1
            if s1Count[lIndex] == s2Count[lIndex]:
                matches += 1
            elif s1Count[lIndex] - 1 == s2Count[lIndex]:
                matches -= 1
            l += 1
        return matches == 26