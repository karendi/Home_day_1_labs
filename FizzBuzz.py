# a function that checks if a number , n is divisible by 3 and 5  , or 3 or 5
# if its not it returns the number itself

def fizz_buzz(n):
  if n % 3 == 0 and n % 5 ==0:
    return 'FizzBuzz'
  elif n % 3 == 0:
    return 'Fizz'
  elif n % 5 == 0:
    return 'Buzz'
  else:
    return n
