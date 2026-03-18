from django.db import models

# Criação das opções de nacionalidade - utilizando o modo "choice"
#(Campo exibido na lista, nome designado)
NATIONALITY_CHOICES = (
    ('BRA', 'Brasil'),
    ('ARG', 'Argentina'),
    ('USA', 'Estados Unidos'),
    ('CAN', 'Canadá'),
    ('MEX', 'México'),
    ('POR', 'Portugal'),
    ('ESP', 'Espanha'),
    ('FRA', 'França'),
    ('GER', 'Alemanha'),
    ('ITA', 'Itália'),
    ('GBR', 'Reino Unido'),
    ('JPN', 'Japão'),
    ('CHN', 'China'),
    ('RUS', 'Rússia'),
    ('IND', 'Índia'),
    ('AUS', 'Austrália'),
    ('ZAF', 'África do Sul'),
    ('EGY', 'Egito'),
    ('KOR', 'Coreia do Sul'),
    ('NGA', 'Nigéria'),
    ('COL', 'Colômbia'),
    ('CHI', 'Chile'),
    ('PER', 'Peru'),
    ('URU', 'Uruguai'),
    ('PAR', 'Paraguai'),
    ('BOL', 'Bolívia'),
    ('VEN', 'Venezuela'),
    ('ECU', 'Equador'),
    ('SWE', 'Suécia'),
    ('NOR', 'Noruega'),
    ('DEN', 'Dinamarca'),
    ('FIN', 'Finlândia'),
    ('NED', 'Países Baixos'),
    ('BEL', 'Bélgica'),
    ('SUI', 'Suíça'),
    ('AUT', 'Áustria'),
    ('POL', 'Polônia'),
    ('GRE', 'Grécia'),
    ('TUR', 'Turquia'),
    ('ISR', 'Israel'),
    ('SAU', 'Arábia Saudita'),
    ('UAE', 'Emirados Árabes Unidos'),
    ('THA', 'Tailândia'),
    ('VIE', 'Vietnã'),
    ('PHI', 'Filipinas'),
    ('NZL', 'Nova Zelândia'),
)

# Classe Ator
class Actor (models.Model):
    name = models.CharField(max_length=200)
    birthday = models.DateField(null=True, blank=True)
    nationality = models.CharField(
        max_length=100,
        choices=NATIONALITY_CHOICES,
        blank=True,
        null=True,
    )
    
    def __str__(self):
        return self.name