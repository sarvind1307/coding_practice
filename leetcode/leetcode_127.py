'''
127. Word Ladder

A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

Every adjacent pair of words differs by a single letter.
Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.
'''


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wset = set(wordList)
        q = collections.deque()
        q.append((beginWord, 1))
        wl = len(beginWord)
        
        while q:
            w,s = q.popleft()
            if endWord == w:
                return s
            
            for i in range(wl):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    nw = w[:i] + c + w[i+1:]
                    if nw in wset:
                        wset.remove(nw)
                        q.append((nw, s+ 1))
                # print(q)
        return 0