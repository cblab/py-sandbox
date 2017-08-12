import numpy as np

x = [1, 4, 8, 10, 12]

#print(np.mean(x))
#print(np.median(x))

baseball = [[180,75,32],[190,80,34],[200,100,34],[210,120,25],[215,121,25]]
np_baseball = np.array(baseball)

# Create np_height from np_baseball
np_height = np_baseball[:,0]

print(np_height)

# Print out the mean of np_height
print(np.mean(np_height))

# Print out the median of np_height
print(np.median(np_height))

# Print mean height (first column)
avg = np.mean(np_baseball[:,0])
print("Average: " + str(avg))

# Print median height. Replace 'None'
med = np.median(np_baseball[:,0])
print("Median: " + str(med))

# Print out the standard deviation on height. Replace 'None'
stddev = np.std(np_baseball[:,0])
print("Standard Deviation: " + str(stddev))

# Print out correlation between first and second column. Replace 'None'
corr = np.corrcoef(np_baseball[:,0], np_baseball[:,1])
print("Correlation: " + str(corr))