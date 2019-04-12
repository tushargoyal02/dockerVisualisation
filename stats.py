#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[1]:


from pyspark import SparkContext,SparkConf


# In[2]:


conf = SparkConf().setAppName("lo").setMaster("local")


# In[3]:


sc.stop()
sc = SparkContext(conf=conf)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[4]:


# [reading the file using rdd]
rdd4 = sc.textFile("/home/tushar/Desktop/gitRepos/ML/show.json")
#rdd4.collect()


# In[ ]:





# In[5]:


list1=[]

# splitting the rdd with comma seprated value
rdd5 = rdd4.flatMap(lambda x: x.split(","))

#[Down here is to print]
#rdd5.collect()


# In[6]:


abc=rdd5.collect()[0]
print(type(abc))
percu_list=[]

# [calculating the percpu from rdd]
for num in rdd5.collect():
    if 'percpu' in num:
        percpu=num.split("[")[1]
        percu_list.append(int(percpu))
        #print(type(percpu))

        #print(num)
print(percu_list,type(percu_list[1]))


        
#print(list1)


# In[7]:


kernel_list=[]

# [kernel value from rdd]
for kernel in rdd5.collect():
    if 'usage_in_kerne' in kernel:
        kernel_mod=kernel.split(":")[1]
        kernel_list.append(int(kernel_mod))
print(kernel_list)


# In[ ]:





# In[8]:


cpu_total=[]

# this is for cpu stats
for total in rdd5.collect():
    if 'cpu_stats' in total:
        total_usage=total.split("{")[2].split(":")[1]
        cpu_total.append(int(total_usage))
        
print(cpu_total)


#total_usuage in data
percpu_usuage=[]
for usuage in rdd5.collect():
    if 'percpu_' in usuage:
        cpu_usuage=usuage.split(":")


# In[9]:


# system_cpu_usuage of above data

system_cpu_usuage=[]
for system in rdd5.collect():
    if 'system_cpu_us' in system:
        system_cpu=system.split(":")[1]
        system_cpu_usuage.append(int(system_cpu))
print(system_cpu_usuage)


# In[ ]:





# In[10]:


# [Calculating the cpu delta ]
import pandas as pd
i=0

cpu_calculation=[]
delta_cpu=[]
delta_system=[]

try:
#print(len(system_cpu_usuage))
    while(i<len(system_cpu_usuage)):
        #print(system_cpu_usuage[i+1])
       # [calculating the delta system ]
        if(i==len(system_cpu_usuage)-2):
            break
   
        delta_system.append(float(system_cpu_usuage[i+1]) - float(system_cpu_usuage[i]))
        system_delta = float(system_cpu_usuage[i+1]) - float(system_cpu_usuage[i])
        
        delta_cpu.append(float(cpu_total[i+1]) - float(cpu_total[i]))
        cpu_delta=float(cpu_total[i+1]) - float(cpu_total[i])
    
        #print(len(cpu_total))
        #print(cpu_total[i+1])
    
        # [making a list to make it into dataframe]
        cpu_calculation.append((cpu_delta / system_delta) * float(len(percu_list)) * 100.0)
    
        cpu_percentage = (cpu_delta / system_delta) * float(len(percu_list)) * 100.0
        #print(cpu_percentage)
            
        i=i+1
        
        
        # [Creating dataframe for visualisation]
        dataframe={'cpuDelta':delta_cpu,'system_delta':delta_system,'cpu_calculation':cpu_calculation}
        df = pd.DataFrame(dataframe)
except Exception:
        print("out of bound")
        
print(df)


# In[11]:


# [This is all for the graph plotting]

import time
from IPython import display
import matplotlib.pyplot as plt
import seaborn as sns

get_ipython().run_line_magic('matplotlib', 'inline')


# In[ ]:





# In[12]:


# this is a random try !!
"""count=0
while count < 5 :
    time.sleep(3)
    display.clear_output(wait=True)
    plt.figure( figsize=(30,30 ) )
    sns.barplot(x="cpuDelta",y="system_delta",data=df)
    plt.show()
    count=count+1
"""


# In[ ]:





# In[ ]:





# In[ ]:





# In[13]:


# taking all values from dataframe

deltaCpu=df["cpuDelta"]
print(deltaCpu,"\n")

deltaSystem=df["system_delta"]
print(deltaSystem,"\n\n")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[14]:


# this is for bar graph

for i in range(len(df["cpu_calculation"])):
    time.sleep(0.2)
    #plt.xlabel("Inspiring bardeen container")
    plt.xlabel("CPU delta")
    plt.title("Cpu Usuage Percentage")
    display.clear_output(wait=True)
    plt.ylabel("System Delta")
    x=df["cpuDelta"][i]
    y=df["system_delta"][i]

    #x=["Cont1","cont2"]
        
    z=df["cpu_calculation"][i]
    color=(0.2, 0.4, 0.8, 0.6)
    plt.bar(x,y,data=z,color=color)
    plt.show()


# In[17]:


# for the scatter graph


    # [This will show the data after sometime . Have some patience buddy.]

for i in range(len(df["cpu_calculation"])):
    time.sleep(0.2)
    display.clear_output(wait=True)

    plt.figure( figsize = ( 15,15 ) )

    #plt.xlabel("Inspiring bardeen container")
    plt.xlabel("CPU delta")
    plt.title("Cpu Usuage Percentage")
    plt.ylabel("System Delta")
    x=df["cpuDelta"][i]
    y=df["system_delta"][i]
    
    #x=["Cont1","cont2"]
    
    z=df["cpu_calculation"][i]
    color=['green','blue','red']
    plt.ylim(y)
    plt.xlim(x)
    plt.xlim(left=0,right=2*x)
    plt.ylim(0,2*y)

    color=(0.2, 0.4, 0.8, 0.6)
    plt.grid(True)

    plt.scatter(x,y,data=z,s=z,color=color)
    plt.show()
    


# In[16]:


# this is a try to plot a continuous monitoring graph 
plt.style.use('ggplot')
plt.ion()

fig = plt.figure(figsize=(13,6))
ax = fig.add_subplot(111)
        # create a variable for the line so we can later update it
line1, = ax.plot(deltaCpu,deltaSystem,'-o',alpha=0.8)    
plt.ylabel("System Delta")
plt.xlabel("cpu delta")
plt.title("Cpu Percentage")

line1.set_ydata(deltaSystem)
plt.pause(0.5)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




