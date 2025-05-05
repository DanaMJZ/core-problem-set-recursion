# factorial
def factorial(n):
    if n < 0:
        raise ValueError
    if n == 0:
        return 1
    return n * factorial(n - 1)


# reverse
def reverse(text):
    if len(text) <= 1:
        return text
    return reverse(text[1:]) + text


# bunny
def bunny(count):
    if count == 0:
        return 0
    return 2 + bunny(count - 1)


# is_nested_parens
def is_nested_parens(parens):
    if not parens:
        return True
    return (parens[0] == '(' and 
            parens[-1] == ')' and 
            is_nested_parens(parens[1:-1]))

