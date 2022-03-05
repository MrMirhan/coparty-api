def FirstFactorial(num: int):
    fact = num
    while num != 1:
        print(1, fact)
        num = num - 1
        print(2, num)
        fact = fact * num
    return fact
  


# keep this function call here 
print(3, FirstFactorial(int(input())))