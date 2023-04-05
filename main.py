import openai

openai.api_key = "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"
weight = input("How much do you weigh?\n> ")
goalCode = input("What are your workout goals? Lose weight, Gain muscle, or Maintain and build stamina. "
                 "Type 1, 2, or 3.\n> ")
goal = ''
experience = ''
equipment = ''


if goalCode == "1":
    goal = "lose weight"
    targetWeight = input("What is your target weight?\n> ")

if goalCode == "2":
    goal = "gain muscle"
    targetWeight = input("What is your target weight?\n> ")

if goalCode == "3":
    goal = "build stamina"
    targetWeight = weight

experienceCode = input("How much experience do you have lifting? Beginner, Intermediate, or Expert. "
                       "Type 1, 2, or 3.\n> ")

if experienceCode == 1:
    experience = "beginner"

if experienceCode == 2:
    experience = "intermediate"

if experienceCode == 3:
    experience = "expert"

equipmentCode = input("What equipment do you have access to? No weights, Dumbbells, Full gym. Type 1, 2, or 3.\n> ")

if equipmentCode == 1:
    equipment = "no weights"

if equipmentCode == 2:
    equipment = "dumbbells"

if equipmentCode == 3:
    equipment = "a full gym"

workoutsPerWeek = input("How many times do you want to workout per week?\n> ")

workoutLength = input("How long do you want your workouts to be?\n> ")

extraNotes = input("Do you have any extra notes? (specific muscle group, any injuries, etc.)\n> ")

systemPrompt = """
The output should be in the exact format as the following example. Don't add any extra info. Take into account that the amount of days or amount of exercises may be different depending on the input.
EXAMPLE:

Day 1: 
- Bench Press 4x5
- Incline Press 4x5
- Pull Ups 3x6 or Failure
- Bent Over Rows 3x10
- Tricep Dips 3x5 or Failure
- DB Military Press 4x5

Day 2:
- Leg Press 3x10
- Front Squats 3x8
- Split Squat 3x6
- Romanian Deadlift 3x8
- Calf Raises 2x20;1xFailure

Day 3:
- Pull Ups 3x6 or Failure
- Incline DB Press 3x8
- DB Military Press 4x5
- Back Cable Rows 3x8
- Bicep Curls 3x8
- Tricep Extensions 3x8

Day 4:
- Split Squat 3x6
- Deadlift 4x5
- Single Leg RDL 3x6
- Glute Ham Raises 3x8
- Eccentric Calf Raises 3x15"""

prompt = "Generate a workout plan for someone who weighs " + weight + " pounds. " \
         "They want to " + goal + ". Their target weight is " + targetWeight + "pounds. " \
         "They are a " + experience + " lifter. They have access to " + equipment + ". " \
         "They want to workout " + workoutsPerWeek + "times a week. " \
         "They want their workouts to be " + workoutLength + " minutes long. "

print(prompt)

response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
        {"role": "system", "content": systemPrompt},
        {"role": "user", "content": prompt},
    ]
)

print(response['choices'][0]['message']['content'])



