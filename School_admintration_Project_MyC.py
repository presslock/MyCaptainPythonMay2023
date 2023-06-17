#!/usr/bin/env python
# coding: utf-8

# In[18]:


import csv

def write_into_csv(info_list):
    with open("student_info.csv", 'a', newline='') as csv_file:
        writer = csv.writer(csv_file)
       
    if csv_file.tell() == 0:
         writer.writerow(["Name","Age","Contact Number", "E-Mail Id"])
             
    writer.writerow(info_list)

if __name__ == "__main__":
    condition = True

    while(condition):
        student_info = input("Please enter student's information in the following format (Name Age Contact_No E-mail_Id):")
    
        print("Entered Information: " + student_info)
    
        #split
        student_info_list = student_info.split(' ')
        print("Entered split up information is:" + str(student_info_list))
        
        print("\nThe Entered Information is -\nName: {}\nContact_Number: {}\nE-mail id: {}".format(student_info_list[0], student_info_list[1], student_info_list[2], student_info_list[3]))
        
        choice_check = input("is the entered Information correct? (yes/no): ")
        
        if choice_check == "yes":
            write_into_csv(student_info_list)
    
            condition_check = input("Type yes/no if you want to enter information for another student:")
            if condition_check == "yes":
                condition = True
                student_num = student_num + 1
            elif condition_check == "no":
                condition = False
        elif choice_check == "no":
              print("\nPlease re-enter the values!")


# In[ ]:





# In[ ]:




