class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str):
        """插入一个单词到Trie中"""
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word: str) -> bool:
        """查找一个单词是否在Trie中"""
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def starts_with(self, prefix: str) -> bool:
        """检查是否存在以指定前缀开头的单词"""
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

    def autocomplete(self, prefix: str) -> list:
        """根据前缀返回所有可能的自动联想结果"""
        def dfs(node, path, results):
            if node.is_end_of_word:
                results.append(path)
            for char, child_node in node.children.items():
                dfs(child_node, path + char, results)

        node = self.root
        results = []
        for char in prefix:
            if char not in node.children:
                return results
            node = node.children[char]

        dfs(node, prefix, results)
        return results

# 示例用法
trie = Trie()
trie.insert("apple")
trie.insert("app")
trie.insert("application")
trie.insert("bat")
trie.insert("ball")
trie.insert("banana")

print(trie.autocomplete("app"))  # 输出: ['app', 'apple', 'application']
print(trie.autocomplete("ba"))   # 输出: ['bat', 'ball', 'banana']
print(trie.autocomplete("cat"))  # 输出: []

