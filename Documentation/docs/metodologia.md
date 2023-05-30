# Metodologia proposta

Nessa sessão será abordado como será a metodologia utilizada para que seja possivel o calculo do Round Trip Time e o calculos da Latência, iremos explicar os cenários que serão compostos os testes e os tamanhos das mensagens que serão enviadas.




### Definição do Cenário de Teste:

Quando vamos trabalhar com o locust a primeira coisa que é feita é definir o cenário de teste, e esse cenário é composto por quais ações os usuários irão realizar, quais tarefas que serão executadas com maior frequência, como é a inicialização de cada usuário e como será o comportamento do usuário ao final do teste. 

Nas simulações os usuários serão comparados a dispositivos que enviam e recebem informações através de publicações e assinaturas.

Essas simulações serão realizadas em 2 ambientes distintos, um dos ambientes será realizado utilizando
um broker no ambiente local, ou seja o computador que está excitando o envio das publicações estará localizado na mesma
rede local que o broker. 

No segundo ambiente configurado será utilizado o mesmo computador que excitou o envio das publicações porém agora
iremos utilizar um servidor que foi configurado um broker MQTT porém que se encontra localizado no estado de são paulo.

Com isso temos o objetivo de calcular a latência em um ambiente fabril que possui um broker local e um ambiente fabril que iria trocar informação com um broker que se encontra na nuvem.

![alt text for screen readers](image/ambiente.png 'Text to show on mouseover')


### Criação de Usuários Simulados:

Com base no cenário de teste definido, o Locust cria um número especificado de usuários simulados. Cada usuário simulado é representado por um greenlet (microprocesso leve).

#### greenlet

Um greenlet são microprocessos que são executados dentro de um unico processo. Eles são implementados como um mecanisco cooperativo de programação concorrente. O termo cooperativo é relacionado como os greenlets são executados, nesse modo de execução cada greenlet precisa explicitamente ceder o controle para outro greenlet. Já programação concorrente é um paradigma de programação que lida com a execução simultânea de várias tarefas ou processos em um sistema computacional. 


Uma das principais diferenças entre threads tradicionais e greenlet é que threads são executadas de forma preemptiva pelos sistema operacional, ou seja o sistema operacional que decide qual thread é executado e qual será interrompido. Isso pode resultar em problemas de concorrência.

Como os greenlets são executados de forma cooperativa, é possível evitar problemas comuns de concorrência e sincronização encontrados nas threads.

### Execução dos Greenlets:

Durante a execução dos testes, cada greenlet representa um usuário simulado e executa as tarefas especificadas no cenário de teste.

## Simulações que serão realizadas

Serão realizadas simulações utilizando: 

- 1 dispositivo publicando informação em um tópico com tamanhos de pacotes de 6 bytes.
- 5 dispositivo publicando informação em um tópico com tamanhos de pacotes de 6 bytes.
- 20 dispositivo publicando informação em um tópico com tamanhos de pacotes de 6 bytes.
- 50 dispositivo publicando informação em um tópico com tamanhos de pacotes de 6 bytes.
- 100 dispositivo publicando informação em um tópico com tamanhos de pacotes de 6 bytes.

- 1 dispositivo publicando informação em um tópico com tamanhos de pacotes de e 256 bytes.
- 5 dispositivo publicando informação em um tópico com tamanhos de pacotes de e 256 bytes.
- 20 dispositivo publicando informação em um tópico com tamanhos de pacotes de e 256 bytes.
- 50 dispositivo publicando informação em um tópico com tamanhos de pacotes de e 256 bytes.
- 100 dispositivo publicando informação em um tópico com tamanhos de pacotes de e 256 bytes.

Para cada um desses teste será realizado uma amostragem piloto, enviando 200 mensagens por dispositivo. 

Exemplo com 5 dispisitivos e tamanho de pacote de 6 bytes:

Para calcular o tamanho da amostra iremos realizar uma amostra piloto enviando 200 mensagens por dispositivo, ou seja ao todo nessa amostra piloto iremos publicar o total de 1000 mensagens. Essas mensagens são enviadas aleatoriamente em um espaçamento de 0,5 segundos a 6 segundos por dispositivo.

## Intervalo de confiança

Um intervalo de confiança é uma amplitude de valores, que são derivadas de estatísticas de amostras, que tem a probabilidade de conter o valor de um parâmetro populacional desconhecido.

O **nível de confiança** ($1 - \alpha$) representa a probabilidade de acerto da estimativa. De forma complementar o **nível de significância** ($\alpha$) expressa a probabilidade de erro da estimativa.

O **nível de confiança** representa o grau de confiabilidade do resultado da estimativa estar dentro de determinado intervalo. Quando fixamos em uma pesquisa um **nível de confiança** de 95%, por exemplo, estamos assumindo que existe uma probabilidade de 95% dos resultados da pesquisa representarem bem a realidade, ou seja, estarem corretos.

O **nível de confiança** de uma estimativa pode ser obtido a partir da área sob a curva normal como ilustrado na figura abaixo.

