# from package.module import function as myModule
# import math
# # import numpy as np
# import matplotlib.pyplot as plt
import pandas as pd
import requests
    
    
    
    # userdata = {"firstname": "John", "lastname": "Doe", "password": "jdoe123"}
    # resp = requests.post('http://www.mywebsite.com/user', data=userdata)
    

    # url = "http://www.datacamp.com/teach/documentation"
    # r = requests.get(url)
    # text = r.text # r.json()
    # print(text)


# t_init = "running python script"
    # t_package ="loaded numpy package"
    # t_array ="printed numpy array"


    # array = np.array([1,2,3])
    # print(t_init)
    # print(t_package)
    # print(array)
    # print(t_array)
    # print( 2* math.pi * 3)

    # plt.plot([1,2,3], [4,5,6])
    # plt.show()
    # plt.clf()

    # plt.scatter([1,2,3], [4,5,6])
    # plt.show()


# Simulate bet of 1000 dice rolls reaching 60 steps.
    # Dice roll = 1,2 -->      -1 step
    # Dice roll = 3,4,5 -->    +1 step
    # Dice roll = 6 -->        +next roll step

    # simulationResult = {}
    # simulationCount = 1
    # while simulationCount < 10000:
    #     np.random.seed(simulationCount)
    #     step = 0

    #     for x in range(100) :
    #         roll = np.random.randint(1,7)
    #         if roll <= 2 and  step > 0:
    #             step = step - 1
    #         elif roll < 6:
    #             step = step + 1
    #         else:
    #             step = step + np.random.randint(1,7)

    #     simulationResult[simulationCount] = step
    #     simulationCount = simulationCount + 1
        
    # # print(simulationResult)
    # npSimulationResultsValues = np.array( list(simulationResult.values()) )  
    # simulationGreaterThan60 = (npSimulationResultsValues >= 60)
    # # print(simulationGreaterThan60)
    # countSimulationsGreaterThan60 =  len(npSimulationResultsValues[simulationGreaterThan60])
    # print( "For 10000 Simulations of x100 Rolls, the # times >= 60 steps: " + str(countSimulationsGreaterThan60))
    # print ("The %% success: " + str( countSimulationsGreaterThan60/10000 *100))
    # plt.hist(simulationResult.values())
    # plt.show()


# Import necessary module
    # from sqlalchemy import create_engine
    # engine = create_engine("sqlite:///Chinook.sqlite")
    # table_names = engine.table_names()
    # print(table_names)
