"""稀疏数组搜索。有个排好序的字符串数组，其中散布着一些空字符串，编写一种方法，找出给定字符串的位置。
 输入: words = ["at", "", "", "", "ball", "", "", "car", "", "","dad", "", ""], s = "ta"
 输出：-1
 说明: 不存在返回-1
 输入：words = ["at", "", "", "", "ball", "", "", "car", "", "","dad", "", ""], s = "ball"
 输出：4
"""

#方法一，哈希查询
class Solution:
    def findString(self, words: List[str], s: str) -> int:
        if len(words)==0:
            return -1
        words_copy={}
        start,end=0,len(words)-1
        i=0
        for word in words:
            if word!="":
                words_copy[word]=i
            i+=1
        if s in words_copy:
            return words_copy[s]
        return -1


#方法二，二分查找
class Solution:
    def findString(self, words: List[str], s: str) -> int:
        if len(words)==0:
            return -1
        start,end=0,len(words)-1
        while start<=end:
            mid_right=mid=start+(end-start)//2
            while mid<=end and words[mid]=="":
                mid+=1
            if mid>end:
                end=mid_right-1
                continue
            if s>words[mid]:
                start=mid+1
            elif s<words[mid]:
                end=mid-1
            else:
                return mid
        return -1


#此处的二分查找涉及到空字符串的处理，此处我们采取的解决办法是右移mid指针，当mid指针超出
#end边界时可知mid至end处都为空串，所以此时将end边界变为mid-1,其余的操作步骤与二分法一致
