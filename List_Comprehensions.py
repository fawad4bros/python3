#Double Price
prices = [2,4,6,10,50,100]
Double_price = []
for price in prices:
    Double_price.append(price*2)
print(Double_price)
#List Comprehensions Method
Double_price = [price*2 for price in prices]
print(Double_price)
#Squaring numbers
nums = [1,2,3,4,5,6,7,8,9]
Squared_even_nums = []
for num in nums:
    if(num **2) % 2 == 0:
        Squared_even_nums.append(num**2)
print(Squared_even_nums)
#List Comprehensions Method
Squared_even_nums = [num**2 for num in nums if (num**2) % 2 == 0]
print(Squared_even_nums)