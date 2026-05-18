from config.llm import get_llm
from tools.retriever import get_retriever
from graph.workflow import build_graph

llm = get_llm()
retriever = get_retriever()

graph = build_graph()

question = input("Pose ta question : ")

result = graph.invoke({
    "question": question,
    "llm": llm,
    "retriever": retriever
})

print(result.get("answer", "X Pas de réponse générée"))