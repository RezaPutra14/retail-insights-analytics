# Retail Insights & Analytics — Power BI Portfolio

An end-to-end business intelligence portfolio project focused on exploring sales performance, gross profit, product categories, geographic distribution, and sales trends over time.

> **Project status:** Portfolio documentation scaffold created from the structure of the supplied Power BI report (`.pbix`). The original embedded data model is stored in Power BI's XPress9-compressed format and has not been independently extracted or validated here. Therefore, this repository does not publish source records, KPI values, or numerical business conclusions. Add approved/exported data and dashboard screenshots before presenting quantified findings.

## Business objective

Provide a concise view of sales performance to help stakeholders understand:
- Which product categories contribute most to sales and gross profit?
- How does sales performance vary by state?
- How do sales and gross profit change over time?
- Which sub-categories and geographic areas warrant further investigation?

## Dashboard overview

The supplied report contains one report page with eight visual elements:

| Visual | Analysis focus | Fields identified in report |
|---|---|---|
| KPI | Sales by product category | `Category`, `Sales` |
| KPI | Gross profit by category | `Gross_Profit`, `Category` |
| Bar chart | Sales by state and category | `Sales`, `State`, `Category` |
| Combo chart | Sales and gross profit over time | `Order Date` (Year/Quarter/Month/Day), `Sales`, `Gross_Profit` |
| Area chart | Monthly sales trend | `Sales`, `Order Date Month` |
| Multi-row card | Category-level performance | `Category`, `Gross_Profit`, `Quantity`, `Sales` |
| Filled map | Quantity by state | `State`, `Quantity` |
| Slicer | Sub-category filter | `Sub-Category` |

## Tools & skills

- **Power BI** — dashboard design, interactive filtering, KPI reporting, geographic and time-series visuals.
- **Data analysis** — sales, gross profit, quantity, product-category and regional analysis.
- **Business communication** — translating dashboard views into stakeholder-oriented questions and recommendations.

## Data model: fields observed

The report references these entities/tables:
- `sales_details`
- `product_details`
- `Place_details`
- `order_details`

Fields visible in report queries:
- Measures/columns: `Sales`, `Gross_Profit`, `Quantity`
- Product: `Category`, `Sub-Category`
- Geography: `State`
- Date: `Order Date`

The exact relationships, calculated measures, data types, row counts, refresh history, and source provenance should be documented from Power BI Model view / Power Query before publishing.

## Repository structure

```text
.
├── README.md
├── docs/
│   ├── data-dictionary.md
│   ├── analysis-plan.md
│   └── portfolio-checklist.md
└── analysis/
    └── analysis_template.py
```

## How to reproduce and complete the project

1. Open the original `.pbix` file in Power BI Desktop.
2. Confirm data source permissions and whether the dataset may be redistributed.
3. Export an approved, non-sensitive data extract (CSV) or provide a documented synthetic dataset.
4. Validate relationships and measures in Model view.
5. Capture clear screenshots of the dashboard and add them under `images/`.
6. Complete the analysis plan with actual findings, supporting values, and business recommendations.
7. Publish the report to Power BI Service only if permitted; otherwise include screenshots and the `.pbix` file only when redistribution is allowed.

## Important publishing note

Do not upload customer-level, confidential, licensed, or otherwise restricted data to a public GitHub repository. If the original dataset cannot be shared, publish screenshots with sensitive details removed and use a clearly labelled synthetic dataset for reproducible code examples. Never present synthetic results as findings from the original report.

## Author

**Reza Pangestu**

Add your LinkedIn profile, email, and Power BI report link here if you want them public.
