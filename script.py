import mysql.connector as mysql
import string
import random
from faker import Faker
from datetime import datetime, timedelta
faker = Faker(locale='pt-BR')


db_connection = mysql.connection.MySQLConnection(
    host='localhost',
    user='root',
    password='4rth1802',
    database='projeto_queijosFinos'
)

cursor = db_connection.cursor()

tecnologias = ["Cheddar","Gouda","Brie","Parmesão","Roquefort","Mozzarella","Gorgonzola","Feta","Camembert","Provolone",
    "Emmental","Queijo de cabra","Queijo de ovelha","Queijo de cabra","Requeijão","Ricota","Cottage","Queijo Azul","Queijo Coalho",
    "Queijo Canastra","Queijo Minas","Queijo Serra da Estrela","Queijo Gruyère","Queijo Gouda","Queijo Edam","Queijo Gruyère",
    "Queijo Parmesão","Queijo Gouda","Queijo Boursin","Queijo Feta","Queijo Taleggio","Queijo Stilton","Queijo Roquefort","Queijo Camembert",
    "Queijo de Cabra","Queijo de Azeitão","Queijo do Reino","Queijo Prato","Queijo Mussarela","Queijo Gouda","Queijo Coalho",
    "Queijo Canastra","Queijo Minas","Queijo Serra da Estrela","Queijo Gruyère","Queijo Gouda","Queijo Edam","Queijo Gruyère",
    "Queijo Parmesão","Queijo Gouda","Queijo Boursin","Holandesa","Jersey","Guzerá","Sindi","Nelore","Caracu",
    "Tabapuã","Girolando","Simental","Brahman","Bonsmara","Senepol","Angus","Hereford","Red Angus","Santa Gertrudis","Mestiça","Pardo Suíço",
    "Gir Leiteiro","Normando","Pitangueiras","Canchim","Limousin","Marchigiana","Braford","Simbrasil","Charolesa","Zebu",
    "Brangus","Simental", "Brahman","Bonsmara","Senepol","Angus","Hereford","Red Angus","Santa Gertrudis","Mestiça","Pardo Suíço",
    "Gir Leiteiro","Normando","Pitangueiras","Canchim","Limousin","Marchigiana","Braford","Simbrasil","Charolesa","Zebu"
]
nichos_de_fornecedores = ["Fornecedores de leite cru","Fornecedores de leite pasteurizado","Fornecedores de culturas lácticas","Fornecedores de coalho",
    "Fornecedores de fermento","Fornecedores de sal","Fornecedores de prensas de queijo","Fornecedores de formas de queijo",
    "Fornecedores de tanques de fermentação","Fornecedores de equipamentos de resfriamento de leite","Fornecedores de equipamentos de aquecimento de leite",
    "Fornecedores de equipamentos de pasteurização","Fornecedores de máquinas de ordenha","Fornecedores de tanques de armazenamento de leite",
    "Fornecedores de queijarias modulares","Fornecedores de sistemas de controle de temperatura","Fornecedores de sistemas de limpeza CIP (Cleaning-in-Place)",
    "Fornecedores de embalagens para queijo","Fornecedores de etiquetas personalizadas","Fornecedores de sistemas de rastreabilidade",
    "Fornecedores de equipamentos de corte e embalagem","Fornecedores de máquinas de envase","Fornecedores de sistemas de transporte interno",
    "Fornecedores de análise laboratorial de leite e queijo","Fornecedores de sistemas de tratamento de água","Fornecedores de aditivos alimentares",
    "Fornecedores de produtos de limpeza e sanitização","Fornecedores de uniformes e equipamentos de proteção individual (EPIs)","Fornecedores de consultoria em produção de queijo",
    "Fornecedores de treinamento em técnicas de fabricação de queijo","Fornecedores de serviços de certificação e qualidade","Fornecedores de sistemas de gestão de produção",
    "Fornecedores de sistemas de gestão de estoque","Fornecedores de sistemas de gestão de vendas","Fornecedores de sistemas de gestão financeira",
    "Fornecedores de soluções de embalagem sustentável","Fornecedores de energia renovável","Fornecedores de seguro para indústria de laticínios",
    "Fornecedores de transporte refrigerado","Fornecedores de logística de distribuição","Fornecedores de tecnologia de embalagem a vácuo",
    "Fornecedores de equipamentos de transporte de queijo","Fornecedores de equipamentos de inspeção de qualidade",
    "Fornecedores de equipamentos de análise de textura","Fornecedores de equipamentos de análise de umidade",
    "Fornecedores de sistemas de purificação de ar","Fornecedores de sistemas de controle de umidade","Fornecedores de sistemas de tratamento de efluentes",
    "Fornecedores de tecnologia de resfriamento rápido","Fornecedores de sistemas de embalagem a vácuo"
]


