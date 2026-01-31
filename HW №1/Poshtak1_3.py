class Task1_3:
    
    def task_a(self, n: int, k: int) -> None:
        k += 1 # k = k + 1 -> 4 
        i = n # 2 
        while i > 0: # 3 * (n + 1)
            i -= 1 # i = i - 1 -> 4 * n
        return None
    # T(n) = 4 + 2 + 3(n+1) + 4n = 7n + 9 
    
    def task_b(self, n: int, k: int) -> None:
        i = n # 2
        while i > 1: # 3 * ([log(n)] + 1)
            k += 1 # k = k + 1 -> 4 * [log(n)]
            i //= 2 # i = i // 2 -> 4 * [log(n)]
        return None
    # T(n) = 2 + 3([log(n)] + 1) + 8 * [log(n)] = 11 * [log(n)] + 5
    
    def task_c(self, n: int, k: int) -> None:
        i = 0 # 2
        while i < n: # 3 * ([n/2] + 1)
            j = 0 # 2 * ([n/2])
            while j < n: # 3 * ([n/2]) * ([n/2] + 1)
                k += 1 # 4 * ([n/2]) * ([n/2])
                j += 2 # 4 * ([n/2]) * ([n/2])
            i += 2 # 4 * ([n/2])
        return None 
    # T(n) = 2 + 3([n/2] + 1) + 2([n/2]) + 3([n/2])([n/2] + 1) + 8([n/2])**2 + 4([n/2]) = 11([n/2])^2 + 12([n/2]) + 5
    
    def task_d(self, n: int, k: int) -> None:
        i = 0 # 2   
        while i < n: # 3 * (n + 1)
            j = 0 # 2 * n
            while j < i * i: # 5 * sum(i^2)  = 5 * (n(n-1)(2n-1)/6 + n) = 5 * (2n^3 - 3n^2 + 7n)/6
                k += 1 # k = k + 1 -> 4 * sum(i^2) = 4 * (n(n-1)(2n-1)/6) = 4 * (2n^3 - 3n^2 + n)/6
                j += 1 # j = j + 1 -> 4 * sum(i^2) = 4 * (n(n-1)(2n-1)/6) = 4 * (2n^3 - 3n^2 + n)/6
            i += 1 # i = i + 1 -> 4 * n
        return None
    # T(n) = 2 + 3(n+1) + 2n + 5 * (2n^3 - 3n^2 + 7n)/6 + 8 * (2n^3 - 3n^2 + n)/6 + 4n = (26n^3 - 39n^2 + 97n + 30)/6
    
    def task_e(self, n: int, k: int) -> None:
        i = 1 # 2
        while i < n: # 3 * ([log(n)] + 1)
            j = 1 # 2 * [log(n)]
            while j < n: # 3 * [log(n)] * ([log(n)] + 1)
                k += 1 # k = k + 1 -> 4 * [log(n)] * [log(n)]
                j *= 2 # j = j * 2 -> 4 * [log(n)] * [log(n)]
            i *= 2 # i = i * 2 -> 4 * [log(n)]
        return None
    # T(n) = 2 + 3([log(n)]+1) + 2[log(n)] + 3[log(n)]([log(n)]+1) + 8[log(n)]^2 + 4 * [log(n)] = 11[log(n)]^2  + 8[log(n)] + 5
    
    def task_f(self, n: int, k: int) -> None:
        i = 1 # 2
        while i < n: # 3 * ([log(n)] + 1)
            j = i # 2 * [log(n)]
            while j < n: # 3 * (([log(n)]([log(n)]+1))/2 + [log(n)])
                k += 1 # k = k + 1 -> 4 * (([log(n)]([log(n)]+1))/2)
                j *= 2 # j = j * 2 -> 4 * (([log(n)]([log(n)]+1))/2)
            i *= 2 # i = i * 2 -> 4 * [log(n)]
        return None
    # T(n) = 2 + 3([log(n)] + 1) + 2 * [log(n)] + 3 * (([log(n)]([log(n)]+1))/2 + [log(n)])) + 8 * (([log(n)]([log(n)]+1))/2) + 4 * [log(n)] = 5.5 * ([log(n)])^2 + 17.5 * [log(n)] + 5