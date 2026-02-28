import sys

class Counter:
    def __init__(self, iterable: list[str]) -> None:
        self.capacity = 100003
        self.table = [[] for _ in range(self.capacity)]
        if iterable:
            for item in iterable:
                self.add(item)

    def _hash(self, key: str) -> int:
        h = 0
        for char in str(key):
            h = (h * 31 + ord(char)) % self.capacity
        return h
    
    def add(self, item: str) -> None:
        index = self._hash(item)
        for i, pair in enumerate(self.table[index]):
            if pair[0] == item:
                self.table[index][i] = (item, pair[1] + 1)
                return
        self.table[index].append((item, 1))

    def keys(self) -> list:
        result = []
        for bucket in self.table:
            for k, v in bucket:
                result.append(k)
        return result

    def get(self, key: str) -> int:
        index = self._hash(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        return 0

class Solution:
    def __init__(self, vocab_list: list[str], text_lines_list: list[str]) -> None:
        self.vocab_list = vocab_list
        self.text_lines_list = text_lines_list

    def check_text(self) -> str:
        vocab = [word.lower() for word in self.vocab_list]

        text = ' '.join(self.text_lines_list).lower()
        clean_text = ''.join(c if c.isalpha() else ' ' for c in text)
        words_in_text = clean_text.split()

        text_counter = Counter(words_in_text)

        if any(word not in vocab for word in text_counter.keys()):
            return "Some words from the text are unknown."
        
        if any(text_counter.get(word) == 0 for word in vocab):
            return "The usage of the vocabulary is not perfect."
        
        return "Everything is going to be OK."

if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().split())
    vocab = [sys.stdin.readline().strip() for _ in range(n)]
    text_lines = [sys.stdin.readline().strip() for _ in range(m)]
    print(Solution(vocab, text_lines).check_text())