def gerar_senha(tamanho=12):
    caracteres = string.ascii_letters + string.digits
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha


def url_aleatoria():

    # Função para gerar uma string aleatória de comprimento especificado
    def generate_random_string(length):
        letters_and_digits = string.ascii_letters + string.digits
        return ''.join(random.choice(letters_and_digits) for _ in range(length))

    # Domínios de exemplo
    dominios = ['example.com', 'example.org', 'example.net']

    # Gerar um domínio aleatório
    dominio_aleatorio = random.choice(dominios)

    # Gerar caminho aleatório (comprimento entre 1 e 10 segmentos)
    caminho_aleatorio = '/'.join(generate_random_string(random.randint(1, 10)) for _ in range(random.randint(1, 5)))

    # Montar a URL
    url_aleatoria = f'http://{dominio_aleatorio}/{caminho_aleatorio}'

    # Exibir a URL aleatória gerada
    return url_aleatoria


def data_aleatoria():
    data_inicial = datetime(2010, 1, 1)
    data_final = datetime.now()

    diferenca = data_final - data_inicial

    dias_aleatorios = random.randint(0, diferenca.days)

    data_aleatoria = data_inicial + timedelta(days=dias_aleatorios)

    return data_aleatoria


def generate_cpf():
    cpf = [random.randint(0, 9) for x in range(9)]

    for _ in range(2):
        val = sum([(len(cpf) + 1 - i) * v for i, v in enumerate(cpf)]) % 11

        cpf.append(11 - val if val > 1 else 0)

    return '%s%s%s.%s%s%s.%s%s%s-%s%s' % tuple(cpf)


def generate_cnpj():
    def calculate_special_digit(l):
        digit = 0

        for i, v in enumerate(l):
            digit += v * (i % 8 + 2)

        digit = 11 - digit % 11

        return digit if digit < 10 else 0

    cnpj = [1, 0, 0, 0] + [random.randint(0, 9) for x in range(8)]

    for _ in range(2):
        cnpj = [calculate_special_digit(cnpj)] + cnpj

    return '%s%s.%s%s%s.%s%s%s/%s%s%s%s-%s%s' % tuple(cnpj[::-1])


def propriedade_n_1():
    cursor.execute("select max(id_propriedade) from propriedade ")

    for id in cursor:
        ultimo_id = id
        ultimo_id = int(ultimo_id[0])

    for i in range(1000000):
        # PROPRIEDADES----------------------------------------
        print('Inserindo propriedade')
        ultimo_id += 1
        endereco1_parts = faker.address().split('\n')
        endereco1_ultima_parte = endereco1_parts[-1].split(' / ')
        logradouro = endereco1_parts[0]
        bairro = endereco1_parts[1]
        cidade = endereco1_ultima_parte[0][9:]
        estado = endereco1_ultima_parte[1]
        latitude = random.uniform(-24.474888, -24.896904)
        longitude = random.uniform(-53.606572, -54.021158)

        nome_proprieade = faker.company()

        sql_query = ("insert into propriedade (`nome_propriedade`, `email`, `status`, `CPF`, `CNPJ`, `telefone`, `celular`, "
                     "`rua`, `bairro`, `cidade`, `UF`, `latitude`, `longitude`, `nome_produtor`) "
                     "values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")


        params = [nome_proprieade, (faker.name() + "@gmail.com").replace(" ", "."), random.randint(0, 2), generate_cpf(), generate_cnpj(),
                  faker.phone_number(), faker.phone_number(), logradouro, bairro, cidade, estado, latitude, longitude,
                  faker.name()]


        cursor.execute(sql_query, params)
        db_connection.commit()

        # CONTRATOS---------------------------------------
        print('Inserindo contrato')
        sql_query = "insert into contrato (`nome`, `data_emissao`, `data_vercimento`, `propriedade_id_propriedade`)values (%s,%s,%s,%s)"

        params = ['Contrato da '+nome_proprieade, data_aleatoria(), data_aleatoria(), ultimo_id]

        cursor.execute(sql_query, params)

        # IMAGENS-----------------------------------------
        for j in range(10):
            print('Inserindo imagem: ' + str(j))
            sql_query = "insert into imagem (`url`, `propriedade_id_propriedade`)values (%s,%s)"

            params = [url_aleatoria(), ultimo_id]
            cursor.execute(sql_query, params)

        for k in range(20):
            print('Inserindo amostra: ' + str(k))
            sql_query = "insert into amostra (`data`, `quantidade_queijo`, `quantidadeleite`, observacao, `propriedade_id_propriedade`)values (%s,%s, %s, %s, %s)"

            params = [data_aleatoria(), round(random.uniform(1, 20), 2), round(random.uniform(1, 20), 2), faker.text(), ultimo_id]
            cursor.execute(sql_query, params)

        print("Quantidade de loop: " + str(i))
        db_connection.commit()


