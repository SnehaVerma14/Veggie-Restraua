#Creating border and heading
print(115*"_")
heading="Veggie Restraus"
underline=len(heading)*"-"
print(underline.center(255),"\n",heading.center(250),"\n",underline.center(253))
print("[Open - 8AM]".rjust(245),"\n","[Close - 9PM]".rjust(245))

#Importing time from library
import time
t=time.localtime()
Ptime=t.tm_hour
#Ptime=int(input("Enter hr: "))

#Installed pandas & tabulate package from PIP 
import pandas as pd
from tabulate import tabulate

#Using if,elif,else statements for time 
if Ptime>=8 and Ptime<=10:
      #Using dictionary for creating menu
      Breakfast={'Menu': ['Masala Dosa','Vada (2)','Idli(2)','Upma(2)','Sambhar','Aloo Paratha','Gobi Paratha','Oat Meal','Whole wheat toast (2)'], '':['Rs.45','Rs.15','Rs.15','Rs.15','Rs.25','Rs.35','Rs.35','Rs.25','Rs.15']}
      print("BREAKFAST TIME!\n","\n","Here is your MENuuu")
      print(tabulate(pd.DataFrame(Breakfast),headers='firstrow',tablefmt="plain")) #Creating table or data frame from packages 
      p1=[45,15,15,15,25,35,35,25,15] #list of dish prices
      print("")
      print("INSTRUCTION:\n1. [Give Orders in serial numbers]\n2. [If there is no order then type '-1']")
      col1=1
      BL=[]
      print("")
      #Using for loop - Taking record of orders and quantity
      for i in p1:
            B=int(input("Orders here: "))
            BL.append(B)
            if B==-1:
                  break
            quan1=int(input("~ Enter quantity: "))
            i=p1[B]*quan1
            col1+=i
      #Adding ALL DAY menu 
      AllDay={'Menu': ['Tea','Coffee','Papdi Chat','Cold Drinks','Ice cream','Sweet (1)'], '':['Rs.25','Rs.45','Rs.35','Rs.25','Rs.30','Rs.25']}
      print("All DAY!\n","\n","MENuuu")
      print(tabulate(pd.DataFrame(AllDay),headers='firstrow',tablefmt="plain"))
      #Taking input from user whether to order from ALL DAY menu or not.
      Ask1=input("Would you like to Order from All DAY Menu? (y/n) ")
      if Ask1=='y':
            p5=[25,45,35,25,30,25]
            print("")
            print("INSTRUCTION:\n1. [Give Orders in serial numbers]\n2. [If there is no order then type '-1']")
            col5=1
            AL=[]
            print("")
            for i in p5:
                  A=int(input("Orders here: "))
                  AL.append(A)
                  if A==-1:
                        break
                  quan5=int(input("~ Enter quantity: "))
                  i=p5[A]*quan5
                  col5+=i
            AL.pop(-1)
            l5=list(AllDay.values())
            M5=l5[0]
            BL.pop(-1)
            l1=list(Breakfast.values())
            M1=l1[0]
            print("")
            print("BILL:\nYour Orders:")
            for i in AL:
                  print(">",M5[i])
            for i in BL:
                  print(">",M1[i])
            print("Total Amount:",(col1-1)+(col5-1))
      elif Ask1=='n':
            BL.pop(-1)
            l1=list(Breakfast.values())
            M1=l1[0]
            print("")
            print("BILL:\nYour Orders:")
            for i in BL:
                  print(">",M1[i])
            print("Total Amount:",col1-1)      
      
