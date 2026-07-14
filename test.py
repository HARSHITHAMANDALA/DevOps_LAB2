
def convert_case(text):
    print(text.swapcase() )
def reverse_string(text):
	reverse=text[::-1]
	print(reverse)

def search_character(text):
  temp=char(input("Enter the character you want to search:"))
  for i in text:
    if i==temp:
      print("character found")
      return True
  print("character not found")
  return False

def replace_character(text):
	result = text.replace("p", "x")
	print(result)

while True:
  print("String Operations")
  print("1.Convert case")
  print("2.Reverse String")
  print("3.Search Character")
  print("4.Replace Character")

text=str(input("Enter your string:"))
choice=int(input("Enter choice:"))
text=input("Enter string:")

if choice==1:
  convert_case(text)
elif choice==2:
  reverse_string(text)
elif choice==3:
  search_character(text)
elif choice==4:
  replace_character(text)
else :
  print("Invalid choice")
  break

