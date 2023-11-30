import csv

# Replace 'your_file.csv' with the actual path to your CSV file
csv_file_path = 'databases/mergedDatabase.csv'

# Create an empty set to store unique genres
unique_genres = set()

# Open the CSV file and read the genres from each row
with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    header = next(reader)  # Assuming the first row is the header

    for row in reader:
        genres = row[2]  # Assuming the genres are in the third column, adjust if needed
        genres_list = eval(genres)  # Convert the string representation of a list to an actual list
        unique_genres.update(str(genre) for genre in genres_list)

# Print the unique genres
print(list(unique_genres))
