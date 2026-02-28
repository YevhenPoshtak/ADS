import sys
class Counter:
    def __init__(self, iterable: list[str]) -> None:
        self.table = {}
        if iterable:
            for item in iterable:
                self.add(item)
    
    def add(self, item: str) -> None:
        if item in self.table:
            self.table[item] += 1
        else:
            self.table[item] = 1

    def get(self, key: str) -> int:
        return self.table[key] if key in self.table else 0

    def keys(self) -> list:
        result = []
        for key in self.table:  
            result.append(key)
        return result

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