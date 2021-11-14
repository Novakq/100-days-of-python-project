

numbers = [1,2,3]
new_list = [n*2 for n in range(1,5) if n%3 == 0]

print(new_list)



sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# Don't change code above 👆


result = { word: len(word) for word in sentence.split()}

# Write your code below:

print(result)

#ok