import random

# l.append(["agent1","yes","25",["sales","support","spanish speaker"]])
# l.append(["agent2","no","40",["sales"]])
# l.append(["agent3","yes","80",["sales","support"]])
# l.append(["agent4","yes","60",["support","spanish speaker","marketing"]])


def issue(l):
    issue=input("enter issues separated by comma: ").split(",")
    sel_mode=input("Selection mode (all_available, least_busy, random): ")

    lst=[]
    lst1=[]
    lst2=[]

    o=[]
    o1=[]
    o2=[]
    s=[]
    for i in l:
        s.append(i[2])
    for i in l:
        if(i[1]=="yes" or i[1]=="YES" or i[1]=="Yes"):
            if(sel_mode=="all_available" or sel_mode=="ALL_AVAILABLE" or sel_mode=="All_Available"):
                for j in i[-1]:
                    if j in issue:
                        lst.append(i[0])
            if(sel_mode=="least_busy" or sel_mode=="LEAST_BUSY" or sel_mode=="Least_busy"):
                ma=max(s)
                for j in i[-1]:
                    if ((j in issue) and (i[2]==ma)):
                        lst1.append(i[0])
            if(sel_mode=="random" or sel_mode=="Random" or sel_mode=="RANDOM"):
                for j in i[-1]:
                    if j in issue:
                        lst2.append(i[0])
    if(sel_mode=="all_available" or sel_mode=="ALL_AVAILABLE" or sel_mode=="All_Available"):
        for i in lst:
            if i not in o:
                o.append(i)
        if len(o)>0:
            print(*o,sep="\n")
        else:
            print("No agents matching")
    if(sel_mode=="least_busy" or sel_mode=="LEAST_BUSY" or sel_mode=="Least_busy"):
        for i in lst1:
            if i not in o1:
                o1.append(i)
        if len(o1)>0:
            print(*o1,sep="\n")
        else:
            print("No agents matching")

    if(sel_mode=="random" or sel_mode=="Random" or sel_mode=="RANDOM"):
        for i in lst2:
            if i not in o2:
                o2.append(i)
        if len(o2)>0:
            print(random.choice(o2))
        else:
            print("No agents matching")

l=[]
n=int(input("Enter Number of agents: "))
for i in range(n):
    name=input("Enter name : ")
    is_avail=input("Is the agent available(yes or no): ")
    avail_since=input("the agent had been available since(in mins): ")
    roles=input("Enter the roles of the agent separated by comma: ").split(",")
    a=[name,is_avail,avail_since,roles]
    l.append(a)
issue(l)
