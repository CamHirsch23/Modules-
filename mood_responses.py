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
