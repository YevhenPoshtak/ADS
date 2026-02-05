def max_cyclic_shift(n: int)-> int:
    shifts = [bin(n)[2:][i:] + bin(n)[2:][:i] for i in range(len(bin(n)[2:]))]
    return max(int(shift, 2) for shift in shifts)

n = int(input())
print(max_cyclic_shift(n))