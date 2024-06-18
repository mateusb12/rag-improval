import nltk
from sklearn.model_selection import train_test_split


def tokenize_text(text):
    """
    Tokenizes a string of text.

    Parameters:
    text (str): The text to tokenize.

    Returns:
    list: A list of tokens.
    """
    return nltk.word_tokenize(text)


def split_data(data, labels, test_size=0.2, random_state=42):
    """
    Splits the data into training and validation sets.

    Parameters:
    data (array-like): The data to split.
    labels (array-like): The labels to split.
    test_size (float): The proportion of the dataset to include in the test split.
    random_state (int): The seed used by the random number generator.

    Returns:
    tuple: The training data, the validation data, the training labels, and the validation labels.
    """
    return train_test_split(data, labels, test_size=test_size, random_state=random_state)


def main():
    # Load your data here
    # For example:
    # with open('datasets/narrativeQA/documents.csv', 'r') as f:
    #     data = f.read()

    # Tokenize the data
    tokens = tokenize_text(data)

    # Split the data into training and validation sets
    train_data, val_data, train_labels, val_labels = split_data(tokens, labels)

    # Continue with your code...


if __name__ == "__main__":
    main()
