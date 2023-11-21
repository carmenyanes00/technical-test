#!/bin/bash

# Crear un directorio para los certificados
mkdir certs

# Generar una clave privada
openssl genrsa -out certs/server.key 2048

# Generar una solicitud de firma de certificado (CSR)
openssl req -new -key certs/server.key -out certs/server.csr -subj "/CN=localhost"

# Firmar el certificado con la clave privada para obtener el certificado autofirmado
openssl x509 -req -days 365 -in certs/server.csr -signkey certs/server.key -out certs/server.crt
