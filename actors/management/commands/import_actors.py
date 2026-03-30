# Comandos personalizados

# Importando o arquivo nativo CSV
import csv

# Importando o formato de data
from datetime import datetime

# Para utilização é necessário importar a base de comandos "baseCommand"
from django.core.management.base import BaseCommand

# Importando o model de actors para realizar o cadastro
from actors.models import Actor


# Criação da Classe padrão
class Command(BaseCommand):
    
    # Utilizando um argumento:
    def add_arguments(self, parser):
        parser.add_argument(
            'file_name',
            type=str,
            help='Nome do arquivo CSV atores',
        )
    
    def handle(self, *args, **options):
        # com o argumento:
        file_name = options['file_name']
        
        with open(file_name, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                name = row['Name']
                birthday = datetime.strptime(row['Birthday'], '%Y-%m-%d').date()
                nationality = row['Nationality']
                
                # Exibição do nome do ator no momento da captura
                self.stdout.write(self.style.NOTICE(name))
                
                Actor.objects.create(
                    name=name,
                    birthday=birthday,
                    nationality=nationality, 
                )
        
        # exibindo uma mensagem de command
        self.stdout.write(self.style.SUCCESS('Atores importados com sucesso'))        