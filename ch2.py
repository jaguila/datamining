#Data Mining Ch. 2


#####Choices for type of formula to implement are based on the following criterie
#####    if grade inflation(where each user may use a different scale) - use Pearsons
#####    if data is dense(mostly non zeros) and magnitude matters - use manhattan or euclidean
#####    if data is sparse - use cosine


#Manhattan distance
#|x1-x2|+|y1-y2| where you try to find the distance of known datapoints from your datapoint in question coordinates
#note only find the difference when both exist

#Euclidean distance or pythagorean 
#((x1-x2)^2+(y1-y2)^2))^(1/2)

## pearsons
## [sum(xy)-sum(x)sum(y)/n]/[sqrt(sum(x**2)-(sum(x)**2)/n)*sqrt(sum(y**2)-(sum(y)**2)/n)

##cos
##x dot y/||x||*||y||

## k nearest


####CODE BELOW#####



from xlrd import open_workbook
import math
from math import sqrt
from collections import defaultdict
from operator import itemgetter

Hailey=["x",1,2]
#print Hailey
#print sum(int(x) for x in Hailey)
#excel=open_workbook("C:\dex\datascience\datamining\ch2.xlsx",on_demand=True)
#for i in excel.sheet_by_name("Sheet1").col(0):
#music=excel.sheet_by_name("Sheet1").col(0)[1:]
#hail=excel.sheet_by_name("Sheet1").col(1)[1:]
#excel1=excel.sheet_by_name("Sheet1")
#veron=excel1.col(2)[1:]
#hail1=dict(zip(music,hail))
#veronica=dict(zip(music,veron))
#hail=[0,4,1,4,0,0,4,1]
#veron=[3,0,0,5,4,2.5,3,0]
#jord=[0,4.5,4,5,5,4.5,4,4]

users = {"Angelica": {"Blues Traveler": 3.5, "Broken Bells": 2.0, "Norah Jones": 4.5, "Phoenix": 5.0, "Slightly Stoopid": 1.5, "The Strokes": 2.5, "Vampire Weekend": 2.0},
         "Bill":{"Blues Traveler": 2.0, "Broken Bells": 3.5, "Deadmau5": 4.0, "Phoenix": 2.0, "Slightly Stoopid": 3.5, "Vampire Weekend": 3.0},
         "Chan": {"Blues Traveler": 5.0, "Broken Bells": 1.0, "Deadmau5": 1.0, "Norah Jones": 3.0, "Phoenix": 5, "Slightly Stoopid": 1.0},
         "Dan": {"Blues Traveler": 3.0, "Broken Bells": 4.0, "Deadmau5": 4.5, "Phoenix": 3.0, "Slightly Stoopid": 4.5, "The Strokes": 4.0, "Vampire Weekend": 2.0},
         "Hailey": {"Broken Bells": 4.0, "Deadmau5": 1.0, "Norah Jones": 4.0, "The Strokes": 4.0, "Vampire Weekend": 1.0},
         "Jordyn":  {"Broken Bells": 4.5, "Deadmau5": 4.0, "Norah Jones": 5.0, "Phoenix": 5.0, "Slightly Stoopid": 4.5, "The Strokes": 4.0, "Vampire Weekend": 4.0},
         "Sam": {"Blues Traveler": 5.0, "Broken Bells": 2.0, "Norah Jones": 3.0, "Phoenix": 5.0, "Slightly Stoopid": 4.0, "The Strokes": 5.0},
         "Veronica": {"Blues Traveler": 3.0, "Norah Jones": 5.0, "Phoenix": 4.0, "Slightly Stoopid": 2.5, "The Strokes": 3.0},
         "Clara": {"Blues Traveler": 4.75, "Norah Jones": 4.5, "Phoenix": 5.0, "Slightly Stoopid": 4.25, "The Strokes": 4.0},
          "Robert": {"Blues Traveler": 4, "Norah Jones": 3, "Phoenix": 5.0, "Slightly Stoopid": 2.0, "The Strokes": 1.0}
        }


#print users["Veronica"]



def dsum(*dicts):
    ret=defaultdict(int)
    for d in dicts:
        for k, v in d.items():
            print ret[k]
            print v
    return dict(ret)

#print (dsum(hail1,veronica))
#def euc(d1,d2):
#    k=[]
#    for i,v in zip(d1,d2):
#        if i>0 and v>0:
#            k.append((i-v)**2)
#    out=math.sqrt(sum(k))
#    print out
#    return
    
