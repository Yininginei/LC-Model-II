import pandas as pd
import math
import numpy as np
from loglikelihood import *
from statistics import *
from biogeme import *
import biogeme.database as db
import biogeme.biogeme as bio
import biogeme.models as models
import biogeme.messaging as msg
import biogeme.expressions as ex
from biogeme.expressions import *

dat = pd.read_csv("LC_dataset.csv",sep=',').iloc[:, 1:]
database = db.Database("dat",dat)
globals().update(database.variables)
database.panel('1_no')
R = 10
B = 3*8*6+3*8*12
np.random.seed(0)
minimum = -0.1
maximum = 0.1
startset = np.random.uniform(minimum,maximum,(R,B))
classset = np.random.rand(R,3)
Modelset = pd.read_csv('Ind.csv',header=0,index_col=0)

for r in range(0,R):
    #Variables Definition
    ASC1_a1_0 = Beta("ASC1_a1_0", startset[r,0], None, None, 1)
    ASC1_a2_0 = Beta("ASC1_a2_0", startset[r,1], None, None, 1)
    ASC1_a3_0 = Beta("ASC1_a3_0", startset[r,2], None, None, 1)
    ASC1_a4_0 = Beta("ASC1_a4_0", startset[r,3], None, None, 1)
    ASC1_a5_0 = Beta("ASC1_a5_0", startset[r,4], None, None, 1)
    ASC1_a6_0 = Beta("ASC1_a6_0", startset[r,5], None, None, 1)
    ASC1_a7_0 = Beta("ASC1_a7_0", startset[r,6], None, None, 1)
    ASC1_a8_0 = Beta("ASC1_a8_0", startset[r,7], None, None, 1)
    ASC1_a9_0 = Beta("ASC1_a9_0", startset[r,8], None, None, 1)
    ASC1_a10_0 = Beta("ASC1_a10_0", startset[r,9], None, None, 1)
    ASC1_a11_0 = Beta("ASC1_a11_0", startset[r,10], None, None, 1)
    ASC1_a12_0 = Beta("ASC1_a12_0", startset[r,11], None, None, 1)
    ASC1_a1_1 = Beta("ASC1_a1_1", startset[r,12], None, None, 0)
    ASC1_a2_1 = Beta("ASC1_a2_1", startset[r,13], None, None, 0)
    ASC1_a3_1 = Beta("ASC1_a3_1", startset[r,14], None, None, 0)
    ASC1_a4_1 = Beta("ASC1_a4_1", startset[r,15], None, None, 0)
    ASC1_a5_1 = Beta("ASC1_a5_1", startset[r,16], None, None, 0)
    ASC1_a6_1 = Beta("ASC1_a6_1", startset[r,17], None, None, 0)
    ASC1_a7_1 = Beta("ASC1_a7_1", startset[r,18], None, None, 0)
    ASC1_a8_1 = Beta("ASC1_a8_1", startset[r,19], None, None, 0)
    ASC1_a9_1 = Beta("ASC1_a9_1", startset[r,20], None, None, 0)
    ASC1_a10_1 = Beta("ASC1_a10_1", startset[r,21], None, None, 0)
    ASC1_a11_1 = Beta("ASC1_a11_1", startset[r,22], None, None, 0)
    ASC1_a12_1 = Beta("ASC1_a12_1", startset[r,23], None, None, 0)
    ASC1_a1_2 = Beta("ASC1_a1_2", startset[r,24], None, None, 0)
    ASC1_a2_2 = Beta("ASC1_a2_2", startset[r,25], None, None, 0)
    ASC1_a3_2 = Beta("ASC1_a3_2", startset[r,26], None, None, 0)
    ASC1_a4_2 = Beta("ASC1_a4_2", startset[r,27], None, None, 0)
    ASC1_a5_2 = Beta("ASC1_a5_2", startset[r,28], None, None, 0)
    ASC1_a6_2 = Beta("ASC1_a6_2", startset[r,29], None, None, 0)
    ASC1_a7_2 = Beta("ASC1_a7_2", startset[r,30], None, None, 0)
    ASC1_a8_2 = Beta("ASC1_a8_2", startset[r,31], None, None, 0)
    ASC1_a9_2 = Beta("ASC1_a9_2", startset[r,32], None, None, 0)
    ASC1_a10_2 = Beta("ASC1_a10_2", startset[r,33], None, None, 0)
    ASC1_a11_2 = Beta("ASC1_a11_2", startset[r,34], None, None, 0)
    ASC1_a12_2 = Beta("ASC1_a12_2", startset[r,35], None, None, 0)
    ASC1_a1_3 = Beta("ASC1_a1_3", startset[r,36], None, None, 0)
    ASC1_a2_3 = Beta("ASC1_a2_3", startset[r,37], None, None, 0)
    ASC1_a3_3 = Beta("ASC1_a3_3", startset[r,38], None, None, 0)
    ASC1_a4_3 = Beta("ASC1_a4_3", startset[r,39], None, None, 0)
    ASC1_a5_3 = Beta("ASC1_a5_3", startset[r,40], None, None, 0)
    ASC1_a6_3 = Beta("ASC1_a6_3", startset[r,41], None, None, 0)
    ASC1_a7_3 = Beta("ASC1_a7_3", startset[r,42], None, None, 0)
    ASC1_a8_3 = Beta("ASC1_a8_3", startset[r,43], None, None, 0)
    ASC1_a9_3 = Beta("ASC1_a9_3", startset[r,44], None, None, 0)
    ASC1_a10_3 = Beta("ASC1_a10_3", startset[r,45], None, None, 0)
    ASC1_a11_3 = Beta("ASC1_a11_3", startset[r,46], None, None, 0)
    ASC1_a12_3 = Beta("ASC1_a12_3", startset[r,47], None, None, 0)
    ASC1_a1_4 = Beta("ASC1_a1_4", startset[r,48], None, None, 0)
    ASC1_a2_4 = Beta("ASC1_a2_4", startset[r,49], None, None, 0)
    ASC1_a3_4 = Beta("ASC1_a3_4", startset[r,50], None, None, 0)
    ASC1_a4_4 = Beta("ASC1_a4_4", startset[r,51], None, None, 0)
    ASC1_a5_4 = Beta("ASC1_a5_4", startset[r,52], None, None, 0)
    ASC1_a6_4 = Beta("ASC1_a6_4", startset[r,53], None, None, 0)
    ASC1_a7_4 = Beta("ASC1_a7_4", startset[r,54], None, None, 0)
    ASC1_a8_4 = Beta("ASC1_a8_4", startset[r,55], None, None, 0)
    ASC1_a9_4 = Beta("ASC1_a9_4", startset[r,56], None, None, 0)
    ASC1_a10_4 = Beta("ASC1_a10_4", startset[r,57], None, None, 0)
    ASC1_a11_4 = Beta("ASC1_a11_4", startset[r,58], None, None, 0)
    ASC1_a12_4 = Beta("ASC1_a12_4", startset[r,59], None, None, 0)
    ASC1_a1_5 = Beta("ASC1_a1_5", startset[r,60], None, None, 0)
    ASC1_a2_5 = Beta("ASC1_a2_5", startset[r,61], None, None, 0)
    ASC1_a3_5 = Beta("ASC1_a3_5", startset[r,62], None, None, 0)
    ASC1_a4_5 = Beta("ASC1_a4_5", startset[r,63], None, None, 0)
    ASC1_a5_5 = Beta("ASC1_a5_5", startset[r,64], None, None, 0)
    ASC1_a6_5 = Beta("ASC1_a6_5", startset[r,65], None, None, 0)
    ASC1_a7_5 = Beta("ASC1_a7_5", startset[r,66], None, None, 0)
    ASC1_a8_5 = Beta("ASC1_a8_5", startset[r,67], None, None, 0)
    ASC1_a9_5 = Beta("ASC1_a9_5", startset[r,68], None, None, 0)
    ASC1_a10_5 = Beta("ASC1_a10_5", startset[r,69], None, None, 0)
    ASC1_a11_5 = Beta("ASC1_a11_5", startset[r,70], None, None, 0)
    ASC1_a12_5 = Beta("ASC1_a12_5", startset[r,71], None, None, 0)
    ASC1_a1_6 = Beta("ASC1_a1_6", startset[r,72], None, None, 0)
    ASC1_a2_6 = Beta("ASC1_a2_6", startset[r,73], None, None, 0)
    ASC1_a3_6 = Beta("ASC1_a3_6", startset[r,74], None, None, 0)
    ASC1_a4_6 = Beta("ASC1_a4_6", startset[r,75], None, None, 0)
    ASC1_a5_6 = Beta("ASC1_a5_6", startset[r,76], None, None, 0)
    ASC1_a6_6 = Beta("ASC1_a6_6", startset[r,77], None, None, 0)
    ASC1_a7_6 = Beta("ASC1_a7_6", startset[r,78], None, None, 0)
    ASC1_a8_6 = Beta("ASC1_a8_6", startset[r,79], None, None, 0)
    ASC1_a9_6 = Beta("ASC1_a9_6", startset[r,80], None, None, 0)
    ASC1_a10_6 = Beta("ASC1_a10_6", startset[r,81], None, None, 0)
    ASC1_a11_6 = Beta("ASC1_a11_6", startset[r,82], None, None, 0)
    ASC1_a12_6 = Beta("ASC1_a12_6", startset[r,83], None, None, 0)
    ASC1_a1_7 = Beta("ASC1_a1_7", startset[r,84], None, None, 0)
    ASC1_a2_7 = Beta("ASC1_a2_7", startset[r,85], None, None, 0)
    ASC1_a3_7 = Beta("ASC1_a3_7", startset[r,86], None, None, 0)
    ASC1_a4_7 = Beta("ASC1_a4_7", startset[r,87], None, None, 0)
    ASC1_a5_7 = Beta("ASC1_a5_7", startset[r,88], None, None, 0)
    ASC1_a6_7 = Beta("ASC1_a6_7", startset[r,89], None, None, 0)
    ASC1_a7_7 = Beta("ASC1_a7_7", startset[r,90], None, None, 0)
    ASC1_a8_7 = Beta("ASC1_a8_7", startset[r,91], None, None, 0)
    ASC1_a9_7 = Beta("ASC1_a9_7", startset[r,92], None, None, 0)
    ASC1_a10_7 = Beta("ASC1_a10_7", startset[r,93], None, None, 0)
    ASC1_a11_7 = Beta("ASC1_a11_7", startset[r,94], None, None, 0)
    ASC1_a12_7 = Beta("ASC1_a12_7", startset[r,95], None, None, 0)
    ASC2_a1_0 = Beta("ASC2_a1_0", startset[r,96], None, None, 1)
    ASC2_a2_0 = Beta("ASC2_a2_0", startset[r,97], None, None, 1)
    ASC2_a3_0 = Beta("ASC2_a3_0", startset[r,98], None, None, 1)
    ASC2_a4_0 = Beta("ASC2_a4_0", startset[r,99], None, None, 1)
    ASC2_a5_0 = Beta("ASC2_a5_0", startset[r,100], None, None, 1)
    ASC2_a6_0 = Beta("ASC2_a6_0", startset[r,101], None, None, 1)
    ASC2_a7_0 = Beta("ASC2_a7_0", startset[r,102], None, None, 1)
    ASC2_a8_0 = Beta("ASC2_a8_0", startset[r,103], None, None, 1)
    ASC2_a9_0 = Beta("ASC2_a9_0", startset[r,104], None, None, 1)
    ASC2_a10_0 = Beta("ASC2_a10_0", startset[r,105], None, None, 1)
    ASC2_a11_0 = Beta("ASC2_a11_0", startset[r,106], None, None, 1)
    ASC2_a12_0 = Beta("ASC2_a12_0", startset[r,107], None, None, 1)
    ASC2_a1_1 = Beta("ASC2_a1_1", startset[r,108], None, None, 0)
    ASC2_a2_1 = Beta("ASC2_a2_1", startset[r,109], None, None, 0)
    ASC2_a3_1 = Beta("ASC2_a3_1", startset[r,110], None, None, 0)
    ASC2_a4_1 = Beta("ASC2_a4_1", startset[r,111], None, None, 0)
    ASC2_a5_1 = Beta("ASC2_a5_1", startset[r,112], None, None, 0)
    ASC2_a6_1 = Beta("ASC2_a6_1", startset[r,113], None, None, 0)
    ASC2_a7_1 = Beta("ASC2_a7_1", startset[r,114], None, None, 0)
    ASC2_a8_1 = Beta("ASC2_a8_1", startset[r,115], None, None, 0)
    ASC2_a9_1 = Beta("ASC2_a9_1", startset[r,116], None, None, 0)
    ASC2_a10_1 = Beta("ASC2_a10_1", startset[r,117], None, None, 0)
    ASC2_a11_1 = Beta("ASC2_a11_1", startset[r,118], None, None, 0)
    ASC2_a12_1 = Beta("ASC2_a12_1", startset[r,119], None, None, 0)
    ASC2_a1_2 = Beta("ASC2_a1_2", startset[r,120], None, None, 0)
    ASC2_a2_2 = Beta("ASC2_a2_2", startset[r,121], None, None, 0)
    ASC2_a3_2 = Beta("ASC2_a3_2", startset[r,122], None, None, 0)
    ASC2_a4_2 = Beta("ASC2_a4_2", startset[r,123], None, None, 0)
    ASC2_a5_2 = Beta("ASC2_a5_2", startset[r,124], None, None, 0)
    ASC2_a6_2 = Beta("ASC2_a6_2", startset[r,125], None, None, 0)
    ASC2_a7_2 = Beta("ASC2_a7_2", startset[r,126], None, None, 0)
    ASC2_a8_2 = Beta("ASC2_a8_2", startset[r,127], None, None, 0)
    ASC2_a9_2 = Beta("ASC2_a9_2", startset[r,128], None, None, 0)
    ASC2_a10_2 = Beta("ASC2_a10_2", startset[r,129], None, None, 0)
    ASC2_a11_2 = Beta("ASC2_a11_2", startset[r,130], None, None, 0)
    ASC2_a12_2 = Beta("ASC2_a12_2", startset[r,131], None, None, 0)
    ASC2_a1_3 = Beta("ASC2_a1_3", startset[r,132], None, None, 0)
    ASC2_a2_3 = Beta("ASC2_a2_3", startset[r,133], None, None, 0)
    ASC2_a3_3 = Beta("ASC2_a3_3", startset[r,134], None, None, 0)
    ASC2_a4_3 = Beta("ASC2_a4_3", startset[r,135], None, None, 0)
    ASC2_a5_3 = Beta("ASC2_a5_3", startset[r,136], None, None, 0)
    ASC2_a6_3 = Beta("ASC2_a6_3", startset[r,137], None, None, 0)
    ASC2_a7_3 = Beta("ASC2_a7_3", startset[r,138], None, None, 0)
    ASC2_a8_3 = Beta("ASC2_a8_3", startset[r,139], None, None, 0)
    ASC2_a9_3 = Beta("ASC2_a9_3", startset[r,140], None, None, 0)
    ASC2_a10_3 = Beta("ASC2_a10_3", startset[r,141], None, None, 0)
    ASC2_a11_3 = Beta("ASC2_a11_3", startset[r,142], None, None, 0)
    ASC2_a12_3 = Beta("ASC2_a12_3", startset[r,143], None, None, 0)
    ASC2_a1_4 = Beta("ASC2_a1_4", startset[r,144], None, None, 0)
    ASC2_a2_4 = Beta("ASC2_a2_4", startset[r,145], None, None, 0)
    ASC2_a3_4 = Beta("ASC2_a3_4", startset[r,146], None, None, 0)
    ASC2_a4_4 = Beta("ASC2_a4_4", startset[r,147], None, None, 0)
    ASC2_a5_4 = Beta("ASC2_a5_4", startset[r,148], None, None, 0)
    ASC2_a6_4 = Beta("ASC2_a6_4", startset[r,149], None, None, 0)
    ASC2_a7_4 = Beta("ASC2_a7_4", startset[r,150], None, None, 0)
    ASC2_a8_4 = Beta("ASC2_a8_4", startset[r,151], None, None, 0)
    ASC2_a9_4 = Beta("ASC2_a9_4", startset[r,152], None, None, 0)
    ASC2_a10_4 = Beta("ASC2_a10_4", startset[r,153], None, None, 0)
    ASC2_a11_4 = Beta("ASC2_a11_4", startset[r,154], None, None, 0)
    ASC2_a12_4 = Beta("ASC2_a12_4", startset[r,155], None, None, 0)
    ASC2_a1_5 = Beta("ASC2_a1_5", startset[r,156], None, None, 0)
    ASC2_a2_5 = Beta("ASC2_a2_5", startset[r,157], None, None, 0)
    ASC2_a3_5 = Beta("ASC2_a3_5", startset[r,158], None, None, 0)
    ASC2_a4_5 = Beta("ASC2_a4_5", startset[r,159], None, None, 0)
    ASC2_a5_5 = Beta("ASC2_a5_5", startset[r,160], None, None, 0)
    ASC2_a6_5 = Beta("ASC2_a6_5", startset[r,161], None, None, 0)
    ASC2_a7_5 = Beta("ASC2_a7_5", startset[r,162], None, None, 0)
    ASC2_a8_5 = Beta("ASC2_a8_5", startset[r,163], None, None, 0)
    ASC2_a9_5 = Beta("ASC2_a9_5", startset[r,164], None, None, 0)
    ASC2_a10_5 = Beta("ASC2_a10_5", startset[r,165], None, None, 0)
    ASC2_a11_5 = Beta("ASC2_a11_5", startset[r,166], None, None, 0)
    ASC2_a12_5 = Beta("ASC2_a12_5", startset[r,167], None, None, 0)
    ASC2_a1_6 = Beta("ASC2_a1_6", startset[r,168], None, None, 0)
    ASC2_a2_6 = Beta("ASC2_a2_6", startset[r,169], None, None, 0)
    ASC2_a3_6 = Beta("ASC2_a3_6", startset[r,170], None, None, 0)
    ASC2_a4_6 = Beta("ASC2_a4_6", startset[r,171], None, None, 0)
    ASC2_a5_6 = Beta("ASC2_a5_6", startset[r,172], None, None, 0)
    ASC2_a6_6 = Beta("ASC2_a6_6", startset[r,173], None, None, 0)
    ASC2_a7_6 = Beta("ASC2_a7_6", startset[r,174], None, None, 0)
    ASC2_a8_6 = Beta("ASC2_a8_6", startset[r,175], None, None, 0)
    ASC2_a9_6 = Beta("ASC2_a9_6", startset[r,176], None, None, 0)
    ASC2_a10_6 = Beta("ASC2_a10_6", startset[r,177], None, None, 0)
    ASC2_a11_6 = Beta("ASC2_a11_6", startset[r,178], None, None, 0)
    ASC2_a12_6 = Beta("ASC2_a12_6", startset[r,179], None, None, 0)
    ASC2_a1_7 = Beta("ASC2_a1_7", startset[r,180], None, None, 0)
    ASC2_a2_7 = Beta("ASC2_a2_7", startset[r,181], None, None, 0)
    ASC2_a3_7 = Beta("ASC2_a3_7", startset[r,182], None, None, 0)
    ASC2_a4_7 = Beta("ASC2_a4_7", startset[r,183], None, None, 0)
    ASC2_a5_7 = Beta("ASC2_a5_7", startset[r,184], None, None, 0)
    ASC2_a6_7 = Beta("ASC2_a6_7", startset[r,185], None, None, 0)
    ASC2_a7_7 = Beta("ASC2_a7_7", startset[r,186], None, None, 0)
    ASC2_a8_7 = Beta("ASC2_a8_7", startset[r,187], None, None, 0)
    ASC2_a9_7 = Beta("ASC2_a9_7", startset[r,188], None, None, 0)
    ASC2_a10_7 = Beta("ASC2_a10_7", startset[r,189], None, None, 0)
    ASC2_a11_7 = Beta("ASC2_a11_7", startset[r,190], None, None, 0)
    ASC2_a12_7 = Beta("ASC2_a12_7", startset[r,191], None, None, 0)
    ASC3_a1_0 = Beta("ASC3_a1_0", startset[r,192], None, None, 1)
    ASC3_a2_0 = Beta("ASC3_a2_0", startset[r,193], None, None, 1)
    ASC3_a3_0 = Beta("ASC3_a3_0", startset[r,194], None, None, 1)
    ASC3_a4_0 = Beta("ASC3_a4_0", startset[r,195], None, None, 1)
    ASC3_a5_0 = Beta("ASC3_a5_0", startset[r,196], None, None, 1)
    ASC3_a6_0 = Beta("ASC3_a6_0", startset[r,197], None, None, 1)
    ASC3_a7_0 = Beta("ASC3_a7_0", startset[r,198], None, None, 1)
    ASC3_a8_0 = Beta("ASC3_a8_0", startset[r,199], None, None, 1)
    ASC3_a9_0 = Beta("ASC3_a9_0", startset[r,200], None, None, 1)
    ASC3_a10_0 = Beta("ASC3_a10_0", startset[r,201], None, None, 1)
    ASC3_a11_0 = Beta("ASC3_a11_0", startset[r,202], None, None, 1)
    ASC3_a12_0 = Beta("ASC3_a12_0", startset[r,203], None, None, 1)
    ASC3_a1_1 = Beta("ASC3_a1_1", startset[r,204], None, None, 0)
    ASC3_a2_1 = Beta("ASC3_a2_1", startset[r,205], None, None, 0)
    ASC3_a3_1 = Beta("ASC3_a3_1", startset[r,206], None, None, 0)
    ASC3_a4_1 = Beta("ASC3_a4_1", startset[r,207], None, None, 0)
    ASC3_a5_1 = Beta("ASC3_a5_1", startset[r,208], None, None, 0)
    ASC3_a6_1 = Beta("ASC3_a6_1", startset[r,209], None, None, 0)
    ASC3_a7_1 = Beta("ASC3_a7_1", startset[r,210], None, None, 0)
    ASC3_a8_1 = Beta("ASC3_a8_1", startset[r,211], None, None, 0)
    ASC3_a9_1 = Beta("ASC3_a9_1", startset[r,212], None, None, 0)
    ASC3_a10_1 = Beta("ASC3_a10_1", startset[r,213], None, None, 0)
    ASC3_a11_1 = Beta("ASC3_a11_1", startset[r,214], None, None, 0)
    ASC3_a12_1 = Beta("ASC3_a12_1", startset[r,215], None, None, 0)
    ASC3_a1_2 = Beta("ASC3_a1_2", startset[r,216], None, None, 0)
    ASC3_a2_2 = Beta("ASC3_a2_2", startset[r,217], None, None, 0)
    ASC3_a3_2 = Beta("ASC3_a3_2", startset[r,218], None, None, 0)
    ASC3_a4_2 = Beta("ASC3_a4_2", startset[r,219], None, None, 0)
    ASC3_a5_2 = Beta("ASC3_a5_2", startset[r,220], None, None, 0)
    ASC3_a6_2 = Beta("ASC3_a6_2", startset[r,221], None, None, 0)
    ASC3_a7_2 = Beta("ASC3_a7_2", startset[r,222], None, None, 0)
    ASC3_a8_2 = Beta("ASC3_a8_2", startset[r,223], None, None, 0)
    ASC3_a9_2 = Beta("ASC3_a9_2", startset[r,224], None, None, 0)
    ASC3_a10_2 = Beta("ASC3_a10_2", startset[r,225], None, None, 0)
    ASC3_a11_2 = Beta("ASC3_a11_2", startset[r,226], None, None, 0)
    ASC3_a12_2 = Beta("ASC3_a12_2", startset[r,227], None, None, 0)
    ASC3_a1_3 = Beta("ASC3_a1_3", startset[r,228], None, None, 0)
    ASC3_a2_3 = Beta("ASC3_a2_3", startset[r,229], None, None, 0)
    ASC3_a3_3 = Beta("ASC3_a3_3", startset[r,230], None, None, 0)
    ASC3_a4_3 = Beta("ASC3_a4_3", startset[r,231], None, None, 0)
    ASC3_a5_3 = Beta("ASC3_a5_3", startset[r,232], None, None, 0)
    ASC3_a6_3 = Beta("ASC3_a6_3", startset[r,233], None, None, 0)
    ASC3_a7_3 = Beta("ASC3_a7_3", startset[r,234], None, None, 0)
    ASC3_a8_3 = Beta("ASC3_a8_3", startset[r,235], None, None, 0)
    ASC3_a9_3 = Beta("ASC3_a9_3", startset[r,236], None, None, 0)
    ASC3_a10_3 = Beta("ASC3_a10_3", startset[r,237], None, None, 0)
    ASC3_a11_3 = Beta("ASC3_a11_3", startset[r,238], None, None, 0)
    ASC3_a12_3 = Beta("ASC3_a12_3", startset[r,239], None, None, 0)
    ASC3_a1_4 = Beta("ASC3_a1_4", startset[r,240], None, None, 0)
    ASC3_a2_4 = Beta("ASC3_a2_4", startset[r,241], None, None, 0)
    ASC3_a3_4 = Beta("ASC3_a3_4", startset[r,242], None, None, 0)
    ASC3_a4_4 = Beta("ASC3_a4_4", startset[r,243], None, None, 0)
    ASC3_a5_4 = Beta("ASC3_a5_4", startset[r,244], None, None, 0)
    ASC3_a6_4 = Beta("ASC3_a6_4", startset[r,245], None, None, 0)
    ASC3_a7_4 = Beta("ASC3_a7_4", startset[r,246], None, None, 0)
    ASC3_a8_4 = Beta("ASC3_a8_4", startset[r,247], None, None, 0)
    ASC3_a9_4 = Beta("ASC3_a9_4", startset[r,248], None, None, 0)
    ASC3_a10_4 = Beta("ASC3_a10_4", startset[r,249], None, None, 0)
    ASC3_a11_4 = Beta("ASC3_a11_4", startset[r,250], None, None, 0)
    ASC3_a12_4 = Beta("ASC3_a12_4", startset[r,251], None, None, 0)
    ASC3_a1_5 = Beta("ASC3_a1_5", startset[r,252], None, None, 0)
    ASC3_a2_5 = Beta("ASC3_a2_5", startset[r,253], None, None, 0)
    ASC3_a3_5 = Beta("ASC3_a3_5", startset[r,254], None, None, 0)
    ASC3_a4_5 = Beta("ASC3_a4_5", startset[r,255], None, None, 0)
    ASC3_a5_5 = Beta("ASC3_a5_5", startset[r,256], None, None, 0)
    ASC3_a6_5 = Beta("ASC3_a6_5", startset[r,257], None, None, 0)
    ASC3_a7_5 = Beta("ASC3_a7_5", startset[r,258], None, None, 0)
    ASC3_a8_5 = Beta("ASC3_a8_5", startset[r,259], None, None, 0)
    ASC3_a9_5 = Beta("ASC3_a9_5", startset[r,260], None, None, 0)
    ASC3_a10_5 = Beta("ASC3_a10_5", startset[r,261], None, None, 0)
    ASC3_a11_5 = Beta("ASC3_a11_5", startset[r,262], None, None, 0)
    ASC3_a12_5 = Beta("ASC3_a12_5", startset[r,263], None, None, 0)
    ASC3_a1_6 = Beta("ASC3_a1_6", startset[r,264], None, None, 0)
    ASC3_a2_6 = Beta("ASC3_a2_6", startset[r,265], None, None, 0)
    ASC3_a3_6 = Beta("ASC3_a3_6", startset[r,266], None, None, 0)
    ASC3_a4_6 = Beta("ASC3_a4_6", startset[r,267], None, None, 0)
    ASC3_a5_6 = Beta("ASC3_a5_6", startset[r,268], None, None, 0)
    ASC3_a6_6 = Beta("ASC3_a6_6", startset[r,269], None, None, 0)
    ASC3_a7_6 = Beta("ASC3_a7_6", startset[r,270], None, None, 0)
    ASC3_a8_6 = Beta("ASC3_a8_6", startset[r,271], None, None, 0)
    ASC3_a9_6 = Beta("ASC3_a9_6", startset[r,272], None, None, 0)
    ASC3_a10_6 = Beta("ASC3_a10_6", startset[r,273], None, None, 0)
    ASC3_a11_6 = Beta("ASC3_a11_6", startset[r,274], None, None, 0)
    ASC3_a12_6 = Beta("ASC3_a12_6", startset[r,275], None, None, 0)
    ASC3_a1_7 = Beta("ASC3_a1_7", startset[r,276], None, None, 0)
    ASC3_a2_7 = Beta("ASC3_a2_7", startset[r,277], None, None, 0)
    ASC3_a3_7 = Beta("ASC3_a3_7", startset[r,278], None, None, 0)
    ASC3_a4_7 = Beta("ASC3_a4_7", startset[r,279], None, None, 0)
    ASC3_a5_7 = Beta("ASC3_a5_7", startset[r,280], None, None, 0)
    ASC3_a6_7 = Beta("ASC3_a6_7", startset[r,281], None, None, 0)
    ASC3_a7_7 = Beta("ASC3_a7_7", startset[r,282], None, None, 0)
    ASC3_a8_7 = Beta("ASC3_a8_7", startset[r,283], None, None, 0)
    ASC3_a9_7 = Beta("ASC3_a9_7", startset[r,284], None, None, 0)
    ASC3_a10_7 = Beta("ASC3_a10_7", startset[r,285], None, None, 0)
    ASC3_a11_7 = Beta("ASC3_a11_7", startset[r,286], None, None, 0)
    ASC3_a12_7 = Beta("ASC3_a12_7", startset[r,287], None, None, 0)
    B_eld_10 = Beta("eld_10", startset[r,288], None, None, 1)
    B_dif_10 = Beta("dif_10", startset[r,289], None, None, 1)
    B_hel_10 = Beta("hel_10", startset[r,290], None, None, 1)
    B_ful_10 = Beta("ful_10", startset[r,291], None, None, 1)
    B_nee_10 = Beta("nee_10", startset[r,292], None, None, 1)
    B_veh_10 = Beta("veh_10", startset[r,293], None, None, 1)
    B_eld_11 = Beta("eld_11", startset[r,294], None, None, 0)
    B_dif_11 = Beta("dif_11", startset[r,295], None, None, 0)
    B_hel_11 = Beta("hel_11", startset[r,296], None, None, 0)
    B_ful_11 = Beta("ful_11", startset[r,297], None, None, 0)
    B_nee_11 = Beta("nee_11", startset[r,298], None, None, 0)
    B_veh_11 = Beta("veh_11", startset[r,299], None, None, 0)
    B_eld_12 = Beta("eld_12", startset[r,300], None, None, 0)
    B_dif_12 = Beta("dif_12", startset[r,301], None, None, 0)
    B_hel_12 = Beta("hel_12", startset[r,302], None, None, 0)
    B_ful_12 = Beta("ful_12", startset[r,303], None, None, 0)
    B_nee_12 = Beta("nee_12", startset[r,304], None, None, 0)
    B_veh_12 = Beta("veh_12", startset[r,305], None, None, 0)
    B_eld_13 = Beta("eld_13", startset[r,306], None, None, 0)
    B_dif_13 = Beta("dif_13", startset[r,307], None, None, 0)
    B_hel_13 = Beta("hel_13", startset[r,308], None, None, 0)
    B_ful_13 = Beta("ful_13", startset[r,309], None, None, 0)
    B_nee_13 = Beta("nee_13", startset[r,310], None, None, 0)
    B_veh_13 = Beta("veh_13", startset[r,311], None, None, 0)
    B_eld_14 = Beta("eld_14", startset[r,312], None, None, 0)
    B_dif_14 = Beta("dif_14", startset[r,313], None, None, 0)
    B_hel_14 = Beta("hel_14", startset[r,314], None, None, 0)
    B_ful_14 = Beta("ful_14", startset[r,315], None, None, 0)
    B_nee_14 = Beta("nee_14", startset[r,316], None, None, 0)
    B_veh_14 = Beta("veh_14", startset[r,317], None, None, 0)
    B_eld_15 = Beta("eld_15", startset[r,318], None, None, 0)
    B_dif_15 = Beta("dif_15", startset[r,319], None, None, 0)
    B_hel_15 = Beta("hel_15", startset[r,320], None, None, 0)
    B_ful_15 = Beta("ful_15", startset[r,321], None, None, 0)
    B_nee_15 = Beta("nee_15", startset[r,322], None, None, 0)
    B_veh_15 = Beta("veh_15", startset[r,323], None, None, 0)
    B_eld_16 = Beta("eld_16", startset[r,324], None, None, 0)
    B_dif_16 = Beta("dif_16", startset[r,325], None, None, 0)
    B_hel_16 = Beta("hel_16", startset[r,326], None, None, 0)
    B_ful_16 = Beta("ful_16", startset[r,327], None, None, 0)
    B_nee_16 = Beta("nee_16", startset[r,328], None, None, 0)
    B_veh_16 = Beta("veh_16", startset[r,329], None, None, 0)
    B_eld_17 = Beta("eld_17", startset[r,330], None, None, 0)
    B_dif_17 = Beta("dif_17", startset[r,331], None, None, 0)
    B_hel_17 = Beta("hel_17", startset[r,332], None, None, 0)
    B_ful_17 = Beta("ful_17", startset[r,333], None, None, 0)
    B_nee_17 = Beta("nee_17", startset[r,334], None, None, 0)
    B_veh_17 = Beta("veh_17", startset[r,335], None, None, 0)
    B_eld_20 = Beta("eld_20", startset[r,336], None, None, 1)
    B_dif_20 = Beta("dif_20", startset[r,337], None, None, 1)
    B_hel_20 = Beta("hel_20", startset[r,338], None, None, 1)
    B_ful_20 = Beta("ful_20", startset[r,339], None, None, 1)
    B_nee_20 = Beta("nee_20", startset[r,340], None, None, 1)
    B_veh_20 = Beta("veh_20", startset[r,341], None, None, 1)
    B_eld_21 = Beta("eld_21", startset[r,342], None, None, 0)
    B_dif_21 = Beta("dif_21", startset[r,343], None, None, 0)
    B_hel_21 = Beta("hel_21", startset[r,344], None, None, 0)
    B_ful_21 = Beta("ful_21", startset[r,345], None, None, 0)
    B_nee_21 = Beta("nee_21", startset[r,346], None, None, 0)
    B_veh_21 = Beta("veh_21", startset[r,347], None, None, 0)
    B_eld_22 = Beta("eld_22", startset[r,348], None, None, 0)
    B_dif_22 = Beta("dif_22", startset[r,349], None, None, 0)
    B_hel_22 = Beta("hel_22", startset[r,350], None, None, 0)
    B_ful_22 = Beta("ful_22", startset[r,351], None, None, 0)
    B_nee_22 = Beta("nee_22", startset[r,352], None, None, 0)
    B_veh_22 = Beta("veh_22", startset[r,353], None, None, 0)
    B_eld_23 = Beta("eld_23", startset[r,354], None, None, 0)
    B_dif_23 = Beta("dif_23", startset[r,355], None, None, 0)
    B_hel_23 = Beta("hel_23", startset[r,356], None, None, 0)
    B_ful_23 = Beta("ful_23", startset[r,357], None, None, 0)
    B_nee_23 = Beta("nee_23", startset[r,358], None, None, 0)
    B_veh_23 = Beta("veh_23", startset[r,359], None, None, 0)
    B_eld_24 = Beta("eld_24", startset[r,360], None, None, 0)
    B_dif_24 = Beta("dif_24", startset[r,361], None, None, 0)
    B_hel_24 = Beta("hel_24", startset[r,362], None, None, 0)
    B_ful_24 = Beta("ful_24", startset[r,363], None, None, 0)
    B_nee_24 = Beta("nee_24", startset[r,364], None, None, 0)
    B_veh_24 = Beta("veh_24", startset[r,365], None, None, 0)
    B_eld_25 = Beta("eld_25", startset[r,366], None, None, 0)
    B_dif_25 = Beta("dif_25", startset[r,367], None, None, 0)
    B_hel_25 = Beta("hel_25", startset[r,368], None, None, 0)
    B_ful_25 = Beta("ful_25", startset[r,369], None, None, 0)
    B_nee_25 = Beta("nee_25", startset[r,370], None, None, 0)
    B_veh_25 = Beta("veh_25", startset[r,371], None, None, 0)
    B_eld_26 = Beta("eld_26", startset[r,372], None, None, 0)
    B_dif_26 = Beta("dif_26", startset[r,373], None, None, 0)
    B_hel_26 = Beta("hel_26", startset[r,374], None, None, 0)
    B_ful_26 = Beta("ful_26", startset[r,375], None, None, 0)
    B_nee_26 = Beta("nee_26", startset[r,376], None, None, 0)
    B_veh_26 = Beta("veh_26", startset[r,377], None, None, 0)
    B_eld_27 = Beta("eld_27", startset[r,378], None, None, 0)
    B_dif_27 = Beta("dif_27", startset[r,379], None, None, 0)
    B_hel_27 = Beta("hel_27", startset[r,380], None, None, 0)
    B_ful_27 = Beta("ful_27", startset[r,381], None, None, 0)
    B_nee_27 = Beta("nee_27", startset[r,382], None, None, 0)
    B_veh_27 = Beta("veh_27", startset[r,383], None, None, 0)
    B_eld_30 = Beta("eld_30", startset[r,384], None, None, 1)
    B_dif_30 = Beta("dif_30", startset[r,385], None, None, 1)
    B_hel_30 = Beta("hel_30", startset[r,386], None, None, 1)
    B_ful_30 = Beta("ful_30", startset[r,387], None, None, 1)
    B_nee_30 = Beta("nee_30", startset[r,388], None, None, 1)
    B_veh_30 = Beta("veh_30", startset[r,389], None, None, 1)
    B_eld_31 = Beta("eld_31", startset[r,390], None, None, 0)
    B_dif_31 = Beta("dif_31", startset[r,391], None, None, 0)
    B_hel_31 = Beta("hel_31", startset[r,392], None, None, 0)
    B_ful_31 = Beta("ful_31", startset[r,393], None, None, 0)
    B_nee_31 = Beta("nee_31", startset[r,394], None, None, 0)
    B_veh_31 = Beta("veh_31", startset[r,395], None, None, 0)
    B_eld_32 = Beta("eld_32", startset[r,396], None, None, 0)
    B_dif_32 = Beta("dif_32", startset[r,397], None, None, 0)
    B_hel_32 = Beta("hel_32", startset[r,398], None, None, 0)
    B_ful_32 = Beta("ful_32", startset[r,399], None, None, 0)
    B_nee_32 = Beta("nee_32", startset[r,400], None, None, 0)
    B_veh_32 = Beta("veh_32", startset[r,401], None, None, 0)
    B_eld_33 = Beta("eld_33", startset[r,402], None, None, 0)
    B_dif_33 = Beta("dif_33", startset[r,403], None, None, 0)
    B_hel_33 = Beta("hel_33", startset[r,404], None, None, 0)
    B_ful_33 = Beta("ful_33", startset[r,405], None, None, 0)
    B_nee_33 = Beta("nee_33", startset[r,406], None, None, 0)
    B_veh_33 = Beta("veh_33", startset[r,407], None, None, 0)
    B_eld_34 = Beta("eld_34", startset[r,408], None, None, 0)
    B_dif_34 = Beta("dif_34", startset[r,409], None, None, 0)
    B_hel_34 = Beta("hel_34", startset[r,410], None, None, 0)
    B_ful_34 = Beta("ful_34", startset[r,411], None, None, 0)
    B_nee_34 = Beta("nee_34", startset[r,412], None, None, 0)
    B_veh_34 = Beta("veh_34", startset[r,413], None, None, 0)
    B_eld_35 = Beta("eld_35", startset[r,414], None, None, 0)
    B_dif_35 = Beta("dif_35", startset[r,415], None, None, 0)
    B_hel_35 = Beta("hel_35", startset[r,416], None, None, 0)
    B_ful_35 = Beta("ful_35", startset[r,417], None, None, 0)
    B_nee_35 = Beta("nee_35", startset[r,418], None, None, 0)
    B_veh_35 = Beta("veh_35", startset[r,419], None, None, 0)
    B_eld_36 = Beta("eld_36", startset[r,420], None, None, 0)
    B_dif_36 = Beta("dif_36", startset[r,421], None, None, 0)
    B_hel_36 = Beta("hel_36", startset[r,422], None, None, 0)
    B_ful_36 = Beta("ful_36", startset[r,423], None, None, 0)
    B_nee_36 = Beta("nee_36", startset[r,424], None, None, 0)
    B_veh_36 = Beta("veh_36", startset[r,425], None, None, 0)
    B_eld_37 = Beta("eld_37", startset[r,426], None, None, 0)
    B_dif_37 = Beta("dif_37", startset[r,427], None, None, 0)
    B_hel_37 = Beta("hel_37", startset[r,428], None, None, 0)
    B_ful_37 = Beta("ful_37", startset[r,429], None, None, 0)
    B_nee_37 = Beta("nee_37", startset[r,430], None, None, 0)
    B_veh_37 = Beta("veh_37", startset[r,431], None, None, 0)
    s1 = Beta("s1",classset[r,0],-100,100,1)
    s2 = Beta("s2",classset[r,1],-100,100,0)
    s3 = Beta("s3",classset[r,2],-100,100,0)

    V1_a1_0 = ASC1_a1_0 + B_ful_10*full_time + B_nee_10*neet

    V1_a2_0 = ASC1_a2_0 + B_veh_10*vehicle

    V1_a3_0 = ASC1_a3_0

    V1_a4_0 = ASC1_a4_0 + B_dif_10*difficulties

    V1_a5_0 = ASC1_a5_0 + B_eld_10*elder + B_hel_10*help_needed

    V1_a6_0 = ASC1_a6_0 + B_hel_10*help_needed

    V1_a7_0 = ASC1_a7_0 + B_hel_10*help_needed

    V1_a8_0 = ASC1_a8_0

    V1_a9_0 = ASC1_a9_0 + B_hel_10*help_needed

    V1_a10_0 = ASC1_a10_0

    V1_a11_0 = ASC1_a11_0 + B_hel_10*help_needed

    V1_a12_0 = ASC1_a12_0

    V1_a1_1 = ASC1_a1_1 + B_ful_11*full_time + B_nee_11*neet

    V1_a2_1 = ASC1_a2_1 + B_veh_11*vehicle

    V1_a3_1 = ASC1_a3_1

    V1_a4_1 = ASC1_a4_1 + B_dif_11*difficulties

    V1_a5_1 = ASC1_a5_1 + B_eld_11*elder + B_hel_11*help_needed

    V1_a6_1 = ASC1_a6_1 + B_hel_11*help_needed

    V1_a7_1 = ASC1_a7_1 + B_hel_11*help_needed

    V1_a8_1 = ASC1_a8_1

    V1_a9_1 = ASC1_a9_1 + B_hel_11*help_needed

    V1_a10_1 = ASC1_a10_1

    V1_a11_1 = ASC1_a11_1 + B_hel_11*help_needed

    V1_a12_1 = ASC1_a12_1

    V1_a1_2 = ASC1_a1_2 + B_ful_12*full_time + B_nee_12*neet

    V1_a2_2 = ASC1_a2_2 + B_veh_12*vehicle

    V1_a3_2 = ASC1_a3_2

    V1_a4_2 = ASC1_a4_2 + B_dif_12*difficulties

    V1_a5_2 = ASC1_a5_2 + B_eld_12*elder + B_hel_12*help_needed

    V1_a6_2 = ASC1_a6_2 + B_hel_12*help_needed

    V1_a7_2 = ASC1_a7_2 + B_hel_12*help_needed

    V1_a8_2 = ASC1_a8_2

    V1_a9_2 = ASC1_a9_2 + B_hel_12*help_needed

    V1_a10_2 = ASC1_a10_2

    V1_a11_2 = ASC1_a11_2 + B_hel_12*help_needed

    V1_a12_2 = ASC1_a12_2

    V1_a1_3 = ASC1_a1_3 + B_ful_13*full_time + B_nee_13*neet

    V1_a2_3 = ASC1_a2_3 + B_veh_13*vehicle

    V1_a3_3 = ASC1_a3_3

    V1_a4_3 = ASC1_a4_3 + B_dif_13*difficulties

    V1_a5_3 = ASC1_a5_3 + B_eld_13*elder + B_hel_13*help_needed

    V1_a6_3 = ASC1_a6_3 + B_hel_13*help_needed

    V1_a7_3 = ASC1_a7_3 + B_hel_13*help_needed

    V1_a8_3 = ASC1_a8_3

    V1_a9_3 = ASC1_a9_3 + B_hel_13*help_needed

    V1_a10_3 = ASC1_a10_3

    V1_a11_3 = ASC1_a11_3 + B_hel_13*help_needed

    V1_a12_3 = ASC1_a12_3

    V1_a1_4 = ASC1_a1_4 + B_ful_14*full_time + B_nee_14*neet

    V1_a2_4 = ASC1_a2_4 + B_veh_14*vehicle

    V1_a3_4 = ASC1_a3_4

    V1_a4_4 = ASC1_a4_4 + B_dif_14*difficulties

    V1_a5_4 = ASC1_a5_4 + B_eld_14*elder + B_hel_14*help_needed

    V1_a6_4 = ASC1_a6_4 + B_hel_14*help_needed

    V1_a7_4 = ASC1_a7_4 + B_hel_14*help_needed

    V1_a8_4 = ASC1_a8_4

    V1_a9_4 = ASC1_a9_4 + B_hel_14*help_needed

    V1_a10_4 = ASC1_a10_4

    V1_a11_4 = ASC1_a11_4 + B_hel_14*help_needed

    V1_a12_4 = ASC1_a12_4

    V1_a1_5 = ASC1_a1_5 + B_ful_15*full_time + B_nee_15*neet

    V1_a2_5 = ASC1_a2_5 + B_veh_15*vehicle

    V1_a3_5 = ASC1_a3_5

    V1_a4_5 = ASC1_a4_5 + B_dif_15*difficulties

    V1_a5_5 = ASC1_a5_5 + B_eld_15*elder + B_hel_15*help_needed

    V1_a6_5 = ASC1_a6_5 + B_hel_15*help_needed

    V1_a7_5 = ASC1_a7_5 + B_hel_15*help_needed

    V1_a8_5 = ASC1_a8_5

    V1_a9_5 = ASC1_a9_5 + B_hel_15*help_needed

    V1_a10_5 = ASC1_a10_5

    V1_a11_5 = ASC1_a11_5 + B_hel_15*help_needed

    V1_a12_5 = ASC1_a12_5

    V1_a1_6 = ASC1_a1_6 + B_ful_16*full_time + B_nee_16*neet

    V1_a2_6 = ASC1_a2_6 + B_veh_16*vehicle

    V1_a3_6 = ASC1_a3_6

    V1_a4_6 = ASC1_a4_6 + B_dif_16*difficulties

    V1_a5_6 = ASC1_a5_6 + B_eld_16*elder + B_hel_16*help_needed

    V1_a6_6 = ASC1_a6_6 + B_hel_16*help_needed

    V1_a7_6 = ASC1_a7_6 + B_hel_16*help_needed

    V1_a8_6 = ASC1_a8_6

    V1_a9_6 = ASC1_a9_6 + B_hel_16*help_needed

    V1_a10_6 = ASC1_a10_6

    V1_a11_6 = ASC1_a11_6 + B_hel_16*help_needed

    V1_a12_6 = ASC1_a12_6

    V1_a1_7 = ASC1_a1_7 + B_ful_17*full_time + B_nee_17*neet

    V1_a2_7 = ASC1_a2_7 + B_veh_17*vehicle

    V1_a3_7 = ASC1_a3_7

    V1_a4_7 = ASC1_a4_7 + B_dif_17*difficulties

    V1_a5_7 = ASC1_a5_7 + B_eld_17*elder + B_hel_17*help_needed

    V1_a6_7 = ASC1_a6_7 + B_hel_17*help_needed

    V1_a7_7 = ASC1_a7_7 + B_hel_17*help_needed

    V1_a8_7 = ASC1_a8_7

    V1_a9_7 = ASC1_a9_7 + B_hel_17*help_needed

    V1_a10_7 = ASC1_a10_7

    V1_a11_7 = ASC1_a11_7 + B_hel_17*help_needed

    V1_a12_7 = ASC1_a12_7

    V2_a1_0 = ASC2_a1_0 + B_ful_20*full_time + B_nee_20*neet

    V2_a2_0 = ASC2_a2_0 + B_veh_20*vehicle

    V2_a3_0 = ASC2_a3_0

    V2_a4_0 = ASC2_a4_0 + B_dif_20*difficulties

    V2_a5_0 = ASC2_a5_0 + B_eld_20*elder + B_hel_20*help_needed

    V2_a6_0 = ASC2_a6_0 + B_hel_20*help_needed

    V2_a7_0 = ASC2_a7_0 + B_hel_20*help_needed

    V2_a8_0 = ASC2_a8_0

    V2_a9_0 = ASC2_a9_0 + B_hel_20*help_needed

    V2_a10_0 = ASC2_a10_0

    V2_a11_0 = ASC2_a11_0 + B_hel_20*help_needed

    V2_a12_0 = ASC2_a12_0

    V2_a1_1 = ASC2_a1_1 + B_ful_21*full_time + B_nee_21*neet

    V2_a2_1 = ASC2_a2_1 + B_veh_21*vehicle

    V2_a3_1 = ASC2_a3_1

    V2_a4_1 = ASC2_a4_1 + B_dif_21*difficulties

    V2_a5_1 = ASC2_a5_1 + B_eld_21*elder + B_hel_21*help_needed

    V2_a6_1 = ASC2_a6_1 + B_hel_21*help_needed

    V2_a7_1 = ASC2_a7_1 + B_hel_21*help_needed

    V2_a8_1 = ASC2_a8_1

    V2_a9_1 = ASC2_a9_1 + B_hel_21*help_needed

    V2_a10_1 = ASC2_a10_1

    V2_a11_1 = ASC2_a11_1 + B_hel_21*help_needed

    V2_a12_1 = ASC2_a12_1

    V2_a1_2 = ASC2_a1_2 + B_ful_22*full_time + B_nee_22*neet

    V2_a2_2 = ASC2_a2_2 + B_veh_22*vehicle

    V2_a3_2 = ASC2_a3_2

    V2_a4_2 = ASC2_a4_2 + B_dif_22*difficulties

    V2_a5_2 = ASC2_a5_2 + B_eld_22*elder + B_hel_22*help_needed

    V2_a6_2 = ASC2_a6_2 + B_hel_22*help_needed

    V2_a7_2 = ASC2_a7_2 + B_hel_22*help_needed

    V2_a8_2 = ASC2_a8_2

    V2_a9_2 = ASC2_a9_2 + B_hel_22*help_needed

    V2_a10_2 = ASC2_a10_2

    V2_a11_2 = ASC2_a11_2 + B_hel_22*help_needed

    V2_a12_2 = ASC2_a12_2

    V2_a1_3 = ASC2_a1_3 + B_ful_23*full_time + B_nee_23*neet

    V2_a2_3 = ASC2_a2_3 + B_veh_23*vehicle

    V2_a3_3 = ASC2_a3_3

    V2_a4_3 = ASC2_a4_3 + B_dif_23*difficulties

    V2_a5_3 = ASC2_a5_3 + B_eld_23*elder + B_hel_23*help_needed

    V2_a6_3 = ASC2_a6_3 + B_hel_23*help_needed

    V2_a7_3 = ASC2_a7_3 + B_hel_23*help_needed

    V2_a8_3 = ASC2_a8_3

    V2_a9_3 = ASC2_a9_3 + B_hel_23*help_needed

    V2_a10_3 = ASC2_a10_3

    V2_a11_3 = ASC2_a11_3 + B_hel_23*help_needed

    V2_a12_3 = ASC2_a12_3

    V2_a1_4 = ASC2_a1_4 + B_ful_24*full_time + B_nee_24*neet

    V2_a2_4 = ASC2_a2_4 + B_veh_24*vehicle

    V2_a3_4 = ASC2_a3_4

    V2_a4_4 = ASC2_a4_4 + B_dif_24*difficulties

    V2_a5_4 = ASC2_a5_4 + B_eld_24*elder + B_hel_24*help_needed

    V2_a6_4 = ASC2_a6_4 + B_hel_24*help_needed

    V2_a7_4 = ASC2_a7_4 + B_hel_24*help_needed

    V2_a8_4 = ASC2_a8_4

    V2_a9_4 = ASC2_a9_4 + B_hel_24*help_needed

    V2_a10_4 = ASC2_a10_4

    V2_a11_4 = ASC2_a11_4 + B_hel_24*help_needed

    V2_a12_4 = ASC2_a12_4

    V2_a1_5 = ASC2_a1_5 + B_ful_25*full_time + B_nee_25*neet

    V2_a2_5 = ASC2_a2_5 + B_veh_25*vehicle

    V2_a3_5 = ASC2_a3_5

    V2_a4_5 = ASC2_a4_5 + B_dif_25*difficulties

    V2_a5_5 = ASC2_a5_5 + B_eld_25*elder + B_hel_25*help_needed

    V2_a6_5 = ASC2_a6_5 + B_hel_25*help_needed

    V2_a7_5 = ASC2_a7_5 + B_hel_25*help_needed

    V2_a8_5 = ASC2_a8_5

    V2_a9_5 = ASC2_a9_5 + B_hel_25*help_needed

    V2_a10_5 = ASC2_a10_5

    V2_a11_5 = ASC2_a11_5 + B_hel_25*help_needed

    V2_a12_5 = ASC2_a12_5

    V2_a1_6 = ASC2_a1_6 + B_ful_26*full_time + B_nee_26*neet

    V2_a2_6 = ASC2_a2_6 + B_veh_26*vehicle

    V2_a3_6 = ASC2_a3_6

    V2_a4_6 = ASC2_a4_6 + B_dif_26*difficulties

    V2_a5_6 = ASC2_a5_6 + B_eld_26*elder + B_hel_26*help_needed

    V2_a6_6 = ASC2_a6_6 + B_hel_26*help_needed

    V2_a7_6 = ASC2_a7_6 + B_hel_26*help_needed

    V2_a8_6 = ASC2_a8_6

    V2_a9_6 = ASC2_a9_6 + B_hel_26*help_needed

    V2_a10_6 = ASC2_a10_6

    V2_a11_6 = ASC2_a11_6 + B_hel_26*help_needed

    V2_a12_6 = ASC2_a12_6

    V2_a1_7 = ASC2_a1_7 + B_ful_27*full_time + B_nee_27*neet

    V2_a2_7 = ASC2_a2_7 + B_veh_27*vehicle

    V2_a3_7 = ASC2_a3_7

    V2_a4_7 = ASC2_a4_7 + B_dif_27*difficulties

    V2_a5_7 = ASC2_a5_7 + B_eld_27*elder + B_hel_27*help_needed

    V2_a6_7 = ASC2_a6_7 + B_hel_27*help_needed

    V2_a7_7 = ASC2_a7_7 + B_hel_27*help_needed

    V2_a8_7 = ASC2_a8_7

    V2_a9_7 = ASC2_a9_7 + B_hel_27*help_needed

    V2_a10_7 = ASC2_a10_7

    V2_a11_7 = ASC2_a11_7 + B_hel_27*help_needed

    V2_a12_7 = ASC2_a12_7

    V3_a1_0 = ASC3_a1_0 + B_ful_30*full_time + B_nee_30*neet

    V3_a2_0 = ASC3_a2_0 + B_veh_30*vehicle

    V3_a3_0 = ASC3_a3_0

    V3_a4_0 = ASC3_a4_0 + B_dif_30*difficulties

    V3_a5_0 = ASC3_a5_0 + B_eld_30*elder + B_hel_30*help_needed

    V3_a6_0 = ASC3_a6_0 + B_hel_30*help_needed

    V3_a7_0 = ASC3_a7_0 + B_hel_30*help_needed

    V3_a8_0 = ASC3_a8_0

    V3_a9_0 = ASC3_a9_0 + B_hel_30*help_needed

    V3_a10_0 = ASC3_a10_0

    V3_a11_0 = ASC3_a11_0 + B_hel_30*help_needed

    V3_a12_0 = ASC3_a12_0

    V3_a1_1 = ASC3_a1_1 + B_ful_31*full_time + B_nee_31*neet

    V3_a2_1 = ASC3_a2_1 + B_veh_31*vehicle

    V3_a3_1 = ASC3_a3_1

    V3_a4_1 = ASC3_a4_1 + B_dif_31*difficulties

    V3_a5_1 = ASC3_a5_1 + B_eld_31*elder + B_hel_31*help_needed

    V3_a6_1 = ASC3_a6_1 + B_hel_31*help_needed

    V3_a7_1 = ASC3_a7_1 + B_hel_31*help_needed

    V3_a8_1 = ASC3_a8_1

    V3_a9_1 = ASC3_a9_1 + B_hel_31*help_needed

    V3_a10_1 = ASC3_a10_1

    V3_a11_1 = ASC3_a11_1 + B_hel_31*help_needed

    V3_a12_1 = ASC3_a12_1

    V3_a1_2 = ASC3_a1_2 + B_ful_32*full_time + B_nee_32*neet

    V3_a2_2 = ASC3_a2_2 + B_veh_32*vehicle

    V3_a3_2 = ASC3_a3_2

    V3_a4_2 = ASC3_a4_2 + B_dif_32*difficulties

    V3_a5_2 = ASC3_a5_2 + B_eld_32*elder + B_hel_32*help_needed

    V3_a6_2 = ASC3_a6_2 + B_hel_32*help_needed

    V3_a7_2 = ASC3_a7_2 + B_hel_32*help_needed

    V3_a8_2 = ASC3_a8_2

    V3_a9_2 = ASC3_a9_2 + B_hel_32*help_needed

    V3_a10_2 = ASC3_a10_2

    V3_a11_2 = ASC3_a11_2 + B_hel_32*help_needed

    V3_a12_2 = ASC3_a12_2

    V3_a1_3 = ASC3_a1_3 + B_ful_33*full_time + B_nee_33*neet

    V3_a2_3 = ASC3_a2_3 + B_veh_33*vehicle

    V3_a3_3 = ASC3_a3_3

    V3_a4_3 = ASC3_a4_3 + B_dif_33*difficulties

    V3_a5_3 = ASC3_a5_3 + B_eld_33*elder + B_hel_33*help_needed

    V3_a6_3 = ASC3_a6_3 + B_hel_33*help_needed

    V3_a7_3 = ASC3_a7_3 + B_hel_33*help_needed

    V3_a8_3 = ASC3_a8_3

    V3_a9_3 = ASC3_a9_3 + B_hel_33*help_needed

    V3_a10_3 = ASC3_a10_3

    V3_a11_3 = ASC3_a11_3 + B_hel_33*help_needed

    V3_a12_3 = ASC3_a12_3

    V3_a1_4 = ASC3_a1_4 + B_ful_34*full_time + B_nee_34*neet

    V3_a2_4 = ASC3_a2_4 + B_veh_34*vehicle

    V3_a3_4 = ASC3_a3_4

    V3_a4_4 = ASC3_a4_4 + B_dif_34*difficulties

    V3_a5_4 = ASC3_a5_4 + B_eld_34*elder + B_hel_34*help_needed

    V3_a6_4 = ASC3_a6_4 + B_hel_34*help_needed

    V3_a7_4 = ASC3_a7_4 + B_hel_34*help_needed

    V3_a8_4 = ASC3_a8_4

    V3_a9_4 = ASC3_a9_4 + B_hel_34*help_needed

    V3_a10_4 = ASC3_a10_4

    V3_a11_4 = ASC3_a11_4 + B_hel_34*help_needed

    V3_a12_4 = ASC3_a12_4

    V3_a1_5 = ASC3_a1_5 + B_ful_35*full_time + B_nee_35*neet

    V3_a2_5 = ASC3_a2_5 + B_veh_35*vehicle

    V3_a3_5 = ASC3_a3_5

    V3_a4_5 = ASC3_a4_5 + B_dif_35*difficulties

    V3_a5_5 = ASC3_a5_5 + B_eld_35*elder + B_hel_35*help_needed

    V3_a6_5 = ASC3_a6_5 + B_hel_35*help_needed

    V3_a7_5 = ASC3_a7_5 + B_hel_35*help_needed

    V3_a8_5 = ASC3_a8_5

    V3_a9_5 = ASC3_a9_5 + B_hel_35*help_needed

    V3_a10_5 = ASC3_a10_5

    V3_a11_5 = ASC3_a11_5 + B_hel_35*help_needed

    V3_a12_5 = ASC3_a12_5

    V3_a1_6 = ASC3_a1_6 + B_ful_36*full_time + B_nee_36*neet

    V3_a2_6 = ASC3_a2_6 + B_veh_36*vehicle

    V3_a3_6 = ASC3_a3_6

    V3_a4_6 = ASC3_a4_6 + B_dif_36*difficulties

    V3_a5_6 = ASC3_a5_6 + B_eld_36*elder + B_hel_36*help_needed

    V3_a6_6 = ASC3_a6_6 + B_hel_36*help_needed

    V3_a7_6 = ASC3_a7_6 + B_hel_36*help_needed

    V3_a8_6 = ASC3_a8_6

    V3_a9_6 = ASC3_a9_6 + B_hel_36*help_needed

    V3_a10_6 = ASC3_a10_6

    V3_a11_6 = ASC3_a11_6 + B_hel_36*help_needed

    V3_a12_6 = ASC3_a12_6

    V3_a1_7 = ASC3_a1_7 + B_ful_37*full_time + B_nee_37*neet

    V3_a2_7 = ASC3_a2_7 + B_veh_37*vehicle

    V3_a3_7 = ASC3_a3_7

    V3_a4_7 = ASC3_a4_7 + B_dif_37*difficulties

    V3_a5_7 = ASC3_a5_7 + B_eld_37*elder + B_hel_37*help_needed

    V3_a6_7 = ASC3_a6_7 + B_hel_37*help_needed

    V3_a7_7 = ASC3_a7_7 + B_hel_37*help_needed

    V3_a8_7 = ASC3_a8_7

    V3_a9_7 = ASC3_a9_7 + B_hel_37*help_needed

    V3_a10_7 = ASC3_a10_7

    V3_a11_7 = ASC3_a11_7 + B_hel_37*help_needed

    V3_a12_7 = ASC3_a12_7


    V1_a1 = {0:V1_a1_0,1:V1_a1_1,2:V1_a1_2,3:V1_a1_3,
             4:V1_a1_4,5:V1_a1_5,6:V1_a1_6,7:V1_a1_7}
    V1_a2 = {0:V1_a2_0,1:V1_a2_1,2:V1_a2_2,3:V1_a2_3,
             4:V1_a2_4,5:V1_a2_5,6:V1_a2_6,7:V1_a2_7}
    V1_a3 = {0:V1_a3_0,1:V1_a3_1,2:V1_a3_2,3:V1_a3_3,
             4:V1_a3_4,5:V1_a3_5,6:V1_a3_6,7:V1_a3_7}
    V1_a4 = {0:V1_a4_0,1:V1_a4_1,2:V1_a4_2,3:V1_a4_3,
             4:V1_a4_4,5:V1_a4_5,6:V1_a4_6,7:V1_a4_7}
    V1_a5 = {0:V1_a5_0,1:V1_a5_1,2:V1_a5_2,3:V1_a5_3,
             4:V1_a5_4,5:V1_a5_5,6:V1_a5_6,7:V1_a5_7}
    V1_a6 = {0:V1_a6_0,1:V1_a6_1,2:V1_a6_2,3:V1_a6_3,
             4:V1_a6_4,5:V1_a6_5,6:V1_a6_6,7:V1_a6_7}
    V1_a7 = {0:V1_a7_0,1:V1_a7_1,2:V1_a7_2,3:V1_a7_3,
             4:V1_a7_4,5:V1_a7_5,6:V1_a7_6,7:V1_a7_7}
    V1_a8 = {0:V1_a8_0,1:V1_a8_1,2:V1_a8_2,3:V1_a8_3,
             4:V1_a8_4,5:V1_a8_5,6:V1_a8_6,7:V1_a8_7}
    V1_a9 = {0:V1_a9_0,1:V1_a9_1,2:V1_a9_2,3:V1_a9_3,
             4:V1_a9_4,5:V1_a9_5,6:V1_a9_6,7:V1_a9_7}
    V1_a10 = {0:V1_a10_0,1:V1_a10_1,2:V1_a10_2,3:V1_a10_3,
             4:V1_a10_4,5:V1_a10_5,6:V1_a10_6,7:V1_a10_7}
    V1_a11 = {0:V1_a11_0,1:V1_a11_1,2:V1_a11_2,3:V1_a11_3,
             4:V1_a11_4,5:V1_a11_5,6:V1_a11_6,7:V1_a11_7}
    V1_a12 = {0:V1_a12_0,1:V1_a12_1,2:V1_a12_2,3:V1_a12_3,
             4:V1_a12_4,5:V1_a12_5,6:V1_a12_6,7:V1_a12_7}
    V2_a1 = {0:V2_a1_0,1:V2_a1_1,2:V2_a1_2,3:V2_a1_3,
             4:V2_a1_4,5:V2_a1_5,6:V2_a1_6,7:V2_a1_7}
    V2_a2 = {0:V2_a2_0,1:V2_a2_1,2:V2_a2_2,3:V2_a2_3,
             4:V2_a2_4,5:V2_a2_5,6:V2_a2_6,7:V2_a2_7}
    V2_a3 = {0:V2_a3_0,1:V2_a3_1,2:V2_a3_2,3:V2_a3_3,
             4:V2_a3_4,5:V2_a3_5,6:V2_a3_6,7:V2_a3_7}
    V2_a4 = {0:V2_a4_0,1:V2_a4_1,2:V2_a4_2,3:V2_a4_3,
             4:V2_a4_4,5:V2_a4_5,6:V2_a4_6,7:V2_a4_7}
    V2_a5 = {0:V2_a5_0,1:V2_a5_1,2:V2_a5_2,3:V2_a5_3,
             4:V2_a5_4,5:V2_a5_5,6:V2_a5_6,7:V2_a5_7}
    V2_a6 = {0:V2_a6_0,1:V2_a6_1,2:V2_a6_2,3:V2_a6_3,
             4:V2_a6_4,5:V2_a6_5,6:V2_a6_6,7:V2_a6_7}
    V2_a7 = {0:V2_a7_0,1:V2_a7_1,2:V2_a7_2,3:V2_a7_3,
             4:V2_a7_4,5:V2_a7_5,6:V2_a7_6,7:V2_a7_7}
    V2_a8 = {0:V2_a8_0,1:V2_a8_1,2:V2_a8_2,3:V2_a8_3,
             4:V2_a8_4,5:V2_a8_5,6:V2_a8_6,7:V2_a8_7}
    V2_a9 = {0:V2_a9_0,1:V2_a9_1,2:V2_a9_2,3:V2_a9_3,
             4:V2_a9_4,5:V2_a9_5,6:V2_a9_6,7:V2_a9_7}
    V2_a10 = {0:V2_a10_0,1:V2_a10_1,2:V2_a10_2,3:V2_a10_3,
             4:V2_a10_4,5:V2_a10_5,6:V2_a10_6,7:V2_a10_7}
    V2_a11 = {0:V2_a11_0,1:V2_a11_1,2:V2_a11_2,3:V2_a11_3,
             4:V2_a11_4,5:V2_a11_5,6:V2_a11_6,7:V2_a11_7}
    V2_a12 = {0:V2_a12_0,1:V2_a12_1,2:V2_a12_2,3:V2_a12_3,
             4:V2_a12_4,5:V2_a12_5,6:V2_a12_6,7:V2_a12_7}
    V3_a1 = {0:V3_a1_0,1:V3_a1_1,2:V3_a1_2,3:V3_a1_3,
             4:V3_a1_4,5:V3_a1_5,6:V3_a1_6,7:V3_a1_7}
    V3_a2 = {0:V3_a2_0,1:V3_a2_1,2:V3_a2_2,3:V3_a2_3,
             4:V3_a2_4,5:V3_a2_5,6:V3_a2_6,7:V3_a2_7}
    V3_a3 = {0:V3_a3_0,1:V3_a3_1,2:V3_a3_2,3:V3_a3_3,
             4:V3_a3_4,5:V3_a3_5,6:V3_a3_6,7:V3_a3_7}
    V3_a4 = {0:V3_a4_0,1:V3_a4_1,2:V3_a4_2,3:V3_a4_3,
             4:V3_a4_4,5:V3_a4_5,6:V3_a4_6,7:V3_a4_7}
    V3_a5 = {0:V3_a5_0,1:V3_a5_1,2:V3_a5_2,3:V3_a5_3,
             4:V3_a5_4,5:V3_a5_5,6:V3_a5_6,7:V3_a5_7}
    V3_a6 = {0:V3_a6_0,1:V3_a6_1,2:V3_a6_2,3:V3_a6_3,
             4:V3_a6_4,5:V3_a6_5,6:V3_a6_6,7:V3_a6_7}
    V3_a7 = {0:V3_a7_0,1:V3_a7_1,2:V3_a7_2,3:V3_a7_3,
             4:V3_a7_4,5:V3_a7_5,6:V3_a7_6,7:V3_a7_7}
    V3_a8 = {0:V3_a8_0,1:V3_a8_1,2:V3_a8_2,3:V3_a8_3,
             4:V3_a8_4,5:V3_a8_5,6:V3_a8_6,7:V3_a8_7}
    V3_a9 = {0:V3_a9_0,1:V3_a9_1,2:V3_a9_2,3:V3_a9_3,
             4:V3_a9_4,5:V3_a9_5,6:V3_a9_6,7:V3_a9_7}
    V3_a10 = {0:V3_a10_0,1:V3_a10_1,2:V3_a10_2,3:V3_a10_3,
             4:V3_a10_4,5:V3_a10_5,6:V3_a10_6,7:V3_a10_7}
    V3_a11 = {0:V3_a11_0,1:V3_a11_1,2:V3_a11_2,3:V3_a11_3,
             4:V3_a11_4,5:V3_a11_5,6:V3_a11_6,7:V3_a11_7}
    V3_a12 = {0:V3_a12_0,1:V3_a12_1,2:V3_a12_2,3:V3_a12_3,
             4:V3_a12_4,5:V3_a12_5,6:V3_a12_6,7:V3_a12_7}

    av = {0:1,1:1,2:1,3:1,4:1,5:1,6:1,7:1}
    probClass1 = ex.exp(s1)/(ex.exp(s1) + ex.exp(s2) + ex.exp(s3))
    probClass2 = ex.exp(s2)/(ex.exp(s1) + ex.exp(s2) + ex.exp(s3))
    probClass3 = ex.exp(s3)/(ex.exp(s1) + ex.exp(s2) + ex.exp(s3))

    prob1_a1 = models.logit(V1_a1, av, a1)
    prob1_a2 = models.logit(V1_a2, av, a2)
    prob1_a3 = models.logit(V1_a3, av, a3)
    prob1_a4 = models.logit(V1_a4, av, a4)
    prob1_a5 = models.logit(V1_a5, av, a5)
    prob1_a6 = models.logit(V1_a6, av, a6)
    prob1_a7 = models.logit(V1_a7, av, a7)
    prob1_a8 = models.logit(V1_a8, av, a8)
    prob1_a9 = models.logit(V1_a9, av, a9)
    prob1_a10 = models.logit(V1_a10, av, a10)
    prob1_a11 = models.logit(V1_a11, av, a11)
    prob1_a12 = models.logit(V1_a12, av, a12)
    prob2_a1 = models.logit(V2_a1, av, a1)
    prob2_a2 = models.logit(V2_a2, av, a2)
    prob2_a3 = models.logit(V2_a3, av, a3)
    prob2_a4 = models.logit(V2_a4, av, a4)
    prob2_a5 = models.logit(V2_a5, av, a5)
    prob2_a6 = models.logit(V2_a6, av, a6)
    prob2_a7 = models.logit(V2_a7, av, a7)
    prob2_a8 = models.logit(V2_a8, av, a8)
    prob2_a9 = models.logit(V2_a9, av, a9)
    prob2_a10 = models.logit(V2_a10, av, a10)
    prob2_a11 = models.logit(V2_a11, av, a11)
    prob2_a12 = models.logit(V2_a12, av, a12)
    prob3_a1 = models.logit(V3_a1, av, a1)
    prob3_a2 = models.logit(V3_a2, av, a2)
    prob3_a3 = models.logit(V3_a3, av, a3)
    prob3_a4 = models.logit(V3_a4, av, a4)
    prob3_a5 = models.logit(V3_a5, av, a5)
    prob3_a6 = models.logit(V3_a6, av, a6)
    prob3_a7 = models.logit(V3_a7, av, a7)
    prob3_a8 = models.logit(V3_a8, av, a8)
    prob3_a9 = models.logit(V3_a9, av, a9)
    prob3_a10 = models.logit(V3_a10, av, a10)
    prob3_a11 = models.logit(V3_a11, av, a11)
    prob3_a12 = models.logit(V3_a12, av, a12)

    ProbIndiv_1_a1 = PanelLikelihoodTrajectory(prob1_a1)
    ProbIndiv_1_a2 = PanelLikelihoodTrajectory(prob1_a2)
    ProbIndiv_1_a3 = PanelLikelihoodTrajectory(prob1_a3)
    ProbIndiv_1_a4 = PanelLikelihoodTrajectory(prob1_a4)
    ProbIndiv_1_a5 = PanelLikelihoodTrajectory(prob1_a5)
    ProbIndiv_1_a6 = PanelLikelihoodTrajectory(prob1_a6)
    ProbIndiv_1_a7 = PanelLikelihoodTrajectory(prob1_a7)
    ProbIndiv_1_a8 = PanelLikelihoodTrajectory(prob1_a8)
    ProbIndiv_1_a9 = PanelLikelihoodTrajectory(prob1_a9)
    ProbIndiv_1_a10 = PanelLikelihoodTrajectory(prob1_a10)
    ProbIndiv_1_a11 = PanelLikelihoodTrajectory(prob1_a11)
    ProbIndiv_1_a12 = PanelLikelihoodTrajectory(prob1_a12)
    ProbIndiv_2_a1 = PanelLikelihoodTrajectory(prob2_a1)
    ProbIndiv_2_a2 = PanelLikelihoodTrajectory(prob2_a2)
    ProbIndiv_2_a3 = PanelLikelihoodTrajectory(prob2_a3)
    ProbIndiv_2_a4 = PanelLikelihoodTrajectory(prob2_a4)
    ProbIndiv_2_a5 = PanelLikelihoodTrajectory(prob2_a5)
    ProbIndiv_2_a6 = PanelLikelihoodTrajectory(prob2_a6)
    ProbIndiv_2_a7 = PanelLikelihoodTrajectory(prob2_a7)
    ProbIndiv_2_a8 = PanelLikelihoodTrajectory(prob2_a8)
    ProbIndiv_2_a9 = PanelLikelihoodTrajectory(prob2_a9)
    ProbIndiv_2_a10 = PanelLikelihoodTrajectory(prob2_a10)
    ProbIndiv_2_a11 = PanelLikelihoodTrajectory(prob2_a11)
    ProbIndiv_2_a12 = PanelLikelihoodTrajectory(prob2_a12)
    ProbIndiv_3_a1 = PanelLikelihoodTrajectory(prob3_a1)
    ProbIndiv_3_a2 = PanelLikelihoodTrajectory(prob3_a2)
    ProbIndiv_3_a3 = PanelLikelihoodTrajectory(prob3_a3)
    ProbIndiv_3_a4 = PanelLikelihoodTrajectory(prob3_a4)
    ProbIndiv_3_a5 = PanelLikelihoodTrajectory(prob3_a5)
    ProbIndiv_3_a6 = PanelLikelihoodTrajectory(prob3_a6)
    ProbIndiv_3_a7 = PanelLikelihoodTrajectory(prob3_a7)
    ProbIndiv_3_a8 = PanelLikelihoodTrajectory(prob3_a8)
    ProbIndiv_3_a9 = PanelLikelihoodTrajectory(prob3_a9)
    ProbIndiv_3_a10 = PanelLikelihoodTrajectory(prob3_a10)
    ProbIndiv_3_a11 = PanelLikelihoodTrajectory(prob3_a11)
    ProbIndiv_3_a12 = PanelLikelihoodTrajectory(prob3_a12)

    # Likelihood Calculation
    LL = log(probClass1*ProbIndiv_1_a1*ProbIndiv_1_a2*ProbIndiv_1_a3*ProbIndiv_1_a4*ProbIndiv_1_a5*ProbIndiv_1_a6*ProbIndiv_1_a7*ProbIndiv_1_a8*ProbIndiv_1_a9*ProbIndiv_1_a10*ProbIndiv_1_a11*ProbIndiv_1_a12 + \
             probClass2*ProbIndiv_2_a1*ProbIndiv_2_a2*ProbIndiv_2_a3*ProbIndiv_2_a4*ProbIndiv_2_a5*ProbIndiv_2_a6*ProbIndiv_2_a7*ProbIndiv_2_a8*ProbIndiv_2_a9*ProbIndiv_2_a10*ProbIndiv_2_a11*ProbIndiv_2_a12 + \
             probClass3*ProbIndiv_3_a1*ProbIndiv_3_a2*ProbIndiv_3_a3*ProbIndiv_3_a4*ProbIndiv_3_a5*ProbIndiv_3_a6*ProbIndiv_3_a7*ProbIndiv_3_a8*ProbIndiv_3_a9*ProbIndiv_3_a10*ProbIndiv_3_a11*ProbIndiv_3_a12)
    # Estimation Starts
    biogeme = bio.BIOGEME(database, LL)
    biogeme.modelName = "LC3_" + str(r+1)
    try:
        results = biogeme.estimate()
        print("Starting value set" + str(r+1) + "/ LL:" + str(results.getGeneralStatistics()['Final log likelihood'][0]))
        print("Starting value set" + str(r+1) + "/ LL:" + str(results.getGeneralStatistics()['Akaike Information Criterion'][0]))
    except:
        print("Starting value set" + str(r+1) + "/ Convergence Error")
