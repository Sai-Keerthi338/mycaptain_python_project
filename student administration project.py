# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 03:47:46 2023

@author: Dell
"""

import csv

def write_into_csv(info_list):
    with open('student_info.csv','a',newline='')as csv_file:
        writer=csv.writer(csv_file)
        
        if csv_file.tell()==0:
            writer.writerow(info_list)
            
if(__name__=='__main__'):
    condition=True
    student_num=1

    while(condition):
        
        student_info=input("enter student information for student #{} in the following format (name age contact_number email_id):".format(student_num))
        student_info_list=student_info.split(' ')
           
        print("\nThe entered information is -\rname: {}\nage {}\ncontact_number: {}\nemail_id: {}".format(student_info_list[0],student_info_list[1],student_info_list[2],student_info_list[3]))
        
        choice_check=input("is the entered information correct?(yes/no): ")
        
        if choice_check=="yes":
            write_into_csv(student_info_list)
            
            condition_check=input("enter(yes/no) if you need another student information: ")
            if condition_check=="yes":
                condition=True
                student_num=student_num+1
            elif condition_check=="no":
                 condition=False
        elif choice_check=="no":
            print("\nPlease re-enter the values!")
            