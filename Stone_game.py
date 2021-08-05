/*Alex and Lee play a game with piles of stones.  There are an even number of piles arranged in a row, and each pile has a positive integer number of stones piles[i].

The objective of the game is to end with the most stones.  The total number of stones is odd, so there are no ties.

Alex and Lee take turns, with Alex starting first.  Each turn, a player takes the entire pile of stones from either the beginning or the end of the row.  This continues until there are no more piles left, at which point the person with the most stones wins.

Assuming Alex and Lee play optimally, return True if and only if Alex wins the game.

 

Example 1:

Input: piles = [5,3,4,5]
Output: true
Explanation: 
Alex starts first, and can only take the first 5 or the last 5.
Say he takes the first 5, so that the row becomes [3, 4, 5].
If Lee takes 3, then the board is [4, 5], and Alex takes 5 to win with 10 points.
If Lee takes the last 5, then the board is [3, 4], and Alex takes 4 to win with 9 points.
This demonstrated that taking the 
 first 5 was a winning move for Alex, so we return true.
 
 
 Constraints:

2 <= piles.length <= 500
piles.length is even.
1 <= piles[i] <= 500
sum(piles) is odd.


My explaination :
Since alex always start the game s alex have the choce to choose the pile from beginning or end.
if alex chooses the even index the lee will have only option left to choose from odd index.
and if alex chooses from odd index lee will alwys have the option to choose from even indx.
1) alex has the option to choose from either all even or odd index.
2) the length of piles array is always even
3) no of stones in each pils is odd so there will be no tie 
4) no of even indices is always equal to no of odd indices 
*** alex will always win no matter what 
*/

#Solution 1 

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n=len(piles)
        j=0
        alex=odd=even=0
        lee=0
        for i in range(len(piles)):
            if i%2==0:
                even+=piles[i]
            else:
                odd+=piles[i]
        for i in range(len(piles)):
            if even>odd:
                if i%2==0:
                    alex+=piles[i]
                else:
                    lee+=piles[i]
            else:
                if i%2==0:
                    lee+=piles[i]
                else:
                    alex+=piles[i] 
            
            
        if alex>lee:
            return True
        else:
            return False
        
  #solution 2 
  
  class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
      return 1
