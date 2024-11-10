"""
This module provides a function to compare two lines of text
and calculate the word and character-level precision.
"""

def compare_lines(correct_line, user_line):
    """
    Compare lines and return precision metrics.
    """
    correct_words = correct_line.split()
    user_words = user_line.split()
    
    word_matches = sum(1 for c, u in zip(correct_words, user_words) if c == u)
    word_precision = word_matches / len(correct_words)

    char_errors = {}
    correct_chars = 0
    total_chars = sum(len(word) for word in correct_words)

    for c_word, u_word in zip(correct_words, user_words):
        for c_char, u_char in zip(c_word, u_word):
            if c_char == u_char:
                correct_chars += 1
            else:
                char_errors[c_char] = char_errors.get(c_char, 0) + 1
        if len(u_word) > len(c_word):
            for i in u_word[len(c_word):]:
                char_errors[i] = char_errors.get(i, 0) + 1

    char_precision = correct_chars / total_chars if total_chars > 0 else 0
    return word_precision, char_precision, char_errors
