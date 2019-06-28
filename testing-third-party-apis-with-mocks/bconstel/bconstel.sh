#!/bin/bash

nomes=$1

test -z $nomes && echo "Informe um arquivo com os nomes das pessoas, um nome por linha. Ex: bconstel arquivo_com_os_nomes".

awk 'BEGIN{ print "#,REGIONAL,ÁREA,NOME,EMAIL,MATRICULA,RAMAL,CHEFIA,EMAIL-CHEFIA,RAMAL-CHEFIA" }' 2> /dev/null
i=1
while read -r nome; do
  nomelc=$(echo $nome | tr '[:upper:]' '[:lower:]' | sed -e "s/ /+/g" | iconv -f UTF-8 -t ASCII//TRANSLIT)
  #echo "$nomelc"
  ID_MANAGER=$(curl -s https://constel.serpro.gov.br/s.php?term="$nomelc" \
			| jq -r '.[0].manager')
  #echo "$ID_MANAGER"

  DATA_MANAGER=$(curl -s https://constel.serpro.gov.br/s.php?term="$ID_MANAGER" \
  			| jq -r '.[0].cn, .[0].mail, .[0].telephonenumber' \
  			| awk 'BEGIN{RS="" ; FS="\n" } {print $1","$2","$3}')
  #echo "$DATA_MANAGER"

  DATA_EMPLOYEE=$(curl -s https://constel.serpro.gov.br/s.php?term="$nomelc" \
			| jq -r '.[0].usrlocal, .[0].ou, .[0].cn, .[0].mail, .[0].employeenumber, .[0].telephonenumber' \
			| awk -v x=$i 'BEGIN{RS="" ; FS="\n" } {print x","$1","$2","$3","$4","$5","$6}')
  #echo "$DATA_EMPLOYEE"
  echo "$DATA_EMPLOYEE,$DATA_MANAGER"
  i=$[i+1]
  #echo $i
done < $nomes

#curl -s https://constel.serpro.gov.br/s.php?term="Andre Teixeira Limaverde"
#curl -s https://constel.serpro.gov.br/s.php?term="Wesley Evaristo Queiroz de Sousa"
#curl -s https://constel.serpro.gov.br/s.php?term="NTdpS2FWVlZQTCs3QXA3T2RpOEc4Zz09"
#curl -s https://constel.serpro.gov.br/s.php?term="DE305"
#curl -s https://constel.serpro.gov.br/s.php?term="misael.santos@serpro.gov.br"
