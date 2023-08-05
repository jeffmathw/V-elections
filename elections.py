import pickle
import matplotlib.pyplot as plt
import mysql.connector as sqlcont
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from os import system,name
from subprocess import call
from goto import with_goto




mycon=sqlcont.connect(host="localhost",user="root",password='root123',
                      database="result")
cursor=mycon.cursor()

def clrscr():
    if name=='nt':
        _=system('cls')
def confirm():
    x=input("\nPress enter to continue.")
def back1():
    print("\nProceeding will require you to enter information.\n")
    ch=input("Do you want to go back?(yes|no) : ")
    print()
    if ch in ('y','yes','YES','Y'):
        candidate()
def back2():
    print("\nProceeding will require you to enter information.\n")
    ch=input("Do you want to go back?(yes|no) : ")
    print()
    if ch in ('y','yes','YES','Y'):
        vote()
    
def exit1():
    sys.exit()
    
def display(st):
    print(st)
    s=list(st)
    if s[1]=='\t':
        print('\t\t','   ','-'*len(st),'\n')
    else:
        print('-'*len(st),'\n')
    
#add candidates.dat file if not present.the main program starts here.
      
def candidate():
    clrscr()
    st="\nWELCOME TO THE CANDIDATE'S PAGE\n"
    display(st)
    print("1.Add a candidate\n\n2.View candidates\n\n3.Delete candidate\n\n4.Update candidates\n\n5.RETURN\n\n")
    ch=input("Enter choice : ")
    if ch=='1':
        add()
    elif ch=='2':
        flag=0
        view(flag)
    elif ch=='3':
        delete()
    elif ch=='4':
        update()
    elif ch=='5':
        main()
    else:
        print("wrong input\n")
        candidate()

def add():
    clrscr()
    st="\nAdd candidate\n"
    display(st)
    back1()
    name=input("Please enter candidate name : ")
    symbol=input("\nPlease enter candidate symbol : ")
    post=input("\nEnter the post you are standing for : ")
    l1=[name,symbol,post]
    f=open(name+'.dat','wb')
    pickle.dump(l1,f)
    ch=input("\nWould you like to add a bio(yes/no) : ")
    if ch=='yes':
        bio=input("YOU CAN ENTER YOUR BIO HERE : ")
        pickle.dump(bio,f)
        f.close()
        
    f1=open("candidates.dat",'rb')   #adds name into candidate file
    l1=pickle.load(f1)
    l1.append(name)
    f2=open("candidates.dat",'wb')
    pickle.dump(l1,f2)
    f1.close()
    
    confirm()
  

def delete():
    clrscr()
    st="\nDelete candidate.\n"
    display(st)
    print("\nHERE IS A LIST OF ALL THE CANDIDATES\n")
    f=open("candidates.dat",'rb')
    l=pickle.load(f)
    f.close()
    print("TOTAL NUMBER OF CANDIDATES = ",len(l),"\n")
    if len(l)==0:
        print("THERE ARE NO CANDIDATES.\n")
    else:
        for i in range(0,len(l)):
            print(i+1,".",l[i],'\n')

    back1()
    nam=input("Enter name of the candidate to be deleted : ")
    f=open("candidates.dat",'rb')
    l=pickle.load(f)
    f.close()
    if nam in l:
        l.remove(nam)
        f1=open("candidates.dat",'wb')
        pickle.dump(l,f1)
        f1.close()
        print("\nYour account has been successfully deleted.")
    else:
        print("\nThere is no candidate named ",nam,'.')
    confirm()


