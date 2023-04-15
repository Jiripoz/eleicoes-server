from flask import jsonify, request, Response
from src.controller.sql_controller import SQLController
import pandas as pd 


def setup_routes(app, controller: SQLController):
    @app.route("/city-list")
    def get_city_list():
        year = request.args.get('y')
        print("entered get_city_list function, query parameter:", year)
        
        query = controller.select.city_list(year)
        df = pd.DataFrame(query, columns=["cidades"])
        print(df)
        response = Response(
            response = df.to_json(orient='records', force_ascii=False),
            status = 200,
            mimetype= 'application/json'
        )
        return response
    
    @app.route("/city-data")
    def get_city_data():
        city = request.args.get('c')
        year = request.args.get('y')
        query = controller.select.city_data(city, year)
        df = pd.read_sql(query, controller.conn)

        return jsonify(df.to_json(orient='records'))
