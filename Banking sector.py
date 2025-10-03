import numpy as np
transactions = np.array([
    [120, 150, 100, 200, 180, 170],  
    [80, 90, 70, 60, 110, 95],       
    [200, 220, 210, 230, 250, 240],  
    [150, 160, 170, 140, 180, 175]   
])

print("Transaction Data:\n", transactions)
totals = transactions.sum(axis=1)
print("\nTotal transactions per branch:", totals)
highest_branch = np.argmax(totals) + 1  
print("Branch with highest total transactions:", highest_branch)
average = transactions.mean()
print("Average monthly transaction volume:", average)
reshaped = transactions.reshape(3, 8)
print("\nReshaped (3x8):\n", reshaped)
print("Implication: Reshaping changes how data is viewed, "
      "but original branch-month meaning is lost.")