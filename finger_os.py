import os
import sys
import shutil
from random import sample
from collections import OrderedDict


if len(sys.argv) < 2:
    print('input val num')
    exit()

valNum = int(sys.argv[1])

fin=['two','three','four','five','six','seven','eight','nine','ten']

for lists in fin:

    lst = os.listdir(lists)
    lst.remove('classes.txt')

    for f in lst:
        if 'txt' not in f:
            extension = f.split('.')[-1]
            break

    names = [i.split('.')[0] for i in lst]
    names = list(OrderedDict.fromkeys(names))

    valNames = sorted(sample(names, valNum))
    names = sorted(list(set(names).difference(set(valNames))))

    paths = [os.path.join('right',lists,'images', 'train'),
            os.path.join('right',lists,'images', 'val'),
            os.path.join('right',lists,'labels', 'train'),
            os.path.join('right',lists,'labels', 'val')]

    for p in paths:
        os.makedirs(p)

    trainPath = []
    for fname in valNames:
        orgImgPath = os.path.join(lists, f'{fname}.{extension}')
        newImgPath = os.path.join(paths[0], f'{fname}.{extension}')
        trainPath.append(os.path.abspath(newImgPath) + '\n')
        
        orgTxtPath = os.path.join(lists, f'{fname}.txt')
        newTxtPath = os.path.join(paths[2], f'{fname}.txt')
        
        shutil.copy(orgImgPath, newImgPath)
        shutil.copy(orgTxtPath, newTxtPath)

    valPath = []
    for fname in valNames:
        orgImgPath = os.path.join(lists, f'{fname}.{extension}')
        newImgPath = os.path.join(paths[1], f'{fname}.{extension}')
        valPath.append(os.path.abspath(newImgPath) + '\n')
        
        orgTxtPath = os.path.join(lists, f'{fname}.txt')
        newTxtPath = os.path.join(paths[3], f'{fname}.txt')
        
        shutil.copy(orgImgPath, newImgPath)
        shutil.copy(orgTxtPath, newTxtPath)

    with open('train.txt', 'a') as f:
        f.writelines(trainPath)
        
    with open('val.txt', 'a') as f:
        f.writelines(valPath)
        
    shutil.copy(os.path.join(lists, 'classes.txt'), 'classes.names')
