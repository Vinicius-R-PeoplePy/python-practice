import requests 
# Making a GET request 
response = requests.get("https://api.github.com")
print(response.json())
# Making a POST request 
payload = {'key':'value'}
response = requests.post('https://httpbin.org/post', data=payload)
print(response.text)

# While Selenium and Requests serve different 
# purposes, they can be combined to create powerful 
# automation scripts. For instance,
# Selenium can be used to navigate and interact
# with JavaScript-heavy web pages, 
# extract URLs or form dat 
# and then use Requests to make HTTP 
# requests based on the extracted information. 
'''
This synergy allows developers to tackle a wide range of automation 
tasks, from web scrapping to 
automating complex web workflows. 

Selenium and Requests are just the tip of the iceberg in Python's 
automation capabilities,
but they exemplify the language's 
versatility and power. 
By understanding and leveraging these libraries,
developers can automate a vast aray of tasks, making their workflows 
more efficient and creative. 
Whether it's automating web browsers with Selenium or 
mastering HTTP requests with Requests, 
the potential for innovation and efficiency is boundless. 


'''