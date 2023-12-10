from functions import salary, hello_who

print(salary(2,10))

if salary(4,20) !=160:
    print('Error')
else:
    print('Super')
if hello_who('Ari') != 'hello,Ari':
    print('Failed')
else:
    print('Good')