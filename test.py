"""
this module represents the tests.
"""

import time
from metrices import calculate_wpm_metrics, calculate_precision
from comparison import compare_lines
from storage import save_score
from categories import get_animal_category


def typing_test(filename):
    """Run typing test and track performance"""
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    stats = {
        'total_words_correct': 0,
        'total_words': 0,
        'total_chars_correct': 0,
        'total_chars': 0,
        'misspelled_chars': {},  
        'user_total_words': 0
    }
    start_time = time.time()

    for i, line in enumerate(lines, 1):
        print(f"\nType this line ({i}/{len(lines)}):\n{line.strip()}")
        user_input = input()

        current_elapsed = time.time() - start_time
        user_words = len(user_input.split())
        stats['user_total_words'] += user_words

        word_prec, char_prec, char_errors = compare_lines(line.strip(), user_input)
        
        stats['total_words_correct'] += word_prec * len(line.split())
        stats['total_words'] += len(line.split())
        stats['total_chars_correct'] += char_prec * sum(len(word) for word in line.split())
        stats['total_chars'] += sum(len(word) for word in line.split())
        
        for char, count in char_errors.items():
            if char not in stats['misspelled_chars']:
                stats['misspelled_chars'][char] = 0
            stats['misspelled_chars'][char] += count

        word_precision = calculate_precision(stats['total_words_correct'], stats['total_words'])
        char_precision = calculate_precision(stats['total_chars_correct'], stats['total_chars'])
        
        print_performance_stats(stats, word_precision, char_precision, current_elapsed)

    final_time = time.time() - start_time
    incorrect_words = stats['user_total_words'] - stats['total_words_correct']
    _, net_wpm, _ = calculate_wpm_metrics(stats['user_total_words'], incorrect_words, final_time)
    
    animal = get_animal_category(net_wpm)
    print(f"\nFinal time (test time): {final_time:.2f} seconds")
    print(f"Your typing speed category is: {animal}")

    name = input("Enter a username: ")

    difficulty = filename.split('/')[-1].split('.')[0].lower()
    save_score(name, word_precision, char_precision, difficulty)

def print_performance_stats(stats, word_precision, char_precision, elapsed_time):
    """Print current performance statistics"""
    incorrect_words = stats['user_total_words'] - stats['total_words_correct']
    gross_wpm, net_wpm, accuracy = calculate_wpm_metrics(
        stats['user_total_words'], incorrect_words, elapsed_time
    )
    
    print(f"\nWord precision: {word_precision:.2f}% # {int(stats['total_words_correct'])}/{stats['total_words']}")
    print(f"Character precision: {char_precision:.2f}% # {int(stats['total_chars_correct'])}/{stats['total_chars']}")
    print(f"Gross WPM: {gross_wpm:.2f}")
    print(f"Net WPM: {net_wpm:.2f}")
    print(f"Accuracy: {accuracy:.2f}%")
    print("Misspelled characters:")
    for char, count in sorted(stats['misspelled_chars'].items(), key=lambda x: (-x[1], x[0])):
        print(f"   {char}: {count}")
    print("=========================")

def timed_character_test():
    """Run a timed character typing test"""
    try:
        seconds = int(input("Enter test duration in seconds: "))
        if seconds <= 0:
            print("Duration must be positive")
            return
            
        # Predefined sequence of characters to type
        test_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.'
        char_index = 0
        errors = {}  
        total_chars = 0
        correct_chars = 0
        
        start_time = time.time()
        end_time = start_time + seconds
        
        while time.time() < end_time:
            target_char = test_chars[char_index % len(test_chars)]
            print(f"\nType this character: {target_char}")
            
            remaining_time = end_time - time.time()
            if remaining_time <= 0:
                break
                
            user_input = input()
            total_chars += 1
            
            if user_input != target_char:
                if target_char not in errors:
                    errors[target_char] = 0
                errors[target_char] += 1
            else:
                correct_chars += 1
                
            char_index += 1
                
        elapsed_time = time.time() - start_time
        minutes = elapsed_time / 60
        
        chars_per_minute = total_chars / minutes if minutes > 0 else 0
        error_percentage = (sum(errors.values()) / total_chars * 100) if total_chars > 0 else 0
        
        print("\nTest completed. You won")
        print(f"Characters per minute: {chars_per_minute:.2f}")
        print(f"Error percentage: {error_percentage:.2f}%")
        print("\nCharacter errors (sorted by frequency):")
        
        for char, count in sorted(errors.items(), key=lambda x: (-x[1], x[0])):
            print(f"'{char}': {count} errors")
            
    except ValueError:
        print("Please enter a valid number of seconds")
        