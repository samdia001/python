
# Kmom10 - Typing Test Project
* Samah Diab, sadi24
* Date Started: 2024-10-20
* Date Completed: 2024-10-31

## Requirements 1-3
This project is a typing test program developed in Python, meeting specified functional requirements as follows:

### Key Functions and Structure
The code is structured around several key functions in functions.py that handle different aspects of the typing test. The main function, typing_test(), serves as the primary test runner, reading lines from a specified difficulty file and processing user input in real-time.

* Accuracy Calculations: The compare_lines() function calculates both word-level and character-level accuracy, allowing for detailed precision measurements.
* Real-Time Statistics Tracking: I implemented real-time statistics tracking using a dictionary that keeps running totals of correct words, characters, and errors.

### Performance Tracking and Statistics
Performance tracking is handled by calculate_precision() and print_performance_stats():

* Precision and Typing Speed (WPM): The functions calculate and display word precision, character precision, and typing speed (WPM).
* Character Error Tracking: Using a defaultdict, character errors are counted and sorted by frequency for a detailed report.

### High Scores Management
High scores are managed through:

* Saving Scores: The save_score() function saves scores to a score.txt file, storing details like name, word precision, character precision, and difficulty level.
* Displaying Scores: The print_results_list() function groups and displays high scores by difficulty (hard, medium, easy) and sorts them by accuracy. This was achieved with a single sorting operation using itemgetter, ensuring efficiency.


### Code Organization and Readability
The code is organized into well-defined functions, each with a single responsibility, making the code easy to read and maintain. Functions are modular and self-contained, with a clear division of responsibilities.

## Requirement 4 - Timing Function
The timing function is implemented using Python’s time module:

* Timing Logic: Start and end times are captured within the typing_test() function, with elapsed time calculated throughout the test.
* Minute Calculation: The calculate_minutes() function rounds up minutes as specified (rounding up after 30 seconds, minimum of 1 minute).
* WPM Metrics: calculate_wpm_metrics() calculates:
* Gross WPM: Total words typed per minute
* Net WPM: Gross WPM minus errors per minute
* Accuracy: (Net WPM / Gross WPM) * 100

### Animal Speed Categories
The get_animal_category() function maps WPM ranges to specific animal categories, which provides fun feedback on typing speed.

### Performance Display
The print_performance_stats() function provides continuous feedback on:

* Word and character precision
* Gross and net WPM
* Accuracy percentage
* Character error counts

### Best Practices
Code Organization: The code follows best practices by:
* Breaking down problems into specific functions
* Using clear variable names

* Following specification requirements accurately
Scalable Animal Categories: The animal categories can be easily modified to accommodate additional speed ranges in the future.


## Requirement 5 - Single Sorting Operation for High Scores
The single-sort requirement for high scores has been effectively implemented in print_results_list().

* Score Saving: The save_score() function stores scores with details such as name, word precision, character precision, and difficulty level in score.txt.
* Sorting by Difficulty and Precision: print_results_list() implements sorting by:
1. Difficulty Priority: A dictionary maps difficulties to priorities (hard=0, medium=1, easy=2).
2. Sorting Logic: Using sorted() with itemgetter(0, 2, 3), the function sorts by:
* Priority (groups by difficulty in hard->medium->easy order)
* Word precision (as float)
* Character precision (as float)

This solution efficiently meets the requirement for single-sort grouping and precision sorting.

## Requirement 6 - Timed Character Test
The timed character test implementation is located in timed_character_test() in test.py.

* Test Setup: The function prompts the user for a test length in seconds and validates the input.
* Character Set: ASCII letters, digits, and a period (".") are used as the character set for this test.
* Test Loop: The test runs until the specified time is up, displaying:
1. A random character for the user to type
2. Capturing user input and tracking correct/incorrect entries with a defaultdict

* Metrics Calculated: Upon completion, the test displays:
1. Characters per minute (CPM)
2. Error rate
3. A sorted list of character errors by frequency
### Edge Cases
The function handles edge cases like:

* Invalid input for duration (handled with try/except)
* Ensuring time tracking accuracy
* Efficient error tracking with defaultdict for character errors

### Project Reflection
The project was relatively straightforward for me due to my familiarity with Python, though requirements 5 and 6 were somewhat challenging. The project took about 10 days, and the main difficulty was the manual testing of the code.


## main.py
The main.py module serves as the entry point for the project, calling the necessary functions to run the typing test and display the results.

