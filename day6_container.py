

fin = open('lines.txt', 'r', 'encoding=utf_8')
fout = open('lines.html','w')
outbytes = bytearray()
for line in fin:
    for c in line:
        if ord(c)>127:
            outbytes  += bytes('&#{:04d};'.format (ord(c)),encoding = 'utf_8')

        else:
            outbytes.append(ord(c))
    outstr = str(outbytes, encoding = 'lines')
    print(outstr, file = fout)
    print(outstr)
    print('Done')


    def reverse_word(input_string):
        word = input_string.split()
        reverse_word = word[:: -1]
        reverse_string = ''.join(reverse_word)
        return reverse_string
    
    input_string = "Hello World"

    output_string = reverse_word(input_string)

print(output_string)

