import requests

menu_moedas = """

=== Opções de Moedas para Consulta ===

Tradicionais:

- USD-BRL (Dólar Americano)
- EUR-BRL (Euro)
- GBP-BRL (Libra Esterlina)
- ARS-BRL (Peso Argentino)

Criptomoedas:

- BTC-BRL (Bitcoin)
- ETH-BRL (Ethereum)

=====================================

"""

print(menu_moedas)


def consultar_moeda(moeda):

    url = f"https://economia.awesomeapi.com.br/json/last/{moeda}"

    resposta = requests.get(url)

    if resposta.status_code == 200:
        return resposta.json()
    else:
        return None


moeda_desejada = input(
    "Digite a moeda que deseja consultar (ex: USD-BRL): "
)

dados_api = consultar_moeda(moeda_desejada)


if dados_api:

    chave = moeda_desejada.replace("-", "")

    valor = dados_api[chave]["bid"]

    print("\nRequisição bem-sucedida!")

    print(
        f"O valor atual de {moeda_desejada} é: "
        f"R$ {float(valor):.2f}"
    )

else:

    print(
        f"\nErro ao consultar a moeda '{moeda_desejada}'. "
        "Verifique se o formato está correto (ex: USD-BRL)."
    )
