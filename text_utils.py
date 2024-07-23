# Question 1
# Task 1 

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
