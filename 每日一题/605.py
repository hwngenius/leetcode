class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for i in range(len(flowerbed)):
            if flowerbed[i]==1:
                continue
            if i==len(flowerbed)-1:
                if flowerbed[i-1]==0:
                    n-=1
            elif i==0:
                if flowerbed[i+1]==0:
                    n-=1
                    flowerbed[i]=1
            else:
                if flowerbed[i+1]==0 and flowerbed[i-1]==0:
                    n-=1
                    flowerbed[i]=1
        return n<=0

# 执行用时：
# 60 ms
# , 在所有 Python3 提交中击败了
# 80.49%
# 的用户
# 内存消耗：
# 14.8 MB
# , 在所有 Python3 提交中击败了
# 21.11%
# 的用户