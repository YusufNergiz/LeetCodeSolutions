### Goal is to find whether if all the parantheses has a closing pair
### Ex: s = "()"
### Result = True
### Ex: s = "(]"
### Result = False
###########################################################################
s = ")()("

def find_match():
    stack = []
    parantheses_dict = {
        ")": "(",
        "]": "[",
        "}": "{",
    }

    for char in s:
        if char in parantheses_dict:      ## if current char is one of ")", "]", "}".
            # try:
            if stack[-1] == parantheses_dict[char]:  ## if the last char in the stack list == value of current char in dict
                stack.pop()  ## remove the last char from the stack list
            else:    ## if the last char in stack list != value of current char in dict
                return False
            # except IndexError: ## returns False if the stack list is empty when the char == key in dict
            #     return False

        else:
            stack.append(char)  ## if char not a key in dict add it to the stack list

    if len(stack) > 0:
        return False  ## if the stack list is not empty -> means that one of the opening parantheses is left inside without
                    ## a match
    else:
        return True  ## if the stack list is empty -> means that all the opening parantheses have a closing pair

print(find_match())



