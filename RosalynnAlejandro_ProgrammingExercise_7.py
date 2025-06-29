# This program will get a paragraph from the user,
# then display the sentences, and
# the total number of sentences.

# Import regular expressions
import re

# Get a paragraph as input and display the sentences,
# and the number of sentences.
def main():
    # Get a paragraph input from the user
    my_paragraph = input("Enter a paragraph: ")

    # Call a function to pass users my_paragraph input
    # to sentence_count()
    sentences = sentence_count(my_paragraph)

    # Display the sentences
    print("Sentences found:")
    for i in sentences:
        print('->', i)

    #Display the total number of sentences found
    print(f'Total sentences found: {len(sentences)}')

# Find the sentences and the number of sentences.
def sentence_count(my_paragraph):
    # Set a pattern to analyze sentences
    sentence_pattern = r'[0-9A-Z].*?[.!?](?= [0-9A-Z]|$)'

    # Find the sentences and return sentences to main()
    sentences = re.findall(sentence_pattern, my_paragraph, flags=re.DOTALL | re.MULTILINE)
    return sentences

# Call the main function
if __name__ == '__main__':
    main()