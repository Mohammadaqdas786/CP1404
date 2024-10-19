def count_words(text):
    """
    Counts the occurrences of words in a string.

    Args:
    text (str): The input string.

    Returns:
    dict: A dictionary where the keys are the words and the values are the counts.

    Time Estimate: 30 minutes
    """
    # Convert the text to lowercase and split it into words
    words = text.lower().split()

    # Create a dictionary to store the word counts
    word_counts = {}

    # Iterate over each word in the list
    for word in words:
        # Remove punctuation from the word
        word = ''.join( e for e in word if e.isalnum() )

        # Check if the word is already in the dictionary
        if word in word_counts:
            # If it is, increment the count
            word_counts[word] += 1
        else:
            # If it's not, add it to the dictionary with a count of 1
            word_counts[word] = 1

    return word_counts


def print_word_counts(word_counts):
    """
    Prints the word counts in a formatted way.

    Args:
    word_counts (dict): A dictionary where the keys are the words and the values are the counts.
    """
    # Find the longest word in the list
    max_word_length = max( len( word ) for word in word_counts.keys() )

    # Sort the word counts by key
    sorted_word_counts = dict( sorted( word_counts.items() ) )

    # Print the word counts
    for word, count in sorted_word_counts.items():
        print( f"{word:{max_word_length}} : {count}" )


def main():
    # Ask the user for a string
    text = input( "Text: " )

    # Count the occurrences of words in the string
    word_counts = count_words( text )

    # Print the word counts
    print_word_counts( word_counts )


if __name__ == "__main__":
    main()
