def palindrome_partitioner(s: str) -> int:
    pal_cache = {}

    def is_palindrome(sub: str) -> str:
        if sub in pal_cache:
            return pal_cache[sub]
        result = sub == sub[::-1]
        pal_cache[sub] = result
        return result

    def min_cuts(remaining: str) -> int:
        if is_palindrome(remaining):
            return 0
        best = len(remaining) - 1
        for i in range(1, len(remaining)):
            first_piece = remaining[:i]
            if is_palindrome(first_piece):
                rest_cuts = min_cuts(remaining[i:])
                best = min(best, 1 + rest_cuts)
        return best

    if len(s) <= 1:
        return 0
    return min_cuts(s)


print(palindrome_partitioner("abc"))
