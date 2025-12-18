# Ascend Data Systems Analyst – Pre-Work Submission

This repository contains my submission for the Ascend Public Charter Schools  
**Data Systems Analyst pre-work assignment**.

The goal of this work was to evaluate the current state of a staff access dataset, identify data quality and access issues, and propose a scalable approach for cleaning, validating, and maintaining accurate access data across systems.

---

## Repository Contents

- **main.py**  
  Python script using `pandas` to:
  - Normalize job titles
  - Identify missing access fields (username/email)
  - Detect permission mismatches between expected and actual access
  - Report counts and affected Excel row numbers for review

- **Data Systems Analyst Task.xlsx**  
  Dataset provided as part of the pre-work assignment.

- **Writeup.(pdf/docx)**  
  Written analysis addressing:
  - Current state of the data
  - Trends and high-level takeaways
  - Data cleaning and preparation approach
  - Recommendations to prevent dirty data in the future
  - A high-level implementation plan

---

## Summary of Approach

The analysis focuses on two primary data quality risks:

1. **Missing identity/access fields**  
   Records missing required fields such as username or email, which would block authentication and downstream provisioning.

2. **Permission mismatches**  
   Records where the assigned permissions (teacher / behavior / counselor) do not align with expectations inferred from job titles.

The Python script programmatically surfaces these issues, including:
- Total counts
- Lists of affected Excel row numbers
- Separation of clean vs. not-clean records

This approach allows issues to be reviewed, validated, and corrected without making unsafe assumptions or silently overwriting data.

---

## How to Run the Analysis

Requirements:
- Python 3.x
- pandas

Run the script from the project directory:

```bash
python3 main.py
