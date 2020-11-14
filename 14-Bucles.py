for i in [1,2,3]:
   print(str(i) +  " Hola", i)

email = False
for i in "lazarete@outlook.com":
    if (i=="@"):
        email = True

if email:
    print("Email correcto")
else:
    print("Email incorrecto")

for i in range(5):
    print (i)