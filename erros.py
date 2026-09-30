"""A única exceção que o projeto usa para sinalizar entrada inválida ou regra de negócio
violada — em `sentencing/`, `agent/`, `api/agente.py` e `database/repositorio.py`.

A mensagem de um InputError é sempre segura para mostrar a quem enviou a requisição
(nunca traz caminho de arquivo, string de conexão ou detalhe interno). Continua sendo um
ValueError, então o código que já trata `except ValueError` continua funcionando sem
mudança nenhuma.

Qualquer OUTRA exceção (erro de programação, falha de uma biblioteca) não é um
InputError, e a API nunca devolve a mensagem dela: vira um erro genérico, com o
detalhe indo só para o log do servidor (api/app.py, `erro_inesperado`).
"""


class InputError(ValueError):
    """Entrada inválida ou regra de negócio violada; a mensagem é segura para exibir."""
