def convert_case(text):
    return text.swapcase() 

while True:
  print("String Operations")
  print("1.Convert case")
  print("2.Reverse String")
  print("3.Search Character")
  print("4.Replace Character")

choice=int(input("Enter choice:"))

if choice==1:
  convert_case(choice)
elif choice==2:
  reverse_string(choice)
elif choice==3:
  search_character(choice)
elif choice==4:
  replace_character(choice)
else :
  print("Invalid choice")
  break

