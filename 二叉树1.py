#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/12/4 10:15
# @Author  : hbw
# @File    : 二叉树.py
# @Software: PyCharm
# 构造节点对象
class Node(object):
    def __init__(self,item):
        self.item=item
        self.left=None
        self.right=None
# 构造二叉树对象
class Tree(object):
    # 初始化一棵树  根节点为空
    def __init__(self):
        self.root=None

    # 添加节点
    def add(self,item):
        # 创造节点
        node=Node(item)
        # 判断根节点是否为空
        if self.root is None:
           #为空  赋值
           self.root=node
           return
        # 不为空 将根节点放入队列中
        q=[self.root]
        while True:
        # 从队列中取出一个节点
            cur_node=q.pop(0)
        # 判断左子树
            if cur_node.left is None:
                # 左子树为空  填入
                cur_node.left=node
                return
        # 判断右子树
            elif cur_node.right is None:
                cur_node.right=node
                return
            else:
                q.append(cur_node.left)
                q.append(cur_node.right)
    # 先序遍历
    def preorder(self,root):
        if root is None:
            return []
        result=[root.item] # 遍历根节点
        left=self.preorder(root.left) # 遍历左子树
        right=self.preorder(root.right)  # 遍历右子树
        return result+left+right   #根左右
    # 中序遍历
    def inorder(self,root):
        if root is None:
            return []
        result=[root.item] # 遍历根节点
        left=self.inorder(root.left) # 遍历左子树
        right=self.inorder(root.right)  # 遍历右子树
        return left+result+right  #左跟右

    # 后序遍历
    def postorder(self, root):
        if root is None:
            return []
        result = [root.item]  # 遍历根节点
        left = self.postorder(root.left)  # 遍历左子树
        right = self.postorder(root.right)  # 遍历右子树
        return left + right + result   #左右跟
    # 层次遍历 （广度优先）
    def cengci(self):
        if self.root is None:
            return []
        else:
            results=[]
            q=[self.root]
            while q:  # 当待访问的队列为空时，结束循环
                node=q.pop(0) # 取出当前节点
                results.append(node.item)
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
            return results
if __name__ == '__main__':
    tree=Tree()
    for i in  range(9):
        tree.add(i+1)
    print(tree.preorder(tree.root))
    print(tree.inorder(tree.root))
    print(tree.postorder(tree.root))
    print(tree.cengci())
