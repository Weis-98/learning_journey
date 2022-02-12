class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {'is_word': False}


    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        direction = self.root
        for i in word:
            if i not in direction:
                direction[i] = {'is_word': False}
                direction = direction[i]
            else:
                direction = direction[i]
        direction['is_word'] = True
        print(direction)




    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        direction = self.root
        for i in word:
            if i not in direction:
                return False
            else:
                direction = direction[i]
        return direction['is_word']


    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        direction = self.root
        for i in prefix:
            if i not in direction:
                return False
            else:
                direction = direction[i]
        return True



# Your Trie object will be instantiated and called as such:
obj = Trie()
obj.insert('apple')
param_2 = obj.search('apple')
param_3 = obj.startsWith('prefix')
param_4 = obj.startsWith('app')
print(param_2, param_3, param_4)