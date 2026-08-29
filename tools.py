from langchain_core.tools import tool
from pathlib import Path
from langchain_core.tools import tool
from langchain_community.document_loaders import PyPDFLoader, Docx2txtLoader
import pandas as pd 

@tool
def file_type_detector(file_path: str) -> dict:
    """
    Detect the uploaded file type and return the extraction tool that should be used for processing it.
    """

    path = Path(file_path)

    if not path.exists():
        return {
            "status": "error",
            "message": "File not found."
        }

    extension = path.suffix.lower()

    tool_mapping = {
        ".pdf": "pdf_extractor",
        ".docx": "docx_extractor",
        ".csv": "csv_extractor",
        ".xlsx": "excel_extractor",
        ".xls": "excel_extractor",
    }

    if extension not in tool_mapping:
        return {
            "status": "error",
            "file_type": extension,
            "message": "Unsupported file type."
        }

    return {
        "status": "success",
        "file_name": path.name,
        "file_type": extension,
        "next_tool": tool_mapping[extension]
    }

@tool
def pdf_extractor(file_path: str) -> str:
    """Extract text from a PDF file."""

    loader = PyPDFLoader(file_path)
    documents = loader.load()

    text = ""

    for document in documents:
        text += document.page_content + "\n"

    return text

@tool
def excel_extractor(file_path: str) -> str:
    """Extract data from an Excel file."""

    excel_file = pd.ExcelFile(file_path)

    text = ""

    for sheet_name in excel_file.sheet_names:

        dataframe = pd.read_excel(
            file_path,
            sheet_name=sheet_name
        )

        text += f"\n--- Sheet: {sheet_name} ---\n"

        text += dataframe.to_string(
            index=False
        )

        text += "\n"

    return text

@tool
def docx_extractor(file_path: str) -> str:
    """Extract text from a DOCX file."""

    loader = Docx2txtLoader(file_path)
    documents = loader.load()

    text = ""

    for document in documents:
        text += document.page_content + "\n"

    return text

@tool
def csv_extractor(file_path: str) -> str:
    """Extract data from a CSV file."""

    dataframe = pd.read_csv(file_path)

    return dataframe.to_string(index=False)