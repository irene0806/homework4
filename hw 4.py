import requests
import string

url1 = "https://www.gutenberg.org/cache/epub/70832/pg70832.txt"
url2 = "https://www.gutenberg.org/cache/epub/70831/pg70831.txt"
book1 = requests.get(url1)
book2 = requests.get(url2)
book1=book1.text
book2=book2.text

words1 = book1.lower().split()
words1= [word.strip(string.punctuation) for word in words1]
words2 = book2.lower().split()
words2=[word.strip(string.punctuation) for word in words2]

unique1 = len(set(words1))
unique2 = len(set(words2))

print("The number of unique words in URL 1 is:", unique1)
print("The number of unique words in URL 2 is:", unique2)

# Calculate the ratio of unique words to total words in each book
total1 = len(words1)
total2 = len(words2)
unique_ratio1 = unique1/total1
unique_ratio2 = unique2/total2

print("The ratio of unique to total words in URL 1 is:", unique_ratio1)
print("The ratio of unique to total words in URL 2 is:", unique_ratio2)

if unique1 > unique2:
    print("Book 1 has more unique words.")
elif unique2 > unique1:
    print("Book 2 has more unique words.")
else:
    print("The two books have the same number of unique words.")

if unique_ratio1 > unique_ratio2:
    print("Book 1 has a higher ratio of unique to total words.")
elif unique_ratio2 > unique_ratio1:
    print("Book 2 has a higher ratio of unique to total words.")
else:
    print("The two books have the same ratio of unique to total words.")