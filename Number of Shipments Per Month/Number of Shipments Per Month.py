# Import your libraries
import pandas as pd

# column to store the month
amazon_shipment['month'] = amazon_shipment['shipment_date'].dt.to_period('m')

# column for unique key
amazon_shipment['key'] = amazon_shipment['shipment_id'].astype(str) + amazon_shipment['sub_id'].astype(str)

# group by month and count key
amazon_shipment.groupby('month')['key'].count().reset_index()