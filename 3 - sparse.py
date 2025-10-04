# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 20:56:32 2023

@author: Super Warrior
"""
import scipy.sparse as sparse

x = sparse.diags([-1,1,2,1]  , [-2,-1,0,1] ,  [10,10]).toarray()