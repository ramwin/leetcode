# 执行用时： 132 ms , 在所有 Python3 提交中击败了 65.03% 的用户
# 内存消耗： 27.7 MB , 在所有 Python3 提交中击败了 72.92% 的用户

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.words = {}

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        item = self.words
        for i in range(len(word)):
            if word[i] not in item:
                item[word[i]] = {}
            item = item[word[i]]
        item['exist'] = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        item = self.words
        for i in range(len(word)):
            if word[i] not in item:
                return False
            item = item[word[i]]
        return 'exist' in item

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given
        prefix.
        """

        item = self.words
        for i in range(len(prefix)):
            if prefix[i] not in item:
                return False
            item = item[prefix[i]]
        return True
