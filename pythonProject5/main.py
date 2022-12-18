import webbrowser
import colorama
import datetime


def adoption():
    # adoption of child
    print()
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~WELCOME~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print()
    print(colorama.Fore.GREEN +"READ THE FOLLOWING INSTRUCTIONS CAREFULLY:-")
    print()
    print(colorama.Fore.GREEN +"1) THE PROSPECTIVE ADOPTIVE PARENTS NEED TO BE PHYSICALLY AND MENTALLY STABLE.")
    print(colorama.Fore.GREEN +"2) THEY SHOULD BE FINANCIALLY STABLE.")
    print(colorama.Fore.GREEN +"3) AGE OF ADOPTIVE PARENTS SHOULD BE IN THE RANGE OF 21 TO 50 YEARS.")
    print(colorama.Fore.GREEN +"4) THE ADOPTIVE PARENTS MUST TAKE CARE OF THEIR WARD IN THE FUTURE AND NO PROBLEM SHOULD BE FACED BY THE CHILD IN THE FUTURE.")
    print()

    f=open( "adopt.txt","a")

    def questions():
        print()
        print()
        print(" KINDLY ANSWER THE FOLLOWING QUESTIONS :-")
        print()
        ans1=input ("Q1) of which age group you want a child ? [a)newly born - 2 yrs old b)3yrs old - 7 yrs old c)8yrs old - 14 yrs old] Ans :-")
        print()
        print("Q2) Any specification you want in child ? { ** IF NOT,ENTER NIL}")
        ans2=input ("       a> Any specific skin colour :")
        ans3=input ("       b> Gender of child :")

        return ans1,ans2, ans3

    def rule():
        print()
        print()
        print(colorama.Fore.RED + "YOU NEED TO ATTACH THE FOLLOWING DOCUMENTS FOR VERIFICATION STRICTLY :-")
        print()
        print(colorama.Fore.RED + "1. 2 4*6 SIZE PHOTOGRAPH OF ADOPTIVE PARENT(/S) ")
        print(colorama.Fore.RED + "2. AADHAR CARD ")
        print(colorama.Fore.RED + "3. PAN CARD ")
        print(colorama.Fore.RED + "4. MARRIAGE CERTIFICATE (not for unmarried people)")
        print(colorama.Fore.RED + "5. HIV REPORT ")
        print(colorama.Fore.RED + "6. INCOME CERTIFICATE")
        print()
        print(colorama.Fore.RED + "KINDLY  THESE DOCUMENTS IN THE OFFICE IN THE REQUIRED FORMATS.")
        print()
        print(colorama.Fore.RED + "      !!************************THANK YOU FOR ADOPTING CHILD*******************!!            ")
        print(colorama.Fore.RED +" !!* ***********************MAY YOU HAVE A WONDERFUL LIFE AHEAD****************************!! ")
        print()
        print()
        print("-----------------------------------X------------------------------------X----------------------------------------X-----------------X")
        print()

    # main
    print(colorama.Style.RESET_ALL)
    print(colorama.Back.CYAN + "===) KINDLY FILL THE FORM :")
    print()

    print(colorama.Style.RESET_ALL)
    martial=input ("Are you married or unmarried:")  # ch  ices have given in order the user is a bachelor or couple
    if martial.upper()=="MA RR IED":
        name1=input ("    a> Name of adoptive father:")
        age1=int( input("    b>Age:"))
        occ1=input ("    c>Occupation :")

        print()
        name2=input ("     e> Name of adoptive mother:")
        age2=int( input("    f> Age:"))
        occ2=input ("    g> Occupation :")
        print()

        add=input ("    i> Residential Address : ")
        phone=int( input("    j>Contact Number : "))


        q1,q2,q3=questions()
        rule()
        f.write(  '\n')  # writing in file
        f.write(name1)
        f.write('\n')
        f.write(str(age1))

        f.write('\n')
        f.write(occ1)
        f.write('\n')
        f.write(name2)
        f.write('\n')
        f.write(str(age2))
        f.write('\n')
        f.write(occ2)
        f.write('\n')
        f.write(add)
        f.write('\n')
        f.write(str(phone))
        f.write('\n')

        f.write(q1)
        f.write('\n')
        f.write(q2)
        f.write('\n')
        f.write(q3)
        f.write('\n')

    elif martial.upper()=="UNMARRIED":
        print()
        gender=input("    a> Male or Female : ")
        name=input("    b> Name of adoptive parent:")
        age=int(input("    c> Age :"))
        occ=input("    d> Occupation :")
        print()
        add=input("    f> Residential Address : ")
        phone=int(input("    g> Contact Number : "))



        q1,q2,q3=questions()
        rule()
        f.write('\n')
        f.write(gender)
        f.write('\n')
        f.write(name)
        f.write('\n')
        f.write(str(age))
        f.write('\n')
        f.write(occ)
        f.write('\n')
        f.write(add)
        f.write('\n')
        f.write(str(phone))
        f.write('\n')

        f.write(q1)
        f.write('\n')
        f.write(q2)
        f.write('\n')
        f.write(q3)
        f.write('\n')
        f.close()


    else:

        print()
        print("ERROR !! YOU ENTERED INAPPROPRIATE ANSWER.")
        print("Kindly fill the appropriate word.")
        print("NOW YOU HAVE TO FILL FROM STARTING. ")
        print()
        print(colorama. Fore.RED +"        !!************************************THANK-YOU FOR USING********************************!!")
        print()
        print(colorama.Style.RESET_ALL)



