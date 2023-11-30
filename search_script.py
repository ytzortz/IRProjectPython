import json
from collections import Counter

from whoosh import index
from whoosh.qparser import QueryParser, MultifieldParser


def searchDatabase(title, genres, query):

    # Step 1: Open the index
    ix = index.open_dir("../index")

    # Step 2: Create a searcher
    searcher = ix.searcher()


    # Step 3: Define a query
    query_string = query  # Replace with your  search query

    if title == 1:
        # Search titles
        fields_to_search = ["title"]
    else:
        if title == 2: # search both
            fields_to_search = ["title", "overview", "keywords"]
        else:   # search overview
            fields_to_search = ["overview", "keywords"]

    # f'{field_name}.name:"Animation"' change animation to any other genre we want
    # Step 4: Parse the query
    # parser = QueryParser(fieldname="overview", schema=ix.schema)
    parser = MultifieldParser(fields_to_search, schema=ix.schema)
    query = parser.parse(query_string)

    results_list = []
    for result in searcher.search(query, limit=2000):
        common_genres = set(result["genres"]).intersection(genres)
        print(f"Result Genres: {result['genres']}")
        print(f"Common Genres: {len(common_genres)}")
        result_dict = {
            "title": result["title"],
            "common_genres_count": len(common_genres),
            "genres": result["genres"],
            "keywords": result["keywords"]
        }
        results_list.append(result_dict)

    # Sort the results by the number of common genres
    sorted_results = sorted(results_list, key=lambda x: x["common_genres_count"], reverse=True)

    # Return only the top 15
    results_json = json.dumps(sorted_results[:15])


    # Step 6: Close the searcher
    searcher.close()
    return results_json


