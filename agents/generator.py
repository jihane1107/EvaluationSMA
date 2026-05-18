def generator_agent(state):
    llm = state["llm"]
    plan = state["plan"]

    answer = llm.invoke(f"Réponds avec ce plan:\n{plan}")

    return {
        **state,
        "answer": answer
    }