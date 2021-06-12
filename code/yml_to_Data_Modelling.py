import sys
import os
import pandas as pd

if __name__ == '__main__':
    path2 = 'input/'
    filenames2 = []
    for file1 in os.listdir(path2):
        if file1.endswith(('.yaml')):
            filenames2.append(file1)
    filenames2.sort()
    for GCP_name_of_file in filenames2:
        yml_file = open(r"input/" + GCP_name_of_file)
        file_yml = yml_file.readlines()

        headerArr = []
        tableArr = []
        for iterations1 in file_yml:
            if 'header' in iterations1:
                tableNumber_initial = iterations1.replace("'header':", "'header'=")
                tableNumber = tableNumber_initial.split("=")
                tableNumber = tableNumber[1]
                tableNumber = str(tableNumber)
                remove_colon_tableNum = tableNumber.replace(":", "")
                remove_last_comma_tb_num = remove_colon_tableNum.replace(",\n", "")
                remove_first_commas_tb_num = remove_last_comma_tb_num.replace("'", "").upper()
                headerArr.append(remove_first_commas_tb_num)
            if 'bq.table' in iterations1:
                tableName_initial = iterations1.replace("'bq.table':", "'bq.table'=")
                tableName = tableName_initial.split("=")
                tableName = tableName[1]
                tableName = str(tableName)
                remove_colon_table = tableName.replace(":", "")
                remove_last_comma_tb = remove_colon_table.replace(",\n", "")
                remove_first_commas_tb = remove_last_comma_tb.replace("'", "").upper()
                tableArr.append(remove_first_commas_tb)

        df = pd.DataFrame({'TARGET_TABLE_NAME': tableArr, 'TABLE_NUMBER': headerArr})
        df.to_csv('out.csv', sep='|', index=False)
