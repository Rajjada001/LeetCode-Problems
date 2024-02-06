class Solution:
    def groupAnagrams(self, words: List[str]) -> List[List[str]]:
        ga = {}
        for word in words:
            sw = ''.join(sorted(word))
            if sw in ga:
                ga[sw].append(word)
                # print(ga)
            else:
                ga[sw] = [word]
        return ga.values()
