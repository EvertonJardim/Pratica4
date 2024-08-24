# main_pessoa.py

from Pessoa import Pessoa
from PessoaFisica import PessoaFisica
from PessoaJuridica import PessoaJuridica

# Instancia um objeto da classe Pessoa
pessoa = Pessoa(
    nome="João",
    numeroConta="123456",
    dataAberturaConta="2024-08-01",
    status=False
)
pessoa.imprimirValores()

# Instancia um objeto da classe PessoaFisica
pessoa_fisica = PessoaFisica(
    nome="Ana",
    numeroConta="654321",
    dataAberturaConta="2024-08-01",
    status=True,
    dataNascimento="1990-05-15",
    cpf="123.456.789-00",
    rg="123456789"
)
pessoa_fisica.imprimirValores()

# Instancia um objeto da classe PessoaJuridica
pessoa_juridica = PessoaJuridica(
    nome="Empresa XYZ",
    numeroConta="789456",
    dataAberturaConta="2024-08-01",
    status=True,
    dataAberturaEmpresa="2024-01-01",
    cnpj="00.000.000/0001-00"
)
pessoa_juridica.imprimirValores()
