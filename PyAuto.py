'''import os 
import shutil 
# Define the directory to be organized 
directory = "/home/ovni/Documentos/"
# Traverse through each file in the directory 
for filename in os.listdir(directory):
    if os.path.isfile(os.path.join(directory,filename)):
        # Extract the file extension and create a directory name 
        file_extension = filename.split('.')[-1] # what this does? Apparently it serves to get the file extension type.
        new_directory = os.path.join(directory, file_extension)
        # Create the directory if it doesn't exist 
        if not os.path.exists(new_directory):
            os.makedirs(new_directory)
            # Move the file to the new directory 
            shutil.move(os.path.join(directory,filename), new_directory)'''
            
# Ok, this script works well, but now we want to move the files
# to their respective directories. Although there's a line already to
# handle moving the file (?)...

# it moved one or other file, but not all files. 

'''
The cornestorne of any succesfull automation script lies in its
definition. A well-defined task serves as a compass, guiding
the development process and providing clarity to the script's
objectives. Our script, destined to sort files into folders 
based on their extensions, demands a clear outline: 

- Objective: To automate the organization of files within a directory
by categorizing them into subdirectories based on file type.
- Scope: The script shall traverse a user-specified directory, 
assess each file's extension, and relocate the files to their 
designated folder. If a folder for a specific file type does 
not exist, the script will create it. 
- Constraints: The script must handle common exceptions, 
such as permission errors, and ensure compatibility across
different operating systems. 


'''

'''
import os 

# Placeholder for the directory path 

directory = "/home/ovni/Documentos"

# A simple demonstration of traversing the directory 

for item in os.listdir(directory):
    if os.path.isfile(os.path.join(directory,item)):
        print(f"Found file: {item}")
    else:
        print(f"Found directory: {item}")
'''

'''import os 
import shutil 

def organize_files_by_extension(directory):
    # Ensure the provided directory exists 
    if not os.path.exists(directory):
        print(f"The directory {directory} does not exist.")
        return 
    
    # Traverse through the items in the directory 
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        
        # Skip directories 
        if os.path.isdir(item_path):
            continue 
        
    # Extract the file extension and prepare the destination directory 
    file_extension = item.split('.')[-1].lower()
    destination_dir = os.path.join(directory, file_extension)
    
    # Create the destination directory if it does not exist 
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)
        
    # Move the file
    shutil.move(item_path, destination_dir)
    print(f"Moved: {item} -> {destination_dir}/")
    
# Example usage

if __name__ == "__main__":
    target_directory = input("Enter the path to the directory to organize: ")
    organize_files_by_extension(target_directory)'''
    
# The code above, for some reason, is moving only pdf's... 

'''
Going further.

1. The Syntax of Safety: Implementing 'try-except' blocks is straightforward
yet profound. A 'try' block wraps the code that might raise an exception,
while the 'except' block catches and responds to specific errors. 

2. Custom Exception Classes: For more granular control, Python permits
the creation of custom exception classes. This approach is beneficial for
distinguishing between different types of failures specific to 
our  script's domain. 

3. Logging for Insight: Beyond merely catching exceptions, 
logging them is crucial for post-mortem analysis. Python 'logging'
module enables detailed logging of exceptions, providing insights 
into their nature and context. 

'''

'''
import logging 

try:
    # Potentially problematic code goes here 
    pass 
except Exception as e:
    logging.error(f"Error encountered: {e}")
    # Additional error handling logic here
'''   

# Let's apply error handling and optimization 
# techniques to enhance the code resilience and performance.

'''import os 
import shutil 
import logging 

def organize_files_by_extension_optimized(directory):
    try:
        # Optimization: Use os.scandir() for efficient directory traversal
        with os.scandir(directory) as entries:
            for entry in entries:
                if entry.is_file():
                    _, file_extension = os.path.splitext(entry.name)
                    destination_dir = os.path.join(directory, file_extension.lower())
                    if not os.path.exists(destination_dir):
                        os.makedirs(destination_dir)
                        
                        shutil.move(entry.path, destination_dir)
                        logging.info(f"Moved: {entry.name} -> {destination_dir}/")
    except Exception as e:
        logging.error("File organization script completed.")
    finally:
        logging.info("File organization script completed.")
        
# Example usage 

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    target_directory = input("Enter the path to the directory to organize: ")
    organize_files_by_extension_optimized(target_directory)'''
                    
