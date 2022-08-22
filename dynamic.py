#dynamic programming (bottom up approach)

def NumberOfCoins(TypesOfcoins,sum):
    
    dp=[0]*(sum+1)
    for i in range(1,sum+1):
        dp[i]=max(TypesOfcoins)
        for coin in range(len(TypesOfcoins)):
            if i-TypesOfcoins[coin]>=0:
                result=dp[i-TypesOfcoins[coin]]
                if result!=max(TypesOfcoins):
                    dp[i]=min(dp[i],result+1)
    return dp[sum]
TypesOfcoins=list(map(int,input().split()))
sum=int(input('enter sum'))
a=NumberOfCoins(TypesOfcoins,sum)
print(a)