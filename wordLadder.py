from collections import deque
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        wordList = set(wordList)
        if endWord not in wordList:
            return 0

        queue = deque([beginWord])
        distance = {beginWord: 1}

        while queue:
            word = queue.popleft()
            if word == endWord:
                return distance[word]

            for next_word in self.get_next_words(word, wordList):
                if next_word in distance:
                    continue
                queue.append(next_word)
                distance[next_word] = distance[word] + 1

        return 0

    # get_next_words() 遍历所有边
    def get_next_words(self, word, wordList):
        valid_next_words = []
        alpha = 'abcdefghijklmnopqrstuvwxyz'

        for i in range(len(word)):
            left, right = word[:i], word[i + 1:]
            for char in alpha:
                if word[i] == char:
                    continue
                next_word = left + char + right
                if next_word in wordList:
                    valid_next_words.append(next_word)

        return valid_next_words
