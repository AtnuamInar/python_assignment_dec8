def even(num):
   if num%2==1:
       return 1
   else:
       return 0
num=int(input('Enter the number'))
a=even(num)
if a==1:
    print('{} number is odd'.format(num))
else:
    print('{} is even'.format(num))
