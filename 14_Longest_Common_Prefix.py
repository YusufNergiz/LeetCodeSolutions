given_words = ["flower", "flow", "flight"]

def find_prefix():
    result = ""
    for i in range(len(given_words[0])):
        for word in given_words:
            if len(word) == i or word[i] != given_words[0][i]:
                return result
        result += given_words[0][i]
    return result

print(find_prefix())