def details():
    global date  #so as to use it inside the function definition as well as in main body
    date=datetime.date.today()

    f=open("inmates_d etails.txt","a")
    while True:
        print()

        print(colorama.Back.YELLOW +" FILL THE FOLLOWING DETAILS FOR ADDING A CHILD :-")
        print()
        print(colorama.Style.RESET_ALL)
        regno=int(input("    a> Enter the serial number :"))
        name=input("    b> Enter the name of the child :")
        gender=input("     c> Enter the gender(male/female) of the child :")
        age=int(input("    d> Enter the current age of the child :"))
        DOB=input("    e> Enter the current age of the child :")
        DOJ=str(date)
        print()
        ans=input(colorama.Fore.RED +" DO YOU WANT TO ADD MORE DATA Y/N: ")
        print()
        rec =str( regno ) +" ,  " +name+ "  , "+ gender+"  ,  "+str (age )+" ,   "+DOB+" , "+DOJ+" . "
        f.write("\n")
        f.write(rec)

        if ans.upper()=='N':
            break
    f.close()
    print()
    print(colorama.Fore.RED +"DATA OF NEW CHILD/CHILDREN HA BEEN ADDED IN THE SOFTWARE .")
    print()
    print(colorama.Style.BRIGHT +"!!================================THANK-YOU=============================!!")
    print()
    print(
        )
    print("------------------------x-----------------------------x---------------------------x---------------------------------x")
    print()
    print(colorama.Style.


RESET_ALL)

def details_read():
    file=open("inmates _details.txt","r")
    print()
    print(colorama.Style.

    RESET_ALL)
    def search_details():
        line=file. read()
        data=line.split( )
        count_boy=0
        count_girl=0
        for x in data:
            if x.upper()=="MALE":
                count_boy+=1
            elif x.upper()=="FEMALE":
                count_girl+=1
        file.close()


        print(colorama.Fore.MAGENTA + "     DOREMON ORPHANAGE   :)) ")
        print()
        print("        Total Nu mber of Girls in orphanage :",count_girl)
        print("        Total N umber of Boys in orphanage :",count_boy)

    search_details()
    print(colorama.Style.RESET_ALL)
    print ( )
    while True:
        reg=int(input("Enter the serial number of child whom you want to  v iew : "))
        FoundPhrase=""
        file1=open('inmates_details.txt',"r")
        for TextLine in file1:
            if str(reg) in TextLine :
                FoundPhrase=TextLine
                break
        else:
            print(" THEIR IS NO ASSOCIAT ED WITH REGISTRATION NUMBER ",reg)
            continue

        lst=FoundPhrase.split()
        reg=lst[0]
        name =lst[2]
        if len (lst)==13:  # decided as per the details added/stored in  v ariables
            sur_name=lst[3]  # if there is surnam e  of the child
            gen=lst[5]
            age=[7]
            dob=lst[9]
            doa=lst[11]
            print()
            print("      -> Reg. no:",reg)
            print("      -> Name :",name)
            print("      -> Second name :",sur_name)
            print("      -> Gender :",gen)
            print("      -> Age :",age)
            print("      -> DOB :",dob)
            print("      -> DOA  :" ,doa)

        elif len(lst)==12:

            gen=lst[4]
            age=lst[6]
            dob=lst[8]
            doa=lst[10]

            print()
            print("      -> Reg. no:",reg)
            print("      -> Name :",name)  # no surname column is specified
            print("       -> Gender :",gen)
            print( "      -> Age :",age)
            print( "      -> DOB :",dob)
            print( "      -> DOA :",doa)

        else:
            pass

        print()
        ans1=input("Do you want to search more children ? " )
        if ans1=="Y":
            continue
        else:
            break
    print()
    print("---------------------------------x-------------------------------x--------------------------x---------------------------------x")
    print()
    def fund():f=open("fund.txt","a")
    while True :
        name=input("Name of person/institution/Trust  : ")
        add=input("Address :")
        print()
        print("Contact details:-")
        contact=int(input("      a> Contact number:") )
        email=input("       b> Email ID : ")
        amt=float(input("Given Amount :" ) )
        gift=input("Other gift/service: " )
        mode=input("Mode of transaction (cash/debit card/cheque) : ")
        ans=input(colorama.Style.RESET_ALL)
        f.write("\n")
        f.write(str(date ))
        rec=name+" ,   "+add + " , "+str(contact) + " , " + email + " ,  \
            "+str (amt) + " ,  " +gift + " , "+ mode +'\n'
        f.write("\n")
        f.write(rec)
        if ans.upper()=='N':
            break

    f.close()
    print()
    print(colorama.Style.BRIGHT +"!!=============================================THANK-YOU FOR THE DONATION==================================!!")
    print()
    print()
    print(
        "--------------------------------x-----------------------------------x------------------------------------x------------------------------x")
    print()
    print(colorama.Style.RESET_ALL)


