# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None
class Solution:
    strl='google'
    # 返回对应char
    def FirstAppearingOnce(self):
        # write code here
        count=[1]*len(self.strl)
        for i,s in enumerate(self.strl):
            if count[i]>1:
                continue
            for ii,ss in enumerate(self.strl[(i+1):]):
                if ss==s:
                    count[ii+i+1]+=1
                    count[i]=2
            if count[i] == 1:
                return s
        return '#'
    def Insert(self, char):
        # write code here
        self.strl=self.strl+char

    def EntryNodeOfLoop(self, pHead):
        # write code here
        # 测试用例,{}{1,2,3,4,5}   {1}{}   {1,2}{3,4,5}
        pSlow=pHead
        pFast=pHead
        if not pHead.next or not pHead.next.next:
            return None
        while pFast and pSlow :
            pSlow=pSlow.next if pSlow.next else None
            pFast=pFast.next.next if pFast.next and pFast.next.next else None
            if pSlow ==pFast:
                break
            if not pSlow or not pFast:
                return

        if pFast==pHead:
            return pHead

        pFast=pHead

        while pFast and pSlow:
            pSlow=pSlow.next if pSlow.next else None
            pFast=pFast.next if pFast.next else None
            if pSlow ==pFast:
                break
        return pFast

    def GetNext(self, pNode):
        # write code here
        if not pNode:
            return None
        # 该节点有右子树,下一个节点是右子树的最左边节点
        if pNode.right:
            pNode=pNode.right
            while pNode.left:
                pNode=pNode.left
            return pNode
        # 该节点没有右子树,该节点是根节点
        elif not pNode.next:
            return None
        #  该节点没有右子树,该节点是父节点的左节点
        elif pNode==pNode.next.left:
            return pNode.next
        # 该节点没有右子树,该节点是父节点的右节点
        else:
            pNode=pNode.next
            while pNode:
                if not pNode.next:
                    return None
                if pNode==pNode.next.left:
                    return pNode.next
                pNode=pNode.next





L1=ListNode(1)
L2=ListNode(2)
L3=ListNode(3)
L4=ListNode(4)
L5=ListNode(5)
L1.next,L2.next,L3.next,L4.next,L5.next=L2,L3,L4,L5,L1
sol=Solution()
print sol.FirstAppearingOnce()
print sol.EntryNodeOfLoop(L1).val