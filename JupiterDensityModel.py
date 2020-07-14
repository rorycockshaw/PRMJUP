import numpy as np 
import matplotlib.pyplot as plt

radiusRho = open(r"C:\Users\roryc\Documents\jupiterdensity.txt").read()

radiusRho = radiusRho.replace("\t",",")
radiusRho = radiusRho.replace("\n",",")
radiusRho = radiusRho.split(",") 

dataSet = np.array([])
for i in radiusRho: 
     dataSet = np.append(dataSet,float(i))


        
radius = np.array([])
rho = np.array([])

i = 0
while i < len(radiusRho) / 2 : 
    radius = np.append(radius,dataSet[2 * i] * 69911)
    rho = np.append(rho,dataSet[2 * i + 1])
    i+=1
    
j = 0
while j < len(radius) - 1: 
    xvalues = [radius[j],radius[j+1]]
    yvalues = [rho[j],rho[j+1]]
    plt.plot(xvalues,yvalues)
    j+=1

plt.title("Jovian density distribution")
plt.xlabel("Radius/km")
plt.ylabel("Density/g $cm^-3$")
    
plt.show()
    
