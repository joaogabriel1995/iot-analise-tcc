Os passos abaixo mostram como gerar as chaves e certificados usando o OpenSSL em um sistema Ubuntu 20.04:

1. Criação de uma chave CA (Autoridade Certificadora) para o cliente:
```
openssl genrsa -des3 -out ca.key 2048
```
Esta linha de comando gera uma chave privada com criptografia de 2048 bits para a Autoridade Certificadora do cliente. O parâmetro -des3 é usado para criptografar a chave privada com um algoritmo de criptografia de 3 chaves.

Criação do certificado CA usando a chave CA:
```
openssl req -new -x509 -days 1833 -key ca.key -out ca.crt
```
Essa linha de comando gera o certificado da Autoridade Certificadora do cliente usando a chave privada gerada no passo anterior. O parâmetro -x509 é usado para indicar que estamos criando um certificado de autoridade certificadora autoassinado.

Criação da chave do broker sem criptografia:
```
openssl genrsa -out server.key 2048
```
Essa linha de comando gera a chave privada para o broker do Mosquitto. A chave privada não é criptografada, pois ela será usada para gerar um arquivo de solicitação de certificado (CSR).

Solicitação do certificado do broker e criação do arquivo .csr:
```
openssl req -new -out server.csr -key server.key
```
Essa linha de comando gera um arquivo de solicitação de certificado (CSR) para o broker do Mosquitto. O CSR é usado para solicitar um certificado assinado pela Autoridade Certificadora.

Criação do certificado do broker:
```
openssl x509 -req -in server.csr -CA ca.crt -CAkey ca.key -CAcreateserial -out server.crt -days 360
```
Essa linha de comando gera o certificado do broker assinado pela Autoridade Certificadora. O parâmetro -req indica que estamos usando um arquivo de solicitação de certificado (CSR) como entrada. Os parâmetros -CA e -CAkey são usados para especificar o certificado e a chave privada da Autoridade Certificadora, respectivamente. O parâmetro -CAcreateserial é usado para criar um número de série para o certificado. O parâmetro -out é usado para especificar o nome do arquivo de saída. O parâmetro -days é usado para definir a validade do certificado (360 dias neste exemplo).


Iremos utilizar o broker denominado `Eclipse Mosquitto` que é um broker MQTT de software livre (licenciado por EPL/EDL).

Irei seguir a documentação oficial do mosquitto, que se encontra no seguinte [link](https://mosquitto.org/man/mosquitto-tls-7.html)
[link](https://www.youtube.com/watch?v=1Tu0tc0VHuc)
Primeiro passo é criar uma pasta denominada `mosquitto`, dentro dessa pasta é necessário criar a seguinte estrutura:

```
.
|-- config
|   `-- mosquitto.conf
|-- data
|-- docker-compose.yml
`-- log
    `-- mosquitto.log
```

3 directories, 3 files