import codecademylib3_seaborn
import random

# Import pyplot from matplotlib module and rename it plt
# you can import functions, variables, etc. from another python file
from matplotlib import pyplot as plt
#Set variable equal to range between 1 and 12
numbers_a = range(1, 13)
#set it equal to a random sample of twelve numbers within 0 and 1000
numbers_b = random.sample(range(1001), 12)
#Plot numbers against each other
plt.plot(numbers_a, numbers_b)
plt.show()







