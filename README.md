# Cleaned Sales Dataset

## Overview
This dataset contains cleaned sales transaction records, with missing values and errors handled for accurate analysis.

## Cleaning Steps
1. Standardized column names: lowercase, no spaces or parentheses.  
2. Replaced "UNKNOWN", "ERROR", and blanks with NaN.  
3. Converted `quantity` and `total_spent` to numeric; `transaction_date` to datetime.  
4. Cleaned categorical columns (`item`, `payment_method`, `location`) with title case and filled missing as "Unknown".  
5. Corrected `total_spent` = `quantity * price_per_unit`. Dropped rows with missing critical values.

## Columns
- `transaction_date` (datetime)  
- `item` (string)  
- `quantity` (numeric)  
- `price_per_unit` (numeric)  
- `total_spent` (numeric)  
- `payment_method` (string)  
- `location` (string)

## Summary
- Shape: `(9, 8)`   
- No missing values in critical columns (`quantity`, `price_per_unit`, `total_spent`)


