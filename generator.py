
def creator():
    i=1
    while i<=200:
        yield i
        i += 1
        
print(creator())
x=creator()
print(next(x))