''' Write a Python program to count the occurrences of each word in a given sentence. '''

def count_word_occurrences(sentence):
    """
    Function to count the occurrences of each word in a given sentence.

    Args:
    sentence (str): The input sentence.

    Returns:
    dict: A dictionary where keys are unique words in the sentence and values are their occurrences.
    """
    # Split the sentence into words
    words = sentence.split()
    # Initialize an empty dictionary to store word occurrences
    word_count = {}
    # Count occurrences of each word
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count

# Sample sentence
sample_sentence = "Write a Python program to count the occurrences of each word in a given sentence"
# Count word occurrences
occurrences = count_word_occurrences(sample_sentence)
print("Occurrences of each word:", occurrences)
