# Retail Insights & Analytics — Power BI Portfolio

An interactive **Business Intelligence and Data Analytics project** built with Power BI to explore retail sales performance, gross profit, product category contributions, geographic distribution, and trends over time.

This project demonstrates how business data can be organized and visualized to support performance monitoring, identify potential business opportunities, and provide insights for data-driven decision-making.

> **Project Status:** Portfolio documentation and analysis framework.
>
> This project is based on the structure of a supplied Power BI report (`.pbix`). The original embedded data model uses Power BI's XPress9 compression format and has not been independently extracted or validated. Consequently, this repository does not currently publish the original source records, verified KPI values, or quantitative business findings. Actual findings will be added after the underlying data has been validated.

---

## 1. Business Objectives

The primary objective is to analyze retail business performance and provide stakeholders with a clearer understanding of sales, profitability, product categories, and regional trends.

Key business questions include:

- Which product categories contribute most to total sales?
- Which categories generate the highest gross profit?
- How does sales performance vary across different states?
- How do sales and gross profit change over time?
- Which product sub-categories and geographic areas require further investigation?

## 2. Dashboard Overview

The Power BI report contains one dashboard page with eight visual elements designed to support different aspects of retail performance analysis.

| Dashboard Visual | Analysis Focus | Fields |
|---|---|---|
| KPI | Sales by product category | `Category`, `Sales` |
| KPI | Gross profit by category | `Gross_Profit`, `Category` |
| Bar Chart | Sales by state and category | `Sales`, `State`, `Category` |
| Combo Chart | Sales and gross profit trends | `Order Date`, `Sales`, `Gross_Profit` |
| Area Chart | Monthly sales trends | `Sales`, `Order Date Month` |
| Multi-row Card | Category-level performance | `Category`, `Gross_Profit`, `Quantity`, `Sales` |
| Filled Map | Quantity distribution by state | `State`, `Quantity` |
| Slicer | Interactive sub-category filtering | `Sub-Category` |

## 3. Tools & Technologies

| Tool / Skill | Application |
|---|---|
| **Power BI** | Dashboard development, data visualization, KPI reporting, and interactive filtering |
| **Data Analysis** | Sales performance, gross profit, quantity, product category, and regional analysis |
| **Business Intelligence** | Translating business data into meaningful analytical perspectives |
| **Data Visualization** | Presenting geographic distributions and time-series trends |
| **Business Communication** | Developing stakeholder-oriented questions and recommendations |

## 4. Data Model & Dataset Structure

The report references four primary tables:

- `sales_details`
- `product_details`
- `Place_details`
- `order_details`

### Identified Fields

| Category | Fields |
|---|---|
| Sales Metrics | `Sales`, `Gross_Profit`, `Quantity` |
| Product Information | `Category`, `Sub-Category` |
| Geographic Information | `State` |
| Date Information | `Order Date` |

**Data validation note:** The exact table relationships, calculated measures, data types, row counts, refresh history, and original data-source provenance still need to be verified using Power BI Model View and Power Query.

## 5. Repository Structure

```text
retail-insights-analytics/
│
├── README.md
│
├── docs/
│   ├── data-dictionary.md
│   ├── analysis-plan.md
│   └── portfolio-checklist.md
│
├── analysis/
│   └── analysis_template.py
│
└── data/
    └── .gitkeep
```

## 6. Project Workflow

The following workflow describes the steps required to complete and reproduce the analysis:

1. **Report Inspection** — Review the original Power BI report and identify its visual components and analytical fields.
2. **Data Validation** — Verify data sources, table relationships, column definitions, and calculated measures.
3. **Data Preparation** — Export an approved dataset or prepare a clearly documented synthetic dataset.
4. **Exploratory Data Analysis** — Examine sales, gross profit, product categories, geographic distribution, and time-based trends.
5. **Data Visualization** — Develop interactive Power BI dashboards to communicate analytical results.
6. **Business Insights** — Identify meaningful patterns and translate validated findings into actionable recommendations.
7. **Portfolio Documentation** — Document the analytical process, findings, limitations, and supporting visualizations.

## 7. Expected Analytical Outcomes

Once the underlying dataset has been validated, the project aims to deliver:

- **Sales Performance Analysis:** Understand sales contributions across product categories.
- **Profitability Analysis:** Evaluate gross profit distribution and identify strong-performing categories.
- **Geographic Analysis:** Explore differences in sales and quantity across states.
- **Time-Series Analysis:** Examine sales and gross profit trends over daily, monthly, quarterly, and yearly periods.
- **Product Analysis:** Investigate sub-category performance to identify areas for further analysis.

*These are the intended analytical outcomes, not verified findings from the original dataset.*

## 8. How to Reproduce and Complete the Project

1. Open the original `.pbix` file using Power BI Desktop.
2. Verify data-source permissions and confirm whether the dataset can be redistributed.
3. Export an approved, non-sensitive dataset in CSV format, or prepare a documented synthetic dataset.
4. Validate table relationships, data types, and measures in Power BI.
5. Capture dashboard screenshots and save them in an `images/` directory.
6. Complete the analysis using actual validated data.
7. Document findings with supporting metrics, visualizations, and business recommendations.
8. Publish the Power BI report only when the necessary permissions are available.

## 9. Data Privacy & Publishing Disclaimer

This repository is intended for educational and professional portfolio purposes.

- Do not publish confidential, customer-level, licensed, or restricted business data.
- Remove sensitive information before sharing dashboard screenshots.
- Use synthetic data when the original dataset cannot be redistributed.
- Clearly distinguish synthetic results from findings based on actual business data.
- Do not report unverified KPI values or business conclusions.

## 10. Author

**Reza Pangestu**

Data Analytics & Business Intelligence Portfolio

- GitHub: [RezaPutra14](https://github.com/RezaPutra14)
- Project Repository: [Retail Insights & Analytics](https://github.com/RezaPutra14/retail-insights-analytics)
- LinkedIn: [Reza Pangestu](https://www.linkedin.com/in/reza-pangestu-sukarno-putra-03571636b/)
- Email: rezasukarno14@gmail.com

---

*This project is part of my Data Analytics portfolio, demonstrating my approach to business intelligence, data visualization, and analytical problem-solving using Power BI.*