def n_nTables():
    for i in range(100):
        # CURSOS----------------------------------------
        print('Inserindo curso')

        sql_query = ("insert into curso (`nome`, `duracao`, `conteudo`, `professor`) "
                     "values (%s,%s,%s,%s)")
        params = ["Curso do " + faker.name(), str(random.randint(0, 60)) + " semanas", faker.text(), faker.name()]

        cursor.execute(sql_query, params)

        # TECNOLOGIAS---------------------------------------
        print('Inserindo tecnologia')
        sql_query = ("insert into tecnologias (`nome`, `observacao`) "
                     "values (%s,%s)")

        params = [tecnologias[i], faker.text()]

        cursor.execute(sql_query, params)

        # FORNECEDOR-----------------------------------------
        print('Inserindo fornecedor')
        sql_query = ("insert into fornecedor (`nome`, `nicho`, `email`, `qualidade`) "
                     "values (%s,%s,%s,%s)")

        nome_fornecedor = faker.company()
        randNicho = random.randint(0, 49)

        params = [nome_fornecedor, nichos_de_fornecedores[randNicho], (nome_fornecedor + "@gmail.com").replace(" ", "."), random.randint(0, 4)]

        cursor.execute(sql_query, params)

        db_connection.commit()

def usuarios():
    for i in range(100):
        # USUARIOS----------------------------------------
        print('Inserindo usuario')

        sql_query = ("insert into usuarios (`email`, `nome`, `senha`) "
                     "values (%s,%s,%s)")

        nome_usuario = faker.name()
        params = [(nome_usuario + "@gmail.com").replace(" ", "."), nome_usuario, gerar_senha()]

        cursor.execute(sql_query, params)

        db_connection.commit()


def ligacaoFornecedor():
    cursor.execute("select max(id_propriedade) from propriedade ")

    for id in cursor:
        ultimo_id = id
        ultimo_id_propriedade = int(ultimo_id[0])

    cursor.execute("select min(id_propriedade) from propriedade ")

    for id in cursor:
        ultimo_id = id
        primeiro_id_propriedade = int(ultimo_id[0])

    cursor.execute("select max(id) from fornecedor ")

    for id in cursor:
        ultimo_id = id
        ultimo_id_fornecedor = int(ultimo_id[0])

    cursor.execute("select min(id) from fornecedor ")

    for id in cursor:
        ultimo_id = id
        primeiro_id_fornecedor = int(ultimo_id[0])


    while primeiro_id_propriedade <= ultimo_id_propriedade:
        ultimos_id = []

        for j in range(10):
            flag = 1
            sql = ("insert into fornecedor_has_propriedade (propriedade_id_propriedade, fornecedor_id_fornecedor)"
                   "values (%s, %s)")

            while flag == 1:
                flag = 0
                id_fornecedor = random.randint(primeiro_id_fornecedor, ultimo_id_fornecedor)

                for id in ultimos_id:
                    if id == id_fornecedor:
                        flag = 1

            ultimos_id.append(id_fornecedor)
            params = [primeiro_id_propriedade, id_fornecedor]
            cursor.execute(sql, params)

        primeiro_id_propriedade += 1
        print("Relacionamento feito fornecedor")
        db_connection.commit()


