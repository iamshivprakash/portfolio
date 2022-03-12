import mysql.connector

conn = mysql.connector.connect(
    user='gkE3pmBbcM', password='eU6P0N24QO', host='remotemysql.com', database='gkE3pmBbcM')
# print(conn.is_connected())
cursor = conn.cursor()
cursor.execute('select * from accomplishments order by issuing_date desc')
certificates = cursor.fetchall()
cursor.execute('select * from projects')
projects = cursor.fetchall()
# print(certificates)
# print(projects)
# projects = [
#     (1, 'Expense Tracker', 'This project is made for practising Firebase Realtime Database and Javascript.',
#      'https://expanse-tracker-f0438.web.app/index.html', 'expense.png'),
#     (2, 'SpaceX-Falcon-9-First-Stage-Landing-Prediction', 'The goal of this project is to estimate if falcon 9 stage 1 would land successfully or not, as it plays a major role in predicting the price of its relaunch.',
#      'https://github.com/iamshivprakash/SpaceX-Falcon-9-First-Stage-Landing-Prediction', 'spacex.jpg')
# ]

cert = [(2, 'Applied Data Science Capstone', 'IBM', 'Coursera', '2022, 1, 16', 'This certification does not expire', '77RWQKBDU52A', '96.16', 'https://www.coursera.org/account/accomplishments/certificate/77RWQKBDU52A'),
        (8, 'Machine Learning with Python', 'IBM', 'Coursera', '2022, 1, 6', 'This certification does not expire',
        'F5JE46CRKVDZ', '100.00', 'https://www.coursera.org/account/accomplishments/certificate/F5JE46CRKVDZ'),
        (3, 'Data Visualization with Python', 'IBM', 'Coursera', '2021, 12, 30', 'This certification does not expire',
        'ZLHXDG76Y9YJ', '96.91', 'https://www.coursera.org/account/accomplishments/certificate/ZLHXDG76Y9YJ'),
        (4, 'Databases and SQL for Data Science with Python', 'IBM', 'Coursera', '2021, 12, 24', 'This certification does not expire',
        'RXQSZUYGFR4Y', '99.42', 'https://www.coursera.org/account/accomplishments/certificate/RXQSZUYGFR4Y'),
        (5, 'Python Project for Data Science', 'IBM', 'Coursera', '2021, 12, 20', 'This certification does not expire',
        'NT62RVUMRWK6', '100.00', 'https://www.coursera.org/account/accomplishments/certificate/NT62RVUMRWK6'),
        (1, 'Data Analysis with Python', 'IBM', 'Coursera', '2021, 12, 8', 'This certification does not expire',
        'H79UV2LF6HCF', '97.00', 'https://www.coursera.org/account/accomplishments/certificate/H79UV2LF6HCF'),
        (7, 'Data Science Methodology', 'IBM', 'Coursera', '2021, 11, 27', 'This certification does not expire',
        '4MKUVYG8NJBJ', '94.16', 'https://www.coursera.org/account/accomplishments/certificate/4MKUVYG8NJBJ'),
        (9, 'Python for Data Science, AI & Development', 'IBM', 'Coursera', '2021, 11, 26', 'This certification does not expire',
        'ARPBEHB3JLCW', '97.30', 'https://www.coursera.org/account/accomplishments/certificate/ARPBEHB3JLCW'),
        (10, 'Tools for Data Science', 'IBM', 'Coursera', '2021, 11, 25', 'This certification does not expire',
        '8C8KJVSSCQGS', '95.83', 'https://www.coursera.org/account/accomplishments/certificate/8C8KJVSSCQGS'),
        (6, 'What is Data Science?', 'IBM', 'Coursera', '2021, 11, 8', 'This certification does not expire', 'YENWM25VZNUH', '93.00', 'https://www.coursera.org/account/accomplishments/certificate/YENWM25VZNUH')]
