def add(num1, num2):
  return num1 + num2
def subtract(num1, num2):
  return num1 - num2
def multiply(num1, num2):
  return num1 * num2
def divide(num1, num2):
  return num1 / num2

print(""" Select one of the operations:

1. Addition
2. Subtraction
3. multiply
4. Division
5. Powers
6. Remainders""")

select = int(input('Which operation do you need?1/2/3/4/5/6: '))

num1 = int(input('Please enter your first number: '))
num2 = int(input('Please enter your second number: '))
# using f-string is a simple way instead of writing the variable again and again !
if select == 1:
  adding = add(num1, num2)
  print(f"{num1} + {num2} = {adding}")
  #print(num1, '+', num2, '=', add(num1, num2))
elif select == 2:
  subtracting = subtract (num1, num2)
  print (f"{num1} - {num2} = {subtracting}")
  #print(num1, '-', num2, '=', subtract(num1, num2))
elif select == 3:
  multiplying = multiply (num1, num2)
  print (f"{num1} x {num2} = {multiplying}")
  #print(num1, 'x', num2, '=', multiply(num1, num2))
elif select == 4:
  div = divide(num1, num2)
  print (f"{num1} / {num2} = {div}")
  #print(num1, '/', num2, '=' , divide(num1, num2))
elif select == 5:
  # just do the same as above here - Try it yourself, I know you can do it !
  print(num1, '^', num2, '=', num1**num2)
elif select == 6:
  # F-string here also - if you have problems , type on google "f-string" !
  print(num1, 'R', num2, '=',  num1 % num2)
else:
   print("Invalid input!")
