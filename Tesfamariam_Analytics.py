# Standard library imports
import csv
import json
import os  # Import os only once
from pathlib import Path
import requests

# Define root folder
root_folder = 'C:/Users/Tesfamariam/datafun-03-analysis2'

# Define folder names and filenames
txt_folder_name = 'data-txt'
csv_folder_name = 'data-csv'
json_folder_name = 'data-json'
txt_filename = 'data.txt'
csv_filename = 'data.csv'
json_filename = 'data.json'

# Define your URLs
txt_url = 'https://bit.ly/47S3jz5'
csv_url = 'https://bit.ly/3vPMOXg'
json_url = 'https://bit.ly/47Yp28x'

# Function to fetch and write text data
def fetch_and_write_txt_data(folder_name, filename, url):
    response = requests.get(url)
    if response.status_code == 200:
        write_txt_file(folder_name, filename, response.text)
    else:
        print(f"Failed to fetch text data from {url}")

# Function to fetch and write CSV data
def fetch_and_write_csv_data(folder_name, filename, url):
    response = requests.get(url)
    if response.status_code == 200:
        write_csv_file(folder_name, filename, response.text)
    else:
        print(f"Failed to fetch CSV data from {url}")

# Function to fetch and write JSON data
def fetch_and_write_json_data(folder_name, filename, url):
    response = requests.get(url)
    if response.status_code == 200:
        write_json_file(folder_name, filename, response.text)
    else:
        print(f"Failed to fetch JSON data from {url}")

# Function to write text data to file
def write_txt_file(folder_name, filename, data):
    file_path = Path(root_folder) / folder_name / filename
    with open(file_path, 'w') as file:
        file.write(data)
    print(f"Text data saved to {file_path}")

# Function to write CSV data to file
def write_csv_file(folder_name, filename, data):
    file_path = Path(root_folder) / folder_name / filename
    with open(file_path, 'w', newline='') as file:
        file.write(data)
    print(f"CSV data saved to {file_path}")

# Function to write JSON data to file
def write_json_file(folder_name, filename, data):
    file_path = Path(root_folder) / folder_name / filename
    with open(file_path, 'w') as file:
        file.write(data)
    print(f"JSON data saved to {file_path}")

# Fetch and write data
fetch_and_write_txt_data(txt_folder_name, txt_filename, txt_url)
fetch_and_write_csv_data(csv_folder_name, csv_filename, csv_url)
fetch_and_write_json_data(json_folder_name, json_filename, json_url)

# Create the directory if it doesn't exist
directory_path = os.path.join(root_folder, txt_folder_name)
if not os.path.exists(directory_path):
    os.makedirs(directory_path)
    print(f"Directory '{directory_path}' created successfully")
else:
    print(f"Directory '{directory_path}' already exists")
