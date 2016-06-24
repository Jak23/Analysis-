#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np
import cPickle,os,pdb,itertools
import csv

def analyze(fp,op):

    with open(fp,'rb') as h:data = cPickle.load(h)

    targets = data['pages'][0][1]
    meanj = [j for j in range(len(targets)) if targets[j].count('mean') > 0]

    print('meanj',[targets[x] for x in meanj])

    pages = data['pages']
    sm = []
    for j in meanj:
	#sm = []
	targ = targets[j]
	print('targ',targ,meanj)

	# calculate the sensitivity of targ
	# sm should be a 3,2 matrix
	# should calculate a matrix for each point in time, 
	#	across the whole parameter space, for each species (r1,r2,r3)

	t = -1
        for i in range(len(pages)):
	    psppage = pages[i]
	    pspdata = psppage[0]
	    #targets = psppage[1]
	    header = psppage[2]
        timedata = pspdata[0][t]
        mean_1data = pages[i][0][1][t]
        for j in range(len(pages)):
         meandata = pspdata[i][t]
       # plt.plot(timedata,meandata,marker = 'o')

###############################################################################
#Single time slice brute force senstivity matrix calc
###############################################################################
    smg = np.array([[],[]])
    sma = np.array([[],[]])
    SM = np.array([[],[]])
    SMt = np.array([[],[]])  
    SMt1 = np.array([[],[]]) 
    SMt2 = np.array([[],[]]) 
    SMt3 = np.array([[],[]]) 
    StepS = np.array([[],[]]) 
    StepS1 = np.array([[],[]])
    StepS2 = np.array([[],[]])
    StepS3 = np.array([[],[]])
    StepS4 = np.array([[],[]])
    Sa = np.array([[],[]])
    Sg = np.array([[],[]])
    Var_a = np.array([[],[]])
    #SumV = np.array([[],[]])
    ga = np.array([[],[]])
    alpha1 = np.array([[],[]])
    for q in range(len(pages[0][0][0])):
        g = 0.1
        alpha = 10
        
        m11 = (pages[2][0][1][q]-pages[0][0][1][q])/g
        m12 = (pages[5][0][1][q]-pages[3][0][1][q])/g
        m13 = (pages[8][0][1][q]-pages[6][0][1][q])/g
        m21 = (pages[6][0][1][q]-pages[0][0][1][q])/alpha
        m22 = (pages[7][0][1][q]-pages[1][0][1][q])/alpha
        m23 = (pages[8][0][1][q]-pages[2][0][1][q])/alpha
        smg = [m11,m12,m13]
        sma = [m21,m22,m23]
        timem = pages[0][0][0][q]
        timem1 = [pages[0][0][0][q], pages[0][0][0][q], pages[0][0][0][q]]
        StepS = np.append(StepS, timem1)
        StepS1 = np.append(StepS1, timem)
        SM = [smg,sma]
        Sg = np.append(Sg, smg)
        Sa = np.append(Sa, sma)
        SMt = np.append(SMt, SM)
        SMt2 = [np.append(SMt1, Sg),np.append(SMt1, Sa)]
        SMt3 = np.append(SMt3, SM)
        ga = np.append(ga, m12)
        alpha1 = np.append(alpha1, m22)
        varavg = 0
        varavg1 = 0
        

        for d in range(len(pages)):
            varavg = varavg + pages[d][0][6][q]
            varavg1 = varavg/len(pages)
        Var_a = np.append(Var_a, varavg1)
        #plt.plot(ga,StepS1,marker = 'o')
        #plt.plot(StepS1,alpha1,marker = 'o')
    plt.plot(StepS1,ga,marker = 'o')
    plt.xlabel('Time')
    plt.ylabel('r1 mean sensitivity(g)')
        #plt.ylabel('r1 mean sensitivity(alpha)')
    plt.title('r1 mean sensitivity(g) vs time')
    plt.show()

#plt.title('r1 mean sensitivity(alpha) vs time')
#plt.ylabel('Mean Sensitivity of alpha')

#plt.show()
#plt.show()


    plt.plot(StepS1,alpha1,marker = 'o')
    plt.xlabel('Time')
    plt.ylabel('r1 mean sensitivity(alpha)')
    plt.title('r1 mean sensitivity(alpha) vs time')
    plt.show()

##############################################################################
#var
#############################################################################











############################################################################
############################################################################


###############################################################################
    final_array = np.array([[],[]])
    final_array1 = np.array([[],[]])
    t_array = np.array([[],[]])
    for m in range(len(pages[0][0][0])):
        value_array = np.array([[],[]])
        value_array1 = np.array([[],[]])
        for x in range(len(pages)):
        
            val = pages[x][0][1][m]
            value_array = np.append(value_array, val)
            t_array = np.append(t_array, m)
       
       


        final_array = np.append(final_array, value_array)
        final_array1 = [t_array,final_array ]
        final_array2 = [t_array,final_array[m] ]

        numtest = (value_array[2]-value_array[0])/0.1
        
#plt.plot(final_array1[0],final_array1[1])
#plt.show()
##############################################################################
  #test cell      
###############################################################################
    final_arrayw = np.array([[],[]])
    final_arrayw1 = np.array([[],[]])
# final_arrayx = np.array([[],[]])
    t_arrayw = np.array([[],[]])
    for x in range(len(pages)):
        value_arrayw = np.array([[],[]])
        value_arrayw1 = np.array([[],[]])
        for m in range(len(pages[0][0][0])):
            time = pages[0][0][0][m]
            valw = pages[x][0][1][m]
            value_arrayw = np.append(value_arrayw, valw)
            t_arrayw = np.append(t_arrayw, time)
              
        final_arrayw = np.append(final_arrayw, value_arrayw)
        final_arrayw1 = [t_arrayw,final_arrayw ]
        final_arrayw2 = [t_arrayw,final_arrayw[m] ]
# final_arrayx = np.append(final_arrayx, final_arrayw)

        numtest = (value_array[2]-value_array[0])/0.1
        
#plt.plot(final_arrayw1[0],final_arrayw1[1])
#plt.show()
    outputFile = open('output.csv', 'w')
    outputWriter = csv.writer(outputFile)
    for ii in range(len(pages[0][0][0])):
        outputWriter.writerow([t_arrayw[ii],final_arrayw[ii],final_arrayw[ii+100],final_arrayw[ii+100],final_arrayw[ii+300],final_arrayw[ii+400]])
    outputFile.close()

##############################################################################

##############################################################################




    with open(op,'wb') as h:cPickle.dump(sm,h)
    pdb.set_trace()

def tellmewhatsup(fp):
    with open(fp,'rb') as h:data = cPickle.load(h)
    print('this is up',data)
    pdb.set_trace()

if __name__ == '__main__':
    fi = os.path.join(os.getcwd(),'ensemble','statistics_output.pkl')
    op = os.path.join(os.getcwd(),'sensimatrix.pkl')
    analyze(fi,op)
    tellmewhatsup(op)


