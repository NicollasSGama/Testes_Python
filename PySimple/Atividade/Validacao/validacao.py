def validacao_cpf(cpf):
    match cpf:
        case _ if len(cpf) == 11:
            return cpf.isdigit()  # deixa como True


cpf = '12345678911'
print(validacao_cpf(cpf))

d = '1'
if d.isdigit:
    print(type(d))
else:
    print('Nada')
