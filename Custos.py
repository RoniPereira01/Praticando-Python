faturamento = 1000; #tipo: int -> numero inteiro
custo = 700.0;#tipo: float-> numero com casa decimal

imposto = faturamento * 0.1;

lucro = faturamento - custo- imposto;
margemLucro= lucro / faturamento;

print("Faturamento foi",faturamento);
print("O custo", custo);
print("O lucro foi de", lucro);
print("A margem de lucro foi de", round(margemLucro, 1));# round ele arredonda para casa decimal, o numero e quantas casa decimal

teveLucro = True; #variavel tipo boolean

print(10 % 3);#mod -> resto da divisão

tempoContrato = 179;
tempoAnos = 1790/12;
print("Tempo em anos",int(tempoAnos));
tempoMeses = 170 % 12;
print("Tempo em meses",tempoMeses);


print(f"Faturamentos da empresa: {faturamento}, Custo: {custo}, lucro: {lucro}");
emailCliente ="qualquercoisa@gmail.com";

#maiuculo
emailCliente = emailCliente.upper();
print(emailCliente)
#minuscula
emailCliente = emailCliente.lower();
print(emailCliente);

#"acha a posiçao que esta o elemento no texto"
print(emailCliente.find("@"));

#tamanho do texto
print(len(emailCliente));

#pegar um caracter
print(emailCliente[8]);

#pegar um pedaço do texto
print(emailCliente[:4]);# 4:5

#trocar um pedaço do texto
novoEmail = emailCliente.replace("gmail.com", "hotmail.com");
print(novoEmail);

nome = "Fulano Tal";
#trabalhar com nomes
print(nome.capitalize());
print(nome.title());


#pegar o servidor do email
posiçaoArroba = emailCliente.find("@") + 1;
servidor = emailCliente[posiçaoArroba:];

#pegar primeiro nome
posicaoEspaco = nome.find(" ");
primeiroNome = nome[:posicaoEspaco];

#pegar o sobre nome
sobreNOme= nome[posicaoEspaco:+1];
print(primeiroNome);

margemLucro= round(margemLucro, 2);
print(f"Faturamentos da empresa: R${faturamento: .2f}, Custo: {custo:.2f}, lucro: {lucro:.2f}");