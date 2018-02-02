# This program is to get the students who are common in both the python and web courses


python_list = ['sai mohith', 'rajesh', 'minh', 'nathan', 'brian', 'joe', 'vince']  # list students attending python
web_list = ['moe', 'long', 'snance', 'joe', 'surya', 'rajesh', 'minh']  # list students attending web application
print("Students common in both courses: ", set(python_list) & set(web_list))  # print the students attending both classes
print("Students who are not common in both courses: ", set(python_list) ^ set(web_list))  # print the students not common in both classes
