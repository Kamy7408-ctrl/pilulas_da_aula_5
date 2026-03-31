def validarSenha(senha):
    if len(senha) < 8:
       return "Senha inválida, muito curta"
    temNumero = False
    temMaiuscula = False
    for c in senha:
        
        if c == " ":
            return 'Senha inválida, não pode conter espaço'
        if c >= '0' and c <= '9':
            temNumero = True
        if c >= 'A' and c <= 'Z':
            temMaiuscula = True
    
    if not temNumero:
        return "Senha inválida, não tem número"
    if not temMaiuscula:
        return "Senha inválida, não tem maiúscula"
        
    return 'Senha Válida'


# "len" serve pra ler quantas letras tem 
# 'pass' serve para ignorar função
#main
senha = input('Digite sua senha: ')
print(validarSenha(senha))