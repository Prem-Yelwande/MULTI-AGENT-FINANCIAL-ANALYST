from agents import *
from states import FinancialData, FinancialAnalysisResult

from langgraph.graph import StateGraph
from langgraph.constants import END
from rich import print 

def extractor_agent(state: dict) -> dict:
    file_path = state["file_path"]
    extractor = Doc_extractor()
    result = extractor.invoke({
        "messages": [
            {
                "role": "user",
                "content": f"Extract all financial data from this file: {file_path}"
            }
        ]
    })

    response: FinancialData = result["structured_response"]
    if response is None:
        raise ValueError("Financial data extraction nai ho paya sorry yawr")

    return {"financial_data": response}

def financial_analyst(state: dict)->dict:
    financial_data : FinancialData = state["financial_data"]
    response = llm2.with_structured_output(FinancialAnalysisResult, method="json_mode").invoke(Financial_prompt(financial_data))
    if response is None:
        raise ValueError("error")
    response.financial_data = financial_data
    return {"financial_analyst": response}


graph = StateGraph(dict)

graph.add_node("extractor", extractor_agent)
graph.add_node("analyst", financial_analyst)

graph.set_entry_point("extractor")

graph.add_edge("extractor", "analyst")
graph.add_edge("analyst", END)

app = graph.compile()


file_path = r"nasdaq-aapl-2025-10K-251437791.pdf"

result = app.invoke({
    "file_path": file_path
})

print("=== EXTRACTED FINANCIAL DATA ===")
print(result["financial_data"])

print("\n=== FINANCIAL ANALYSIS ===")
print(result["financial_analyst"])