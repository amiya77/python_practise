# infile = open('lines.txt', 'r')
# outfile = open('new.txt', 'w')

# for line in infile:
#     print(line, file= outfile, end =' ')
#     print('Done')

#------------------------------------------
#Reading & writing text files
# buffersize= 50000

# infile = open('lines.txt', 'r')
# outfile = open('hi.txt', 'w')
# buffer = infile.read(buffersize)
# while len(buffer):
#     outfile.buffer
#     print('.', end = '')
#     buffer = infile.read(buffersize)
# for line in infile:
#     print(line, file = outfile,end='')
#     print('done')
#------------------------------------------


buffersize = 50000

infile = open('hill_images.jpg', 'rb')
outfile = open('new.jpg', 'wb')
buffer = infile.read(buffersize)
while len(buffer):
    outfile.write(buffer)
    print('.', end='')
    buffer = infile.read(buffersize)
    print()
    print('Done')
for line in infile:
    print(line, end='', )