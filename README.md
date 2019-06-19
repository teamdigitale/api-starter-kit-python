# Starter kit per la pubblicazione di API interoperabili in Python

[![CircleCI](https://circleci.com/gh/teamdigitale/api-starter-kit-python.svg?style=svg)](https://circleci.com/gh/teamdigitale/api-starter-kit-python)
[![Join the #api channel](https://img.shields.io/badge/Slack-%23api-blue.svg?logo=slack)](https://developersitalia.slack.com/messages/CDKBYTG74)
[![Get invited](https://slack.developers.italia.it/badge.svg)](https://slack.developers.italia.it/)
[![API on forum.italia.it](https://img.shields.io/badge/Forum-interoperabilità-blue.svg)](https://forum.italia.it/c/interoperabilita)

Questo repository contiene il template di un'API interoperabile scritta in Python.

## Contenuto

- Un progetto di esempio in python-flask
- Una directory `openapi` con le specifiche

## Istruzioni

Gli step per la creazione di API interoperabili sono:

1. scrivere le specifiche in formato OpenAPI v3 partendo dagli esempi in `openapi`;

2. scrivere o generare il codice a partire dalle specifiche. Ora i tool di swagger per Python
   supportano correttamente OpenAPI v3 dalla version 3.0.9.

3. scrivere i metodi dell'applicazione

### Scrivere le specifiche

Le specifiche devono essere scritte in formato OpenAPIv3
e rispettando le [Linee Guida di interoperabilità](https://docs.italia.it/italia/piano-triennale-ict/lg-modellointeroperabilita-docs).

Queste presentazioni possono essere d'aiuto:

- [Introduzione ad OpenAPI](https://docs.google.com/presentation/d/1blql0E_zcbq7r-wzmslgJPiW7ELkYlIn9_fqIVEXr4A)
- [REST nel nuovo modello di interoperabilità](https://docs.google.com/presentation/u/1/d/1L6R4ZKhLoZAPEmai1KSED1nrq0GNrx3-TU53sGhfrO8/)

### Risolvere le dipendenze negli OpenAPI

Le specifiche OpenAPI possono contenere riferimenti a schemi esterni
o [yaml anchors](). E' possibile risolverli tramite il modulo python
`openapi_resolver`, richamato dal `Makefile`.

In questo repository, i file con anchor e ref hanno estensione `.yaml.src`
ma sono a tutti gli effetti file OAS3 validi e la maggior parte dei
tool li interpreta correttamente. E' comunque possibile dereferenziarli
per comodità tramite il comando:

	make yaml



### Generare il codice del server

Il `Makefile` contiene:

  - un esempio di code generation python direttamente via openapi v3. Basta
    lanciare:

        make python-flask

Il generatore non sovrascrive i file contenuti in `.swagger-codegen-ignore`.

Il server generato viene servito tramite il wsgi container di default di `connexion`.


### Usare HTTPS

Questa API viene erogata via https. Rispetto al codige autogenerato basta sostituire

        # in Dockerfile installare le librerie necessarie a pyOpenSSL
        FROM python:3.6-alpine
        +RUN apk add --no-cache libffi-dev build-base openssl-dev
        -EXPOSE 8080
        +EXPOSE 8443

        # in swagger_server/__main__.py usare un contesto autogenerato
        #  o una coppia chiave-certificato. 
        -app.run(port=8080)
        +app.run(port=8443, ssl_context='adhoc')


### Dipendenze

Per eseguire questa app servono:

```
make
python 3 + tox
docker
```


### Test

E' possibile testare in locale tramite circleci, con:

        circleci build
