# -*- coding: utf-8 -*-
from mul_2 import Regression

def load_data(data_path):
    X=[]
    Y=[]
    with open(data_path,'r') as f:
        content=f.readlines()
        for line in content:
            line_list=[]
            s=line.strip(' ').replace('\n','')
            for num in s.split(' '):
                if not num=='':
                    line_list.append(eval(num))
                
            X.append(line_list[:-1])
            Y.append(line_list[-1])
    
    return X,Y

def evaluation(W_test,X_test,Y_true):
    W=[]
    Y=[]
    w_l,x_l=len(W_test),len(X_test[0])
    if not w_l==x_l and len(X_test)==len(Y_true):
        print('dim error ')
        return
    for w in W_test:
        for num in w:
            W.append(num)
    
    if type(Y_true[0])==list:
        for w in Y_true:
            for num in w:
                Y.append(num)
    else:
        Y=Y_true
#    
#    fenzi=sum([sum([abs(x*w) for x,w in zip(x_row,W)])-abs(y) for x_row,y in zip(X_test,Y)])
#    fenmu=sum([abs(y) for y in Y])
    
    fenzi=sum([abs(sum([x*w for x,w in zip(x_row,W)])-y) for x_row,y in zip(X_test,Y)])
    fenmu=sum(Y)
#    
#    dayin=[sum([x*w for x,w in zip(x_row,W)]) for x_row in X_test]
#    
#    
#    return dayin,Y
    print('acc is :',1-fenzi/fenmu)


if __name__=='__main__':
    data_path='housing.data'
    X,Y=load_data(data_path)
    
    print('all data is : {} rows'.format(len(X)))
    X_train,Y_train=X[:400],Y[:400]
    d=len(X[0])
    n=len(X_train)
    X_test,Y_test=X[400:],Y[400:]
    
    reg=Regression(d,n,X_train,Y_train)
    W=reg.run()
    
    
    for x_row in X_test:
        x_row.append(1)
    
    evaluation(W,X_test,Y_test)