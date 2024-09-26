# Problem Set 1: Indexing and Slicing Strings
# Basic Indexing:
# Given the string magic = 'abracadabra',
# a. Retrieve the 5th character.
# b. Retrieve the second to last character.
# c. Find the first occurrence of the letter 'c'.
sentence= "abracadabra"
print(sentence[5])
print(sentence[:-2])
print(sentence.find("c"))

# Advanced Slicing:
# Given the string alphabet = 'abcdefghijklmnopqrstuvwxyz',
# a. Extract the letters 'hij'.
text = "abcdefghijklmnopqrstuvwxyz"
substring = text.find("hij")
print(text[7:10])

# b. Extract every second letter starting from 'a' to 'm'.
text = "abcdefghijklmnopqrstuvwxyz"
print(text[0:14:2])
# c. Reverse the entire string using slicing.
text = "abcdefghijklmnopqrstuvwxyz"
print(text[::-1]) 

# Problem Set 2: Extracting Information
# From Descriptions:
# Extract the name of the famous personality from the quote "Ask not what your country can do for you — ask what you can do for your country. - John F. Kennedy"
text2="Ask not what your country can do for you — ask what you can do for your country. - John F. Kennedy"
print(text  )


# Manipulating Words:
# Given the string info = "Python is fun. Fun is good. Good is subjective.",
# a. Extract the word 'subjective' without knowing its exact position.
# b. Extract every third word.
# c. Reverse the positions of the words, but keep the characters in each word in the same order.
text3 =  "Python is fun. Fun is good. Good is subjective."
substring = text.find("subjective")


# Problem Set 3: String Methods
# Upper & Lower:
# Convert the following text to lowercase: "MAY THE FORCE BE WITH YOU."
sentence = "SIMPLE IS ALWAYS BETTER THAN COMPLEX"
print(sentence.lower())

# String Joining and Splitting:
# Given the list motto = ["Make", "haste", "slowly."],
# a. Convert the list into a single string.
word_list = ["Make", "haste", "slowly."]
joined_list = " ".join(word_list)
# b. Now, split the string at every occurrence of the letter 'a'.

# Replacing Words:
# Modify the sentence: "Life is what happens when you are busy making other plans."
# a. Replace "busy" with "distracted".
sentence2 = "Life is what happens when you are busy making other plans."
new_sentence = sentence2.replace("busy","distracted")
print(new_sentence) 
# b. Replace "plans" with "mistakes".
new_sentence = sentence2.replace("plans","mistakes")
print(new_sentence)

# Problem Set 4: String Properties and Advanced Operations
# Repetition:
# Concatenate the word "Iteration" 7 times.
iteration = "iteration" * 7
print(iteration)

# Word Search:
# Check if the word "moonlight" appears in the quote: "With freedom, books, flowers, and the moon, who could not be happy? - Oscar Wilde"
sentence4 = "With freedom, books, flowers, and the moon, who could not be happy? - Oscar Wilde"
print(sentence.find("moonlight"))

# Length and Count:
# a. Calculate the number of characters (including spaces and punctuation) in the word/phrase: "Supercalifragilisticexpialidocious".
phrase = "Supercalifragilisticexpialidocious"
print(len(phrase))
# b. Count the number of times the letter 'i' appears in the same word/phrase.
s = "Supercalifragilisticexpialidocious"
c= s.count("i")
print(c)