def manhattan(r1,r2):
    #takes summation of the absolute value of the difference of all keys that exist in both in r1 and r2 and then posts it into distance
    distance=0
    for i in r1:
        if i in r2:
            distance+=abs(r1[i]-r2[i])
    #print distance
    return distance
#manhattan(users["Hailey"],users["Veronica"])
#manhattan(users["Hailey"],users["Jordyn"])

def computeNearestNeighbor(username, users):
    #iterates over dictionary users and finds the manhattan distance for every username other than the one in question
    #then the appends the distances into a dictionary with the username with the smallest distance sorted on top
    distances = []
    for user in users:
        if user != username:
            distance=manhattan(users[user],users[username])
            distances.append((distance,user))
    distances.sort()
    return distances
#print computeNearestNeighbor('Hailey', users)

def manhattan_act(username,users):
    scores=[]
    for i in users:
        if i <> username:
            score=manhattan(users[username],users[i])
            scores.append((score,i))
        scores.sort()
    return scores
    
def recommend(username,users):
    #Takes the username computed form the manhattan_act(nearest neighbor) and finds that users list
    
    top=manhattan_act(username,users)[0][1]
    neighbor=users[top]
    recommendations=[]
    #finds the neighbors scored books that have no scores in the username in question and then appends those into the recommendations dictionary
    for n in neighbor:
        if n not in users[username]:
            recommendations.append((n,neighbor[n]))
    #recommendations is then sorted in declining order with the highest rated first
    return sorted(recommendations, key=lambda n:n[1],reverse=True)
    


#print recommend("Hailey",users)
#print recommend("Sam", users)
    
def mink(r1,r2,power_):
    #compute the sum of the abs value of the diff
    power_=float(power_)
    power=float(1/power_)
    score_=0
    common=False
    for i in r1:
        if i in r2:
            score_+=pow(abs(r1[i]-r2[i]),power_)
            score=pow(score_,power)
            common=True
    if common:
        return score 
    else:
        print "no common ratings"

    return score
#print mink(users['Hailey'], users['Jordyn'], 2)
#print mink(users['Hailey'], users['Veronica'], 2)

def distance(r1,users):
    #compute closest neighbor
    score=[]
    for i in users:
        if i <> r1:
            #print i
            dis=mink(users[r1],users[i],2)
            score.append((i,dis))
    return sorted(score, key=lambda n:n[1],reverse=False)

#print distance('Hailey',users)


######pearsons

def pearsons(r1,r2):
    xysum=[]
    xsum=[]
    ysum=[]
    x2sum=[]
    y2sum=[]
    n=0
    for i in r1:
        if i in r2:
            xysum.append(r1[i]*r2[i])
            xsum.append(r1[i])
            ysum.append(r2[i])
            x2sum.append(r1[i]**2)
            y2sum.append(r2[i]**2)
            n+=1
    xysum=sum(xysum)
    xsum=sum(xsum)
    ysum=sum(ysum)
    rightnum=((xsum*ysum)/n)
    x2sum=sum(x2sum)
    y2sum=sum(y2sum)
    numerator=xysum-((xsum*ysum)/n)
    lden=sqrt((x2sum)-((xsum**2)/n))
    rden=sqrt((y2sum)-((ysum**2)/n))
    den=lden*rden
    r=numerator/den
    print r
    return r
#print pearsons(users['Clara'],users['Robert'])
#print users['Clara'].values()
def cos(r1,r2):
    x=[]
    y=[]
    for i in r1:
        if i in r2:
            x.append(r1[i]**2)
            y.append(r2[i]**2)
        
    dot=sum([r1[i]*r2[i] for i in r1 if i in r2])
    clen=sqrt(sum(x))*sqrt(sum(y))
    r=dot/clen
    return r
#print cos(users['Clara'],users['Robert'])


class recommender:
    def __init__(self,data, k=1, metric='pearson', n=5):

        #k what metric to use. default to 1
        self.k = k 
        #n number of neighbors to recommend. default to 5
        self.n = n
        self.username2id={}
        self.userid2name={}
        self.productid2name={}
        self.metric = metric
        #if self.metric =='pearson':
            #self.fn = self.pearson
        if type(data).__name__=='dict':
            self.data=data
        print __doc__
    
    def convertProductID2name(self, id):
        #Given product id number return product name
        if id in self.productid2name:
            return self.productid2name[id]
        else:
            return id
    
    def userRatings(self, id, n):
        #returns ratings in order without how ratings created
        print ("Ratings for " + self.useridname[id])
        ratings = self.data[id]


print type(recommender(users).data).__name__

            