from langgraph.graph import StateGraph
from agents.researcher import researcher_agent
from agents.planner import planner_agent
from agents.generator import generator_agent


def build_graph():

    # CRÉATION DU GRAPH 
    graph = StateGraph(dict)

    # Ajouter les nodes
    graph.add_node("researcher", researcher_agent)
    graph.add_node("planner", planner_agent)
    graph.add_node("generator", generator_agent)

    # Définir le workflow
    graph.set_entry_point("researcher")

    graph.add_edge("researcher", "planner")
    graph.add_edge("planner", "generator")

    # Compiler
    return graph.compile()