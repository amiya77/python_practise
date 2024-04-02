#////////////1.04.24 : Day:3//////////

# import re
# def main():
#     fh = open('lines.txt')
#     for line in fh:
#         match = re.search('DevOps',line)
#         # if re.search('DevOps', line):
#         if match:
#             # print(line, end='')
#             print(match.group())
# if __name__== "__main__": main()

#replacing values with regular-expression.-----------------------------------

# import re
# def main():
#     fh = open('lines.txt')
#     for line in fh:
#         if re.search('DevOps', line):
#             print(re.sub('DevOps', 'DevSecOps', line), end='')
# if __name__== "__main__": main()


# import re
# def main():
#     fh = open('lines.txt')
#     for line in fh:
#         if re.search('DevOps', line):
#             print(re.sub('DevOps', 'CloudOps', line), end='')
# if __name__== "__main__":main()

import re
def main():
    fh = open('lines.txt')
    for line in fh:
        brain = re.search('DevOps', line)
        if brain:
            print(line.replace(brain.group(), '???'), end='')

if __name__=="__main__":main()


