#!/usr/bin/env python
# encoding: utf-8
"""
sum_root_to_leaf_numbers.py

Created by Shengwei on 2014-07-15.
"""

# https://oj.leetcode.com/problems/sum-root-to-leaf-numbers/
# tags: medium, tree, sum, recursion

"""
Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers.

For example,

    1
   / \
  2   3
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.

Return the sum = 12 + 13 = 25.
"""

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def sumNumbers(self, root):
        """Push the number formed by path to leaves,
        and sum them up to ancestors.
        """
        
        def sum_root(root, sub_sum=0):
            if root is None:
                return 0
            
            sub_sum = sub_sum * 10 + root.val
            if not root.left and not root.right:
                return sub_sum
            
            left = sum_root(root.left, sub_sum)
            right = sum_root(root.right, sub_sum)
            return left + right
        
        return sum_root(root)
