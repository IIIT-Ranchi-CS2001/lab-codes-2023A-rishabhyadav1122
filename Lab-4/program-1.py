str  = input("Enter the sentence : ")

words  = str.lower().split()

count = sum(word == word[::-1] for word in words)

print(f"The number of palindrome words in sentence is {count}")