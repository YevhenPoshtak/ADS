SIZE = 10007
table = []

def init():
    global table
    table = [[] for _ in range(SIZE)]

def _hash(author, title):
    return hash((author, title)) % SIZE

def addBook(author, title):
    idx = _hash(author, title)
    for a, t in table[idx]:
        if a == author and t == title:
            return
    table[idx].append((author, title))

def find(author, title):
    idx = _hash(author, title)
    for a, t in table[idx]:
        if a == author and t == title:
            return True
    return False

def delete(author, title):
    idx = _hash(author, title)
    chain = table[idx]
    for i in range(len(chain)):
        if chain[i][0] == author and chain[i][1] == title:
            chain.pop(i)
            return

def findByAuthor(author):
    result = []
    for bucket in table:
        for a, t in bucket:
            if a == author:
                result.append(t)
    return sorted(result)