from typing import Callable

def caching_fibonacci() -> Callable[[int], int]:
    cache = {}
    
    def fibonacci(n: int) -> dict.keys:
        if n in cache[n]:
            return cache[n]
        else:
            if n <= 0:
                n = 0
            elif n == 1:
                n = 1
            else:
                n = n        

        cache[n] = fibonacci(n-1) + fibonacci(n-2)
        return cache[n]
    
    return fibonacci

fibonacci_result = caching_fibonacci()
print(fibonacci_result)