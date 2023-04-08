import os
import openai

def getResponse(user_prompt):

  openai.api_key = "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"

  prompt = user_prompt

  response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages= [
      {"role": "user", "content": user_prompt}
      ],      
    temperature= 0
    )
      
  return response['choices'][0]['message']['content']
    #print("Response {}: {}".format(i+1, response['choices'][0]['message']['content']))


with open('input.txt', 'r') as f:
    # Initialize an empty dictionary
    my_dict = {}

    # Iterate over each line in the file
    for line in f:
        # Split the line into key and value pairs
        
        key, value = line.strip().split(': ')

        # Add the key-value pair to the dictionary
        my_dict[key] = (int)(value)

    print(len(my_dict))

# Print the dictionary
print(my_dict)

goal_dict = {1: "cardio", 2: "muscle toning", 3: "ab development", 4: "biscep muscle development", 5: "leg muscle development", 6: "general muscle development"}
experience_dict = {1: "no experience", 2: "some experience", 3: "extensive experience"}
gym_dict = {0: "the gym", 1: "home"}

"""
print(my_dict['weight'])
print(my_dict['height'])
print(my_dict['goal'])
print(goal_dict[my_dict['goal']])
print(experience_dict[my_dict['experience']])
print(my_dict['time_available'])
print(gym_dict[my_dict['location']])
"""

user_prompt = f"Can you please generate a 4-week, {my_dict['days_per_week']} days per week workout plan for someone whose weight is {my_dict['weight']} pounds, has a height of {my_dict['height']} inches, and whose goal for the workout is {goal_dict[my_dict['goal']]}. They have {experience_dict[my_dict['experience']]} with workouts, with {my_dict['time_available']} hours available per day to workout, and will do the workouts at {gym_dict[my_dict['location']]}. In your answer, format it as a json dict file. Also please specify the day of the week by name."

print(user_prompt)


workout_suggestion = getResponse(user_prompt)
print(workout_suggestion)

f = open("output.json", "w")
f.write(workout_suggestion)

"""
input:
weight
height
goal (cardio: 1, weight loss: 2, muscle toning: 3, ab development: 4, bicep muscle development: 5, leg muscle development: 6, general muscle developement: 7)
current_amount_workout (scale of 1-3)
experience (scale of 1-3)
time available 
gym or at home (1 for gym, 2 at home)

output:
workout schedule (day-by-day, week-by-week)
diet (as in general: for ex: eat high proteins, etc)
"""