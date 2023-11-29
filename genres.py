import csv

csv_file_path = "databases/mergedDatabase.csv"  # Replace with the path to your CSV file

# Set to store unique genres
unique_genres = set()

with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    header = next(reader)

    for row in reader:
        # Genres are in the 3rd column (index 2)
        genres = row[2]

        # Assuming genres are stored in a JSON-like format in the CSV, you can use eval to convert it to a list
        genres_list = eval(genres)

        # Update the set of unique genres
        unique_genres.update(genres_list)

# Print the list of unique genres
print("Unique Genres:", list(unique_genres))
