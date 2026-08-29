from agents import Doc_extractor
from rich import print

file_path = r"C:\Users\Prem\Desktop\MULTI-AGENT-FINANCIAL-ANALYST\nasdaq-aapl-2025-10K-251437791.pdf"


def test_extractor():

    extractor = Doc_extractor()

    result = extractor.invoke({
        "messages": [
            {
                "role": "user",
                "content": f"Extract all financial data from this file: {file_path}"
            }
        ]
    })

    print(result["structured_response"])


test_extractor()