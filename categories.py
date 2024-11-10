"""
This module contains the function that categorizes the user's typing speed into a category
"""
def get_animal_category(net_wpm):
    """
    Returns an animal category based on net WPM speed.
    """
    speed_categories = {
        5: "Sloth",
        15: "Snail",
        30: "Manatee",
        40: "Human",
        50: "Gazelle",
        60: "Ostrich",
        70: "Cheetah",
        80: "Swordfish",
        90: "Spur-winged goose",
        100: "White-throated needletail",
        120: "Golden eagle"
    }

    for speed_threshold, animal in speed_categories.items():
        if net_wpm <= speed_threshold:
            return animal
            
    return "Peregrine falcon"