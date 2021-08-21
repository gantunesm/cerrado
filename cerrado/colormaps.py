

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors

def linear(col1,col2):
    cmap = matplotlib.colors.LinearSegmentedColormap.from_list("", [col1,col2])
    return cmap

def tri(col1,col2,col3):
    cmap = matplotlib.colors.LinearSegmentedColormap.from_list("", [col1,col2,col3])
    return cmap

def divergent(col1,col2):
    cmap = matplotlib.colors.LinearSegmentedColormap.from_list("", [col1,"white",col2])
    return cmap

def displinear(col1,col2):
    f,axes = plt.subplots(figsize=(8,0.5), dpi=100,sharey=True)
    f.subplots_adjust(wspace=0,right=0.99,top=0.99,bottom=0.00,left=0.01,hspace=0.0)
    plt.yticks([])
    arr=np.tile(np.arange(1000),100).reshape(100,1000)
    cmap = linear(col1,col2)
    plt.imshow(arr,cmap=cmap)

def disptri(col1,col2,col3):
    f,axes = plt.subplots(figsize=(8,0.5), dpi=100,sharey=True)
    f.subplots_adjust(wspace=0,right=0.99,top=0.99,bottom=0.00,left=0.01,hspace=0.0)
    plt.yticks([])
    arr=np.tile(np.arange(1000),100).reshape(100,1000)
    cmap = tri(col1,col2,col3)
    plt.imshow(arr,cmap=cmap)


def dispdivergent(col1,col2):
    f,axes = plt.subplots(figsize=(8,0.5), dpi=100,sharey=True)
    f.subplots_adjust(wspace=0,right=0.99,top=0.99,bottom=0.00,left=0.01,hspace=0.0)
    plt.yticks([])
    arr=np.tile(np.arange(1000),100).reshape(100,1000)
    cmap = divergent(col1,col2)
    plt.imshow(arr,cmap=cmap)
