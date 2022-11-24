def VerificarAliquotaINSS(salario):
    if salario <= 1212:
        inssAliquota = 0.075;
        return float(inssAliquota);
    elif salario >= 1212.01 and salario <= 2427.35:
        inssAliquota = 0.9;
        return float(inssAliquota);
    elif salario >= 2437.36 and salario <= 3641.03:
        inssAliquota = 0.12;
        return float(inssAliquota);
    elif salario >= 3641.04:
        inssAliquota = 0.14;
        return float(inssAliquota);

def VerificarAliquotaIRRF(salario):
    if salario <= 1903.98:
        irrfAliquota = 0;
        return float(irrfAliquota);
    elif salario >= 1903.99 and salario <= 2826.65:
        irrfAliquota = 0.075;
        return float(irrfAliquota);
    elif salario >= 2826.66 and salario <= 3751.05:
        irrfAliquota = 0.15;
        return float(irrfAliquota);
    elif salario >= 3751.06 and salario <= 4664.68:
        irrfAliquota = 0.225;
        return float(irrfAliquota);
    elif salario >= 4664.69:
        irrfAliquota = 0.275;
        return float(irrfAliquota);


inssAliquota = 0;
irrfAliquota = 0;
salario = float(input("Digite seu salário bruto: "));
inssAliquota = VerificarAliquotaINSS(salario);
irrfAliquota = VerificarAliquotaIRRF(salario);

tempVar = (salario / 12) * 5;
primeiraParcela =  tempVar / 2;

valorDescontoInss = primeiraParcela * inssAliquota;
valorDescontoIrrf = primeiraParcela * irrfAliquota; 

print(inssAliquota);
print(valorDescontoInss);
print("--------------------------------------")
print(irrfAliquota);
print(valorDescontoIrrf);

segundaParcela =  primeiraParcela - valorDescontoInss;
segundaParcela -= valorDescontoIrrf;
print("Primeira parcela R$ %.2f" % primeiraParcela);
print("Segunda Parcela R$ %.2f" % segundaParcela);




















