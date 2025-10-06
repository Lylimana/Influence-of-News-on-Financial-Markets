In this repository I will be tackling thhe following task: 

**S.T.A.R. Framework**

**Situation:** A financial news publication wants to create a new content section featuring data-driven articles on market reactions to company news. I’ve been tasked with developing a proof-of-concept project that demonstrates how to analyze this relationship for a major tech company.

**Task:** Identify the impact of quarterly earnings reports on the stock price of a publicly traded tech company (e.g., Apple, Amazon). The goal is to show a quantifiable relationship between the event and market performance.


**Action:**

- **Data Collection**: Use the **Financial Modeling Prep API** to retrieve daily stock price data (e.g., historical closing prices) for a chosen company.
  
- **Event Identification**: Find the exact dates of the company's past four quarterly earnings report releases from a reliable financial news source.
  
- **Data Analysis**: Merge the stock data with the earnings report dates. Analyze the stock's performance in the days leading up to and following each report. Calculate metrics like the percentage change in stock price over a specific window (e.g., 3 days before to 3 days after) to measure the market reaction.
  
- **Visualization**: Create charts (e.g., a time-series plot with event markers or a bar chart comparing performance across different quarters) to visually represent the findings.