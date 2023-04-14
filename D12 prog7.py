#Dictionary data structure
d={'name':'Seema','roll no':123,'per':98.9}
print(d)
print(type(d))
print(d['roll no'])
print(d.get('name'))
print(d.keys())
print(d.values())
d.update({'roll no':456})
print(d)
d.pop()
print(d)