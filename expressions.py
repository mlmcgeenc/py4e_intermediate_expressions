print('py4e exercise 4.6')

# Exercise 4.6
stringHours = input('Enter your worked hours:')
stringRate = input('Enter your hourly rate:')
try:
  floatHours = float(stringHours)
  floatRate = float(stringRate)
except:
  print('Error, please enter numeric input')
  quit()

if floatHours > 40 :
  otHours = floatHours - 40
  regPay = floatRate * 40
  otPay = otHours * (floatRate * 1.5)
  pay = regPay + otPay
else:
  pay = floatRate * floatHours

print(pay)