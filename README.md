# libraries
$ pip install requests
$ pip install streamlit



# chromadb
This is the python implementation of a backend API that accepts text queries, and runs them through OpenAI embeddings API and saves the results in ChromaDB

# LangChain
$ pip install langchain
$ pip install pdfquery


# HOW TO RUN THE SERVER:
docker build -t intellifind:dev .  
docker run -e OPENAI_API_KEY=$EMBDEDDINGS_OPENAI_API_KEY -v db:/app/db -it -p 88:8080 intellifind:dev

