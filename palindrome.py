def is_palindrome():
    # Input a word or phrase
    user_input = input("Enter a word or phrase: ").strip().lower()
    
    # Remove spaces and non-alphanumeric characters for more accurate checks
    cleaned_input = ''.join(char for char in user_input if char.isalnum())
    
    # Check if the cleaned input is the same as its reverse
    if cleaned_input == cleaned_input[::-1]:
        print(f"'{user_input}' is a palindrome!")
    else:
        print(f"'{user_input}' is not a palindrome.")
        
# Run the palindrome checker
is_palindrome()