elif Ptime>=12 and Ptime<14:
      Lunch={'Menu': ['NorthIndian Veg thali','South Indian Veg thali','Tandoori roti','Naan','Kulcha roti','Fried Rice','Ghee Rice','Paneer kofta','Chola Masala'], '':['Rs.110','Rs.110','Rs.15','Rs.15','Rs.15','Rs.100','Rs.100','Rs.110','Rs.110']}
      print("LUNCH TIME!\n","\n","Here is your MENuuu")
      print(tabulate(pd.DataFrame(Lunch),headers='firstrow',tablefmt="plain"))
      p2=[110,110,15,15,15,100,100,110,110]
      print("")
      print("INSTRUCTION:\n1. [Give Orders in serial numbers]\n2. [If there is no order then type '-1']")
      col2=1
      LL=[]
      print("")
      for i in p2:
            L=int(input("Orders here: "))
            LL.append(L)
            if L==-1:
                  break
            quan2=int(input("~ Enter quantity: "))
            i=p2[L]*quan2
            col2+=i
      AllDay={'Menu': ['Tea','Coffee','Papdi Chat','Cold Drinks','Ice cream','Sweet (1)'], '':['Rs.25','Rs.45','Rs.35','Rs.25','Rs.30','Rs.25']}
      print("All DAY!\n","\n","MENuuu")
      print(tabulate(pd.DataFrame(AllDay),headers='firstrow',tablefmt="plain"))
      Ask2=input("Would you like to Order from All DAY Menu? (y/n) ")
      if Ask2=='y':
            p5=[25,45,35,25,30,25]
            print("")
            print("INSTRUCTION:\n1. [Give Orders in serial numbers]\n2. [If there is no order then type '-1']")
            col5=1
            AL=[]
            print("")
            for i in p5:
                  A=int(input("Orders here: "))
                  AL.append(A)
                  if A==-1:
                        break
                  quan5=int(input("~ Enter quantity: "))
                  i=p5[A]*quan5
                  col5+=i
            AL.pop(-1)
            l5=list(AllDay.values())
            M5=l5[0]
            LL.pop(-1)
            l2=list(Lunch.values())
            M2=l2[0]
            print("")
            print("BILL:\nYour Orders:")
            for i in AL:
                  print(">",M5[i])
            for i in LL:
                  print(">",M2[i])
            print("Total Amount:",(col2-1)+(col5-1))
      elif Ask2=='n':
            LL.pop(-1)
            l2=list(Lunch.values())
            M2=l2[0]
            print("")
            print("BILL:\nYour Orders:")
            for i in LL:
                  print(">",M2[i])
            print("Total Amount:",col2-1)
      
elif Ptime>=16 and Ptime<18:
      Evening={'Menu': ['Kachori (3)','Onion Pakoda (3)','Potati Pakoda (3)','Aloo Bonda(2)','Bajii (2)','Aloo Samosa','Onion Samosa'], '':['Rs.80','Rs.60','Rs.60','Rs.45','Rs.45','Rs.60','Rs.60']}
      print("EVENING SNACKS TIME!\n","\n","Here is your MENuuu")
      print(tabulate(pd.DataFrame(Evening),headers='firstrow',tablefmt="plain"))
      p3=[80,60,60,45,45,60,60]
      print("")
      print("INSTRUCTION:\n1. [Give Orders in serial numbers]\n2. [If there is no order then type '-1']")
      col3=1
      EL=[]
      print("")
      for i in p3:
            E=int(input("Orders here: "))
            EL.append(E)
            if E==-1:
                  break
            quan3=int(input("~ Enter quantity: "))
            i=p3[E]*quan3
            col3+=i
      AllDay={'Menu': ['Tea','Coffee','Papdi Chat','Cold Drinks','Ice cream','Sweet (1)'], '':['Rs.25','Rs.45','Rs.35','Rs.25','Rs.30','Rs.25']}
      print("All DAY!\n","\n","MENuuu")
      print(tabulate(pd.DataFrame(AllDay),headers='firstrow',tablefmt="plain"))
      Ask3=input("Would you like to Order from All DAY Menu? (y/n) ")
      if Ask3=='y':
            p5=[25,45,35,25,30,25]
            print("")
            print("INSTRUCTION:\n1. [Give Orders in serial numbers]\n2. [If there is no order then type '-1']")
            col5=1
            AL=[]
            print("")
            for i in p5:
                  A=int(input("Orders here: "))
                  AL.append(A)
                  if A==-1:
                        break
                  quan5=int(input("~ Enter quantity: "))
                  i=p5[A]*quan5
                  col5+=i
            AL.pop(-1)
            l5=list(AllDay.values())
            M5=l5[0]
            EL.pop(-1)
            l3=list(Evening.values())
            M3=l3[0]
            print("")
            print("BILL:\nYour Orders:")
            for i in AL:
                  print(">",M5[i])
            for i in EL:
                  print(">",M3[i])
            print("Total Amount:",(col3-1)+(col5-1))
      elif Ask3=='n':
            EL.pop(-1)
            l3=list(Evening.values())
            M3=l3[0]
            print("")
            print("BILL:\nYour Orders:")
            for i in EL:
                  print(">",M3[i])
            print("Total Amount:",col3-1)
