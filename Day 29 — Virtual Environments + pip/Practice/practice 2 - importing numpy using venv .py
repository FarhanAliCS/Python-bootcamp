import requests
import numpy as np 

numbers=np.array([12,34,45,65,78])

print("Numbers",numbers)

print("Average :",np.mean(numbers))

response=requests.get("https://example.com")
print("Status :",response.status_code)
