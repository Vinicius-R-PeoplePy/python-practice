def countSetBits(n):

    count = 0
    while n:
        count += (n & 1)   # check last bit
        n >>= 1
        return count

if __name__ == '__main__':

    n = 6

print(f'The total number of set bits in {str(n)} ({bin(n)}) is {countSetBits(n)}')