def even(num):
   if num%2==1:
       return 0
   else:
       return 1
num=int(input('Enter the number'))
a=even(num)
if a==1:
    print('{} number is even'.format(num))
else:
    print('{} is odd'.format(num))
