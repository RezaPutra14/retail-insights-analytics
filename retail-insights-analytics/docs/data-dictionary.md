# Data Dictionary (initial)

This dictionary is based on fields referenced by the Power BI report visuals. It is not a substitute for inspecting the actual source tables and model.

| Table/entity | Field | Business meaning | Validation needed |
|---|---|---|---|
| `sales_details` | `Sales` | Sales amount/value | Currency, precision, nulls, aggregation rule |
| `sales_details` | `Gross_Profit` | Gross profit amount | Currency, precision, nulls, calculation definition |
| `sales_details` | `Quantity` | Units/items sold | Integer/decimal, returns/negative values |
| `product_details` | `Category` | Product category | Category list, blanks, naming consistency |
| `product_details` | `Sub-Category` | Product sub-category | Category hierarchy and naming consistency |
| `Place_details` | `State` | Sales geography/state | Country context, spelling and geographic mapping |
| `order_details` | `Order Date` | Order transaction date | Date type, timezone, date range |

## Model checks to complete

- Confirm primary keys and foreign keys for each dimension/fact table.
- Confirm relationship cardinality and filter direction.
- Confirm whether `Sales`, `Gross_Profit`, and `Quantity` are raw columns or measures.
- Document currency and whether gross profit includes discounts, shipping, or other costs.
- Check duplicate orders, missing dates, null categories, returns, and negative quantities.
- Record dataset source, license, date range, and row counts.
