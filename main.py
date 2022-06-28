import json

#função que mostra a porcentagem de cada estado
def mostrarPorcentagem(dados):
  soma = 0;
  for dado in dados:
    soma+= dado['valor']
  for dado in dados:
    perc = (dado['valor'] / soma) * 100
    print('A porcentagem de representação de',dado['estado'],'é: %.2f' % perc,'%')


if __name__ == '__main__':
  with open("dados.json", encoding='utf-8') as meu_json:
    dados = json.load(meu_json)

  mostrarPorcentagem(dados)