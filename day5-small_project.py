def main():
  input_string = input("Enter a string: ")
  def reverse_word(input_string):
    word = input_string.split()
    reverse_word = word[: : -1]
    reverse_string =  ' '.join(reverse_word)
    return reverse_string
  
  #input_string = "hello devops"
  output_string = reverse_word(input_string)
  print(output_string)


if __name__=="__main__":main()
