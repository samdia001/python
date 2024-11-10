"""
This module contains functions for calculating various metrics related to typing speed and accuracy.
"""
from math import ceil
from categories import get_animal_category

def calculate_precision(correct_count, total_count):
    """
    Calculate precision percentage.
    """
    return (correct_count / total_count) * 100 if total_count > 0 else 0

def calculate_minutes(seconds):
    """
    Calculate rounded minutes from seconds.
    """
    if seconds < 60:
        return 1
    minutes = seconds / 60
    return ceil(minutes) if (seconds % 60) > 30 else int(minutes)
    
def calculate_wpm_metrics(total_words, incorrect_words, elapsed_time):
    """
    calculate gross wpm, net wpm and accuracy. there is a bug in this function lk 3ame.
    """
    minutes = calculate_minutes(elapsed_time)
    gross_wpm = total_words / minutes
    net_wpm = gross_wpm - (incorrect_words / minutes)
    accuracy = ((total_words - incorrect_words) / total_words * 100) if total_words > 0 else 0
    get_animal_category(net_wpm)
    return gross_wpm, net_wpm, accuracy
