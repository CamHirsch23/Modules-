# text_utils.py
class text_utils:
    @staticmethod
    def reverse_string(s):
        return s[::-1]

    @staticmethod
    def capitalize_string(s):
        return s.capitalize()

# mood_responses.py
def mood_response(mood):
    if mood.lower() == "happy":
        return "That's great to hear! Keep smiling!"
    elif mood.lower() == "sad":
        return "I'm sorry to hear that. I hope things get better soon."
    elif mood.lower() == "excited":
        return "Awesome! Excitement is contagious!"
    else:
        return "Thank you for sharing your mood!"

# main.py
import text_utils
import mood_responses

reversed_text = text_utils.reverse_string("hello world")
print(reversed_text)

capitalized_text = text_utils.capitalize_string("hello world")
print(capitalized_text)

mood = input("How are you feeling today? ")
print(mood_responses.mood_response(mood))
