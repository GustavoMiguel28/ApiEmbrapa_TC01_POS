from bs4 import BeautifulSoup
import requests


class EmbrapaConsulta:
    def __init__(self, ano:int, opcao:int, subopcao:int = 1):
        """
        Inicializa a consulta com os parâmetros fornecidos

        Args:
            ano (int): ano da consulta
            opcao (int): código da opção principal
            subopcao (int, optional): código da subopção
        """
        self.ano = ano
        self.opcao = opcao
        self.subopcao = subopcao
        self.url = 'http://vitibrasil.cnpuv.embrapa.br/index.php'

    
    def _definir_parametros(self) -> dict:
        """
        Define os parâmetros da URL com base nos atributos da instância

        Returns:
            dict: parametros da API
        """
        parametros = {
            'ano': self.ano,
            'opcao': f'opt_0{self.opcao}',
            'subopcao': f'subopt_0{self.subopcao}'
            }

        return parametros
    

    def _consultar_url(self, parametros:dict) -> str:
        """
        Faz a requisição HTTP à URL com os parâmetros fornecidos

        Args:
            parametros (dict): dicionario com todos os parametros que serão utilizados na consulta

        Returns:
            str: html com a resposta da API
        """
        response = requests.get(self.url, params=parametros)

        return response.content
    

    def _extrair_dados_tabela(self, html:str) -> list:
        """
        Extrai os dados da tabela HTML retornada pela página

        Args:
            html (str): html com a respota da API
        
        Returns:
            list: lista com os dados extraidos do html
        """
        soup = BeautifulSoup(html, 'html.parser')
        tabela = soup.find('table', class_='tb_base tb_dados')

        colunas = [coluna.get_text(strip=True) for coluna in tabela.find_all('th')]
    
        dados = []
        for linha in tabela.find('tbody').find_all('tr'):
            items = linha.find_all('td')
            if len(items) != len(colunas):
                continue
            valores = [item.get_text(strip=True) for item in items]
            dados.append(dict(zip(colunas, valores)))

        return dados
    

    def consultar_api(self) -> str:
        """
        Realiza a consulta completa e retorna os dados em formato JSON

        Returns:
            str: dados da API extraídos e formatados
        """
        parametros = self._definir_parametros()
        html = self._consultar_url(parametros)
        dados = self._extrair_dados_tabela(html)

        return dados