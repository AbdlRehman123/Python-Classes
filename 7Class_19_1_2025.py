# key: value
my_dict={}
our_dict={"Ali":"1009876","Muhammad":"1009877","Fatima":"1009878"}
contact=["Hiba",109]
student=["Ahsen",101,102]
name={"ahsen":"010","rollno":"010","class":10} # corrected this line
print(my_dict)
print(our_dict)
print(our_dict["Fatima"]) #find
print(contact)
print(student)

# key: value H.Work
my_dict={}
our_dict={"Devdas":"1009876","Raja":"1009877","Fatima":"1009878","Devdas":"1009876","Umer":"1009877","Fatima":"1009878"}
contact=["Hiba",109]
student=["Ahsen",101,102]
name={"Ahsen":"010","Roll No":"010","Class":10} # corrected this line
print(my_dict)
print(our_dict)
print(our_dict["Umer"]) #find
print(our_dict["Devdas"]) # find
print(contact)
print(student)
print(name)

my_dict={} # home work
# key value always come on the sting
my_dict["Ali"]="1009876"
my_dict["Muhammad"]="1009877"
my_dict["Fatima"]="1009878"
print("before",my_dict) #keys called index
print("after",my_dict)
print(my_dict,"before")

people={"Name":"Ali","Age":"20","Class":"Sunday7-10"}
print(people)

def charger ():
  print("Charge Mobile")

charger()

def ramokaka():
  print("ramo Kaka biryani Banao")

ramokaka()

a=1
b=4

def add():
  return a+b

sum=add()
print(sum)

a=1 # Homw work
b=4
c=10
d=50

def add():
  return a+d,b+c,d-a,c-b,a*d,b*c,d/a,c/b

sum=add()
print(sum)

a=1 # Homw work
b=4
c=10
d=50

def subt():
  return a-d,c-b

subt=subt()
print(subt)

a=1 # Homw work
b=4
c=10
d=50

def mult():
  return d*c,c*b

mult=mult()
print(mult)

a=1 # Homw work
b=4
c=10
d=50

def div():
  return d/c,c/b

div=div()
print(div)

print("Welcome! Please follow the instruction for using calculator")
num1=int(input("Enter first number: "))
print("10,Add(+)")
print("20,subtract(-)")
print("30,Divide(/)")
print("40,multiple(*)")
choice=int(input("Enter your choice: "))
num2=float(input("Enter second number: "))
print("Here is your result")
if choice==10:
  print(num1,"+",num2,"=",num1+num2)
elif choice==20:
    print(num1,"-",num2,"=",num1-num2)
elif choice==30:
    print(num1,"*",num2,"=",num1*num2)
elif choice==40:
   print(num1,"/",num2,"=",num1/num2)
   print("invalid input")

def ramo_kaka():
  return "Biryani bangayi"

plate=ramo_kaka()
print(plate)

def ramo_kaka(): # Home work
  return "Biryani bangayi","Pizza","Salad"

plate=ramo_kaka()
Salad_free=plate[0]
print(plate)
print(Salad_free)

# parameter
def greet(name,age):
  print("Assalam o Alekum Sir",name,"your age is",age)

# argumemt
greet("Ali",23)

# parameter Home work
def greet(name,age,relationship):
  print("Assalam o Alekum Sir",name,"my age is",age,"and relationship is",relationship)

# argumemt
greet("Ali",23,"sister")

# Home work
def greet(name,
          Fathers_Name,
          Roll_No,Class,
          Mobile_No,
          Signature):
  print(name,
        Fathers_Name,
        Roll_No,
        Class,
        Mobile_No,
        Signature)
greet("Devan Das",
      "Paru Mal",
      1502,"XII",
      3322694215,
      "@DMM")

# find duplicate number using python
mylist=[1,2,3,4,5,6,7,8,9,10,3,5,8,9]
dupl=[]
uniq=[]
for i in mylist:
  if i not in uniq:
    uniq.append(i)
  elif i not in dupl:
    dupl.append(i)
print(dupl)
print(uniq)
print(mylist)

# find duplicate number using python
mylist=["Ammarah","Khan","Ali","Dileep",
        "Saleem","Hiba","Pars","Dileep"
        ,"Ammarah"]
dupl=[]
uniq=[]
for i in mylist:
  if i not in uniq:
    uniq.append(i)
  elif i not in dupl:
    dupl.append(i)
print(dupl)
print(uniq)
print(mylist)