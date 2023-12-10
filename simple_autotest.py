from functions import salary, hello_who
assert hello_who('Max') == 'hello,Max', 'Hello who error'
assert hello_who('Leo') == 'hello,Leo', 'Hello who error'
assert hello_who('Nikita') == 'hello,Nikita', 'Hello who error'
assert salary(2,1)==4
assert salary(2,2)==8