employee_file= open("employees.txt","r")
#print(employee_file.readable())        # check if the file is readable
#print(employee_file.read())             # read the entire file
print(employee_file.readline())         # read a line at a time

employee_file.close()