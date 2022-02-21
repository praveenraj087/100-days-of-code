sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# Don't change code above 👆
sep_string = [word for word in sentence.split()]

result = {word:len(word) for word in sep_string}
# Write your code below:



print(result)

