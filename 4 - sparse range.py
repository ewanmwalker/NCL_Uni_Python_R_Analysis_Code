# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 21:03:52 2023

@author: Super Warrior
"""
import scipy.sparse as sparse

x = sparse.diags([range(9,0,-1),range(1,11),range(9,0,-1)]  , [-1,0,1] ,  [10,10]).toarray()