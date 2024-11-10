"""
this is the main file that runs the program.
"""
# here I will import all functions, I need them to run the app, from other modules. 
from test import typing_test, timed_character_test
from storage import print_results_list

def main():
    """
    main function to run all the tests.
    """
    while True:
        print("\n--------Let´s start the app----------\n")
        print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
        print("% 1. Typing test easy level          %")
        print("% 2. Typing test medium level        %")
        print("% 3. Typing test hard level          %")
        print("% 4. High Scores list                %")
        print("% 5. Enter seconds for test          %")
        print("% q. Done learning, exit             %")
        print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
        
        try:
            choice = input("\nWhat do you want to do? ")

            if choice == "1":
                typing_test('data/easy.txt')
            elif choice == "2":
                typing_test('data/medium.txt')
            elif choice == "3":
                typing_test('data/hard.txt')
            elif choice == "4":
                print_results_list()
            elif choice == "5":
                timed_character_test()
            elif choice == "q":
                print("\n I hope you have learned something..")
                break
            else:
                print("Please enter one of these choices (1,2,3,4,5,q)")
        except ValueError:
            print("Invalid input, go debugg your code and find your enemy")

if __name__ == "__main__":
    main()
