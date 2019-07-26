#!/usr/bin/env python
# coding: utf-8



import random
from itertools import combinations
import numpy as np
import pandas as pd





def MonteCarloSimul(total_times,lottery_times):
    
    #get combinations of 14 balls
    comb = list(combinations(list(range(14)),4))[0:1000]    
    
    chances = [114,113,112,111,99,89,79,69,59,49,39,29,19,9,6,4]
    
    ##initial times matrix
    s_times = np.zeros((16,16))
    
    ##repeat lottery process
    for MC_times in range(total_times):
        comb2 = comb
        ##allocate combinations
        com_map = list()
        for k in range(16):
            tmp = random.sample(comb2,chances[k])
            comb2 = [j for j in comb2 if j not in tmp]
            com_map.append(tmp)
        
        
        seeds2 = list(range(16))
        for i in range(lottery_times):
            
            com_tmp = comb
            
            which_seed = list()
            
            for times in range(5): ## first 5 round
                
                ##randomly choose a ball
                choose = random.choice(com_tmp)
                
                ##check which seed is the combination in 
                for seed in range(16): ##iteration for all seed
                    
                    check_inside = choose in com_map[seed]
                    
                    if check_inside:
                        s_times[seed,times] += 1
                        com_tmp = [n for n in com_tmp if n not in com_map[seed]]
                        which_seed.append(seed)
            
            ##get non chosen seed
            other_seed = [i for i in seeds2 if i not in which_seed]
            
            ##throw point in the cell 
            
            times2 = list(range(5,16))
                        
            for k in range(11):
                
                s_times[other_seed[k],times2[k]] += 1
    return s_times/(total_times*lottery_times)





lottery_res = MonteCarloSimul(1000,1000)





pd.DataFrame(lottery_res).to_excel('Q2_Monte_carlo_result.xlsx',index=True)







