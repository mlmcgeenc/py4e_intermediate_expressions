print('py4e exercise 3.3')

# Exercise 3.3
score = input("Enter Score: ")
floatScore = float(score)
if floatScore >= 0.9:
  print('A')
elif floatScore >= 0.8:
  print('B')
elif floatScore >= 0.7:
  print('C')
elif floatScore >= 0.6:
  print('D')
else:
  print('F')