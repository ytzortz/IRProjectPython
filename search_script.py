import json
from whoosh import index
from whoosh.qparser import MultifieldParser


def searchDatabase(title, genres, query):
    # Step 1: Open the index
    ix = index.open_dir("../index")

    # Step 2: Create a searcher
    searcher = ix.searcher()

    # Step 3: Define a query
    query_string = query  # Replace with your search query

    if title == 1:
        # Search titles
        fields_to_search = ["title"]
    else:
        if title == 2:  # search both
            fields_to_search = ["title", "overview", "keywords"]
        else:  # search overview
            fields_to_search = ["overview", "keywords"]

    # Step 4: Parse the query
    parser = MultifieldParser(fields_to_search, schema=ix.schema)
    query = parser.parse(query_string)

    results_list = []

    # Check if genres is empty
    if not genres:
        for result in searcher.search(query, limit=2000):

            result_dict = {
                "title": result["title"],
                "genres": result["genres"],
                "keywords": result["keywords"],
                "perc" : "{:.2f} %".format(result.score)
            }
            results_list.append(result_dict)
    else:
        for result in searcher.search(query, limit=2000):
            # Check if at least one genre in the movie matches any genre in the given list
            if any(g in result["genres"] for g in genres):
                print(result.score)
                result_dict = {
                    "title": result["title"],
                    "genres": result["genres"],
                    "keywords": result["keywords"],
                    "perc": "{:.2f} %".format(result.score)
                }
                results_list.append(result_dict)

    # Return only the top 15
    results_json = json.dumps(results_list[:15])

    # Step 6: Close the searcher
    searcher.close()
    return results_json
