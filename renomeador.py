import os

def renomear_arquivos(diretorio, novo_nome, extensao=None, numero_inicial=1):
    try:
        arquivos = os.listdir(diretorio)
        arquivos = sorted(arquivos)
        
        contador = numero_inicial

        for arquivo in arquivos:
            caminho_antigo = os.path.join(diretorio, arquivo)

            if not os.path.isfile(caminho_antigo):
                continue  

            _, ext = os.path.splitext(arquivo)  
            
            if extensao and ext.lower() != f".{extensao.lower()}":
                continue  

            novo_nome_arquivo = f"{novo_nome}_{contador:03d}{ext}"  
            caminho_novo = os.path.join(diretorio, novo_nome_arquivo)
            
            os.rename(caminho_antigo, caminho_novo)  
            print(f"\033[32m{arquivo} → {novo_nome_arquivo}\033[0m")  

            contador += 1
            
        print("\nRenomeação concluída!")
    
    except Exception as e:
        print(f"\033[31mOcorreu um erro: {e}\033[0m")

if __name__ == "__main__":
    pasta = input("Digite o caminho da pasta: ")
    nome_base = input("Novo nome base: ")
    extensao_filtro = input("Extensão específica (enter para todas): ")
    inicio = int(input("Número inicial: "))

    renomear_arquivos(pasta, nome_base, extensao_filtro if extensao_filtro else None, inicio)