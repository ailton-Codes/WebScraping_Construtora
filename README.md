# Web Scraping de Empreendimentos

## Projeto de Extração Automatizada de Dados de Empreendimentos

**Elaborado por:**  
Ailton Daniel Ferreira de Lima

**Data de Criação:**  
Setembro de 2024

---

## Descrição do Projeto

Este projeto foi desenvolvido para automatizar a extração de informações sobre alguns empreendimentos listados. Utilizando **web scraping**, o script coleta dados como nome do empreendimento, endereço, número de dormitórios, status da obra, entre outras informações, e os organiza em um formato estruturado para posterior análise. Os dados são exportados para arquivo CSV.

---

## Tecnologias Utilizadas

- **Linguagem de Programação:** Python 3.7+
- **Bibliotecas:**
  - requests
  - BeautifulSoup
  - pandas

---

## Objetivo

O principal objetivo deste projeto é automatizar a coleta de dados dos empreendimentos, organizando as informações para facilitar o processo de análise e tomada de decisões. O projeto permite exportar os dados para formatos CSV e Excel para uso em outras plataformas de análise.

---

## 1. Visão Geral do Projeto

Este projeto utiliza web scraping para extrair informações dos empreendimentos listados. Através de uma requisição POST, o conteúdo da página é carregado dinamicamente e o script processa o HTML, extraindo informações sobre cada empreendimento, como:
- Nome do empreendimento
- Endereço
- Dormitórios
- Status da obra
- Outras informações relevantes

As informações são organizadas em um **DataFrame** utilizando o **pandas** e exportadas para CSV.

---

## 2. Pré-requisitos

Certifique-se de que as bibliotecas necessárias estão instaladas em seu ambiente Python. Utilize o comando abaixo para instalar todas as dependências:

```
pip install requests beautifulsoup4 pandas
```

---

## 3. Instalação

1. Clone este repositório: `https://github.com/https-ailton-dev/WebScraping_Construtora.git`
2. Navegue até o diretório do projeto.

---

## 4. Uso

Para executar o script e iniciar o processo de scraping, basta rodar o seguinte comando:

```
python scraping_construtora.py
```

O script irá coletar os dados da página de empreendimentos da construtora e salvá-los em arquivo CSV no diretório atual.

---

## 5. Estrutura do Código

- **Requisição POST:** Envia uma requisição POST ao site da construtora para carregar os dados dinâmicos.
- **Parsing com BeautifulSoup:** Faz o parsing do HTML recebido e extrai os dados dos empreendimentos.
- **Organização dos Dados:** Os dados são organizados em um DataFrame para facilitar o processo de manipulação e análise.
- **Exportação de Dados:** O DataFrame é exportado para arquivo CSV para uso posterior.

---

## 6. Funcionalidades

**Extração Automática de Dados:** O script acessa o site da construtora, coleta automaticamente as informações dos empreendimentos e organiza em um formato estruturado.

**Exportação de Dados:** Os dados são exportados para arquivo CSV, facilitando o uso em outras plataformas de análise ou planilhas.

---

## 7. Limitações Conhecidas

**Dados Dinâmicos:** O site da construtora utiliza dados carregados dinamicamente via JavaScript, o que pode dificultar a captura em caso de mudanças no layout ou na estrutura do HTML.

**Estrutura Fixa de Dados:** O script assume uma estrutura fixa para os blocos de dados. Caso a estrutura do HTML seja alterada, pode ser necessário ajustar o código para refletir essas mudanças.

---

## 8. Possíveis Melhorias

**Filtragem de Dados:** Adicionar a funcionalidade de permitir filtros adicionais, como número de dormitórios, tipo de empreendimento, ou faixa de preço, diretamente no script.

**Captura de Mais Informações:** Expandir o projeto para capturar outras informações que possam ser úteis para análise, como áreas úteis e preços por metro quadrado.

**Monitoramento Regular:** Adaptar o script para funcionar de forma contínua, monitorando novos empreendimentos e atualizando os dados regularmente.

---

## 9. Conclusão

Este projeto oferece uma solução simples e eficiente para automatizar a coleta de dados de empreendimentos da MAC Construtora. Com ele, é possível extrair, organizar e exportar informações de forma estruturada, facilitando a análise e o uso em outras plataformas.

---