import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

pd.options.mode.chained_assignment = None  # default='warn'

#colours and formats
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'


df = pd.read_csv('C:/Users/chow/blog/LearningWeb/crypto-markets.csv')
df.head()


todayValue = df[df.date == df.date.max()]
todayValue['market'] = todayValue['market'].map(lambda x: x / 1000000)
todayValue.sort_values(by='market', ascending = False)
Top10 = todayValue.iloc[0:10]
Others = todayValue.iloc[10:]

Others['market'].sum()
Top10['market'].sum()



print(color.BOLD + "E-coin last data date: %s" %df['date'].max())

#Pie Char showing mkt value
labels = 'Top10 Crypto Currencies: %s' %Top10['market'].count() , 'Others Combined: %s' %Others['market'].count()
sizes = [Top10['market'].sum(), Others['market'].sum()]
explode = (0, 0)  # only "explode" the slice (i.e. '')
fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
fig = plt.gcf()
fig.set_size_inches(15,15)
plt.savefig("C:/Users/chow/blog/LearningWeb/output.png")

tlabel = []
tmarket = []

def TopTen(list):
    for i in list:
        tlabel.append(i)

def TopTenM(list):
    for i in list:
        tmarket.append(i)


TopTen(Top10['slug'])
TopTenM(Top10['market'])


#Pie Char showing mkt value
labels = tlabel
sizes = tmarket
explode = (0.1,0,0,0,0,0,0,0,0,0)  # only "explode" the slice (i.e. '')
fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
fig = plt.gcf()
fig.set_size_inches(15,15)
plt.savefig("C:/Users/chow/blog/LearningWeb/output2.png")


dollarVal=input('Please enter a $ value you are going to invest:  ')
DateVal=input('Please enter a date prior to %s and after %s YYYY-MM-DD:  '  %(df.date.max(),df.date.min()) )


# Make the date col our index
df = pd.read_csv('C:/Users/chow/blog/LearningWeb/crypto-markets.csv')
#df.index = df.date
#df['date'] = pd.to_datetime(df['date'], dayfirst = True)
#df = df.drop('date', axis = 1)


TempQ = [] #stores qty
TempS = [] #stores slug
TempP = [] #stores Historial price
TempCP = [] #stores current price, matched with our list
Combined = [] #New array

def equalInvest(cash,InvDate):
    TempD = df[df.date == InvDate]
    avgCash = float(cash)/len(TempD)
    for i in TempD['slug']:
        TempS.append(i)
    for i in TempD['low']:
        TempQ.append(avgCash/i)
    for i in TempD['low']:
        TempP.append(i)
    TempD = df[df.date == df['date'].max()]
    TempD.index = TempD.slug

    for k in range(len(TempS)):
      for j in TempD['slug']:
        if(j == TempS[k]):
          TempCP.append(TempD.loc[j]['low'])
          i=1
      if(i!=1):
        TempCP.append(0)
      i=0



equalInvest(dollarVal,DateVal)




# TempCol = ['slug','qty','hisPrice','curPrice']
# print(TempS)
# print(TempQ)
# print(TempP)
# print(TempCP)
# print(TempCol)


# Combined = list(zip(TempS,TempQ,TempP,TempCP))
# print (Combined)
# Combined = dict(zip(TempCol,Combined))
# print (Combined)

def getHisTotalMktvalue():
    return (sum(np.multiply(TempQ,TempP)))

def getHisMktvalue():
    return (np.multiply(TempQ,TempP))

def getCurTotalMktvalue():
    return (sum(np.multiply(TempQ,TempCP)))

def getCurMktvalue():
    return (np.multiply(TempQ,TempCP))

def getPercentR():
    return (np.divide(TempCP,TempP))

def getCurWallet():
    print(TempS)
    print(TempQ)
    print(TempCP)

# def getReturnHistogram():
#     f, ax = plt.subplots(figsize=(15, 4))
#     sns.countplot(y="slug", hue='left', data=Combined).set_title('Employee Turnover by Salary')
#     plt.show()

def getPieReturn():
    #Pie Char showing mkt value
    labels = TempS
    sizes = getCurMktvalue()
  #  explode = (0.1,0,0,0,0,0,0,0,0,0)  # only "explode" the slice (i.e. '')
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    fig = plt.gcf()
    fig.set_size_inches(15,15)
    plt.savefig("C:/Users/chow/blog/LearningWeb/output3.png")

def getOrigReturn():
    #Pie Char showing mkt value
    labels = TempS
    sizes = getHisMktvalue()
  #  explode = (0.1,0,0,0,0,0,0,0,0,0)  # only "explode" the slice (i.e. '')
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    fig = plt.gcf()
    fig.set_size_inches(15,15)
    plt.savefig("C:/Users/chow/blog/LearningWeb/output4.png")


def getPieReturnCoin():
    #Pie Char showing mkt value
    labels = TempS
    sizes = np.divide(getCurMktvalue(),1000)
  #  explode = (0.1,0,0,0,0,0,0,0,0,0)  # only "explode" the slice (i.e. '')
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    fig = plt.gcf()
    fig.set_size_inches(15,15)
    plt.savefig("C:/Users/chow/blog/LearningWeb/output5.png")

# print(getHisMktvalue())
# print(getCurMktvalue())
# getCurWallet()
# print(TempCP)
# print(getPercentR())

#getPieReturn()
#getReturnHistogram()
print('\n' + '\n' + '\n' + '\n')

print(color.BOLD + "Investment Begin date: %s" %DateVal, "Invested Amount:  %s" %round(float(dollarVal),2) + color.END)
print(color.BOLD + "Investment Ending date: %s" %df['date'].max(), "Current Amount:  %s" %round(getCurTotalMktvalue(),2) + color.END)
print('\n' + color.BOLD +"Percentage Return 100% as base:",round(getCurTotalMktvalue()/float(dollarVal)*100,2),"%")

print('\n' + color.BOLD + "Original Even Investment Split by Mkt Val: number of investments: ", len(TempS))
getOrigReturn()

print(color.BOLD + "Current Investment Investment Split by Mkt Val: number of investments: ", len(TempS))
getPieReturn()





winners=[]
winners.append(getCurMktvalue())
winners.append(TempS)
winners[1].sort()
#print(winners)


win2=np.round_(sorted(winners[0],key=float, reverse=True),decimals=2)

#print([row[:10] for row in winners])
print(color.BOLD +  "End value of Investment:" + color.END)
print(round(getCurTotalMktvalue(),2))

print(color.BOLD +  "Contribution of Top 10 winners in $$" + color.END)
print(win2[0:10])

print(color.BOLD + "Contribution of Top 10 winners in %" + color.END)
print(np.round_(win2[0:10]/getCurTotalMktvalue()*100,decimals=2))
print(color.BOLD +  "Sum of Top 10 winners in $$" + color.END)
print(sum(win2[0:10]))
print(color.BOLD +  "Sum of Top 10 winners in %" + color.END)
print(sum(win2[0:10])/getCurTotalMktvalue()*100, "%")

# def getTop10WinnerName():
#     arrNames=[]
#     arr = np.round_(getCurMktvalue(), decimals=2)
#     for i in range(min(10,len(arr))):
#         for j in range(len(arr)):
#            if(arr[j] == round(win2[i],2)):
#               print(winners[1][j],arr[j])


# print(color.BOLD +  "Name of Top 10 winners:" + color.END)
# getTop10WinnerName()
