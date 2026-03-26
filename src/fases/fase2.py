def gerar_fase(ClasseBloco):
    blocos = []
    # Configuração visual da fase 1
    for linha in range(5):
        for coluna in range(9):
            x = 40 + coluna * 80
            y = 50 + linha * 40
            # Todos com resistência 1 (cor VERDE) [4]
            novo_bloco = ClasseBloco(x, y, 70, 30, 2, (50, 255, 50))
            blocos.append(novo_bloco)
    return blocos