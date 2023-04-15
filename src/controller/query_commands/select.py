class Select:
    def __init__(self,cur):
        self.cur = cur

    def city_data(self, city, year):
        table = 'eleicoes'+str(year)
        query_result = self.cur.execute(f"SELECT * FROM {table} WHERE NM_MUNICIPIO = '{city}'")
        return query_result
    
    def city_list(self, year):
        table = 'eleicoes'+str(year)
        self.cur.execute(f"SELECT DISTINCT NM_MUNICIPIO FROM {table}")
        query_result = self.cur.fetchall()
        return query_result