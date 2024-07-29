# main.py

import mood_responses

mood = input("How are you feeling today? ")
print(mood_responses.mood_response(mood))

# main.py

import text_utils as tu

reversed_text = tu.reverse_string("hello world")
print(reversed_text)

capitalized_text = tu.capitalize_string("hello world")
print(capitalized_text)
