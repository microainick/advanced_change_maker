from os import system
#so the system can talk

#say hello and attempt to do some exception handeling for non mac users
try:
    system('say Hello!')
except OSError:
    print("Sorry you dont have a mac that talks to you")
#this except statement will be written after every system say command

#cashier enters the price
#lets use a while loop to ensure data entry correctness as much as possible
keepitGoing = True
while keepitGoing == True:
    #Loop in here
    #cashier enters purchase price
    pri = input("What is the cost? Use format 00.00: ")
    price = 0
#now i am going to check conditions
#must have positive price
#loop till price is positive
    try: #price could be int or float so must be float type here
        price = float(pri)
        if price < 0:
            print("That's impossible!")
        else:  #when coditions are satisified display entry 
            print("Thank you! " + str(price))
            keepitGoing = False  #use to break out of loop 
            break
    except:  #display help text 
        print("Please input positive number!")

#make decimal
price = float(price)
#produce 100x integer
price = price * 100
#make integer
price = int(price)

#Are you legally old enough to buy items
#run how old.py my age evaluator

#import datetime and use now to check their age
import datetime
now = datetime.datetime.now()

#show date
print(now)
#assign varriable date of years, then months and days.
#and print those values
Current_year = now.year
print(Current_year)
Current_month = now.month
print(Current_month)
Current_day = now.day
print(Current_day)

#run while loop to ensure data entry meets requirments
keepGoing = True
while keepGoing == True:
    #Loop in here
    #assign variable to input from cashier of customer birthdate year
    dob_y = input("Enter your birth year (e.g. 1987): ")
    #create new variable
    idob_y = 0
    try:  #check to see if either one of the 2 coditions are not met
        idob_y = int(dob_y)  #make integer
        if idob_y > 2018 or idob_y < 0000:
            print("That's impossible!")  #loop for bad data entry
        else:  #when succesful display entry
            print("Thank you! " + str(idob_y))
            keepGoing = False
            break  #to get out of loop with conditions allowed
    except:  #display help text
        print("Please input a 4 digit integer!")

#this loop is nearly identical to the preivous.  I copy pasted and changed the variables and conditions
mkeepGoing = True
while mkeepGoing == True:
    #Loop in here
    #get input what month
    dob_m = input("Enter your birth month (e.g. 9): ")
    idob_m = 0 #new variable
    try:  
        idob_m = int(dob_m) #integer
        if idob_m > 12 or idob_m < 1: #ensure entry corresponds to numerical value for a month
            print("That's impossible!")  #loop help text
        else:  #when succesful print and go to break
            print("Thank you! " + str(idob_m))
            mkeepGoing = False
            break
    except:   #display help text
        print("Please input an integer!  (Between 1 and 12)")

#this loop is nearly identical to the preivous.  I copy pasted and changed the variables and conditions
#exception handeler for data entry
dkeepGoing = True
while dkeepGoing == True:
    #Loop in here
    #get input for birthdate days
    dob_d = input("Enter your birth day (e.g. 27): ")
    idob_d = 0
    try:   
        idob_d = int(dob_d)
        #check to see if either one of these two statements is violated
        if idob_d > 31 or idob_d < 1:
            print("That's impossible!")
            #loop for desired input data
        else:  #display data
            print("Thank you!" + str(idob_d))
            dkeepGoing = False
            break #stop loop
    except:  #display help text
        print("Please input an integer!  (Between 1 and 31)")

#make these integers
int(idob_y)
int(idob_m)
int(idob_d)

#make these integers
int(Current_year)
int(Current_month)
int(Current_day)

#print years depending upon the month
print("You are:")

#if the current month is less than persons month of birth
if int(Current_month) < int(idob_m):
    #then they havent had their birthday yet subtract one from years
    ageY = int(Current_year) - int(idob_y) -1
    int(ageY) #make integer
    print(ageY, "years") #display
#if their birthday has happened this year    
elif int(Current_month) > int(idob_m):
    #print difference in years print units
    ageY = int(Current_year) - int(idob_y)
    int(ageY) #integer
    print(ageY, "years") #display
    #now next is else if this means that it is their birth month
    #elif allows the remaining case when birth month is current month
    #so we will compare age with dob day