elif Ptime>=18 and Ptime<21:
      Dinner={'Menu': ['Chole bhature','Tandoori roti','Naan','Kulcha roti','Paneer kofta','Malai Kofta','Dal tadka','Briyani','Fried Rice','Veg Chow mein with manchurian'], '':['Rs.90','Rs.15','Rs.15','Rs.15','Rs.110','Rs.110','Rs.110','Rs.100','Rs.100','Rs.105']}
      print("DINNER TIME!\n","\n","Here is your MENuuu")
      print(tabulate(pd.DataFrame(Dinner),headers='firstrow',tablefmt="plain"))
      p4=[90,15,15,15,110,110,110,100,100,105]
      print("")
      print("INSTRUCTION:\n1. [Give Orders in serial numbers]\n2. [If there is no order then type '-1']")
      col4=1
      DL=[]
      print("")
      for i in p4:
            D=int(input("Orders here: "))
            DL.append(D)
            if D==-1:
                  break
            quan4=int(input("~ Enter quantity: "))
            i=p4[D]*quan4
            col4+=i
      AllDay={'Menu': ['Tea','Coffee','Papdi Chat','Cold Drinks','Ice cream','Sweet (1)'], '':['Rs.25','Rs.45','Rs.35','Rs.25','Rs.30','Rs.25']}
      print("All DAY!\n","\n","MENuuu")
      print(tabulate(pd.DataFrame(AllDay),headers='firstrow',tablefmt="plain"))
      Ask4=input("Would you like to Order from All DAY Menu? (y/n) ")
      if Ask4=='y':
            p5=[25,45,35,25,30,25]
            print("")
            print("INSTRUCTION:\n1. [Give Orders in serial numbers]\n2. [If there is no order then type '-1']")
            col5=1
            AL=[]
            print("")
            for i in p5:
                  A=int(input("Orders here: "))
                  AL.append(A)
                  if A==-1:
                        break
                  quan5=int(input("~ Enter quantity: "))
                  i=p5[A]*quan5
                  col5+=i
            AL.pop(-1)
            l5=list(AllDay.values())
            M5=l5[0]
            DL.pop(-1)
            l4=list(Dinner.values())
            M4=l4[0]
            print("")
            print("BILL:\nYour Orders:")
            for i in AL:
                  print(">",M5[i])
            for i in DL:
                  print(">",M4[i])
            print("Total Amount:",(col4-1)+(col5-1))
      elif Ask4=='n':
            DL.pop(-1)
            l4=list(Dinner.values())
            M4=l4[0]
            print("")
            print("BILL:\nYour Orders:")
            for i in DL:
                  print(">",M4[i])
            print("Total Amount:",col4-1)
elif Ptime<8 or Ptime>21:
      print("**We are very Sorry\n**Veggie Restraus is Closed...")
else:
      AllDay={'Menu': ['Tea','Coffee','Papdi Chat','Cold Drinks','Ice cream','Sweet (1)'], '':['Rs.25','Rs.45','Rs.35','Rs.25','Rs.30','Rs.25']}
      print("All DAY!\n","\n","Here is your MENuuu")
      print(tabulate(pd.DataFrame(AllDay),headers='firstrow',tablefmt="plain"))
      p5=[25,45,35,25,30,25]
      print("")
      print("INSTRUCTION:\n1. [Give Orders in serial numbers]\n2. [If there is no order then type '-1']")
      col5=1
      AL=[]
      print("")
      for i in p5:
            A1=int(input("Orders here: "))
            AL.append(A1)
            if A1==-1:
                  break
            quan5=int(input("~ Enter quantity: "))
            i=p5[A1]*quan5
            col5+=i
      AL.pop(-1)
      l5=list(AllDay.values())
      M5=l5[0]
      print("")
      print("BILL:\nYour Orders:")
      for i in AL:
            print(">",M5[i])
      print("Total Amount:",col5-1)

#Creating border and thanking
print("THANK YOU for coming in Veggie Restraus".center(250))
print(115*"_")



