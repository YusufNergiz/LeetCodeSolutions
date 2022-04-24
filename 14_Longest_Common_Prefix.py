### Goal is to find as many similar letters as possible in all the given words
### Ex: given_words = ["flower", "flow"< "flight]
### Result = "fl"
### Ex: given_words = ["dog", "racecar"]
### Result = ""
################################################################################
import time
start_time = time.time()

given_words = ["flower", "flow", "flight"]

def find_prefix():
    result = ""
    for i in range(len(given_words[0])):     ### loops through given_words.length times
        for word in given_words:
            if len(word) == i or word[i] != given_words[0][i]:  ### checks if the current word has less letters than the i'th loop
                                                                ### or check if the current words i'th letter is not equal to the
                                                                ### first word of the given_words
                return result
        result += given_words[0][i]
    return result

print(find_prefix())

print("--- %s seconds ---" % (time.time() - start_time))