def links():
    while True:
        print()
        print(" SOME USEFUL LINES ARE GIVEN HERE. ")
        print()
        # print(colorama.Fore.RED +"xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
        print()
        print(colorama.Fore.RED + "     AVAILABLE WEBSITE")
        print("      _____________________________________________________")
        print()
        print(colorama.Fore.RED + "    1> MINISTRY OF WOMEN AND CHILD DEVELOPMENT ")
        print(colorama.Fore.RED + "    2> SAVE CHILD WEBSITE")
        print(colorama.Fore.RED + "    3> AICTE- INDIA")
        print(colorama.Fore.RED + "    4> CARA INDIA")
        print(colorama.Fore.RED + "    5> SMILE FUNDATION INDIA")
        print(colorama.Fore.RED + "    6> CLOSE PROGRAME")
        # print(colorama.Fore.RED + "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
        print(colorama.Style.RESET_ALL)
        print()
        print()

        link = int(input("WHICH WEBSITE DID YOU WANT TO OPEN:"))
        if link == 1:
            webbrowser.open_new_tab("https://www.wcd.nic.in/")
        elif link == 2:
            webbrowser.open_new_tab("https://www.soschildrensvillages.in/")
        elif link == 3:
            webbrowser.open_new_tab("https://www.aicte-india.org/")
        elif link == 4:
            webbrowser.open_new_tab("https://www.smilefoundationindia.org/")
        elif link == 5:
            webbrowser.open_new_tab("https://www.cara.nic.in/")
        elif link == 6:
            print()
            print(colorama.Fore.GREEN + "xxxxx PROGRAM END xxxxx")
            print()
            print()
            print(
                "------------------------x----------------------------x--------------------------x--------------------------------x")
            print()
            break
        else:
            print("ENTER VALID CHOICE")
            choice = input("Enter any key to continue :")


# main

print()
print(
    "!!!=========================================YOU'R WELCOME IN DOREMON ORPHANAGE MANAGEMENT SYSTEM========================================!!!")
print()
while True:
    print()
    print()
    print(
        colorama.Fore.MAGENTA + "                                       *************************************************************************")
    print(
        colorama.Fore.MAGENTA + "                                       *************************************************************************")
    print()
    print(
        colorama.Fore.MAGENTA + "                                       Enter 1 : For adding the information of new child.")
    print(
        colorama.Fore.MAGENTA + "                                       Enter 2 : For viewing data of children off Nishhh Orphanage.")
    print(colorama.Fore.MAGENTA + "                                       Enter 3 : For Adoptation process.")
    print(colorama.Fore.MAGENTA + "                                       Enter 4 : For donation process.")
    print(
        colorama.Fore.MAGENTA + "                                       Enter 5 : For similar institutions and useful websites.")
    print(colorama.Fore.MAGENTA + "                                       Enter 6 : For closing program")
    print()
    print()
    ch = int(input(" Enter your choice :- "))
    if ch == 1:
        details()
    elif ch == 2:
        details_read()
    elif ch == 3:
        adoption()
    elif ch == 4:
        fund()
    elif ch == 5:
        links()
    elif ch == 6:
        print()
        print("THE PROGRAM IS ENDED")
        print()
        print(
            colorama.Fore.RED + "!!!=====================================================THANK-YOU FOR USING THE APPLICATION===================================!!!")

        print()
        break
    else:
        print()
        print(colorama.Back.MAGENTA + "  ENTER CORRECT CHOICE.....")
        print()
        choice = input("Enter any key to continue:")
        print(colorama.Style.RESET_ALL)

