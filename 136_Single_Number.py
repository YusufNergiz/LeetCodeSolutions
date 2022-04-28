### Goal is to find the single number from the given_list
### ATTENTION! Only one numer has no duplicates..
### Ex: given_list = [1, 4, 5, 6, 4]
### Answer: 4


given_list = [2, 2, 1]
def Solution():
    arr = []
    for i in given_list:
        if i in arr:
            arr.remove(i)             ### Checks if the iterated number is in the list arr, if yes it removes it.
        else:
            arr.append(i)             ### If the number is not in the list arr it adds it to it.
    return arr[0]