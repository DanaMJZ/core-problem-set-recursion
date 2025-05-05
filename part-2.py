# search
def search(array, query):
    if not array:
        return False
    if array[0] == query:
        return True
    return search(array[1:], query)


# is_palindrome
def is_palindrome(text):
    if len(text) <= 1:
        return True
    if text[0] != text[-1]:
        return False
    return is_palindrome(text[1:-1])


# digit_match
def digit_match(apples, oranges):
    def helper(a, o):
        if a == 0 or o == 0:
            return 0
        match = 1 if a % 10 == o % 10 else 0
        return match + helper(a // 10, o // 10)

    if apples == 0 and oranges == 0:
        return 1  
    return helper(apples, oranges)


