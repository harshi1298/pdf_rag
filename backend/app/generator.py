from backend.app.retriever import retrieve
from backend.app.prompt import RAG_PROMPT
from backend.app.llm import llm

def generate_answer(question, db):

    docs = retrieve(question, db)

    context = "\n\n".join(
        doc.page_content
        for doc in docs
    )

    prompt = RAG_PROMPT.format(
        context=context,
        question=question
    )

    return llm.invoke(prompt)