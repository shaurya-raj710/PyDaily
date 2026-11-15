# Write your reference solution here
import math
score = int(input())

percentage = (score/150)*100



if percentage>=90:
        print(f"Merit scholarship awarded. Percentage: {percentage:.2f}%")

else:
        print(f"Not eligible for merit scholarship. Percentage: {percentage:.2f}%")