
def convert_case(text):
    return text.swapcase() 

def search_character(text):
  temp=char(input("Enter the character you want to search:"))
  for i in text:
    if i==temp:
      return True
  return False

while True:
  print("String Operations")
  print("1.Convert case")
  print("2.Reverse String")
  print("3.Search Character")
  print("4.Replace Character")

text=str(input("Enter your string:"))
choice=int(input("Enter choice:"))

if choice==1:
  convert_case(choice)
elif choice==2:
  reverse_string(choice)
elif choice==3:
  search_character(choice)
elif choice==4:
  replace_character(choice)
  convert_case(text)
elif choice==2:
  reverse_string(text)
elif choice==3:
  result=search_character(text)
  if result:
    print("Found the character")
  else:
    print("Not found") 
elif choice==4:
  replace_character(text)
else :
  print("Invalid choice")
  break

