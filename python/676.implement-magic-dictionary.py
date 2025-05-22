#
# @lc app=leetcode id=676 lang=python3
#
# [676] Implement Magic Dictionary
#

# @lc code=start
from typing import List


class MagicDictionary:
    def __init__(self) -> None:
        self.word_set: set[str] = set()

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            self.word_set.add(word)

    def search(self, searchWord: str) -> bool:
        search_len: int = len(searchWord)

        for word in self.word_set:
            # Get smart and break early
            if searchWord == word:
                continue

            word_len: int = len(word)

            # Words have to be the same length
            if search_len != word_len:
                # Skip to the next word
                # or break out if this is the last word
                continue

            differences: int = 0
            for char_pos in range(word_len):
                if searchWord[char_pos] != word[char_pos]:
                    differences += 1

            # If there is exactly one difference
            # return true
            if differences == 1:
                return True

        return False


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)
# @lc code=end
