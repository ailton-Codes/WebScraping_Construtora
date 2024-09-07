import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL do endpoint da API identificada
api_url = "https://mac.com.br/wp-content/themes/template-wp-mac/internit-search-form/product/product.php"

# Cabeçalhos necessários
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'https://mac.com.br',
    'Referer': 'https://mac.com.br/empreendimentos/',
}

# Parâmetros da requisição POST (ajuste conforme necessário)
payload = {
    "search": None,
    "stage": "",
    "dormitories": "",
    "region": "",
    "price": "",
    "leisure": ""
}

# Enviando a requisição POST
response = requests.post(api_url, headers=headers, data=payload)

# Verificando se a requisição foi bem-sucedida
if response.status_code == 200:
    content = response.text
else:
    print(f"Erro na requisição: {response.status_code}")
    exit()

# Criar o objeto BeautifulSoup para parsear o HTML
soup = BeautifulSoup(content, 'html.parser')

# Listas para armazenar os dados
empreendimentos = []
enderecos = []
regiao = []
informacoes = []
status_obra = []

# Encontrar todos os blocos de empreendimento
blocos = soup.find_all('div', class_='mac__enterprises-items--item')

# Iterar sobre os blocos e extrair os dados
for bloco in blocos:
    # Nome do empreendimento
    nome = bloco.find('h2', class_='mac__enterprises-name').get_text(strip=True)
    
    # Encontrar os itens dentro do wrapper
    itens_informacoes = bloco.find_all('p', class_='mac__enterprises-text')
    
    # Extraindo as informações conforme a ordem esperada
    if len(itens_informacoes) >= 1:
        endereco = itens_informacoes[0].get_text(strip=True)
    else:
        endereco = "N/A"
    
    # Para garantir que todas as informações sejam capturadas, verificaremos até 4 informações adicionais
    if len(itens_informacoes) >= 2:
        info_1 = itens_informacoes[1].get_text(strip=True)
    else:
        info_1 = "N/A"
    
    if len(itens_informacoes) >= 3:
        info_2 = itens_informacoes[2].get_text(strip=True)
    else:
        info_2 = "N/A"
    
    if len(itens_informacoes) >= 4:
        info_3 = itens_informacoes[3].get_text(strip=True)
    else:
        info_3 = "N/A"
    
    
    # Adicionar os dados às listas
    empreendimentos.append(nome)
    enderecos.append(endereco)
    regiao.append(info_1)
    informacoes.append(info_2)
    status_obra.append(info_3)

# Criar o DataFrame com os dados extraídos
df = pd.DataFrame({
    'Empreendimento': empreendimentos,
    'Endereço': enderecos,
    'Região': regiao,  
    'Informações': informacoes,  # Pode ser Status da Obra ou outra informação
    'Status Obra': status_obra
})

# Exibir o DataFrame no console
print(df)

# Exportar para CSV e Excel
df.to_csv('empreendimentos.csv', index=False)

# Mostrar sucesso na execução
print("Dados extraídos e salvos com sucesso!")