import matplotlib.pyplot as plt
import numpy as np



def tutorial_1():
    plt.plot([1,2,3,4])
    plt.ylabel('some numbers')
    plt.show()

# tutorial_1()

def tutorial_2():
    plt.plot([1,2,3,4],[1,4,9,16],'ro')
    plt.ylabel('some numbers')
    # plt.axis([0,6,0,20])
    plt.show()

# tutorial_2()

def tutorial_3():
    t = np.arange(0.,5.,0.2)

    plt.plot(t,t,'r--',t,t**2,'bs',t,t**3,'g^')
    plt.show()


# tutorial_3()

def tutorial_4():
    def f(t):
        return np.exp(-t) * np.cos(2*np.pi*t)

    t1 = np.arange(0.0,5.0,0.1)
    t2 = np.arange(0.0,5.0,0.02)

    # plt.figure(1)
    plt.subplot(211)
    plt.plot(t1,f(t1),'bo',t2,f(t2),'k')

    plt.subplot(212)
    plt.plot(t2,np.cos(2*np.pi*t2),'r--')

    plt.show()

# tutorial_4()

def tutorial_5():
    plt.figure(1)                # the first figure
    plt.subplot(221)             # the first subplot in the first figure
    plt.plot([1, 2, 3])
    plt.subplot(212)             # the second subplot in the first figure
    plt.plot([4, 5, 6])

    # plt.figure(2)                # a second figure
    # plt.plot([4, 5, 6])          # creates a subplot(111) by default

    plt.figure(1)                # figure 1 current; subplot(212) still current
    plt.subplot(212)             # make subplot(211) in figure1 current
    plt.title('Easy as 1, 2, 3')
    plt.show()

# tutorial_5()

def tutorial_6():
    np.random.seed(196800801)
    mu,sigma = 100,15
    x = mu + sigma * np.random.randn(10000)

    n,bins,patches = plt.hist(x,50,normed=1,facecolor='g',alpha=0.75)
    plt.xlabel('smart')
    plt.ylabel('probility')
    plt.title('IQ')
    plt.text(60,.025,r'$\mu=100,\ \sigma=15$')
    plt.axis([40,160,0,0.03])
    plt.grid(True)
    plt.show()


# tutorial_6()

from matplotlib.ticker import NullFormatter
def tutorial_7():
    np.random.seed()
    y = np.random.normal(loc=0.5,scale=0.4,size=1000)
    y = y[(y>0)&(y<1)]
    y.sort()
    x = np.arange(len(y))

    plt.figure(1)

    plt.
