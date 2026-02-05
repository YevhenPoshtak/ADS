class Task2_14:

    def task_a(self, n: int) -> int:
        sum = 0  # O(1)
        for i in range(n+1): # O(n)  
                sum += i # O(1)    
        return sum  # O(1)
    # time complexity: O(n)

    def task_b(self, n: int) -> int:
        sum = 0 # O(1)
        for i in range(n+1): # O(n)
                sum += i * i # O(1)
        return sum # O(1)
    # time complexity: O(n)

    def task_c(self, n: int, a: float) -> float:
        sum = 1.0 # O(1)
        pow = 1.0 # O(1)
        for i in range(n+1): # O(n)
            if i == 0: # O(1)
                continue # O(1)
            pow *= a # O(1)
            sum += pow # O(1)
        return sum # O(1)
    # time complexity: O(n)

    def task_d(self, n: int) -> float:
        sum = 0.0 # O(1)
        for i in range(n+1): # O(n)
            if i == 0: # O(1)
                sum += 1.0 # O(1)
                continue # O(1)
            result = 1.0 # O(1)
            for j in range(i): # O(i)
                result *= i # O(1)
            sum += result # O(1)
        return sum # O(1)
    # time complexity: O(n^2)

    def task_e(self, n: int) -> float:
        product = 1.0 # O(1)
        for i in range(1, n + 1): # O(n)
            product *= 1/(1+i) # O(1)
        return product # O(1)
    # time complexity: O(n)

    def task_f(self, n: int) -> float:
        product = 1.0 # O(1)
        factorial = 1 # O(1)
        for i in range(1, n + 1):  # O(n)
            factorial *= i  # O(1)
            product *= 1/(1 + factorial) # O(1)
        return product # O(1)
    # time complexity: O(n)

    def task_g(self, n: int, a: float) -> float:
        product = 1.0 # O(1)
        factorial = 1 # O(1)
        exponent = 1.0 # O(1)   
        for i in range(1, n + 1): # O(n)
            factorial *= i # O(1)
            exponent *= a # O(1)
            product *= exponent/(1 + factorial) # O(1)
        return product # O(1)
    # time complexity: O(n)

    def task_h(self, n: int, m: int) -> float:
        product = 1.0 # O(1)
        for i in range(1, n + 1): # O(n)
            exponent = 1.0 # O(1)
            for j in range(m): # O(m) 
                exponent *= i # O(1)
            product *= 1 / (1 + exponent) # O(1)
        return product # O(1)
    # time complexity: O(nm)

    def task_i(self, n: int) -> float:
        product = 1.0 # O(1)
        for i in range(1, n + 1): # O(n)
            exponent = 1.0 # O(1)
            for j in range(i): # O(i)
                exponent *= i # O(1)
            product *= 1 / (1 + exponent) # O(1)
        return product # O(1)
    # time complexity: O(n^2)