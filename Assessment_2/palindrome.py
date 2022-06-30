def palindrome(word):
    word = str(word)
    if len(word) == 1:
        return True
    for i in range(len(word)//2):
        word = word.lower()
        if word[i] != word[len(word) - 1 - i]:
            return False
        else:
            return True

if __name__=='__main__':
    word = input('Input your word: ')
    print(palindrome(word))