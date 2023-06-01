import numpy as np
import random

band = {
'soprano_cornet': np.array([3,0,0,0,0]),
'front_cornet_1': np.array([2,1,0,0,0]),
# 'front_cornet_2': np.array([2,1,0,0,0]),
# 'front_cornet_3': np.array([2,1,0,0,0]),
# 'front_cornet_4': np.array([2,1,0,0,0]),
'back_cornet_5': np.array([2,1,0,0,0]),
# 'back_cornet_6': np.array([2,1,0,0,0]),
# 'back_cornet_7': np.array([2,1,0,0,0]),
# 'back_cornet_8': np.array([2,1,0,0,0]),
'repiano_cornet': np.array([2,1,0,0,0]),
'flugelhorn': np.array([1,2,0,0,0]),
'tenor_horn_1': np.array([0,2,1,0,0]),
'tenor_horn_2': np.array([0,2,1,0,0]),
'tenor_horn_3': np.array([0,2,1,0,0]),
'baritone_1': np.array([0,1,2,0,0]),
'baritone_2': np.array([0,1,2,0,0]),
'trombone_1': np.array([0,0,2,1,0]),
'trombone_2': np.array([0,0,2,1,0]),
'euphonium_1': np.array([0,0,1,2,0]),
'euphonium_2': np.array([0,0,1,2,0]),
'bass_trombone_1': np.array([0,0,0,2,1]),
'e_flat_bass_1': np.array([0,0,0,1,2]),
'e_flat_bass_2': np.array([0,0,0,1,2]),
'b_flat_bass_1': np.array([0,0,0,0,3]),
'b_flat_bass_2': np.array([0,0,0,0,3]),
# 'percussion_1': np.array([1,1,1,0,0]),
# 'percussion_2': np.array([0,1,1,1,0]),
# 'percussion_3': np.array([0,0,1,1,1]),
}

items = list(band.items())
random.shuffle(items)

composition = []
for i in range(4):
    composition.append(sum([items[6*i+j][1] for j in range(6)]))

print(composition)


band = {
'soprano_cornet': np.array([3,0,0,0]),
'cornet_1': np.array([2,1,0,0]),
'cornet_2': np.array([2,1,0,0]),
'cornet_3': np.array([2,1,0,0]),
'cornet_4': np.array([2,1,0,0]),
'cornet_5': np.array([1,2,0,0]),
'cornet_6': np.array([1,2,0,0]),
'cornet_7': np.array([1,2,0,0]),
'cornet_8': np.array([1,2,0,0]),
'repiano_cornet': np.array([0,3,0,0]),
'flugelhorn': np.array([0,3,0,0]),
'tenor_horn_1': np.array([0,2,1,0]),
'tenor_horn_2': np.array([0,2,1,0]),
'tenor_horn_3': np.array([0,2,1,0]),
'baritone_1': np.array([0,1,2,0]),
'baritone_2': np.array([0,1,2,0]),
'trombone_1': np.array([0,0,3,0]),
'trombone_2': np.array([0,0,3,0]),
'euphonium_1': np.array([0,0,2,1]),
'euphonium_2': np.array([0,0,2,1]),
'bass_trombone_1': np.array([0,0,1,2]),
'e_flat_bass_1': np.array([0,0,1,2]),
'e_flat_bass_2': np.array([0,0,1,2]),
'b_flat_bass_1': np.array([0,0,0,3]),
'b_flat_bass_2': np.array([0,0,0,3]),
'percussion_1': np.array([1,1,1,0]),
'percussion_2': np.array([1,1,1,0]),
'timpani': np.array([0,1,1,1]),
}

items = list(band.items())
random.shuffle(items)

composition = []
for i in range(4):
    composition.append(sum([items[6*i+j][1] for j in range(6)]))

print(composition)

