class Solution(object):
    def maxProfit(self, prices):
        n=len(prices)
        sellprices = [prices[n-1]]
        maxi = prices[n-1]
        for i in prices[-2::-1]:
            if i > maxi:
                maxi = i
                sellprices.append(maxi)
            else:
                sellprices.append(maxi)
                
        sellprices = sellprices[::-1]
        #print(sellprices)
        if n>1:
            profit = sellprices[1] - prices[0]
        else:
            profit = 0
        for i in range(1,n-1):
            #if (sellprices[i+1] - prices[i]) > profit:
            profit = max(profit,sellprices[i+1] - prices[i])
        return max(0,profit)
            
                
        