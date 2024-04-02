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

# def main():
#     #fh = open(xline.txt)
#     try:
#         for line in readfile('lines.doc'): print(line.strip())
#     except IOError as e:
#         print('cannot read file', e)
#     except ValueError as e:
#         print ('bad file name', e)
# def readfile(filename):
#     if filename.endswith('.txt'):
#         fh = open(filename)
#         return fh.readline()
#     else: raise ValueError('Filename must end with .txt')

# if __name__=="__main__": main()

#---------------------------------------------------------
