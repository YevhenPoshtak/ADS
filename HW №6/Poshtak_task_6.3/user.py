size = 10007 
table = [None] * size
DELETED = ("DELETED", "DELETED")

def init():
    global table
    table = [None] * size

def _hash(author, title):
    return hash((author, title)) % size

def addBook(author, title):
    global table
    idx = _hash(author, title)
    
    first_deleted = -1
    curr = idx
    
    while table[curr] is not None:
        if table[curr] == (author, title):
            return  
        if table[curr] == DELETED and first_deleted == -1:
            first_deleted = curr
        
        curr = (curr + 1) % size
        if curr == idx: break 

    insert_idx = first_deleted if first_deleted != -1 else curr
    table[insert_idx] = (author, title)

def find(author, title):
    idx = _hash(author, title)
    curr = idx
    
    while table[curr] is not None:
        if table[curr] == (author, title):
            return True
        curr = (curr + 1) % size
        if curr == idx: break
        
    return False

def delete(author, title):
    global table
    idx = _hash(author, title)
    curr = idx
    
    while table[curr] is not None:
        if table[curr] == (author, title):
            table[curr] = DELETED
            return
        curr = (curr + 1) % size
        if curr == idx: break

def findByAuthor(author):
    books = []
    for item in table:
        if item and item != DELETED:
            book_author, book_title = item
            if book_author == author:
                books.append(book_title)
    return sorted(books)