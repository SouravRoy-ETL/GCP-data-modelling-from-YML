# GCP-data-modelling-from-YML
> Creation of Data Modelling Sheet in an automated fashion from GCP Composer Airflow Variable setters. This activity has reduced dependency of Data Modelling Team to prepare Mapping Sheet from 100% to 0%. Thus, Making the development team to perform independently automate tasks end to end.

# Structure
TARGET_TABLE_NAME|TARGET_COLUMN_NAME_TARGET_DATA_TYPE

# Installation 
### ```` pip install pandas ````

# Build/Run Command
Use following commands to build/Run the project from the project root. 
This script accepts 1 input(YML) and generates 1 CSV Mapping Sheet

### Config YML File which contains (bq.Table, bq.dataset, etc)
````
python .\Script_name.py 
````
