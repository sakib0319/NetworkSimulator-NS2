import matplotlib.pyplot as plt 
  
area = [250,500,750,1000,1250]
areaThroughPut = [98691.9,89002.4,34441.9,104216,23875.3]
areaDelay = [0.0425172,0.0292307,0.0293694,0.028285,0.0258416]
areaDelivery = [0.928354,0.849612,0.679758,0.834839,0.634783]
areaDrop = [0.0609756,0.144186, 0.283988,0.136774,0.33913]

nn = [20,40,60,80,100]
nnThroughput = [103535,82362.7,73003.7,67536.2,42560.4]
nnDelay = [0.0124528,0.0740352,0.0619089,0.10904,0.226011]
nnDelivery = [0.885517,0.845277,0.816726,0.844444,0.733696]
nnDrop = [0.113103,0.149837,0.16548,0.157576,0.274457]

nf = [10,20,30,40,50]
nfThroughput = [50406.7,90507.6,109900,148041,90763.1]
nfDelay = [0.0234846,0.0320215,0.0185704,0.0131551,0.0442654]
nfDelivery = [0.927711,0.882911,0.857143,0.838858,0.700483]
nfDrop = [0.0662651,0.10443,0.125313,0.157459,0.266908]


def my_function(x,y,xlabel,ylabel,title):
    plt.plot(x, y) 
  
    plt.xlabel(xlabel) 
    plt.ylabel(ylabel) 
  
    plt.title(title) 
  
    plt.show() 


my_function(area,areaThroughPut,'Area (m)','Throughput','Area (m) vs Network Throughput')
my_function(area,areaDelay,'Area (m)','Average Delay','Area (m) vs Average Delay')
my_function(area,areaDelivery,'Area (m)','Delivery Ratio','Area (m) vs Delivery Ratio')
my_function(area,areaDrop,'Area (m)','Drop Ratio','Area (m) vs Drop Ratio')

my_function(nn,nnThroughput,'Number of nodes','Throughput','Number of nodes vs Network Throughput')
my_function(nn,nnDelay,'Number of nodes','Average Delay','Number of nodes vs Average Delay')
my_function(nn,nnDelivery,'Number of nodes','Delivery Ratio','Number of nodes vs Delivery Ratio')
my_function(nn,nnDrop,'Number of nodes','Drop Ratio','Number of nodes vs Drop Ratio')

my_function(nf,nfThroughput,'Number of flow','Throughput','Number of flow vs Network Throughput')
my_function(nf,nfDelay,'Number of flow','Average Delay','Number of flow vs Average Delay')
my_function(nf,nfDelivery,'Number of flow','Delivery Ratio','Number of flow vs Delivery Ratio')
my_function(nf,nfDrop,'Number of flow','Drop Ratio','Number of flow vs Drop Ratio')