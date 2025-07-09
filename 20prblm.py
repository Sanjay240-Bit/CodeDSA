def isValid(s):
    hashmap = {')': '(', '}': '{', ']': '['}
    stack = []

    for c in s:
        if c not in hashmap:
            stack.append(c)
        else:
            if not stack:
                return False
            else:
                popped = stack.pop()
                if popped != hashmap[c]:
                    return False
    return not stack


s = input("Enter the parenthesis: ")

if isValid(s):
    print("The parenthesis is Valid.")
else:
    print("The parenthesis is not valid.")
