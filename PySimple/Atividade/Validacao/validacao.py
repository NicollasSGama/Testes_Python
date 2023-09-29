def validacao_cpf(cpf):
    match cpf:
        case cpf.isdigit() if len(cpf) == 11:
            return cpf


cpf = '12345678911'
print(validacao_cpf(cpf))

d = '1'
if d.isdigit:
    pass
else:
    pass
