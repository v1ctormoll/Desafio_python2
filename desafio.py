print("Bem vindo a triagem do ambulátorio de dermatologia!")

decisao1 = input("Você possui mancha na pele? [S/N]: ")
if decisao1 in 'nN':
    print("Obrigado, aguarde o atendimento! ")

elif decisao1 in 'Ss':
    decisao2 = str(input("Você sente febre? [S/N]: "))

    if decisao2 in 'Ss':
        escala1 = int(input("Quantos desses sintomas, você também apresenta: Cansaço, Falta de apetite, "
                            "Manchas que viram bolhas, Bolhas cheias de liquido? "))
        if escala1 == 1:
            print("Em uma escala de 0 a 6, seu nível de certeza de estar com Catapora é: 3 \n Aguarde o atendimento! ")
        elif escala1 == 2:
            print("Em uma escala de 0 a 6, seu nível de certeza de estar com Catapora é: 4 \n Aguarde o atendimento!")
        elif escala1 == 3:
            print("Em uma escala de 0 a 6, seu nível de certeza de estar com Catapora é: 5 \n Aguarde o atendimento!")
        elif escala1 == 4:
            print("Em uma escala de 0 a 6, seu nível de certeza de estar com Catapora é: 6 \n Aguarde o atendimento!")

    elif decisao2 in 'nN':
        decisao3 = str(input("Você sente perda de sensibilidade? [S/N]: "))
        if decisao3 in 'Ss':
            escala2 = str(input("Você também apresenta diminuição da força muscular? [S/N]: "))
            if escala2 in 'Ss':
                print("Em uma escala de 0 a 3, seu nível de certeza de estar com Hanseníase é: 3  "
                      "\n Aguarde o atendimento!  ")
            elif escala2 in 'Nn':
                print("Em uma escala de 0 a 3, seu nível de certeza de estar com Hanseníase é: 2  "
                      "\n Aguarde o atendimento! ")

        elif decisao3 in 'nN':
            decisao4 = str(input("Você possui alguma ferida ou mancha com bordas irregulares? [S/N]:"))
            if decisao4 in 'Ss':

                escala3: int = int(input("Quantos desses sintomas, você também apresenta:"
                                         "Crescimento da mancha, sangra fácil e coceira,crosta e erosões? "))
                if escala3 == 1:
                    print("Em uma escala de 0 a 5, seu nível de certeza de estar com Câncer de Pele é: 3 "
                          "\n Aguarde o atendimento! ")
                elif escala3 == 2:
                    print("Em uma escala de 0 a 5, seu nível de certeza de estar com Câncer de Pele é: 4  "
                          "\n Aguarde o atendimento! ")
                elif escala3 == 3:
                    print("Em uma escala de 0 a 5, seu nível de certeza de estar com Câncer de Pele é: 5 "
                          "\n Aguarde o atendimento! ")

            elif decisao4 in 'Nn':
                decisao5 = str(input("Você sente alguma coceira? [S/N]:"))

                if decisao5 in 'Ss':
                    escala4= int(
                        input("Quantos desses sintomas, você também apresenta: Lesões, Crostas, ressecamento e dor? "))
                    if escala4 == 1:
                     print("Em uma escala de 0 a 6, seu nível de certeza de estar com Psoríase é: 3 "
                            "\n Aguarde o atendimento!")
                    elif escala4 == 2:
                      print("Em uma escala de 0 a 6, seu nível de certeza de estar com Psoríase é: 4 "
                            "\n Aguarde o atendimento!")
                    elif escala4 == 3:
                      print("Em uma escala de 0 a 6, seu nível de certeza de estar com Psoríase é: 5 "
                            "\n Aguarde o atendimento!")
                    elif escala4 == 4:
                      print("Em uma escala de 0 a 6, seu nível de certeza de estar com Psoríase é: 6 "
                            "\n Aguarde o atendimento!")
                elif decisao5 in 'Nn':
                      print("Obrigado, aguarde atendimento! ")