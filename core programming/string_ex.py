x = "     man1986 is a good movie is a good movie  "
#print(x.isupper())
#print(x.islower())
#print(x.isalnum())
y = x.lower()
y = x.upper()
#print(y)
#print(x.endswith('movie'))
#print(x.startswith('is'))
#print(x.partition('is'))
#print(x.partition('was'))
#print(len(x))
z = x.lstrip()
#print(len(z))
d = x.rstrip()
#print(len(d))
#print(d)
a = "aaabaacdaaxxaa"
b = a.lstrip('ba')
print(b)
print(x.find('movie',24))