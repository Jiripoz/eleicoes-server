import pandas as pd
import csv

class Insert:
    def __init__(self, cur) -> None:
        self.cur = cur
        
    
    def insert_csv_as_new_table(self, year):
        path = f'../csv/{year}.csv'
        df = pd.read_csv(path, encoding='latin1', nrows=0)
        header_raw = df.columns.tolist()
        header = [h.replace('"', '') for h in header_raw[0].split(';')]
        columns = ','.join([f"{col} VARCHAR(255)" for col in header])
        self.cur.execute(f"CREATE TABLE IF NOT EXISTS eleicoes{str(year)} ({columns})")
        with open(path, encoding='latin1') as f:
            reader = csv.reader(f)
            next(reader)
            for raw_row in reader:
                joined_row = ''.join([item for item in raw_row])
                row = [r.replace('"', '').replace("'", '') for r in joined_row.split(';')]
                try:
                    values = ','.join([f"'{val}'" for val in row])
                    self.cur.execute(f"INSERT INTO eleicoes2020 ({','.join(header)}) VALUES ({values})")
                except Exception as e:
                    print("erro:", e)
                    print(f"the number of entries in row is: {len(row)}")
                    print("the raw_row is: ", raw_row)
                    for entry in row:
                        print(entry)
                    continue

    def test_print(self):
        print("deu boa")