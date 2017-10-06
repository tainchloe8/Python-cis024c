
# coding: utf-8

# 
# # CIS024C - Fall 2017 - Thursday 5:30-9:25pm 
# 
# ## Homework 4
# 
# Homework 4 covers exercises in basic collection objects in Python - lists, tuples and dictionaries.
# 
# The below sites have some interesting and useful information on these objects.
# 
# http://sthurlow.com/python/lesson06/
# https://docs.python.org/2/tutorial/datastructures.html
# 
# You will need to download this notebook and use this as a starting point for your homework. You will just need to fill in the content of each code-block (cell) and execute. Once you have completed all the exercises, you will need to save and upload this to your github repository under a folder called hw3.
# 
# Note also the exercises build on top of one another so you might be able to do the next exercise if you have not completed the previous exercise.
# 
# Post any questions you have on our Slack at **cis-024c1.slack.com**
# 
# <h3><font color='red'>
# ALL THE WORK THAT WE DID IN CLASS DURING WEEK 4 IS NOW IN GITHUB AT THE BELOW LINK
# </font></h3>
# 
# https://github.com/cis024c/fall2017classwork/blob/master/week4/week4_classwork.ipynb
# 
# ** Slides ** for Week 4 can be found at https://docs.google.com/presentation/d/1xhyxix3nF5A26qQTe1gSYJcYjUIipnz9BtZO04GvgJ4/edit?usp=sharing
# 
# **Please refer back to hw1 and slack for instructions on how to setup your computer for developing using Python.**

# ### Helpful Jupyter Commands
# 
# Below are some useful commands to know when using Jupyter
# 
# 1. You can add a new cell by clicking on the "+" icon on top.
# 2. You can delete a cell by selecting that cell and clicking on the "scissors" icon on top.
# 3. You can execute a cell by either pressing shift+enter or selecting the "play" button on top.
# 4. You can create a new file in Jupyter via the File menu->New Notebook option. Make sure to select Python 2 when creating your notebook.
# 5. Also, for your code blocks make sure that Code is selected instead of another option like Markdown.
# 6. Use the Enter key to go to the next line in a cell to enter the next statement.
# 7. You can clear results by clicking on the Cell menu item and selecting Current Output->Clear or All Output->Clear depending on whether you are trying to just clear the output for one cell or for all cells.
# 8. In case your program has crashed for some reason (infinite loop, for example), you can restart your Python session by select Kernel in the menu and selecting Restart.
# 

# #### Check Python Version

# In[1]:

get_ipython().system(u'python --version')


# #### Sample Exercises with conditionals and repetitions
# 
# Refer to Week 4 classwork for sample exercises - https://github.com/cis024c/fall2017classwork/blob/master/week4/week4_classwork.ipynb

# **Exercise 1 - Testing your knowledge of lists, tuples and dictionaries**
# 
# Answer the below questions
# 
# 1. What is the main difference between a list and a tuple
# 2. How does a dictionary object differ from a list.

# << Double click this cell and enter your result >> 
# 1. The main difference between a list and a tuple are that lists can be changed while tuples can't be changed.
# 2. A dictionary object is not ordered and has keys, while a lis is in a certain order.

# #### Exercise 2 -  Initializing a list, tuple and dictionary
# 
# 1. Create a list object with a set of any 10 numbers. Print the result
# 2. Create a tuple object with a set of 10 numbers. Print the result
# 3. Create a dictionary object with a set of 10 numbers. Print the result

# In[2]:

### YOUR CODE GOES 
x = [1,2,3,4,5,6,7,8,9,10]
print x

y = (2,97,4,95,13,5,67,98,0,8)
print y

z = {23:32,45:54,63:36,78:87,12:21,25:52,12:21,98:89,8:8,0:0}
print z

### END CODE


# #### Exercise 3 - Displaying values in a list object
# 
# Create a list object with 10 arbitrary numbers. Use a ** for loop ** to display every other element. 
# 
# **Example:**
# 
# If your list has [2,3,4,5,6], then you will need to display [2,4,6]
# 
# **Hint:** Make use the last step parameter in the range function to do this

# In[23]:

### YOUR CODE GOES BELOW
x = [1,2,3,4,5]
for i in range(len(x)):
    print x[0::2]

### END CODE


# #### Exercise 4 - Sorting a list of strings
# 
# Ask the user to enter a list of names. Sort the names in ascending order. 
# 
# Hint: Use the same logic that we used in class to sort numbers. When used with strings, Python will sort the strings in alphabetical order

# In[5]:

### YOUR CODE GOES BELOW
nameList = raw_input("Please enter a list of names: ")
result = []
nameList = nameList.split(",")
for i in range(len(nameList)):
    smallest = min(nameList)
    result.append(smallest)
    nameList.remove(smallest)
print "Result:",result

### END CODE


# #### Exercise 5 - Accessing values in a dictionary object
# 
# Initialize a dictionary object with the below key, value pairs
# 
#  Key  | Value
#  -----|------
# 1|Harry
# 2|Sally
# 3|Joe
# 4|Mathew
# 
# Ask the user to enter a key between 1 and 4.
# 
# Display the corresponding value in the dictionary
# 
# 
# 

# In[70]:

### YOUR CODE GOES BELOW
myDictionary = {1:"Harry", 2:"Sally", 3:"Joe", 4:"Matthew"}
userKey = raw_input("Please enter a key between 1 and 4: ")
for userKey in myDictionary:
    userKey = myDictionary.values()
    print userKey

    
### END CODE


# ## OPTIONAL EXERCISES
# 
# Below is a set of optional exercises. These will not be graded but the solutions will be posted. I would strongly encourage you to try these out if you are done with the mandatory homework exercises to improve your understanding of python.

# #### Exercise 6
# 
# Write a Python script to check if a given key already exists in a dictionary
# 
# **Hint**: Use the **get** method to determine if a key exists

# In[9]:

### YOUR CODE GOES BELOW


### END CODE


# #### Exercise 7
# 
# Write a Python script to create a dictionary that contains a sequence of numbers from 1 to n and their squares. Ask the user to enter n. Display the resulting dictionary.
# 
# **Example**
# If user enters 5, then your dictionary will look like
# 
# {1:1,2:4,3:9:4:16,5:25}
# 
# **Hint** You will need to assign new values to the dictionary to create the dictionary object

# In[13]:

### YOUR CODE GOES BELOW


### END CODE


# #### Exercise 8
# 
# Refer to Exercise 7 for this problem.
# 
# Write a python program to sum all the values in the above dictionary (n:n^2). Display the resulting sum
# 

# In[14]:

### YOUR CODE GOES BELOW


### END CODE


# #### Exercise 9
# 
# Write a Python program to sort the below dictionary by key in descending order. 
# 
#  {2:"Mary",1:"Sally",5:"Harry",4:"Joe"}
#  
# **Hint:** Refer to the class example

# In[15]:

### YOUR CODE GOES BELOW


### END CODE


# #### Exercise 10
# 
# Write a python program to combine the below two dictionaries and display the resulting dictionary
# 
# * Dictionary 1:  {2:"Mary",1:"Sally",5:"Harry",4:"Joe"}
# * Dictionary 2:  {6:"John",9:"Nancy",12:"Peter",8:"Alice"}
#  

# In[ ]:

### YOUR CODE GOES BELOW


### END CODE

