import pandas as pd

df = pd.read_excel("Data Systems Analyst Task.xlsx") # Load data

df["excel_row"] = df.index + 2 # Add 2 to account for header row and 0-based index

df["title_norm"] = df["title"].fillna("").astype(str).str.lower().str.strip() # Normalize title by filling NaNs, converting to string, lowering case, and stripping spaces

# Expected permissions
df["expected_teacher"] = df["title_norm"].str.contains("teacher", na=False).astype(int) # If title contains "teacher" then expected_teacher is 1 else 0
df["expected_behavior"] = df["title_norm"].str.contains("dean", na=False).astype(int) # If title contains "dean" then expected_behavior is 1 else 0
df["expected_counselor"] = df["title_norm"].str.contains("director|counselor", na=False).astype(int) # If title contains "director" or "counselor" then expected_counselor is 1 else 0

# -- Missing Data -- 
# Check if Username or email is missing or blank then mark as missing data 
df["missing_data"] = ( 
    df["Username"].fillna("").astype(str).str.strip().eq("") | 
    df["email"].fillna("").astype(str).str.strip().eq("") 
)

# Normalize permission columns
for col in ["teacher", "behavior", "counselor"]:
    df[col] = pd.to_numeric(df[col], errors="coerce").fillna(0).astype(int)

# -- Permission mismatch -- 
# Creates a boolean column indicating if there is a mismatch between actual and expected permissions based on title
df["permission_mismatch"] = (
    (df["teacher"] != df["expected_teacher"]) |
    (df["behavior"] != df["expected_behavior"]) |
    (df["counselor"] != df["expected_counselor"])
) 

# --- Grouping results ---
# Groups rows with permission mismatches and their corresponding excel row numbers
permission_issue_rows = df.loc[
    df["permission_mismatch"],
    "excel_row"
]

# Groups rows with missing data and their corresponding excel row numbers
missing_data_rows = df.loc[
    df["missing_data"],
    "excel_row"
]

# Groups rows that have both permission mismatches and missing data
both_issue_rows = df.loc[
    df["permission_mismatch"] & df["missing_data"],
    "excel_row"
]

# --- Output results ---
print("Total rows:", len(df) + 1) # print total number of rows processed (+1 for header)

# Prints count and sorted list of excel row numbers that have permission issues
print("\nPermission issues:")
print("Count:", len(permission_issue_rows))
print(sorted(permission_issue_rows.tolist()))

# Prints count and sorted list of excel row numbers that have missing data
print("\nMissing data:")
print("Count:", len(missing_data_rows))
print(sorted(missing_data_rows.tolist()))

# Prints count and sorted list of excel row numbers that have both permission issues and missing data
print("\nBoth permission issue AND missing data:")
print("Count:", len(both_issue_rows))
print(sorted(both_issue_rows.tolist()))

# print(df.columns.tolist()) # prints all column names for debugging
df.to_excel("output.xlsx", index=False)  # Prints the dataframe to an excel file for viewing