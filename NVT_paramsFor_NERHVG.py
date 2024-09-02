# Code for generating NVT parameters for NERHVG algorithms
# Author: Zahir Khan (https://sites.google.com/view/khanzahir98/home)

def normalise(d): 
  #normalization: (X-mean)/max(D), where D = {|Xi-mean|: Xi belongs to d}
    m=sum(d)/len(d) # mean of the signal samples
    for i in range(len(d)):
        d[i]=(d[i]-m) #mean removing from each value
    Max=d[0]
    for i in d:
        if abs(i)>Max:
            Max=abs(i)
    for i in range(len(d)):
        d[i]=d[i]/Max

    return d



#Creating a list of NVT parameters named 'Alphas' for a input list of time series signals: 'signal'
def Alpha(signal,dist):
    idx=[i for i in range(len(signal))]
    cross_idx=[0]
    for i in range(len(signal)-1):
        l=cross_idx[-1]
        if signal[i]*signal[i+1]<0:
            if signal[i]>signal[i+1] and i-l>dist:
                cross_idx.append(i)
            elif signal[i+1]>signal[i] and i+1-l>dist:
                cross_idx.append(i+1)
    last_idx_of_signal=len(signal)-1
    if last_idx_of_signal not in cross_idx:
        cross_idx.append(last_idx_of_signal)
    alphas=[]
    for i in range(len(cross_idx)-1):
        I=[j for j in range(cross_idx[i],cross_idx[i+1]+1)]
        M1=abs(signal[I[0]])
        M=signal[I[0]]
        for k in I:
            if abs(signal[k])>M1:
                M1=abs(signal[k])
                M=signal[k]
        alpha=(abs(signal[cross_idx[i]]-M)+abs(signal[cross_idx[i+1]]-M))/(cross_idx[i+1]-cross_idx[i])
        for _ in range(cross_idx[i+1]-cross_idx[i]):
            alphas.append(round(alpha,3))
    return alphas

#Generating List of 'AVGNVT_{S,d1,d2}' parameters for the input list of time series signals: 'signal'
# S= signal, d1= A, d2= B
def Average_alpha(signal,A,B):
    d1=Alpha(signal,A)
    d2=Alpha(signal,B)
    d=[]
    dif=[]
    for i in range(len(signal)-1):
        d.append((d1[i]+d2[i])/2)
    return d