def update():
    clrscr()
    st="\nUpdate candidate.\n"
    display(st)
    print("\nHERE IS A LIST OF ALL THE CANDIDATES\n")
    f=open("candidates.dat",'rb')
    l=pickle.load(f)
    f.close()
    print("TOTAL NUMBER OF CANDIDATES = ",len(l),"\n")
    if len(l)==0:
        print("THERE ARE NO CANDIDATES.")
    else:
        c=0
        for i in range(0,len(l)):
            print(i+1,".",l[i],'\n')
        back1()
        nam=input("Type the candidates name to update details : ")
        if nam in l:
            f=open(nam+'.dat','rb')
            x=pickle.load(f)
            try:
                y=pickle.load(f)
            except:
                y='Bio of this candidate is not available.'
            clrscr()
            f.close()
            print("\nCANDIDATE DETAILS.\n")
            print("NAME\t\t\t",x[0],"\nCANDIDATE SYMBOL\t",x[1],
                  "\nStanding for the post\t",x[2],"\nBIO\t\t\t",y,"\n")
            print("1.Update symbol.\n2.Update post\n3.Edit bio\n")
            ch=int(input("enter choice : "))
            if ch==1:
                symbol1=input("Enter new symbol : ")
                x[1]=symbol1
            elif ch==2:
                post1=input("Enter new post : ")
                x[2]=post1
            f2=open(nam+'.dat','wb')
            pickle.dump(x,f2)
            pickle.dump(y,f2)
            if ch==3:
                print("\n1.Delete bio\n2.New bio\n")
                ch1=int(input("Enter choice : "))
                if ch1==2:
                    bio1=input("Enter new bio : ")
                    y=bio1
                    pickle.dump(y,f2)
            f2.close()
            print("\nYour file has updated successfully.Go to view candidates to see changes.")
        else:
            print("\nSorry.But there is no candidate named ",nam,"\n")

    confirm()
    
            
#----------------------------------------------------------------------------------------------------------------------------------    
def vote():
    clrscr()
    st="\nWELCOME TO THE VOTER'S PAGE\n"
    display(st)
    print("1.Current elections\n\n2.New election\n\n3.Stop election\n\n4.View candidates\n\n5.RETURN\n")
    ch=input("Enter choice : ")
    if ch=='1':
        celections()
    elif ch=='2':
        nelections()
    elif ch=='3':
        stopelection()
    elif ch=='4':
        flag=1
        view(flag)
    elif ch=='5':
        main()
    else:
        print("wrong input\n")
        vote()
        
def celections():       #view elections
    clrscr()
    st="\nHere are the current elctions.Choose any to vote.\n"
    display(st)
    f=open("elections.dat",'rb')
    bl=pickle.load(f)
    print("Total number of elections = ",len(bl))
    if len(bl)==0:
        print("\nThere are no elections.")
        confirm()
    else:
        for i in range(0,len(bl)):
            print(i+1,'.',bl[i],'\n')
        back2()
        ename=input("Enter election name to choose : ")
        if ename in bl:
            f=open(ename+'.dat','rb')
            l=pickle.load(f)
            f.close()
            voting(l,ename)
        else:
            print("\nThis election is not present.\n")
            confirm()
            
            
    
def voting(l,ename):                            #z is to bulletin
    l3=[]
    d1={}
    while(1):                                                   #very important #core of the program
        clrscr()
        z=0
        st="\n\t\t\tWELCOME TO THE VOTING PAGE.\n"
        display(st)
        print("Here are the candidates for this post.\n")                                    
        f=open("candidates.dat",'rb')           
        l1=pickle.load(f)
        
        print("Candidate Name\t\t\tPost\n")
        for i in range(0,len(l1)):
            f2=open(l1[i]+'.dat','rb')
            l2=pickle.load(f2)                          #l2=candidate acc - [name,symbol,post]   
            if l2[2]==l[1]:                             #l=election acc - [ename,count,post]
                z+=1                                        
                print(z,'.',l2[0],'\t\t\t',l2[1],'\n')
                l3.append(l2[0])                    
        vote=input("\nEnter the name who you wish to vote : ")
        f3=open(ename+'.dat','rb')
        x=pickle.load(f3)
        try:
            d1=pickle.load(f3)
            c1=d1[vote]
        except:
            c=0
        else:
            c=c1
        if vote in l3:
            c+=1
            d1[vote]=c
            f3=open(ename+'.dat','wb')
            pickle.dump(l,f3)
            pickle.dump(d1,f3)
            print("\nYour vote has been successfully recorded.")
    
        else:
            print("\nThe name is not present.\n")

        ch=input("Do you want to stop voting : ")
        if ch=='yes':
            break
    
    confirm()    
        
