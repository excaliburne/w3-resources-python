# Write a Python program to display the examination schedule. (extract the date from exam_st_date). 
# exam_st_date = (11, 12, 2014)
# Sample Output : The examination will start from : 11 / 12 / 2014

exam_st_date = (11, 12, 2014)

l = list(exam_st_date)

print("The examination will start from " + str(l[0]) + "/" + str(l[1]) + "/" + str(l[2]))