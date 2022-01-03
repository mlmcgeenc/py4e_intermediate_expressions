print('py4e exercises 3.1 and 3.3')

# Exercise 3.1
stringHours = input('Enter your worked hours: ')
stringRate = input('Enter your hourly rate: ')
floatHours = float(stringHours)
floatRate = float(stringRate)
if floatHours > 40 :
  otHours = floatHours - 40
  print('Overtime:', otHours)
  regPay = floatRate * 40
  otPay = otHours * (floatRate * 1.5)
  pay = regPay + otPay
else:
  print('Regular:', floatHours)
  pay = floatRate * floatHours
print('Pay:', pay)