student_heights = input('Input a list of student heights').split()                # input a list of student heights separated by spaces

sum = 0                                                     # Convert the input strings to integers and calculate the sum of heights
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
    sum += student_heights[n]
    
print("List of student heights:", student_heights)
average = sum / len(student_heights)                        # Calculate the average height by dividing the sum by the number of heights
print('Average:', round(average))                  # Print the calculated average rounded to the nearest integer



