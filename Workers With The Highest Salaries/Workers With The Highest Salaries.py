# Import your libraries
import pandas as pd

# dataframe containing rows having max salary
worker_max = worker[worker.salary == worker.salary.max()]

# merge dataframes worker & title
data = worker_max.merge(title, left_on='worker_id', right_on='worker_ref_id',how='inner')['worker_title']

# Output
data