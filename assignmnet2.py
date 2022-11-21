import bitarray as ba
import random as r
import time    

numberOfHosts = 2 ** 20 # 1048576
targets = ba.bitarray(numberOfHosts)
vulnerableHosts = ba.bitarray(numberOfHosts)

targets.setall(False)
vulnerableHosts.setall(False)

numberOfVulnerableHosts = round(numberOfHosts / 100)

#for each number in range of numberOfVulnerableHosts
vulnerableCounter = 0
for i in range(numberOfVulnerableHosts):
    #set the random number to true if not already true
    randomHost = r.randint(0, numberOfHosts - 1)
    if vulnerableHosts[randomHost] == False:
        vulnerableCounter += 1
        vulnerableHosts[randomHost] = True

#Add the initial host
vulnerableCounter += 1


#Printing information and starting timer
print("Number of hosts in our network: ", numberOfHosts)
print("Number of vulnerable hosts in the network: ", vulnerableCounter)

#Infecting the first host
infectedHosts = 1
targets[0] = True
counter = 0

#While there are still hosts to infect
while infectedHosts < vulnerableCounter:
    counter += 1
    infectedHostsLastIteration = infectedHosts;

    #For each infected host in the network scan a 100 hosts and infect them if they are vulnerable
    for i in range(infectedHosts * 100):
        #select a random host
        randomHost = r.randint(0, numberOfHosts - 1)
        #if the host is vulnerable and not already infected then infect it
        if vulnerableHosts[randomHost] == True and targets[randomHost] == False:
            targets[randomHost] = True
            infectedHosts += 1
    

    print(counter, infectedHosts)