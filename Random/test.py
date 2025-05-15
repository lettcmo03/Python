from InquirerPy import prompt

perguntas = [
    {
        'type': 'list',
        'message': 'Qual e o seu estado civil? ',
        'choices': ['solteira', 'casada', 'divorciada', 'complicada']
    }
]
resultado = prompt(perguntas)