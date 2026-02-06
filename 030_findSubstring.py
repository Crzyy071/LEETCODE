class Solution(object):
    def findSubstring(self, s, words):
        if not s or not words:
            return []

        from collections import Counter

        w = len(words[0])
        k = len(words)
        total = w * k
        n = len(s)

        need = Counter(words)
        res = []

        for i in range(w):
            left = i
            count = 0
            window = {}

            for j in range(i, n - w + 1, w):
                word = s[j:j + w]
                if word in need:
                    window[word] = window.get(word, 0) + 1
                    count += 1

                    while window[word] > need[word]:
                        left_word = s[left:left + w]
                        window[left_word] -= 1
                        left += w
                        count -= 1

                    if count == k:
                        res.append(left)
                else:
                    window.clear()
                    count = 0
                    left = j + w

        return res
        
        