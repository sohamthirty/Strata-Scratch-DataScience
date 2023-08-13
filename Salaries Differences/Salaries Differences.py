# Import your libraries
import pandas as pd

# merge the two dataframes
data = db_employee.merge(db_dept, left_on='department_id', right_on='id', how='inner')

# difference between highest salaries b/w marketing and engineering
highest_marketing = data.loc[data.department=='marketing', 'salary'].max()
highest_engineering = data.loc[data.department=='engineering', 'salary'].max()

# Output
highest_marketing-highest_engineering