![alt text](https://caelum-online-public.s3.amazonaws.com/1178-estatistica-parte2/01/img007.png)

### Score Z

- É o quanto uma medida se afasta da média em termos de Desvios
  Padrão.
- Quando o escore Z é positivo isto indica que o dado está acima da
  média e quando o mesmo é negativo significa que o dado está abaixo
  da média.
- Seus valores oscilam entre -3 < Z < +3 e isto corresponde a 99,72% da
  área sob a curva da Distribuição Normal.

Em nosso estudo iremos utilizar um nivel de confiança igual a 95% e se consultarmos a tabela de Distribuição normal iremos encontrar um z é aproximadamente 1,96.

Z = 1,96 (tabela da Distribuição Normal)

## Calculando o número de amostra

Para o calculo do número de amostra iremos utilizar a seguinte formula:

$$n = \left(z\frac{s}{e}\right)^2$$

onde:
$z$ = variável normal padronizada

$s$ = desvio padrão amostral

$e$ = erro inferencial

Com a amostra piloto é possivel calcular a o desvio padrão amostral e como foi mencionado acima o z é aproximadamente 1,96. Faltando assim apenas o valor do erro inferencial.

Para um erro de 5% iremos calcular 0,05 vezes a média amostral.

Será realizado esse processo antes de todas as amostras para que seja possivel calcular o número de valores que serão necessários simular

### Wireshark
Como podemos analisar na imagem acima será utilizado o Wireshark que é um programa para análise de protocolo de rede em código aberto, com esse programa é possivel verificar o funcionamento de uma rede.

De maneira geral, os analisadores de pacotes são compostos por duas partes:

- O módulo de captura de pacotes (Packet Capture Library)
- O analisador de protocolos (Protocol Analyzer).

O primeiro é responsavel por capturar todos os pacotes que trafegam pela placa de rede que foi especificada, já o segundo é responsavel por interpretar os cabeçalhos e conteúdos dos pacotes.

Esse programa será fundamental para analisarmos os resultados do nosso teste. Nos permitindo capturar o tempo da saida do nosso pacote e a capturar o tempo de chegada do nosso pacote de confirmação de recebimento do broker.

## Locust
O Locust é uma ferramenta de teste de performance fácil de usar, programável e escalável.

O comportamento do usuário é definindo por código python, então é muito customizável. Em nosso teste iremos definir o comportamento de um dispositivo IoT publicando mensagens em um determinado tópico.

O Locust só vem com suporte embutido para HTTP/HTTPS, mas pode ser estendido para testar quase qualquer protocolo.

Ele permite que você crie cenários de teste em que um grande número de usuários simultâneos interaja com o sistema sendo testado. Vamos entender como o Locust funciona em detalhes.



## Latência

O cálculo de latência pode ser realizado da seguinte maneira:

Quando a simulação é iniciada, o primeiro cliente (Cliente 1) se conecta ao broker e se inscreve no tópico chamado "device-1".

Antes de enviar uma mensagem para o tópico "device-1", o Cliente 1 captura o valor de tempo no momento do envio.

A mensagem percorre o caminho até o servidor e é redirecionada para o tópico "device-1".

Assim que a mensagem é recebida pelo Cliente 1, capturamos o valor de tempo de chegada dessa mensagem.

Subtraindo o valor de tempo de chegada pelo valor de tempo de envio, obtemos o valor de latência.

Em resumo, a latência é calculada subtraindo o tempo de envio do tempo de chegada da mensagem. Esse cálculo nos dá a diferença de tempo entre o momento em que a mensagem foi enviada e o momento em que ela foi recebida pelo Cliente 1, representando a latência da comunicação.

Esses calculos de latência e Round-Trip-Time também seram realizados através dos dados que foram capturados pelo Wireshark, assim será possivel realizar os calculos capturando os valores através do locust e atrávés dos dados capturados pelo Wireshark.

## Round Trip Time

O cálculo do tempo de ida e vinda pode ser realizado da seguinte maneira:

Quando a simulação é iniciada, o Cliente 1 se conecta ao broker e se inscreve no tópico "device-1" com o QoS 1 especificado.

Antes de enviar uma mensagem para o tópico "device-1", o Cliente 1 captura o valor de tempo no momento do envio.

O Cliente 1 envia a mensagem para o broker, solicitando o QoS 1 para garantir a entrega confiável da mensagem.

O broker recebe a mensagem e envia uma confirmação (PUBACK) para o Cliente 1 para informar que a mensagem foi recebida com sucesso.

Assim que o Cliente 1 recebe a confirmação do broker, captura o valor de tempo de chegada da confirmação.

Subtraindo o valor de tempo de chegada da confirmação pelo valor de tempo de envio, obtemos o valor de RTT.

Desta forma, o RTT é calculado subtraindo o tempo de envio da mensagem pelo tempo de chegada da confirmação do broker. Essa diferença de tempo representa o tempo total de ida e volta da mensagem e é conhecida como Round-Trip Time (RTT).













