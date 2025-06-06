from collections import Counter

def run_toolkit():
    while True:
        print("\nWelcome to the Text Transformation Toolkit!")
        print("Choose a transformation:")
        print("1. Reverse Text")
        print("2. Convert to Uppercase")
        print("3. Convert to Lowercase")
        print("4. Title Case")
        print("5. Count Vowels")
        print("6. Remove All Spaces")
        print("7. Replace Vowels with '*'")
        print("8. Check if Palindrome")
        print("9. Word Frequency Counter")
        print("0. Exit")

        try:
            choice = int(input("Enter the number corresponding to your choice: "))
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue

        if choice == 0:
            print("Goodbye!")
            break

        text = input("Enter the text: ").strip()
        if not text:
            print("Text cannot be empty.")
            continue

        vowels = "aeiouAEIOU"

        def reverse_text(txt):
            return txt[::-1]

        def to_uppercase(txt):
            return txt.upper()

        def to_lowercase(txt):
            return txt.lower()

        def to_title_case(txt):
            return txt.title()

        def count_vowels(txt):
            return sum(1 for ch in txt if ch in vowels)

        def remove_spaces(txt):
            return txt.replace(" ", "")

        def replace_vowels(txt):
            return ''.join('*' if ch in vowels else ch for ch in txt)

        def is_palindrome(txt):
            cleaned = ''.join(ch.lower() for ch in txt if ch.isalnum())
            return cleaned == cleaned[::-1]

        def word_frequency(txt):
            words = txt.lower().split()
            return Counter(words)

        if choice == 1:
            print("Reversed text:", reverse_text(text))
        elif choice == 2:
            print("Uppercase text:", to_uppercase(text))
        elif choice == 3:
            print("Lowercase text:", to_lowercase(text))
        elif choice == 4:
            print("Title Case text:", to_title_case(text))
        elif choice == 5:
            print("Number of vowels:", count_vowels(text))
        elif choice == 6:
            print("Text without spaces:", remove_spaces(text))
        elif choice == 7:
            print("Vowels replaced with '*':", replace_vowels(text))
        elif choice == 8:
            print("Is palindrome?", "Yes" if is_palindrome(text) else "No")
        elif choice == 9:
            print("Word Frequencies:")
            for word, freq in word_frequency(text).items():
                print(f"{word}: {freq}")
        else:
            print("Invalid choice! Please choose a number from 0 to 9.")

run_toolkit()
