#!/bin/bash

#get time
datetime=$(date '+%Y%m%d%H%M')

dir="rmfinder/_unisimIDpocos/rand"

cd "$dir" || { echo "Erro ao acessar o diretório $dir"; exit 1; }
mkdir "$datetime"

arquivo_origem="template.txt"
arquivo_destino="Parameters.txt"
arquivo_pesos="../../../out-v2.txt"

id_linha=1
while IFS= read -r linha_pesos; do
    > "$arquivo_destino"
    id_linha_template=1
    while IFS= read -r linha_template; do
        if [ $id_linha_template -eq 13 ]; then
            linha_template="DEFINE RANDOM FALSE"
        elif [ $id_linha_template -eq 17 ]; then
            linha_template="DEFINE $linha_pesos"
        elif [ $id_linha_template -eq 21 ]; then
            linha_template="DEFINE MANUAL_SOLUTIONS"
        fi
        echo "$linha_template" >> "$arquivo_destino"
        ((id_linha_template++))
    done < "$arquivo_origem"

    echo "Executando script com pesos $linha_pesos"

    java -jar RMFinder.jar

    status=$?

    if [ $status -ne 0 ]; then
        echo "O comando java falhou com o código de saída $status"
        exit $status
    fi

    # move pastas
    path="./$datetime/$linha_pesos/"
    mv "results_9" "$path"

    ((id_linha++))
done < "$arquivo_pesos"

exit 0

# todo usar 9 solucoes de rm
# DEFINE NUMBER_SOL_TO_BE_PRINTED 10 usar mais solucoes para gerar a fronteira
# usar as 2 primeiras soluções para unir nas manuais 2x21 = 42
# trocar de 0 para 1
# ao final da exec troca o nome da pasta -> para gerar uma nova results_5
# usar os pesos para nomear as pastas


# coletar os valores das 4 funções e jogar numa planilha
# executar rmfinder com esse csv (1, 1, 1, 1)
# analisar os graficos de crossplots (r4 -> r2) nuvem de pontos da fronteira projetada
# selecionar 3 modelos (salvar os pesos e soluções dos modelos)
# gerar a fronteira e ver quantos modelos tem
# visualizar em r3 (somando fatr, ffreq)
# escrever metodologia em paralelo