def nelections():
    clrscr()
    bl=[]
    st="\nHere you can create a new election.\n"
    display(st)
    back2()
    ename=input("Enter election name : ")
    post=input("\nEnter name of the post which the voters are going to vote : ")
    print("\nYou have created a new election.Check current elections to vote.")
    l=[ename,post]
    f1=open(ename+'.dat','wb')
    pickle.dump(l,f1)
    f1.close()
    
    f=open("elections.dat",'rb')
    bl=pickle.load(f)
    bl.append(ename)
    f1=open("elections.dat",'wb')
    pickle.dump(bl,f1)
    f.close()
    confirm()

def stopelection():
    clrscr()
    st="\nStop an election.\n"
    display(st)
    print("\nHere are the current elctions.Choose any to delete\n")
    f=open("elections.dat",'rb')
    bl=pickle.load(f)
    print("Total number of elections = ",len(bl))
    if len(bl)==0:
        print("\nThere are no elections.")
        confirm()
    else:
        for i in range(0,len(bl)):
            print(i+1,'.',bl[i],'\n')
    back2()
    ename=input("Enter name of the election to be stopped : ")
    f=open("elections.dat",'rb')
    l=pickle.load(f)
    f.close()
    if ename in l:
        l.remove(ename)
        f=open("elections.dat",'wb')
        pickle.dump(l,f)
        f.close()
        
        f3=open(ename+'.dat','rb')
        x=pickle.load(f3)
        post=x[1]
        try:
            y=pickle.load(f3)
        except:
            print("\nNo vote has taken place in this election\n")
        else:
            a=input("\nThe election has been successfully stopped.\nPress enter to view results.")
            p=list(y.keys())
            q=list(y.values())
            w=p[q.index(max(q))]
            print(w,' has won the election with ',max(q),' votes.')

            o=open("tools.dat",'rb')
            record=pickle.load(o)
            ecode=pickle.load(o)
            o.close()
            ecode=ecode+1

            
            for i in range(len(p)):
                record+=1
                sql = "INSERT INTO results (recno,ecode,ename,post,cname,vote) VALUES (%s,%s,%s,%s,%s,%s)"
                val = (record,ecode,ename,post,p[i],q[i])
                cursor.execute(sql, val)
                mycon.commit()
                
            o1=open("tools.dat",'wb')
            pickle.dump(record,o1)
            pickle.dump(ecode,o1)
            o1.close()
    else:
        print("\nThere is no election named ",ename,'.')
    confirm()


def view(flag):
    clrscr()
    st="\nHERE IS A LIST OF ALL THE CANDIDATES\n"
    display(st)
    f=open("candidates.dat",'rb')
    l=pickle.load(f)
    f.close()
    print("TOTAL NUMBER OF CANDIDATES = ",len(l),"\n")
    if len(l)==0:
        print("THERE ARE NO CANDIDATES.")
    else:
        for i in range(0,len(l)):
            print(i+1,".",l[i],'\n')
        ch=input("Do you want to go back?(yes|no) : ")
        if ch in ('y','yes','YES','Y'):
            if flag==0:
                candidate()
            else:
                vote()
        nam=input("Type the candidates name to view details : ")
        if nam in l:
            f=open(nam+'.dat','rb')
            x=pickle.load(f)
            try:
                y=pickle.load(f)
            except:
                y='Bio of this candidate is not available'
            clrscr()
            print("\nCANDIDATE DETAILS.\n")
            print("NAME\t\t\t",x[0],"\nCANDIDATE SYMBOL\t",x[1],
                  "\nStanding for the post\t",x[2],"\nBIO\t\t\t",y,"\n")
        else:
            print("\nSorry.But there is no candidate named ",nam,"\n")
    confirm()
    if flag==0:
        candidate()
    else:
        vote()


