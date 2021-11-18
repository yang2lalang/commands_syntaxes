#check if a string has balanced brackets
s1 = "(()())()" #Balanced
s2 = "()))" #Unbalanced
s3 = ")(" #Unbalanced

def is_syntax_correct(input_string=""):
    stack = []
    result = False
    for i in range(0,len(input_string)):

        if input_string[i] == "(":
            stack.append(input_string[i])

        if not stack:
            result = False
            return result

        if input_string[i] == ")":
            stack.pop()
    if not stack:
        result = True
    else:
        result = False
        

    return result


print(is_syntax_correct(s1))
print(is_syntax_correct(s2))
print(is_syntax_correct(s3))