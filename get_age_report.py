# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 14:50:07 2022

@author: goconnor
"""

from datetime import date
import pandas as pd

def calculate_age(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

#date(year, month, day)

gender_li = ["Male","Female"]

all_male_data, all_female_data = [],[]

def read_data(file: str, gender_choice: str):
    males_tot, females_tot, other_tot = 0,0,0
    
    male_main_list = [0] * (49-16)
    female_main_list = [0] * (49-16)
    
    male_supp_list = [0] * (4)
    female_supp_list = [0] * (4)
    
    male_unknown_list, female_unknown_list = [],[]
    
    df = pd.read_csv(file, header=None)
    for i in range(0, len(df.index)):
        gender = df.iloc[i, 1]
        
        #print(df.iloc[i, 2], df.iloc[i, 3], df.iloc[i, 4], df.iloc[i, 0])
        
        if df.iloc[i, 4] > 1900 and 0 < df.iloc[i,3] < 13 and 0 < df.iloc[i,2] < 32:
            
            year = int(df.iloc[i, 4])
            month = int(df.iloc[i, 3])
            day = int(df.iloc[i, 2])
            
            if gender == "Male" and gender_choice == "Male":
                males_tot += 1
            
                age = calculate_age(date(int(year), int(month), int(day)))
                
                if age >= 16 and age <= 49:
                    male_main_list[age - 16] += 1
                elif age >= 50 and age <= 54:
                    print("Male 50-54")
                    male_supp_list[0] += 1
                elif age >= 55 and age <= 59:
                    print("Male 55-59")
                    male_supp_list[1] += 1
                elif age >= 60 and age <= 64:
                    print("Male 60-64")
                    male_supp_list[2] += 1
                elif age >= 65:
                    print("Male 65 and over")
                    male_supp_list[3] += 1
                else:
                    print("Age_Unknown", gender, age, df.iloc[i, 0])
                    male_unknown_list.append([gender, age, df.iloc[i, 0]])
            
            elif gender == "Female" and gender_choice == "Female":
                females_tot += 1
                
                year = df.iloc[i, 4]
                month = df.iloc[i, 3]
                day = df.iloc[i, 2]
                
                age = calculate_age(date(int(year), int(month), int(day)))
                
                if age >= 16 and age <= 49:
                    female_main_list[age - 16] += 1
                elif age >= 50 and age <= 54:
                    print("Female 50-54")
                    female_supp_list[0] += 1
                elif age >= 55 and age <= 59:
                    print("Female 55-59")
                    female_supp_list[1] += 1
                elif age >= 60 and age <= 64:
                    print("Female 60-64")
                    female_supp_list[2] += 1
                elif age >= 65:
                    print("Female 65 and over")
                    female_supp_list[3] += 1
                else:
                    print("Age_Unknown")
                    print("\t", gender, age, df.iloc[i, 0])
                    female_unknown_list.append([gender, age, df.iloc[i, 0]])
            
            elif gender == "Male" and gender_choice != "Male":
                0
            elif gender == "Female" and gender_choice != "Female":
                0
            elif gender != "Male" or gender != "Female":
                other_tot += 1
                print("No gender found")
            
    #print(males_tot, females_tot, other_tot)
    #print("\n", male_main_list, "\n", female_main_list)
    
    if gender_choice == "Male":
        print("Male Main:", male_main_list)
        print("Male Supp:", male_supp_list)
        print("Male Unknown:", male_unknown_list)
        return male_main_list
    elif gender_choice == "Female":
        print("Female Main:", female_main_list)
        print("Female Supp:", female_supp_list)
        print("Female Unknown:", female_unknown_list)
        return female_main_list

def read_all_data(file_li):
    
    all_male_data, all_female_data = [],[]
    
    for i in range(0, len(file_li)):
        all_male_data.append([file_li[i], read_data(file_li[i], "Male")])
        all_female_data.append([file_li[i], read_data(file_li[i], "Female")])
        
    print("\n\n\n\nAll Male Data", all_male_data)
    print("\n\n\n\nAll Female Data", all_female_data)
    
    return all_male_data, all_female_data

if __name__ == "__main__":
    file_li = ["LC.csv", "4.csv", "./PT/LC.csv", "./PT/other.csv"]
    all_male_data, all_female_data = read_all_data(file_li)