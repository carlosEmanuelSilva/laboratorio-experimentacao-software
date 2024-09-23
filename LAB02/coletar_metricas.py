import os
def executar_comando_em_diretorios(diretorio_principal):
    for raiz, diretorios, arquivos in os.walk(diretorio_principal):
        for diretorio in diretorios:
            os.mkdir(f"/home/carlos/Documentos/faculdade/LES/LAB02/output/{diretorio}")
            caminho_completo = os.path.join(raiz, diretorio)
            os.chdir(caminho_completo)
            print(f"Executando comando")
            os.system(f"java -jar /home/carlos/ck/target/ck-0.7.1-SNAPSHOT-jar-with-dependencies.jar {caminho_completo} true 0 false /home/carlos/Documentos/faculdade/LES/LAB02/output/{diretorio}/")

diretorio_principal = "/home/carlos/Documentos/faculdade/LES/LAB02/repositorios_clonados"

executar_comando_em_diretorios(diretorio_principal)
