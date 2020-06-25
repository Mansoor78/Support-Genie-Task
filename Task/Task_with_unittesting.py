import random
import unittest

# l.append(["agent1","yes","25",["sales","support","spanish speaker"]])
# l.append(["agent2","no","40",["sales"]])
# l.append(["agent3","yes","80",["sales","support"]])
# l.append(["agent4","yes","60",["support","spanish speaker","marketing"]])


def issue(l):
    issue=input("enter issues separated by comma: ").split(",") #for getting the issue
    sel_mode=input("Selection mode (all_available, least_busy, random): ") #for getting the selection mode

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
        if(i[1]=="yes" or i[1]=="YES" or i[1]=="Yes"): #execute if the agent availability is yes
            if(sel_mode=="all_available" or sel_mode=="ALL_AVAILABLE" or sel_mode=="All_Available"): #if the selection mode is all_availabe
                for j in i[-1]:
                    if j in issue:
                        lst.append(i[0])
            if(sel_mode=="least_busy" or sel_mode=="LEAST_BUSY" or sel_mode=="Least_busy"): #if the selection mode is least_busy
                ma=max(s)
                for j in i[-1]:
                    if ((j in issue) and (i[2]==ma)):
                        lst1.append(i[0])
            if(sel_mode=="random" or sel_mode=="Random" or sel_mode=="RANDOM"): #if the selection mode is Random
                for j in i[-1]:
                    if j in issue:
                        lst2.append(i[0])
    if(sel_mode=="all_available" or sel_mode=="ALL_AVAILABLE" or sel_mode=="All_Available"):
        for i in lst:
            if i not in o:
                o.append(i)
        if len(o)>0:
            print(*o,sep="\n")
            return o
        else:
            print("No agents matching")
    if(sel_mode=="least_busy" or sel_mode=="LEAST_BUSY" or sel_mode=="Least_busy"):
        for i in lst1:
            if i not in o1:
                o1.append(i)
        if len(o1)>0:
            print(*o1,sep="\n")
            return o1
        else:
            print("No agents matching")


    if(sel_mode=="random" or sel_mode=="Random" or sel_mode=="RANDOM"):
        for i in lst2:
            if i not in o2:
                o2.append(i)
        if len(o2)>0:
            print(random.choice(o2))
            return random.choice(o2)
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

l1=["agent1","agent2"]
class check(unittest.TestCase):
    def test(self):
        self.assertEqual(issue(l),l1)
"""
Test case 1:
Number of agents : 4
Name:agent1  is_avail=yes avail_since=67 roles=[sales, support]
Name:agent2  is_avail=yes avail_since=45 roles=[sales, support, spanish]
Name:agent3  is_avail=no avail_since=89 roles=[support]
Name:agent4  is_avail=yes avail_since=27 roles=[marketing, tamil,banking]
Issue:sales,support
selection_mode=all_available
Output: [agent1,agent2] Ran 1 test

Test case 2:
Number of agents : 4
Name:agent1  is_avail=yes avail_since=67 roles=[sales, support]
Name:agent2  is_avail=yes avail_since=45 roles=[sales, support, spanish]
Name:agent3  is_avail=no avail_since=89 roles=[support]
Name:agent4  is_avail=yes avail_since=27 roles=[marketing, tamil,banking]
Issue:sales
selection_mode=least_busy
Output: [agent1] Ran 1 test

Test case 3:
Number of agents : 4
Name:agent1  is_avail=yes avail_since=67 roles=[sales, support]
Name:agent2  is_avail=yes avail_since=45 roles=[sales, support, spanish]
Name:agent3  is_avail=no avail_since=89 roles=[support]
Name:agent4  is_avail=yes avail_since=27 roles=[marketing, tamil,banking]
Issue:sales
selection_mode=random
Output: agent1 or agent2 Ran 1 test
"""

if __name__ == '__main__':
    unittest.main()