# The code above is not moving all files and, also, is creating directories
# with . in the begginning, which is not interesting. 

# Python's Built-in Debugger: 'pdb'

'''import pdb 

def debugged_function():
    for i in range(5):
        pdb.set_trace() # This will pause execution and open debugger.
        print(i)
debugged_function()'''

# Unit Testing with 'unittest': Python's 'unittest' framework supports
# the development of test cases, offering a way to automate the validation 
# of your script's components in isolation. Writing unit tests helps 
# ensure that individual functions and classes work as intended. 

import unittest

class TestSum(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(sum([1,2,3]), 6, "Should be 6")

if __name__ == '__main__':
    unittest.main()
    
# Test-Driven Development (TDD): Embracing TDD involves writing
# tests before actually writing the code to pass them. 
# This approach encourages clear thinking about the script's 
# design and requirements before diving into implementation. 

# Imagine our previously optimized file organization script now
# needs validation to ensure its reliability. 
# We would start by writing unit tests for its core functionalities,
# such as file categorization and directory creation. 
# Following that, we'd employ debugging techniques, 
# especially when tests reveal unexpected behaviours,
# to iteratively refine our script. 

# check PEP 8 and flake8 (tool)

# use requirements.txt or Pipfile to maintain sanity. 

# pip-review

# Rubber Duck Debugging: The practice of explaining your code
# line by line to an inanimate object (traditionally a rubber duck)
# can surprisingly lead to epiphanies and error resolutions. 

# Version Control Bisection: Tools like 'git bisect' allow you 
# to use binary search through your project's history to identify 
# the commit that introduced a bug.

# Asserting Truths: 'unittest' provides a plethora of assertion methods
# such as 'assertEqual()', 'assertTrue()', 'assertFalse()' , and assertRaise()',
# among others. These assertions are the critical component of your test methods,
# allowing you to validate the behaviour of your script. 

# Setting Up and Tearing Down: For tests that require a specific context 
# or setup (like populating a database or creating a temporary file), 
# 'unittest' offers 'setUp()' and 'tearDown()' methods. These methods run 
# before and after each test method, respectively, ensuring a clean slate
# for every test. 


import unittest

def add(a, b):
    return a + b 

class TestAddFunction(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(add(2,3),5)
        
if __name__ == '__main__':
    unittest.main()
    
# see later unittest.mock for file systems, databases, APIs... 

# Ioc (Inversion of Control; frameworks)

# Libraries can be as simple as a single file containing reusable
# functions or as complex as a comprehensive package of modules. 

# framework: skeleton, blueprint, that defines architectural pattern
# for your application. 

# HTTP request, parsing JSON (libraries); web applications,
# data analysis pipelines (frameworks)

# Beautiful Soup excels in parsing HTML and XML documents
# and Scrapy offers a full-fledged framework for web crawling
# and extracting data.

# Pandas: For data manipulation and analysis, Pandas offers data
# structures and operations for manipulating numerical tables
# and time series, making it a cornestone in the automation of
# data processing tasks. 

# Django and Flask: For web automation and developing web applications,
# Django provides a high-level framework that encourages rapid 
# development with a clean, pragmatic design. 
# Flask, by contrast, offers more flexibility as a micro-framework,
# suitable for simples web applications and services. 

# Celery: For tasks that require asynchronous processing, 
# Celery is a powerful distributed task queue that integrates seamlessly
# with Django and Flask, allowing you to execute time-consuming tasks
# in the background. 

# While Selenium excels in browser automation, 
# the Requests library shines in handling HTTP requests. 
# It offers a user-friendly API
# for making requests to web servers,
# which is essential for tasks such as API testing, web scraping without a browser, 
# or automating interactions with web services.

# Don't Repeat Yourself (DRY)

# Django's object-relational mapper (ORM)
# enables devs to work with databases
# in a Pythonic way, abstracting 
# the complexities of direct SQL queries. 

# Consider a scenario where a business 
# needs to automate the entry of customer data into 
# a web-based CRM system. 
# Using Django, one can develop a web interface 
# to upload CSV files, 
# and Django can then parse these files and automatically populate the CRM with the extracted data. 

