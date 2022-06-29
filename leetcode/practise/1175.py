class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        def isPrime(n: int):
            if n <= 1:
                return False
            for i in range(2, n // 2 + 1):
                if n % i == 0:
                    return False
            return True

        primes_count = 0
        for i in range(1, n + 1):
            if isPrime(i):
                primes_count += 1

        odds_count = n - primes_count
        ans = 1
        for i in range(1, primes_count + 1):
            ans *= i

        for i in range(1, odds_count + 1):
            ans *= i
        return ans % (10**9 + 7)

def test1(n):
    s = Solution()
    return s.numPrimeArrangements(n)


if __name__ == "__main__":
    test_points = [5, 100]
    for test_point in test_points:
        print(test1(test_point))