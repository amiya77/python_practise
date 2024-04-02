#Handling Exception

# def main():
#     try:
#         fh = open('xlines.txt') #to find a file which is not available. 
#     except IOError as e:
#         print("couldnt open the file" , e)
#     else:
#         for line in fh:print (line)


# if __name__== "__main__": main()
#-----------------------------------------------
# def main():
#     try:
#         fh = open('xlines.txt')
#     except IOError as e:
#         print('couldnot open the file', e)
#     else:
#         for line in fh: print(line)

# if __name__=="__main__": main()
#-----------------------------------------------

#Raising Exception

def main():
    #fh = open(line.txt)
    for line in readfile('lines.txt'): print(line.strip())
def readfile(filename):
    fh = open(filename)
    return fh.readline()

if __name__=="__main__": main()

