class Palindrome:

    @staticmethod
    def is_palindrome(word):
        print "\nIs %s a palindrome?" % word
        word = word.lower()
        palindrome_word = ''
        word_to_pop = [c for c in word]
        i = 0
        while i < len(word):
            palindrome_word += word_to_pop.pop()
            i += 1
        if palindrome_word == word:
            return True
        else:
            return False

while True:
    word = raw_input("\nWhat word would you like to test? ")
    if word == 'q'.lower():
        break
    else:
        print(Palindrome.is_palindrome(word))
