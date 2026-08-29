from typing import Any
from pydantic import BaseModel, ConfigDict, Field
from typing import Optional
from typing import List, Dict, Any
from pydantic import BaseModel, Field, ConfigDict

class FinancialData(BaseModel):
    model_config = ConfigDict(extra="allow")

    company_name: str | None = None
    reporting_period: str | None = None
    currency: str | None = None
    unit: str | None = None

    financial_statements: dict[str, Any] = Field(default_factory=dict)
    financial_metrics: dict[str, Any] = Field(default_factory=dict)
    segments: dict[str, Any] = Field(default_factory=dict)
    notes: list[str] = Field(default_factory=list)
    source_references: list[dict[str, Any]] = Field(default_factory=list)

class FinancialAnalysisResult(BaseModel):

    model_config = ConfigDict(extra="allow")

    company_name: str
    reporting_period: str
    currency: str
    unit: str

    key_metrics: Dict[str, Any] = Field(
        default_factory=dict,
        description="""
        Key financial metrics calculated from the available data.

        For every metric include:
        - value
        - unit
        - formula when calculated
        - source when directly reported

        Do not calculate a metric if required data is missing.

        Useful formulas include:
        Gross Margin = Gross Profit / Revenue × 100
        Operating Margin = Operating Income / Revenue × 100
        Net Profit Margin = Net Income / Revenue × 100
        ROA = Net Income / Total Assets × 100
        ROE = Net Income / Shareholders' Equity × 100
        """
    )

    profitability_analysis: List[str] = Field(
        default_factory=list,
        description="""
        Analyze profitability using available data.

        Formulas:
        Gross Margin = Gross Profit / Revenue × 100
        Operating Margin = Operating Income / Revenue × 100
        Net Profit Margin = Net Income / Revenue × 100
        ROA = Net Income / Total Assets × 100
        ROE = Net Income / Shareholders' Equity × 100
        """
    )

    liquidity_analysis: List[str] = Field(
        default_factory=list,
        description="""
        Analyze liquidity.

        Formulas:
        Current Ratio = Current Assets / Current Liabilities
        Quick Ratio = (Current Assets - Inventory) / Current Liabilities
        Cash Ratio = Cash and Cash Equivalents / Current Liabilities
        """
    )

    leverage_analysis: List[str] = Field(
        default_factory=list,
        description="""
        Analyze leverage and solvency.

        Formulas:
        Debt-to-Equity = Total Debt / Shareholders' Equity
        Debt-to-Assets = Total Debt / Total Assets × 100
        """
    )

    cash_flow_analysis: List[str] = Field(
        default_factory=list,
        description="""
        Analyze cash flow.

        Formulas:
        Free Cash Flow = Operating Cash Flow - Capital Expenditures
        Operating Cash Flow Margin = Operating Cash Flow / Revenue × 100
        Free Cash Flow Margin = Free Cash Flow / Revenue × 100
        """
    )

    efficiency_analysis: List[str] = Field(
        default_factory=list,
        description="""
        Analyze efficiency when all required data exists.

        Formulas:
        Asset Turnover = Revenue / Average Total Assets
        Receivables Turnover = Revenue / Average Accounts Receivable
        Inventory Turnover = Cost of Goods Sold / Average Inventory
        """
    )

    segment_analysis: List[str] = Field(
        default_factory=list,
        description="""
        Analyze geographic or product segments when segment data exists.

        Formula:
        Segment Revenue Contribution = Segment Revenue / Total Revenue × 100
        """
    )

    trend_analysis: List[str] = Field(
        default_factory=list,
        description="""
        Analyze trends only when multiple reporting periods exist.

        Formula:
        Growth Rate = (Current Value - Previous Value) / Previous Value × 100
        """
    )

    financial_strengths: List[str] = Field(
        default_factory=list,
        description="Financial strengths supported by the available data."
    )

    financial_weaknesses: List[str] = Field(
        default_factory=list,
        description="Financial weaknesses supported by the available data."
    )

    key_risks: List[str] = Field(
        default_factory=list,
        description="Material financial risks supported by the available data."
    )

    important_observations: List[str] = Field(
        default_factory=list,
        description="Important data-driven observations."
    )

    unavailable_metrics: Dict[str, str] = Field(
        default_factory=dict,
        description="""
        Metrics that cannot be calculated because required data is missing.

        Key = metric name
        Value = reason the metric could not be calculated.

        Never assume missing data is zero.
        """
    )




