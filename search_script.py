from whoosh import index
from whoosh.qparser import QueryParser, MultifieldParser

# Step 1: Open the index
ix = index.open_dir("C:/Users/s0239369/Desktop/projectPython/index")

# Step 2: Create a searcher
searcher = ix.searcher()

# Step 3: Define a query
query_string = 'jealousy'  # Replace with your  search query

# f'{field_name}.name:"Animation"' change animation to any other genre we want

# Step 4: Parse the query
#parser = QueryParser(fieldname="overview", schema=ix.schema)
parser = MultifieldParser(["keywords"], schema=ix.schema)
query = parser.parse(query_string)

# Step 5: Search and print the first 5 results
results = searcher.search(query, limit=5)

if not results:
    print("NO RESULTS BRO")


for result in results:      #if "Drama" in result["genres"]: you can add this to filter the results
    print("Title:", result["title"])
    print("Overview:", result["overview"])
    print("Genres:", result["genres"])
    print("Keywords:", result["keywords"])
    print("------")



# Step 6: Close the searcher
searcher.close()
