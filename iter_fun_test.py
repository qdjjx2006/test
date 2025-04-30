# -*- coding: utf-8 -*-
"""
Created on Wed Apr 30 17:08:50 2025

@author: pc
"""
import itertools
import dis

dis.dis('a[b] += c')

def vowel(c):
    return c.lower() in 'aeiou'
    
dis.dis("list(filter(vowel,'Aardvark'))")

#%%
list(filter(vowel,'Aardvark'))

#%%
list( itertools.filterfalse(vowel,'Aardvark'))

#%%
list( itertools.filterfalse(vowel,'Aardvark'))

#%%
list( itertools.filterfalse(vowel,'Aardvark'))

#%%
list( itertools.dropwhile(vowel,'Aardvark'))

#%%
list( itertools.takewhile(vowel,'Aardvark'))

#%%
list( itertools.compress('Aardvark',(1,0,1,1,0,1)))
