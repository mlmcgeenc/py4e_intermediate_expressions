print('py4e exercise 4.6')

# Exercise 4.6
def computePay(hours, rate):
  if hours > 40 :
    otHours = hours - 40
    regPay = rate * 40
    otPay = otHours * (rate * 1.5)
    pay = regPay + otPay
  else:
    pay = rate * hours
  return pay
    
stringHours = input('Enter your worked hours:')
stringRate = input('Enter your hourly rate:')
floatHours = float(stringHours)
floatRate = float(stringRate)
pay = computePay(floatHours, floatRate)

print("Pay",p)