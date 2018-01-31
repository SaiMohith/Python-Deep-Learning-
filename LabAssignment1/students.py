python_list = ['sai mohith', 'rajesh', 'minh', 'nathan', 'brian', 'joe', 'vince']  # list students attending python
web_list = ['moe', 'long', 'snance', 'joe', 'vamshi', 'rajesh', 'minh']  # list students attending web application
print("common list: ", set(python_list) & set(web_list))  # print the students attending both classes
print("uncommon list: ", set(python_list) ^ set(web_list))  # print the students not common in both classes
