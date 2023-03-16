import json

class vetement:
    def __init__(self):
        self.dictionnaire = {
            "marque": "nike",
            "prix": 15,
            "taille": "xS",
            "genre": "homme"
        }
    def get_dictionnaire(self):
        return self.dictionnaire
    
    def set_dictionnaire(self, nouveau_dictionnaire):
        self.dictionnaire = nouveau_dictionnaire
    
    def json_obj(self):
        objet_json = json.dumps(self.dictionnaire)
        print(objet_json)

vetement = vetement()
vetement.json_obj()
