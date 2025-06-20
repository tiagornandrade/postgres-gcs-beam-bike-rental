# Postgres GCS Beam - Bike Rental

## Descrição do Projeto

Este projeto, denominado Postgres GCS Beam - Bike Rental, é uma solução para processamento de dados relacionados ao aluguel de bicicletas. Ele utiliza o Apache Beam para criar pipelines de processamento de dados que movem e transformam dados entre o PostgreSQL (Postgres), o Google Cloud Storage (GCS) e diferentes camadas de dados, como landing, raw, trusted e refined.

## Estrutura do Projeto

O projeto está organizado nas seguintes pastas e arquivos:

### Pastas:

1. **utils/gcs**: Contém utilitários relacionados ao Google Cloud Storage, incluindo scripts para transferir dados entre diferentes camadas.

2. **utils/postgres**: Aqui estão os utilitários específicos para interação com o PostgreSQL.

### Arquivos:

1. **utils.postgres.generate.py**: Um script Python responsável por gerar dados simulados para o PostgreSQL.

2. **utils.gcs.landing_to_raw.py**: Um utilitário para transferir dados da camada landing para a camada raw no GCS.

3. **utils.gcs.raw_to_trusted.py**: Utilitário que move dados da camada raw para a camada trusted no GCS após aplicar transformações.

4. **utils.gcs.trusted_to_refined.py**: Utilitário que move dados da camada trusted para a camada refined no GCS.

5. **pipeline_beam/landing_to_raw.py**: Um pipeline Apache Beam para processar dados da camada landing para a camada raw.

6. **pipeline_beam/raw_to_trusted.py**: Outro pipeline Apache Beam para transformar dados da camada raw para a camada trusted.

7. **pipeline_beam/trusted_to_refined.py**: Pipeline Apache Beam para transformar dados da camada trusted para a camada refined.

## Configuração e Execução

Antes de executar qualquer script ou pipeline, certifique-se de configurar corretamente as credenciais do Google Cloud Storage e PostgreSQL.

### Configuração do Ambiente

1. **Google Cloud Storage**: Configure as seguintes variáveis de ambiente:
   - `GCS_BUCKET_NAME`: Nome do bucket no GCS
   - `GOOGLE_APPLICATION_CREDENTIALS`: Caminho para o arquivo de credenciais do Google Cloud

2. **PostgreSQL**: Configure as seguintes variáveis de ambiente:
   - `PG_HOST`: Host do PostgreSQL
   - `PG_USER`: Usuário do PostgreSQL
   - `PG_PASSWORD`: Senha do PostgreSQL
   - `PG_DB`: Nome do banco de dados

### Instalação

```bash
# Instalar dependências
make install

# Ou instalar como pacote Python
pip install -e .
```

### Executando com Makefile (Recomendado)

O projeto inclui um Makefile com comandos pré-configurados:

```bash
# Iniciar PostgreSQL com Docker
make up

# Gerar dados de exemplo no PostgreSQL
make run-postgres-generate

# Executar pipelines Apache Beam
make run-load-raw
make run-load-trusted
make run-load-refined

# Executar scripts GCS diretamente
make run-gcs-landing-to-raw
make run-gcs-raw-to-trusted
make run-gcs-trusted-to-refined

# Parar containers
make down
```

### Executando Manualmente

Se preferir executar manualmente, use o PYTHONPATH:

```bash
# Configurar PYTHONPATH
export PYTHONPATH=$(pwd)

# Executar pipelines
python pipeline_beam/landing_to_raw.py
python pipeline_beam/raw_to_trusted.py
python pipeline_beam/trusted_to_refined.py

# Executar scripts GCS
python utils/gcs/landing_to_raw.py
python utils/gcs/raw_to_trusted.py
python utils/gcs/trusted_to_refined.py

# Gerar dados PostgreSQL
python utils/postgres/main.py
```

### Executando com Docker

Para executar o PostgreSQL com Docker:

```bash
docker-compose up -d
```

## Estrutura de Dados no GCS

O projeto utiliza a seguinte estrutura de pastas no GCS:

- `raw/`: Dados brutos em formato Parquet
- `trusted/`: Dados processados em formato CSV
- `refined/`: Dados refinados em formato CSV

## Configuração do GCS

Consulte o arquivo `gcs_setup.md` para instruções detalhadas sobre como configurar o Google Cloud Storage.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para criar pull requests, reportar problemas ou sugerir melhorias.

## Licença

Este projeto é licenciado sob a [MIT License](LICENSE).