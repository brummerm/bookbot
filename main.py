from pickle import APPEND



def count_characters():
    # Initialize an empty dictionary to store character counts
    char_count = {chr(i): 0 for i in range(97, 123)}
    wordCount = 0

        # Open and read the file
    with open("books/frankenstein.txt", encoding='utf-8') as file:
            # Read the entire file and convert to lowercase
        text = file.read().lower()
        
        words = [word for word in text.split() if word]
        wordCount = len(words) 
            # Count each character
        for char in text:
            if char in char_count:  # Only count a-z characters
                char_count[char] += 1

    sorted_counts = dict(sorted(char_count.items(), key=lambda x: x[1], reverse=True))

        # Print the report
    print("--- Begin report of books/frankenstein.txt ---")
    
    print(f"{wordCount} words found in the document")
        
        # Print counts for all alphabet characters
    for char, char_count in sorted_counts.items():
        print(f"The '{char}' character was found {char_count} times")
            
    print("--- End report ---")    
    




count_characters()
