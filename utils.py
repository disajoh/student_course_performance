#Helper functions to generate data and save to  a file

from faker import Faker 
import pandas as pd
import random
from pathlib import Path

# seed the generators for reproducibility
random.seed(12)
Faker.seed(10)


# create a faker object and set locale to UK
fake = Faker('en_UK')


def generate_name():
    return fake.name()

def save_data(data, file_name='data.csv', data_dir='data'):

     
    #create directory to save the file
    data_dir = Path(data_dir) 
    data_dir.mkdir(parents=True, exist_ok=True)
    file_path = data_dir / file_name
    

    #save to csv
    data.to_csv(file_path, index=False)
    print(f'[INFO] Generated data saved to {file_name} file...')


def generate_performance(num_students=1, save_to_file=True):
    student_data = [
        [
            student_id,                 # Student ID
            fake.name(),                # Name
            random.randint(20, 100),    # Attendance
            random.randint(20, 100),    # Assignment score
            random.randint(20,100),     # Quiz score
            random.randint(20, 100),    # Lab/practical score
            random.randint(20, 100),    # Midterm Exam score
            random.randint(20, 100)     # Final Exam score
        ]
        for student_id in range(num_students)
    ]
    
    columns = ['student_id', 'name', 'attendance', 'assignment', 'quiz', 'lab', 'midterm_exam', 'final_exam']
    
    #create dataframe
    df = pd.DataFrame(student_data, columns=columns)
    
    if save_to_file:
       
        save_data( df, 'student_performance.csv')
    else:
        return df

def generate_engagement(num_students=2, resources=['video', 'audio'], save_to_file=True):
    
    engagement_data = [
  
             [ 
               student_id,              
               resource_type ,            # learning resources: video, quiz, audio
               random.randint(40, 120),    #time spent on the resources
               random.choice([0, 1, 2]),  #Completion of activities in this resource 0: No, 1: partial, 2: yes
                
            ]
            for resource_type in resources 
            
                for student_id in range(num_students)
        ]
    
    columns = ['student_id', 'resource_type', 'time_spent', 'completion']

    #create datafram
    df = pd.DataFrame(engagement_data, columns=columns)

    if save_to_file:
        
        save_data( df, 'engagement_data.csv')
    else:
        return engagement_data
    
    return df



if __name__ == '__main__':

    # change num_students value to generate more students data
    generate_performance(num_students=10000)

    resources = ['pdf', 'quiz', 'podcast', 'video', 'quiz']
    generate_engagement(num_students=10000, resources=resources)
