def researcher_agent(state):
    question = state["question"]
    retriever = state["retriever"]

    docs = retriever.invoke(question)

    context = "\n".join([doc.page_content for doc in docs])

    return {
        **state,
        "context": context
    }