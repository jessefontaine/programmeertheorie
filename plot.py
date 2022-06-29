import matplotlib.pyplot as plt


x = []


with open('/home/laura/programmeertheorie/wn/rushhour6x6_1_bestdepth_10000.txt','r') as csvfile:
    for row in csvfile:
        x.append(int(row))
print(x)
plt.hist(x, bins=100, density=True, label='best depth', alpha=0.8)

x1=[]

with open('/home/laura/programmeertheorie/wn/Rushhour6x6_1_depth_10000.txt','r') as csvfile:
    for row in csvfile:
        x1.append(int(row))
 
plt.hist(x1, bins=100, density=True, label='depth', alpha=0.8)
plt.xlabel('Number of steps')
plt.ylabel('Density')
plt.title('Density plot of depth and the best depth algorithm')
plt.legend()
plt.savefig("/home/laura/programmeertheorie/presentatie.png")