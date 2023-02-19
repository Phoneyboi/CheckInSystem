# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import csv
import datetime
import streamlit as st

csv_file = r"C:\Hutch_Test\export-20230214-204227.csv"
txt_file = r'C:\Hutch_Test\emailLineTest.txt'


def read_from_csv(excel_file):
    data = open(excel_file, encoding="utf-8")
    csv_data = csv.reader(data)
    data_lines = list(csv_data)
    return data_lines


def read_from_txt(text_file, user_list):
    infile = open(text_file, "r")
    user_list = infile.readlines()
    for i in range(len(user_list)):
        user_list[i] = user_list[i].rstrip('/n')
    infile.close()
    return user_list


def write_txt_file(line_with_email):
    with open(txt_file, 'a') as file:
        file.write('\n')
        file.write(line_with_email)
    file.close()


def timestamp():
    now = datetime.datetime.now()
    return str(now)


def streamlit():
    lines = read_from_csv(csv_file)

    # Title
    st.header('CONQUER CHECK-IN')

    # Email
    streamlit_email = st.text_input("EMAIL")

    if streamlit_email:
        for line in lines:  # Parses each line in CSV
            if line[3] == streamlit_email:  # Finds line by email
                break
        else:
            st.write('Email does not match with active user profile.')
            st.write('Please try another or ask to have your email added to our database.')

    # Class options
    classes = ['5:30AM', '6:30AM', '8:30AM', '12:00PM', '4:30PM', '5:30PM', '8:00AM - SATURDAY', '9:15AM - SATURDAY']
    option = st.selectbox('CLASS',
                          classes)

    # Check-In
    checkin = st.button('CHECK-IN')
    if checkin:
        write_txt_file(option + ',' + timestamp() + ',' + streamlit_email)
        st.write('THANK YOU FOR CHECKING IN!')
        st.write('YOU CAN NOW CLOSE THIS BROWSER.')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    streamlit()



