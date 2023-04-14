#Program on diff methods of string class
s='foo bar foo baz qwe foo'
print(s.count('bar'))
print(s.count('o'))
print(s.count('foo',4))#Count for word foo from the starting index as 4
print(s.count('foo',4,9))#from index 4 to 8th index
print(s.count('foo',4,15))
print(s.index('foo'))
print(s.index('foo',4))
print(s.index('baz',4))
print(s.find('foo'))
print(s.find('baz'))
print(s.find('foo',6))
print(s.upper())
print(s.title())
print(s.isdigit())
print(s.isalnum())
print(s.isalpha())