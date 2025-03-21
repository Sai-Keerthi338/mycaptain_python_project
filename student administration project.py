# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 03:47:46 2023

@author: Dell
"""

import csv
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

def write_into_csv(info_list, predicted_score):
    with open('student_info.csv', 'a', newline='') as csv_file:
        writer = csv.writer(csv_file)
        
        if csv_file.tell() == 0:
            writer.writerow(["Name", "Age", "Contact_Number", "Email_ID", "Attendance", "Assignment_Scores", "Predicted_Final_Exam_Score"])
        
        writer.writerow(info_list + [predicted_score])

if __name__ == '__main__':
    condition = True
    student_num = 1

    while condition:
        student_info = input(f"Enter student information for student #{student_num} in this format (Name Age Contact_Number Email_ID Attendance Assignment_Scores): ")
        student_info_list = student_info.split(' ')

        print("\nThe entered information is -\nName: {}\nAge: {}\nContact Number: {}\nEmail ID: {}\nAttendance: {}\nAssignment Scores: {}".format(
            student_info_list[0], student_info_list[1], student_info_list[2], student_info_list[3], student_info_list[4], student_info_list[5]
        ))

        choice_check = input("Is the entered information correct? (yes/no): ")

        if choice_check.lower() == "yes":
            try:
                df = pd.read_csv("student_info.csv")
            except FileNotFoundError:
                df = pd.DataFrame(columns=["Name", "Age", "Contact_Number", "Email_ID", "Attendance", "Assignment_Scores", "Predicted_Final_Exam_Score"])

            if len(df) > 1:  # Ensure enough data is present for training
                X = df[['Attendance', 'Assignment_Scores']].astype(float)
                y = df['Predicted_Final_Exam_Score'].astype(float)

                X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

                model = LinearRegression()
                model.fit(X_train, y_train)

                new_data = np.array([[float(student_info_list[4]), float(student_info_list[5])]])
                predicted_score = model.predict(new_data)[0]
            else:
                predicted_score = "Not Enough Data"

            student_info_list.append(predicted_score)
            write_into_csv(student_info_list, predicted_score)

            condition_check = input("Enter (yes/no) if you need another student information: ")
            condition = condition_check.lower() == "yes"
            student_num += 1

        elif choice_check.lower() == "no":
            print("\nPlease re-enter the values!")