def ligacaoTecnologias():
    cursor.execute("select max(id_propriedade) from propriedade ")

    for id in cursor:
        ultimo_id = id
        ultimo_id_propriedade = int(ultimo_id[0])

    cursor.execute("select min(id_propriedade) from propriedade ")

    for id in cursor:
        ultimo_id = id
        primeiro_id_propriedade = int(ultimo_id[0])

    cursor.execute("select max(id) from tecnologias ")

    for id in cursor:
        ultimo_id = id
        ultimo_id_tecnologia= int(ultimo_id[0])

    cursor.execute("select min(id) from tecnologias ")

    for id in cursor:
        ultimo_id = id
        primeiro_id_tecnologia = int(ultimo_id[0])


    while primeiro_id_propriedade <= ultimo_id_propriedade:
        ultimos_id = []

        for j in range(10):
            flag = 1
            sql = ("insert into tecnologia_has_propriedade (propriedade_id_propriedade, tecnologia_id_tecnologia, data_insercao)"
                   "values (%s, %s, %s)")

            while flag == 1:
                flag = 0
                id_tecnologia = random.randint(primeiro_id_tecnologia, ultimo_id_tecnologia)

                for id in ultimos_id:
                    if id == id_tecnologia:
                        flag = 1

            ultimos_id.append(id_tecnologia)
            params = [primeiro_id_propriedade, id_tecnologia, data_aleatoria()]
            cursor.execute(sql, params)

        primeiro_id_propriedade += 1
        print("Relacionamento feito tecnologia")
        db_connection.commit()


def ligacaoCurso():
    cursor.execute("select max(id_propriedade) from propriedade ")

    for id in cursor:
        ultimo_id = id
        ultimo_id_propriedade = int(ultimo_id[0])

    cursor.execute("select min(id_propriedade) from propriedade ")

    for id in cursor:
        ultimo_id = id
        primeiro_id_propriedade = int(ultimo_id[0])

    cursor.execute("select max(id) from curso ")

    for id in cursor:
        ultimo_id = id
        ultimo_id_curso = int(ultimo_id[0])

    cursor.execute("select min(id) from curso ")

    for id in cursor:
        ultimo_id = id
        primeiro_id_curso = int(ultimo_id[0])


    while primeiro_id_propriedade <= ultimo_id_propriedade:
        ultimos_id = []

        for j in range(10):
            flag = 1
            sql = ("insert into propriedade_has_curso (propriedade_id_propriedade, curso_id_curso, data_inicio, data_conclusao)"
                   "values (%s, %s, %s, %s)")

            while flag == 1:
                flag = 0
                id_curso = random.randint(primeiro_id_curso, ultimo_id_curso)

                for id in ultimos_id:
                    if id == id_curso:
                        flag = 1

            ultimos_id.append(id_curso)
            data_inicio = data_aleatoria()
            data_conclusao = data_aleatoria()

            while data_conclusao < data_inicio:
                data_conclusao = data_aleatoria()

            params = [primeiro_id_propriedade, id_curso, data_inicio, data_conclusao]
            cursor.execute(sql, params)

        primeiro_id_propriedade += 1
        print("Relacionamento feito curso")
        db_connection.commit()








# INICIANDO REGISTRO DE PROPRIEDADE
# endereco_parts = faker.address().split('\n')
# endereco_ultima_parte = endereco_parts[-1].split(' / ')
# logradouro = endereco_parts[0]
# bairro = endereco_parts[1]
# cidade = endereco_ultima_parte[0][9:]
# estado = endereco_ultima_parte[1]
# latitude = random.uniform(-24.474888, -24.896904)
# longitude = random.uniform(-53.606572, -54.021158)
#
# nome_proprieade = faker.company()
#
# sql_query = ("insert into propriedade (`nome_propriedade`, `email`, `status`, `CPF`, `CNPJ`, `telefone`, `celular`, "
#             "`rua`, `bairro`, `cidade`, `UF`, `latitude`, `longitude`, `nome_produtor`) "
#             "values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")
#
#
# params = [nome_proprieade, (faker.name() + "@gmail.com").replace(" ", "."), random.randint(0, 2), generate_cpf(), generate_cnpj(),
#          faker.phone_number(), faker.phone_number(), logradouro, bairro, cidade, estado, latitude, longitude,
#          faker.name()]
#
#
# cursor.execute(sql_query, params)
# db_connection.commit()
#
# propriedade_n_1()
# n_nTables()
# usuarios()


# ligacaoFornecedor()
# ligacaoTecnologias()
ligacaoCurso()

db_connection.close()
