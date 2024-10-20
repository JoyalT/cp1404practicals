def count_word_occurrences(text):
    """Count the occurrences of each word in the given text."""
    word_counts = {}
    words = text.lower().split()
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1
    return word_counts

def display_word_counts(word_counts):
    """Display word counts in a sorted and aligned format."""
    max_word_length = max(len(word) for word in word_counts)
    for word in sorted(word_counts):
        print(f"{word:{max_word_length}} : {word_counts[word]}")

def main():
    text = input("Text: ")
    word_counts = count_word_occurrences(text)
    display_word_counts(word_counts)

if __name__ == "__main__":
    main()