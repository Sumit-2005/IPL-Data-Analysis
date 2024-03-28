76#importing libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#loading the csv
csv=pd.read_csv("C:\\Sumit\\Python Project (IPL Data Analysis)\\matches.csv",index_col=0)

#_____________________________________________________________________________________________________________________________________________________________________________


def intro():
    t='Thank You!'
    print("\t\tCricket is a sport that everyone is well versed with specially in India and speaking if cricket events, every cricket fan admiits that there's no bigger\
          \t\t\t\t\t\t\t\t\t\t\tcricket league in the world than the")
    print()
    print("\t\t\t\t\t\t\t\t\t\t******  *******  **      ")
    print("\t\t\t\t\t\t\t\t\t\t******  *******  **      ")
    print("\t\t\t\t\t\t\t\t\t\t  **    **   **  **      ")
    print("\t\t\t\t\t\t\t\t\t\t  **    *******  **      ")
    print("\t\t\t\t\t\t\t\t\t\t  **    **       **      ")
    print("\t\t\t\t\t\t\t\t\t\t******  **       ******* ")
    print("\t\t\t\t\t\t\t\t\t\t******  **       ******* ")
    print()
    print("\t\t\t\t\t   Yes, THE INDIAN PREMIER LEAGUE. This project is dedicated to data analysis of some IPL matches")
    print(t.center(183))


def p():
    print("The CSV contains detils about IPL matches from the 2008 season to the 2019 season")
    print("It has about 750 rows and contains columns like team names, ground location, toss winner, match winner and much more")
    print("Here is the CSV")
    print(csv)

def col():
    x=csv.columns
    print("Column Names are")
    print(x)

def tr():
    print("Total rows available - 755")
    n=int(input("Enter the number of rows to be viewed from the top:"))
    y=csv.head(n)
    print(y)

def br():
    print("Total rows available - 755")
    n=int(input("Enter the number of rows to be viewed from the bottom:"))
    y=csv.tail(n)
    print(y)

def sr():
    print("IDs available from 1 to 755")
    n=int(input("Enter the ID of the row you want to see:"))
    x=csv.loc[n]
    print(x)

def sprec():
    print("IDs available from 1 to 755")
    print("Column names are")
    col()
    n=int(input("Enter the ID you want to see:"))
    c=input("Enter the column name for the record you want to see:")
    x=csv.at[n,c]
    print(x)

def tena():
    print("All the team names are displayed below")
    x=csv.team1.unique()
    print(x)

def wnr():
    print("Total match IDs available - 755")
    x=int(input("Enter the match ID for the match winner:"))
    n=csv.at[x,'winner']
    print("The match winner was",n,"!")

def tswnr():
    print("Total match IDs available - 755")
    n=int(input("Enter the match ID for the toss winner:"))
    x=csv.at[n,'toss_winner']
    x1=csv.at[n,'toss_decision']
    print("The toss was won by",x,"and chose to",x1)

def city():
    print("Total match IDs available - 755")
    n=int(input("Enter the match ID for the venue details:"))
    x=csv.at[n,'city']
    x1=csv.at[n,'venue']
    print("The match was held in",x1,"in the city of",x)

def date():
    print("Total match IDs available - 755")
    n=int(input("Enter the match ID for the date:"))
    x=csv.at[n,'date']
    print("The match was held on",x)

def umpire():
    print("Total match IDs available - 755")
    n=int(input("Enter the match ID for the Umpire names:"))
    x=csv.at[n,'umpire1']
    x1=csv.at[n,'umpire2']
    print("Umpire 1 was",x)
    print("Umpire 2 was",x1)

def pom():
    print("Total match IDs available - 755")
    n=int(input("Enter the match ID for the Man of the match:"))
    x=csv.at[n,'player_of_match']
    print("The man of the match was awarded to",x)

def margin():
    print("Total match IDs available - 755")
    n=int(input("Enter ID:"))
    x=csv.at[n,'win_by_runs']
    if x!=0:
        print(csv.at[n,'winner'],"won by",x,"runs")
    if x==0:
        y=csv.at[n,'win_by_wickets']
        if y==0:
            print("Match tied")
            a=csv.at[n,'winner']
            print(a,"won the super over")
    else:
        print(csv.at[n,'winner'],"won by",csv.at[n,'win_by_wickets'],"wickets")
    


def dataanal():
    print("\t 1. Dataset Analysis")
    print("\t 2. Match Analysis")
    print("\t 3. Exit")
    n=int(input("Enter your choice:"))
    if n==1:
        setanal()
    if n==2:
        matanal()
    if n==3:
        start()
    else:
        print("Invalid Option")
        dataanal()

    
def start():
    print("\t 1. Introduction")
    print("\t 2. Data Analysis Options")
    print("\t 3. Graph")
    print("\t 4. Exit")
    n=int(input(" Enter your choice:"))
    if n==1:
        intro()
        start()
    elif n==2:
        dataanal()
    elif n==3:
        print("You'll be comparing the number of matches won by teams in a particular season")
        matwon()
    elif n==4:
        print("\t\t\t\t\t\t Thank You for using my IPL DATA ANALYSIS Project. I Hope you liked it, Thank You!")
    else:
        print("Invalid Option")
        


def setanal():
    print("\t 1. View the dataset")
    print("\t 2. View the column names")
    print("\t 3. View n rows from the top of the dataset")
    print("\t 4. View n rows from the bottom of the dataset")
    print("\t 5. View a specific row")
    print("\t 6. View a specific Record (single cell) ")
    print("\t 7. Exit")
    n=int(input("Enter your choice:"))
    if n==1:
        p()
        setanal()
    if n==2:
        col()
        setanal()
    if n==3:
        tr()
        setanal()
    if n==4:
        br()
        setanal()
    if n==5:
        sr()
        setanal()
    if n==6:
        sprec()
        setanal()
    if n==7:
        dataanal()
    else:
        print("Invalid Option")
        setanal()


def matanal():
    print("\t 1. View the team names")
    print("\t 2. Check match winner in a specific match")
    print("\t 3. Check toss winner in a specific match")
    print("\t 4. Venue details for a match")
    print("\t 5. Check the date of the match")
    print("\t 6. Check the umpires of the match")
    print("\t 7. Check the Man of the match award")
    print("\t 8. Check match win margin")
    print("\t 9. Exit")
    n=int(input("Enter your choice:"))
    if n==1:
        tena()
        matanal()
    if n==2:
        wnr()
        matanal()
    if n==3:
        tswnr()
        matanal()
    if n==4:
        city()
        matanal()
    if n==5:
        date()
        matanal()
    if n==6:
        umpire()
        matanal()
    if n==7:
        pom()
        matanal()
    if n==8:
        margin()
        matanal()
    if n==9:
        dataanal()
    else:
        print("Invalid Option")
        matanal()
    

def matwon():
    n=int(input("Enter the number of teams you want to compare:"))
    x=int(input("Enter the year of the season(from 2008 to 2019):"))
    new=csv[csv['season']==x]
    a=new['winner'].tolist()
    a1=[]
    a2=[]
    team=new.team1.unique()
    print("Team names are",team)
    for i in range(n):
        q1=input("Enter the team names:")
        e1=a.count(q1)
        a1.append(q1)
        a2.append(e1)
    plt.bar(a1,a2,label=a1,color=['r','b','g','y'])
    plt.xlabel("Team Names")
    plt.ylabel("NO. of Wins")
    plt.xticks(rotation='vertical')
    plt.title("Matches won by teams in a particular season")
    plt.grid(True)
    plt.legend()
    plt.show()
    
    
    


    
    
    
            
