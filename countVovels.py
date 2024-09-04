def count_vowels(text):

    vowels = 'aeiou'
    return sum(1 for char in text.lower() if char in vowels)

# Example usage
text1 = "Hello World"
text2 = "OpenAI is amazing!"

# Counting the number of vowels in each text
vowel_count1 = count_vowels(text1)
vowel_count2 = count_vowels(text2)

print(f"Number of vowels in '{text1}': {vowel_count1}")  # Output: Number of vowels in 'Hello World': 3
print(f"Number of vowels in '{text2}': {vowel_count2}")  # Output: Number of vowels in 'OpenAI is amazing!