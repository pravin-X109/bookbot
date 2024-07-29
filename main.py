def main():
    # Open and read the contents of books/frankenstein.txt
    with open('books/frankenstein.txt', 'r') as file:
        content = file.read()
    
    # Count the number of words in the content
    word_count = count_words(content)
    
    # Count the number of times each character appears in the content
    character_count = count_characters(content)
    
    # Print the report
    print_report(word_count, character_count)

def count_words(text):
    # Split the text into words
    words = text.split()
    
    # Return the number of words
    return len(words)

def count_characters(text):
    # Convert text to lowercase
    text = text.lower()
    
    # Initialize an empty dictionary to store character counts
    char_count = {}
    
    # Iterate over each character in the text
    for char in text:
        # If the character is not in the dictionary, add it with count 1
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
            
    return char_count

def print_report(word_count, character_count):
    # Print the beginning of the report
    print(f"--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document\n")
    
    # Convert character_count dictionary to a list of dictionaries and sort it
    sorted_char_count = sorted(character_count.items(), key=lambda item: item[1], reverse=True)
    
    # Print the sorted character counts
    for char, count in sorted_char_count:
        print(f"The '{char}' character was found {count} times")
    
    # Print the end of the report
    print("--- End report ---")

if __name__ == "__main__":
    main()
