# odeio PDF com senha

O nome é bem descritivo, aqui contém uma ferramenta pra sanar tal ódio.

Ela recebe um PDF e tenta por **força bruta** todas as senhas contidas no arquivo `passwords.txt`, até encontrar a correta.

Atualmente o arquivo de senhas contém do número `0000` até o `9999`, pois eu estava tentando acertar os quatro primeiros dígitos do CPF de alguém. Caso deseje mudar ele para o tamanho de 2 ou 6 por exemplo, você pode usar o script `password-generator.js`, só precisará do Node.js instalado em sua máquina também.

## Como instalar?

Você precisará de `python` 3 instalado em seu computador, além de duas bibliotecas que podem ser instaladas da forma abaixo:

```
pip3 install pikepdf tqdm
```

## Como acabar com o seu ódio?

Para executar, utilize da forma abaixo, sendo `target.pdf` o nome do arquivo que deseja descobrir a senha.

```
python3 main.py target.pdf
```

## Por que essa ferramenta veio a vida?

Esse projeto além de ter origem em meu ódio por PDFs com senha, se concretizou quando eu precisei do CPF do proprietário do apartamento para pagar o boleto do condomínio de onde eu alugo. Para evitar interação social com a pessoa, ao invés de perguntar eu criei este programa ruim, mas útil.
