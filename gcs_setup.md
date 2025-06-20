# Configuração do Google Cloud Storage (GCS)

## Pré-requisitos

1. **Conta Google Cloud**: Você precisa ter uma conta Google Cloud ativa
2. **Projeto Google Cloud**: Crie ou use um projeto existente
3. **Google Cloud Storage**: Ative o serviço de Storage no seu projeto

## Configuração das Credenciais

### 1. Criar uma Service Account

1. Acesse o [Google Cloud Console](https://console.cloud.google.com/)
2. Vá para "IAM & Admin" > "Service Accounts"
3. Clique em "Create Service Account"
4. Dê um nome à service account (ex: "bike-rental-data-pipeline")
5. Adicione a descrição: "Service account for bike rental data pipeline"
6. Clique em "Create and Continue"

### 2. Conceder Permissões

1. Na seção "Grant this service account access to project"
2. Adicione as seguintes roles:
   - **Storage Object Admin** (para ler/escrever objetos no GCS)
   - **Storage Object Viewer** (para visualizar objetos no GCS)
3. Clique em "Continue" e depois "Done"

### 3. Criar e Baixar a Chave

1. Clique na service account criada
2. Vá para a aba "Keys"
3. Clique em "Add Key" > "Create new key"
4. Selecione "JSON" e clique em "Create"
5. O arquivo JSON será baixado automaticamente

### 4. Configurar as Variáveis de Ambiente

1. Copie o arquivo JSON baixado para um local seguro no seu projeto
2. Configure as seguintes variáveis de ambiente:

```bash
export GOOGLE_APPLICATION_CREDENTIALS="/caminho/para/seu/arquivo-credenciais.json"
export GCS_BUCKET_NAME="nome-do-seu-bucket"
```

## Criar um Bucket no GCS

1. No Google Cloud Console, vá para "Cloud Storage" > "Buckets"
2. Clique em "Create Bucket"
3. Configure:
   - **Name**: Escolha um nome único globalmente (ex: "bike-rental-data-lake")
   - **Location type**: Region
   - **Location**: Escolha uma região próxima (ex: us-central1)
   - **Storage class**: Standard
   - **Access control**: Uniform
4. Clique em "Create"

## Estrutura de Pastas no Bucket

O projeto criará automaticamente a seguinte estrutura:

```
gs://seu-bucket/
├── raw/
│   ├── stations.parquet
│   ├── status.parquet
│   └── trips.parquet
├── trusted/
│   ├── stations.csv
│   ├── status.csv
│   └── trips.csv
└── refined/
    ├── stations.csv
    ├── status.csv
    └── trips.csv
```

## Testando a Configuração

Após configurar tudo, você pode testar executando:

```bash
python utils/gcs/landing_to_raw.py
```

Se tudo estiver configurado corretamente, você verá mensagens de sucesso indicando que os arquivos foram enviados para o GCS.

## Troubleshooting

### Erro: "Could not automatically determine credentials"

- Verifique se a variável `GOOGLE_APPLICATION_CREDENTIALS` está configurada corretamente
- Certifique-se de que o arquivo JSON existe no caminho especificado

### Erro: "Bucket not found"

- Verifique se o nome do bucket está correto na variável `GCS_BUCKET_NAME`
- Certifique-se de que o bucket existe no projeto correto

### Erro: "Permission denied"

- Verifique se a service account tem as permissões necessárias
- Certifique-se de que está usando o projeto correto do Google Cloud 