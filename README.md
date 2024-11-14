A simple app that checks whether a word or phrase is a palindrome (a word that reads the same forwards and backwards).

How It Works:
Input: The program asks the user to enter a word or phrase. It then strips any extra spaces and converts the string to lowercase for uniformity.
Cleaning Input: We remove any non-alphanumeric characters (such as spaces, punctuation, etc.) using a generator expression. This ensures the palindrome check is done on the actual characters.
Checking Palindrome: The program compares the cleaned input with its reverse (using slicing [::-1]), and if both are the same, it's a palindrome.
Output: The result is printed, informing the user if the input is a palindrome or not.

Features:
Case-Insensitive: The program converts everything to lowercase before checking.
Spaces and Punctuation: It ignores spaces, punctuation, and special characters for accurate checks.