elif int(Current_day) <= int(idob_d):
    ageY = int(Current_year) - int(idob_y) -1
    #subtracting one if birthday hasnt occured in current month
    int(ageY) #integer
    print(ageY, "years") #display
else:
    #print difference in years print units
    ageY = int(Current_year) - int(idob_y)
    int(ageY) #integer
    print(ageY, "years") #display
    
#print and then assign variable to newMonth
print("and")
#account for the months lived last calendar year after their birthmonth as follows
newMonth = int(12) - int(idob_m) + int(Current_month)
int(newMonth)
#make it an integer then do modulus 12 to display correct months
#it could be the case where this math produces over 12.  mod12 makes it correct
RealMonths = int(newMonth) % 12
#display months old
print(RealMonths, "months old")

#tell cashier of customers age
print("WARNING customer is")

#if the customer is over 21 have the system say or print it
#also deal with exceptions
if ageY >= 21:
    try:
        system('say Atleast 21 years old')
    except OSError: #exception
        print("Sorry you dont have a mac that talks to you")
        system('say Atleast 21 years old')
        print("Atleast 21 years old") #alternative to say
#if the customer is under 21 but over 18, have the system say or print it
#also deal with exceptions
elif ageY >= 18:
    try:
        system('say 18 but not 21')
    except OSError: #exception
        print("Sorry you dont have a mac that talks to you")
        system('say 18 but not 21')
        print("18 but not 21") #alternative to say
else:
#for all other cases person must be under 18
#exception handeling for system say
    try:
        system('say Under 18')
    except OSError: #exception
        print("Sorry you dont have a mac that talks to you")
        system('say Under 18')
        print("Under 18!") #alternative to say

input("Check products for age restrictions and press enter")
#halt the program to make sure this is not ignored

keepcGoing = True
while keepcGoing == True:
    #Loop in here
    #get input for amount to pay
    #make decimal
    #produce 100x integer
    #make integer
    cashten = input("What is the amount you would like to pay? 00.00")
    cashten = float(cashten)
    cashten = cashten * 100
    cashten = int(cashten)
    CashTendered = 0
    try:  #make sure they are paying enough
        CashTendered = int(cashten) #integer
        #do not values less than total cost
        if CashTendered < price: 
            print("That's not enough! Please re-enter the amount you would like to pay")    
        else: #if correct then display data entered and break out of loop
            print("Thank you!" + str(CashTendered))
            keepcGoing = False
            break
    except:  #display help text
        print("Please pay for your item")


#print both values for visualization of subtraction
print(CashTendered)
print(price)
#create variable for change due from subtraction
ChangeDue = CashTendered - price
#print change due
print(ChangeDue)

#if statement to indicate the entire price has been payed
if ChangeDue >= 0:
    print("Give All Items to customer")
    try:
        system('say thank you for your purchase and please come again.  Also do not forget to take your change from your friendly raspberry pi smart robot cashier')
        #refer to the rpi robot ;) thank customer and remind them to take change
    except OSError:  #exception
        print("Sorry you dont have a mac that talks to you")

#divide by 20 x 100 for units on 20$
#flor division and modulus for units of Twenties to pay out and remainder to update ChangeDue
Twenties = ChangeDue // 2000
ChangeDue = ChangeDue % 2000

#exactly the same for 10's with obvious changes will I will no longer be addressing in my code
#I hope that is ok it changes relative to the denominations in all of the following
Tens = ChangeDue // 1000
ChangeDue = ChangeDue % 1000

#same process
Fives = ChangeDue // 500
ChangeDue = ChangeDue % 500

#same process 
Ones = ChangeDue // 100
ChangeDue = ChangeDue % 100

#same now for coins
Quarters = ChangeDue // 25
ChangeDue = ChangeDue % 25

#same
Dimes = ChangeDue // 10
ChangeDue = ChangeDue % 10

#same
Nickels = ChangeDue // 5
ChangeDue = ChangeDue % 5
#remainder of Change Due must be [0,4] and is assigned directly to pennies to return
Pennies = ChangeDue
#print values to return
print("Please. Give the customer the following bills and coins")
print("Twenties: ", Twenties)
print("Tens:  ", Tens)
print("Fives:  ", Fives)
print("Ones:  ", Ones)
print("Quarters:  ", Quarters)
print("Dimes:  ", Dimes)
print("Nickels:  ", Nickels)
print("Pennies:  ", Pennies)
