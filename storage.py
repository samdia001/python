"""
this module is responsible for saving and displaying the results of the game
"""
from operator import itemgetter

def save_score(name, word_precision, char_precision, difficulty, filename='data/score.txt'):
    """Save score to file"""
    with open(filename, 'a', encoding='utf-8') as score_file:
        score_file.write(f"{name} {word_precision:.2f} {char_precision:.2f} {difficulty}\n")

def print_results_list():
    """Display high scores grouped by difficulty with single sort"""
    try:
        with open('data/score.txt', 'r', encoding='utf-8') as score_file:
            results = score_file.readlines()

        all_results = []
        difficulty_priority = {'hard': 0, 'medium': 1, 'easy': 2}
        
        for line in results:
            parts = line.strip().split()
            if len(parts) >= 4:
                name = ' '.join(parts[:-3])
                word_precision = float(parts[-3])
                char_precision = float(parts[-2])
                difficulty = parts[-1]
                diff_priority = difficulty_priority[difficulty]
                all_results.append((diff_priority, difficulty, word_precision, 
                                  char_precision, name))

        sorted_results = sorted(all_results, key=itemgetter(0, 2, 3))
        print("\nHigh Scores (Smart people):")
        current_difficulty = None
        count = 1
        
        for _, difficulty, word_prec, char_prec, name in sorted_results:
            if difficulty != current_difficulty:
                current_difficulty = difficulty
                print(f"\n{difficulty.upper()} LEVEL:")
                count = 1
            
            print(f"#{count} {name} {word_prec:.2f} {char_prec:.2f}")
            count += 1

    except FileNotFoundError:
        print("No results found. You did not learn anything!")