def results():
    clrscr()
    st="\nThe results of elections are displayed here.\n"
    display(st)
    print("1.Current elections\n\n2.Finished elections\n\n3.RETURN\n")
    ch=input("enter choice : ")
    if ch=='1':
        f2=open("elections.dat",'rb')
        ename=pickle.load(f2)
        f2.close()
        if ename==[]:
            print("There are no elections currently available.\n")
            
        else:
            clrscr()
            p=[]
            print("\nHere is the list of all  current elections.\n")
            for z in range(0,len(ename)):
                print(z+1,'. ',ename[z],'\n')
            i=input('\nEnter election name to view results : ')
            if i in ename:
                f3=open(i+'.dat','rb')
                x=pickle.load(f3)
                try:
                    y=pickle.load(f3)
                except:
                    print('\nThis election has not started yet.\n')
                else:
                    cname=list(y.keys())
                    votes=list(y.values())      #y is a dictionary
                    print("candidate name\t\tvotes\t\tpercentage")
                    for i in range(0,len(cname)):
                        per=(votes[i]/sum(votes))*100
                        p.append(per)
                        print(i+1,'.',cname[i],'\t\t',votes[i],'\t\t',per,'%\n')
                    print("Maximum votes for ",cname[votes.index(max(votes))],'\n')
                    print("Minimum votes for ",cname[votes.index(min(votes))],'\n')
                    print("total votes : ",sum(votes),'\n')
                    print(cname[votes.index(max(votes))]," is currently leading with ",max(p),'% of total votes.')
    
                    ch=input("Load graph? : ")
                    if ch=='yes':
                        plt.bar(cname,votes,color="yellow")
                        plt.xlabel("Candidates ------>")
                        plt.ylabel("No. of votes ------>")
                        plt.title("Results")
                        plt.show()
                    confirm()
            else:
                print("\nThis election is not present.")
                
    elif ch=='2':
        print("\nWelcome to the election database\nHere you can view all records\n")
        cursor.execute('select ename,ecode from results group by ecode')
        data=list(cursor.fetchall())
        print("ecode\t\t\tename\n")
        for row in data:
            print(row[1],'\t\t\t',row[0])
            
        ename=int(input("\nChoose any election code to view details : "))
        clrscr()
        cursor.execute('select * from results where ecode=%s'%(ename,))
        data=cursor.fetchall()
        print("\nelection code is : ",data[0][1],"\n")
        print("election name : ",data[0][2],"\n")
        print("post of this election is : ",data[0][3],"\n")
        print("record no.\tcname\t\tvotes\n")
        for row in data:
            row=list(row)
            if len(row[4])>5:
                print(row[0],'\t\t',row[4],'\t',row[5],'\n')
            else:    
                print(row[0],'\t\t',row[4],'\t\t',row[5],'\n')

        cursor.execute('select cname from results where vote=(select max(vote) from results where ecode=%s)'%(ename,))
        data1=cursor.fetchone()
        print(data1[0],' won this election.\n')

        cursor.execute('select sum(vote) from results where ecode=%s'%(ename,))
        data=cursor.fetchone()
        print('total votes taken place in this election : ',data[0])

    elif ch!='3':
        print("Wrong input.")
        results()

    confirm()
    
def main():
    while(1):
        clrscr()
        call('color b', shell=True)    #this sets the color to light blue
        st="\n\t\t\tWELCOME TO VELECTIONS\n"
        display(st)
        print("1.CANDIDATE'S PAGE\n\n2.VOTER'S PAGE\n\n3.Results\n\n4.EXIT\n\n")
        ch=input("Enter choice : ")
        if ch=='1':
            candidate()
        elif ch=='2':
            vote()
        elif ch=='3':
            results()
        elif ch=='4':
            clrscr()
            x=input("press start button to restart.\nor exit button to exit.")
            break
        else:
            print("\nWrong input.")
            confirm()

def popup():
    f=open("help.txt",'r')
    st=f.read()
    x = messagebox.showinfo("Message",st)
    
def info():
    clrscr()
    call('color e', shell=True)
    f=open("info.txt",'r')
    for i in f:
        print(i)
    f.close()


window=Tk()
window.geometry("312x500")
window.title('program')

label=Label(window,text=" THE ELECTIONS APP ",fg="brown" ).pack()

Button(window,text="START",fg="red",height=5,width=30,command=main).pack()
Button(window,text="README",fg="red",height=5,width=30,command=popup).pack()
Button(window,text="INFO",fg="red",height=5,width=30,command=info).pack()
Button(window, text = "EXIT", command = exit1).pack()
        
icon =ImageTk.PhotoImage(Image.open("logo.jpg"))
label1=Label(window,image=icon).pack()
    
window.mainloop()
    

        

