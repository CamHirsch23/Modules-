# Define the mood_response function
def mood_response(mood):
    if mood.lower() == "happy":
        return "That's great to hear! Keep smiling!"
    elif mood.lower() == "sad":
        return "I'm sorry to hear that. I hope things get better soon."
    elif mood.lower() == "excited":
        return "Awesome! Excitement is contagious!"
    else:
        return "Thank you for sharing your mood!"

# Ask the user for their mood
mood = input("How are you feeling today? ")

# Call the mood_response function and print the result
print(mood_response(mood))

# Simulating text_utils.py within the same file
class text_utils:
    @staticmethod
    def reverse_string(s):
        return s[::-1]

    @staticmethod
    def capitalize_string(s):
        return s.capitalize()

# Utilize the reverse_string function from text_utils
reversed_text = text_utils.reverse_string("hello world")
print(reversed_text)  # Output: "dlrow olleh"

# Utilize the capitalize_string function from text_utils
capitalized_text = text_utils.capitalize_string("hello world")
print(capitalized_text)  # Output: "Hello world"
