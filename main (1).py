start=["WELCOME TO SMART CALCULATOR","HELLO MY NAME IS MARS","SORRY,THIS IS OUT OF MY LIMIT","THANKYOU!!!,FOR USING ME"]
def extract_number(text):
  l=[]
  for i in text.split(" "):
    try:
      l.append(float(i))
    except ValueError:
      pass
  return l
def add (a,b):
  return(a+b)
def sub (a,b):
  return a-b
def mul (a,b):
  return a*b
def div (a,b):
  return a/b
def mod (a,b):
  return a%b
def greatest_integer (a,b):
  return a//b
def fraction_number (a,b):
  return ((a/b)-(a//b))
def lcm (a,b):
  l=a if a>b else b
  while(l<=a*b):
    if l%a==0 and l%b==0:
      return l
    else:
      l+=1
def gcd (a,b):
  x=a
  y=b
  while(y!=0):
    temp=y
    y=x%y
    x=temp
  return x
def exit1():
  print("enter a key to exit")
  input()
  print(start[3])
  exit()
def myname():
  print(start[1])
def sorry():
  print(start[2])
operator={"ADDITION":add,"ADD":add,"PLUS":add,"SUM":add,"+":add,"SUBTRACT":sub,"SUB":sub,"MINUS":sub,"-":sub,"MULTIPLY":mul,"MUL":mul,"*":mul,"X":mul,"INTO":mul,"DIV":div,
"DIVIDE":div,"DIVIDED":div,"/":div,"MODULUS":mod,"MOD":mod,"REMAINDER":mod,"INTEGERPART":greatest_integer,"FLOOR":greatest_integer,
"CEIL":fraction_number,"FRACTION":fraction_number,"DECIMAL":fraction_number,"LCM":lcm,"GCD":gcd}
action={"EXIT":exit1,"END":exit1,"FINISH":exit1,"COMPLETE":exit1,"GETMEOUT":exit1,"NAME":myname,"WHO":myname,"SORRY":sorry,"GETMEOUT":exit1,"LETMEOUT":exit1,"OUT":exit1}
while(1):
  text=input()
  for x in text.split():
    if x.upper() in operator:
     try:
      l=extract_number(text)
      r=operator[x.upper()](l[0],l[1])
      print("THAT WILL BE",r,sep=":")
     except:
       print("SOMETHING IS WRONG PLEASE TRY AGAIN")
     finally:
       break
    elif x.upper() in action:
       action[x.upper()]()
    else:
      sorry()
      break
    
     
      
    
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
