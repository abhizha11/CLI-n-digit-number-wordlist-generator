import os

def generate_number_wordlist(n):
    numbers = [str(i) for i in range(10)]
    wordlist = []
    generate_wordlist_helper("", n, numbers, wordlist)
    return wordlist

def generate_wordlist_helper(prefix, n, numbers, wordlist):
    if n == 0:
        wordlist.append(prefix)
        return
    for num in numbers:
        generate_wordlist_helper(prefix + num, n - 1, numbers, wordlist)


# Display banner
banner = """
===============================================
   CLI-N-Digit Number Wordlist Generator
		BY @abhizha11 (Sagar Jha)
================================================
"""

print(banner)


# Prompt user for input
n = input("Enter the number of digits: ")
if not n.isdigit():
    print("Invalid input for the number of digits. Please enter a positive integer.")
    exit()

filename = input("Enter the file name to save the wordlist: ")
if filename == "":
    print("Invalid input for the file name. Please enter a valid file name.")
    exit()

# Prompt user for file location
file_location = input("Enter the file location (leave blank for current directory): ")
if file_location == "":
    file_location = os.getcwd()  # Get current working directory

# Generate the wordlist
n = int(n)
wordlist = generate_number_wordlist(n)

# Save the wordlist to the file
file_path = os.path.join(file_location, filename)
with open(file_path, "w") as file:
    for word in wordlist:
        file.write(word + "\n")

print("Wordlist saved to", file_path)
