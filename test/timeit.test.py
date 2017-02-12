import timeit

t2 = timeit.Timer('x=range(10)')

print t2.timeit()


t1 = timeit.Timer('print sum(x)','x =(i for i in range(100))')

print t1.timeit()