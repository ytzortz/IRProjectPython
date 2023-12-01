from whoosh import index
from whoosh.fields import Schema, TEXT, STORED
from whoosh.analysis import StandardAnalyzer, KeywordAnalyzer, RegexTokenizer, LowercaseFilter
from whoosh.index import create_in
import csv
from pathlib import Path

def indexing():

    # Custom stop word list. I found this here: https://gist.github.com/sebleier/554280
    stop_words = {"i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
                  "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
                  "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that",
                  "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had",
                  "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as",
                  "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through",
                  "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off",
                  "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how",
                  "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not",
                  "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should",
                  "now"}

    # Custom analyzer for JSON field
    json_analyzer = RegexTokenizer() | LowercaseFilter()

    # Step 1: Define the schema
    schema = Schema(
        overview=TEXT(analyzer=StandardAnalyzer(stoplist=stop_words), stored=True),  # Use StandardAnalyzer with custom stop word list
        title=TEXT(stored=True),
        genres=STORED(),
        keywords=TEXT(analyzer=json_analyzer, stored=True)
    )

    # Step 2: Create the index directory
    index_path = Path("../index")
    index_path.mkdir(exist_ok=True)  # Creates the directory if it doesn't exist

    # Step 3: Create the index
    index.create_in(index_path, schema)

    # Step 4: Open the index for writing
    ix = index.open_dir(index_path)

    # Step 5: Open a writer
    writer = ix.writer()

    # Step 6: Read the CSV file and add documents to the index
    csv_file_path = "databases/mergedDatabase.csv"  # Replace with the path to your CSV file
    with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)  # Assuming the first row is the header

        for row in reader:
            overview, title, genres, keywords = row[3], row[9], row[2], row[1]
            writer.add_document(overview=overview, title=title, genres=genres, keywords=keywords)

    # Step 7: Commit the changes
    writer.commit()

    print("Indexing complete.")
