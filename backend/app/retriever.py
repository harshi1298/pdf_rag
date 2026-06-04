def retrieve(question, db):
    docs = db.similarity_search(
        question,
        k=3
    )
    return docs