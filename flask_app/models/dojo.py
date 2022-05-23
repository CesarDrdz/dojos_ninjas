from flask_app.config.mysqlconnection import connectToMySQL

from flask_app.models.ninja import Ninja

DATABASE = 'dojo_ninjas'

class Dojo:
    def __init__(self, data:dict) -> None:
        self.id = data['id']
        self.name = data['name']
        self.ninjas = []
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    # ! CREATE
    @classmethod
    def save(cls, data:dict) -> int:
        query = "INSERT INTO dojos (name) VALUES (%(name)s);"
        result = connectToMySQL(DATABASE).query_db(query,data)
        return result

    # ! READ/RETRIEVE ALL
    @classmethod
    def get_all(cls) -> list:
        query = "SELECT * FROM dojos;"
        results = connectToMySQL(DATABASE).query_db(query)
        dojos = []
        for u in results:
            dojos.append( cls(u) )
        return dojos
    
    # ! READ/RETRIEVE ONE
    @classmethod
    def get_one(cls,data:dict) -> object:
        query  = "SELECT * FROM dojos WHERE id = %(id)s;"
        result = connectToMySQL(DATABASE).query_db(query,data)
        return cls(result[0])
   
    @classmethod
    def get_one_with_ninjas(cls,data:dict) -> object:
        query  = "SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query,data)
        dojo = cls(results[0])
        for result in results:
            ninja_dict = {
                'id': result['ninjas.id'],
                'first_name': result['first_name'],
                'last_name': result['last_name'],
                'age': result['age'],
                'dojo_id': result['dojo_id'],
                'created_at': result['ninjas.created_at'],
                'updated_at': result['ninjas.updated_at']
            }
            dojo.ninjas.append(Ninja(ninja_dict))
        return dojo

    # ! UPDATE
    @classmethod
    def update(cls,data:dict) -> int:
        query = "UPDATE dojos SET name=%(name)s WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query,data)

    # ! DELETE
    @classmethod
    def destroy(cls,data:dict):
        query  = "DELETE FROM dojos WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query,data)