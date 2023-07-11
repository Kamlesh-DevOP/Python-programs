import statistics as st
def mean_mode_median(l):
    return st.mean(l), st.mode(l), st.mode(l)

l=eval(input('Enter list'))
result=mean_mode_median(l)
print('Mean: ', result[0], 'Mode: ', result[1], 'Median: ', result[2])