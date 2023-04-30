def gerador_getset():
    nome_das_propriedades = input('Digite os nomes dos parametros a serem feitos os getter e setters (separados por espaço apenas): ')

    lista_de_parametros = nome_das_propriedades.split()

    for parametro in lista_de_parametros:
        print(f'@property\ndef {parametro}(self):\n    return self.__{parametro}\n\n@{parametro}.setter\ndef {parametro}(self, {parametro}):\n    self.__{parametro} = {parametro}\n')

        
gerador_getset()        