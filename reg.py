# -*- coding: utf-8 -*-
import random

class Regression():
    def __init__(self,d,n,X=None,Y=None):
        self.d=d
        self.n=n
        self.X=X
        self.Y=Y
        
    def equation(self):
        random.seed(5)
        W=[random.randint(-10,10) for i in range(self.d)]
        s='y='
        for i,w in enumerate(W):
            if i== len(W)-1:
                s+=str(w)+'*x_'+str(i)
            else:
                s+=str(w)+'*x_'+str(i)+'+'
        print('the equation is :{}'.format(s))
        
        random.seed(5)
        X=[[random.uniform(-20,20) for j in range(self.d)] for i in range(self.n)]
        random.seed(6)
        noise=[((-1)**int(random.random()*10))*random.random() for i in range(self.n)]
        Y=[[sum([X[i][j]*W[j] for j in range(self.d)],noise[i])] for i in range(self.n)]
        
        return X,Y
        
    def transposition(self,X):
        print('X shape is {}*{}'.format(str(self.n),str(self.d)))
        X_t=[[0 for j in range(self.n)] for i in range(self.d)]
        for i in range(self.n):
            for j in range(self.d):
                X_t[j][i]=X[i][j]
        
        return X_t
    
    def arrary_add(self,M,N,operator):
        if not len(M)==len(N) and len(M[0])==len(N[0]):
            print('传入矩阵的维度不同')
            return
        else:
            O=[[0 for j in range(len(N))] for i in range(len(M))]
            for i in range(len(M)):
                for j in range(len(M[0])):
                    s=str(M[i][j])+operator+str(N[i][j])
                    O[i][j]=eval(s)
            return O
        
    def array_mul(self,X,X_t):
        rows=len(X)
        M=len(X[0])
        columns=len(X_t[0])
        N=len(X_t)
        
        print('shape of X1 rows columns X2 rows columns is:',rows,M,N,columns)
        
        X_mul=[[0 for j in range(columns)] for i in range(rows)]
        if M==N:
            for i in range(rows):
                for j in range(columns):
                    result=0
                    for k in range(M):
                        result+=X[i][k]*X_t[k][j]
                    X_mul[i][j]=result
                    
            return X_mul

        else:
            print('X is not a 2 dim list')
            return -1
        
        
    def inversion(self,X):
        if not len(X)==len(X[0]):
            print('X is not square list')
            return
        d=len(X)
        unit_arr=[[1 if i==j else 0 for j in range(d)] for i in range(d)]
    #    print(unit_arr)
        step1_arr=[row+row_unit for row,row_unit in zip(X,unit_arr)]
        
        #add the unit matrix to the X
    #        print(step1_arr)
        
        for i,row in enumerate(step1_arr):
            diagonal=1
            #wait
            new_j=0
            for j,ele in enumerate(row):
                if i==j:
                    diagonal=ele
                    new_j=j
    #                print(diagonal)
                    break
            for k,ele in enumerate(row):
                step1_arr[i][k]/=diagonal
            
            
            for l in range(i+1,d):
                mul=step1_arr[l][new_j]
                for m in range(2*d):
                    step1_arr[l][m]-=step1_arr[i][m]*mul
       
        #make the lower triangular matrix
        
        for i in range(d-1,-1,-1):
            for j in range(i-1,-1,-1):
                #j is row
                mul=step1_arr[j][i]
#                print(mul)
                for k in range(2*d):
                    step1_arr[j][k]-=step1_arr[i][k]*mul
                    
        step2_arr=[[step1_arr[i][j] for j in range(d,2*d)] for i in range(d)]
        
        return step2_arr
        
    
    def run(self):
        #W = inv((X_t*X))−X_t*y
        
        if not self.X:
            print('no data give so use random')
            self.X,self.Y=self.equation()
            
        X_t=self.transposition(self.X)
        
        print('shape of X_t rows columns Y rows columns is:',len(X_t),len(X_t[0]),len(self.Y),len(self.Y[0]))
        X_mul=self.array_mul(X_t,self.X)    
        inv=self.inversion(X_mul)
        print('inv shape {}*{}'.format(len(inv),len(inv[0])))     
        W_1=self.array_mul(inv,X_t)       
        W=self.array_mul(W_1,self.Y)
        
        s='y='
        for i,w in enumerate(W):
            for num in w:
                if i== len(W)-1:
                    s+=str(num)+'*x_'+str(i)
                else:
                    s+=str(num)+'*x_'+str(i)+'+'
        print('the current equation is :\n{}'.format(s))
        return W

if __name__=='__main__':
    reg=Regression(5,40)
    W=reg.run()
