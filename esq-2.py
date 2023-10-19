# test array
plant_list = ["A", 5, True], ["Ab", 100, False], [
    "Bc", 34, True], ["Cd", 63, True]
# Input plant height and shade requirements.
plant_height_input = int(input('What height do you want for your plant? >>>'))
plant_shade_input = input(
    'Do you want your plant to live in shade only? Please answer "True" or "False">>>')
# A loop to check if a plant meets the user requirements.
for i in range(len(plant_list)):
    if plant_list[i][1] == plant_height_input and plant_list[i][2] == True:
        # Output if it meets the requirements
        print(plant_list[i])
# Output if it does not meet the requirements
    else:
        print("Whe unfortunately do not have such a plant.")
    break
