alphabet = " abcdefghijklmnopqrstuvwxyz"
vowel = "aeiou"
message = ""

with open("secret.txt") as f:
    for line in f:
        vowel_count = 0 # We need to count the amount of variables in each line and we reset it after every line.
        for char in line: # We iterate through every character in line.
            if char in vowel: # We do an if statement to check if a character is a vowel.
                vowel_count = vowel_count + 1 # If so it adds one vowel to our counter.
        message += alphabet[vowel_count] # We then to append to message the character which is that index.
        # This must be outside the if statement and second for loop before the counter restarts.

print(f"The secret message is: {message}")