import numpy as np
import pandas as pd

def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')
    race_count = pd.Series(df['race'].value_counts(), name='race')

    # What is the average age of men?
    average_age_men = df.loc[df['sex'] == 'Male','age'].mean()
    average_age_men = (average_age_men).round(1)

    # What is the percentage of people who have a Bachelor's degree?
    bacherlors = len(df[df['education'] == 'Bachelors'])
    total_people = len(df)
    percentage_bachelors = (bacherlors/total_people) * 100
    percentage_bachelors = np.round(percentage_bachelors, 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?
    # percentage with salary >50K MAL
    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education_people = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    higher_education_rich = higher_education_people[higher_education_people['salary'] == '>50K'].shape[0]
    higher_education_rich = (higher_education_rich / len(higher_education_people)) * 100
    higher_education_rich = np.round(higher_education_rich, 1)

    lower_education_people = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    lower_education_rich = lower_education_people[lower_education_people['salary'] == '>50K'].shape[0]
    lower_education_rich = (lower_education_rich / len(lower_education_people)) * 100
    lower_education_rich = np.round(lower_education_rich, 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()
    
    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    min_hours_workers = df[df['hours-per-week'] == df['hours-per-week'].min()]
    min_hours_rich = min_hours_workers[min_hours_workers['salary'] == '>50K'].shape[0]
    rich_percentage = (min_hours_rich / len(min_hours_workers)) * 100
    rich_percentage = rich_percentage

    # What country has the highest percentage of people that earn >50K?
    highest_earning_country_table = df.loc[df['salary'] == '>50K', 'native-country']
    #highest_earning_country_diff = len(highest_earning_country_table)/len(df)
    highest_earning_country = df['native-country'].value_counts()
    highest_earning_country = (highest_earning_country_table.value_counts())/df['native-country'].value_counts()
    highest_earning_country = highest_earning_country.idxmax()

    # if i want to know hoy many people are in the country who has the biggest salarys
    #highest_earning_country = (highest_earning_country_table.value_counts()).max()

    highest_earning_country_percentage = ((highest_earning_country_table.value_counts())/df['native-country'].value_counts()).max() * 100
    highest_earning_country_percentage = (highest_earning_country_percentage).round(1)
    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation_table = df.loc[(df['salary'] == '>50K') & (df['native-country'] == 'India')]
    top_IN_occupation = (top_IN_occupation_table['occupation'].value_counts()).idxmax()

    if print_data:
        #print(df['education'].unique())  
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }