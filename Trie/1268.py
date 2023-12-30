class Solution(object):
    def suggestedProducts(self, products, searchWord):
        class TrieNode:
            def __init__(self):
                self.children = collections.defaultdict(TrieNode)
                self.suggestion = []
            
            def add_suggestion(self, product):
                if len(self.suggestion) < 3:
                    self.suggestion.append(product)

        products.sort()
        root = TrieNode()
        for p in products:
            node = root 
            for char in p:
                node = node.children[char]
                node.add_suggestion(p)
        res, node = [], root
        for char in searchWord:
            node = node.children[char]
            res.append(node.suggestion)
        return res