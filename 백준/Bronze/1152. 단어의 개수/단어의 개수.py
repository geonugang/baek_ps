# Read the input string from the user
input_string = input()

# Remove leading and trailing spaces
input_string = input_string.strip()

# Split the string into words
words = input_string.split()

# Count the number of words
num_words = len(words)

# Print the result
print(num_words)