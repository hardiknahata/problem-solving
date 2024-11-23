class Solution {
public:
    int cache[99999][2];
    //to get maximum
    int maximumProfit(vector<int>& prices,int &N,int idx,int indicate) {
        if(idx == N) {
            return 0;
        }
        if(cache[idx][indicate] != -1) {
            return cache[idx][indicate];
        }

        int ans = INT_MIN;
        //if we have not stock purchased previously
        if(indicate == 0) {
            //buy today
            ans = max(ans,maximumProfit(prices,N,idx+1,1) - prices[idx]);
        }
        else {
        //sell and change the indicator
        ans = max(ans,prices[idx] + maximumProfit(prices,N,idx+1,0));
        }

        //if we have purchase a stock
        // dont sell and wait
        ans = max(ans,maximumProfit(prices,N,idx+1,indicate));

        return cache[idx][indicate] = ans;


    }
    int maxProfit(vector<int>& prices) {
        memset(cache,-1,sizeof(cache));
        int N = prices.size();
        return maximumProfit(prices,N,0,0);
    }
};