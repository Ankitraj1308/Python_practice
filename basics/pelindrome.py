word = "Radar"

clean_word = word.lower()
reversed_word = clean_word[::-1]

is_palindrome = clean_word == reversed_word

print(is_palindrome) 
