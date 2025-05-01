import json
import os
import sys
from singleton.singleton_meta import SingletonMeta

class Config(metaclass=SingletonMeta):

    def create_config():
        
        default_config = {
            "credentials": {
                "email": "seu_email@exemplo.com",
                "password": "sua_senha"
            },
            "target_criteria": {
                "role": "Desenvolvedor",
                "keywords": "Python React",
                "empresa": "",
                "localização": "Brasil"
            },
            "settings": {
                "daily_connections": 15,
                "min_likes": 10,
                "max_likes": 25,
                "headless_mode": false
            }
        }
                
        with open('config.json', 'w') as f:
            json.dump(default_config, f, indent=4)
        
        print("Arquivo config.json criado. Por favor, edite-o com suas credenciais e preferências.")
        sys.exit(1)


    def load_config(self):
        """Carrega configurações do arquivo config.json"""
        try:
            if os.path.exists('config.json'):
                with open('config.json', 'r') as f:
                    return json.load(f)
            else:
                print("Arquivo de configuração não encontrado!")
                print("Criando arquivo de configuração padrão...")
                self.create_config()
                
        except Exception as e:
            print(f"Erro ao carregar configurações: {e}")
            sys.exit(1)

config = Config().load_config()