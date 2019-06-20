import numpy as np
import matplotlib.pyplot as plt
import math
iList=[]
jList=[]
dataList=[]
def fpi2bpsk():
    bitNum = 1
    num = pow(2, bitNum)
    for k in range(2):
        for point in range(num):
            bits=str(bin(point))[2:].zfill(bitNum)
            i=(1-2*(int(bits[0])))
            j=(1-2*(int(bits[0])))
            if k==0:
                i /= math.sqrt(2)
                j /= math.sqrt(2)
            elif k==1:
                t=i
                i = -j/math.sqrt(2)
                j = t/math.sqrt(2)
            else:
                raise Exception("only support 0 or 1")
            iList.append(i)
            jList.append(j)
            dataList.append(point)
    return dataList,iList,jList
def fbpsk():
    bitNum = 1
    num = pow(2, bitNum)
    for point in range(num):
        bits=str(bin(point))[2:].zfill(bitNum)
        i=(1-2*(int(bits[0])))
        j=(1-2*(int(bits[0])))
        i /= math.sqrt(2)
        j /= math.sqrt(2)
        iList.append(i)
        jList.append(j)
        dataList.append(point)
    return dataList,iList,jList
def fqpsk():
    bitNum = 2
    num = pow(2, bitNum)
    for point in range(num):
        bits=str(bin(point))[2:].zfill(bitNum)
        i=(1-2*(int(bits[0])))
        j=(1-2*(int(bits[1])))
        i /= math.sqrt(2)
        j /= math.sqrt(2)
        iList.append(i)
        jList.append(j)
        dataList.append(point)
    return dataList,iList,jList
def f16qam():
    bitNum = 4
    num = pow(2, bitNum)
    for point in range(num):
        bits=str(bin(point))[2:].zfill(bitNum)
        i=(1-2*(int(bits[0])))*(2-(1-2*(int(bits[2]))))
        j=(1-2*(int(bits[1])))*(2-(1-2*(int(bits[3]))))
        i /= math.sqrt(10)
        j /= math.sqrt(10)
        iList.append(i)
        jList.append(j)
        dataList.append(point)
    return dataList,iList,jList

def f64qam():
    bitNum = 6
    num = pow(2, bitNum)
    for point in range(num):
        bits=str(bin(point))[2:].zfill(bitNum)
        i=(1-2*(int(bits[0])))*(4-(1-2*(int(bits[2])))*(2-(1-2*(int(bits[4])))))
        j=(1-2*(int(bits[1])))*(4-(1-2*(int(bits[3])))*(2-(1-2*(int(bits[5])))))
        i /= math.sqrt(42)
        j /= math.sqrt(42)
        iList.append(i)
        jList.append(j)
        dataList.append(point)
    return dataList,iList,jList
def f256qam():
    bitNum=8
    num=pow(2,bitNum)
    for point in range(num):
        bits=str(bin(point))[2:].zfill(bitNum)
        i=(1-2*(int(bits[0])))*(8-(1-2*(int(bits[2])))*(4-(1-2*(int(bits[4])))*(2-(1-2*(int(bits[6]))))))
        j=(1-2*(int(bits[1])))*(8-(1-2*(int(bits[3])))*(4-(1-2*(int(bits[5])))*(2-(1-2*(int(bits[7]))))))
        i /= math.sqrt(170)
        j /= math.sqrt(170)
        iList.append(i)
        jList.append(j)
        dataList.append(point)
    return dataList,iList,jList
def show(dataList, iList, jList,title="I-Q"):
    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(111)
    ax.set(xlim=[-2, 2], ylim=[-2, 2], title=title, ylabel='Q', xlabel='I')
    ax.spines['top'].set_visible(False)  # 顶边界不可见
    ax.spines['right'].set_visible(False)  # 右边界不可见
    ax.spines['bottom'].set_position(('axes', 0.5))
    ax.spines['left'].set_position(('axes', 0.5))
    plt.scatter(iList, jList, 28, c=dataList, marker="*")
    for i in dataList:
        plt.text(iList[i], jList[i], i)
    # plt.plot(iList, jList, color='green', linewidth=3)
    plt.show()
def subShow(ax,dataList, iList, jList,title="I-Q"):
    ax.set(xlim=[-2, 2], ylim=[-2, 2], title=title, ylabel='Q', xlabel='I')
    ax.axis('equal')
    ax.spines['top'].set_visible(False)  # 顶边界不可见
    ax.spines['right'].set_visible(False)  # 右边界不可见
    ax.spines['bottom'].set_position(('axes', 0.5))
    ax.spines['left'].set_position(('axes', 0.5))
    ax.scatter(iList, jList, 28, c=dataList, marker="*")
    for i in dataList:
        ax.text(iList[i], jList[i], i)
    # plt.plot(iList, jList, color='green', linewidth=3)
if __name__ == "__main__":
    fig1, axes = plt.subplots(nrows=2, ncols=3)
    dataList, iList, jList = fpi2bpsk()
    subShow(axes[0,0],dataList, iList, jList,"pi/2bpsk")
    dataList=[]
    iList=[]
    jList=[]
    dataList, iList, jList = fbpsk()
    subShow(axes[0, 1],dataList, iList, jList,"bpsk")
    dataList=[]
    iList=[]
    jList=[]
    dataList, iList, jList = fqpsk()
    subShow(axes[0, 2],dataList, iList, jList,"qpsk")
    dataList=[]
    iList=[]
    jList=[]
    dataList, iList, jList = f16qam()
    subShow(axes[1, 0],dataList, iList, jList,"16qam")
    dataList=[]
    iList=[]
    jList=[]
    dataList, iList, jList = f64qam()
    subShow(axes[1, 1],dataList, iList, jList,"64qam")
    dataList=[]
    iList=[]
    jList=[]
    dataList, iList, jList = f256qam()
    subShow(axes[1, 2],dataList, iList, jList,"256qam")
    show(dataList, iList, jList,"256qam")
    dataList=[]
    iList=[]
    jList=[]
    plt.show()
