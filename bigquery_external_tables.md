# BigQuery External Tables for GCS Data Lake

Este documento contém as consultas SQL para criar tabelas externas no Google BigQuery que se conectam aos dados armazenados no Google Cloud Storage (GCS).

---

### ⚠️ **Atenção**

- **Substitua `seu-projeto-gcp`** pelo ID do seu projeto no Google Cloud.
- **Substitua `seu-dataset`** pelo nome do dataset que você quer usar no BigQuery.
- **Substitua `seu-bucket`** pelo nome do seu bucket no GCS.
- Execute estes comandos no **Editor de Consultas do BigQuery**.

---

## 1. Camada Raw (Formato Parquet)

Os dados brutos estão em formato Parquet, que o BigQuery pode inferir o esquema automaticamente.

### Tabela `stations_raw`
```sql
CREATE OR REPLACE EXTERNAL TABLE `seu-projeto-gcp.seu-dataset.stations_raw`
OPTIONS (
  format = 'PARQUET',
  uris = ['gs://seu-bucket/raw/stations.parquet']
);
```

### Tabela `status_raw`
```sql
CREATE OR REPLACE EXTERNAL TABLE `seu-projeto-gcp.seu-dataset.status_raw`
OPTIONS (
  format = 'PARQUET',
  uris = ['gs://seu-bucket/raw/status.parquet']
);
```

### Tabela `trips_raw`
```sql
CREATE OR REPLACE EXTERNAL TABLE `seu-projeto-gcp.seu-dataset.trips_raw`
OPTIONS (
  format = 'PARQUET',
  uris = ['gs://seu-bucket/raw/trips.parquet']
);
```

---

## 2. Camada Trusted (Formato CSV)

Para arquivos CSV, precisamos definir o esquema explicitamente e pular a linha do cabeçalho.

### Tabela `stations_trusted`
```sql
CREATE OR REPLACE EXTERNAL TABLE `seu-projeto-gcp.seu-dataset.stations_trusted` (
  station_id INT64,
  name STRING,
  latitude FLOAT64,
  longitude FLOAT64,
  dockcount INT64,
  landmark STRING,
  installation_date TIMESTAMP,
  created_at TIMESTAMP
)
OPTIONS (
  format = 'CSV',
  uris = ['gs://seu-bucket/trusted/stations.csv'],
  skip_leading_rows = 1
);
```

### Tabela `status_trusted`
```sql
CREATE OR REPLACE EXTERNAL TABLE `seu-projeto-gcp.seu-dataset.status_trusted` (
  station_id INT64,
  bikes_available INT64,
  docks_available INT64,
  time TIMESTAMP,
  created_at TIMESTAMP
)
OPTIONS (
  format = 'CSV',
  uris = ['gs://seu-bucket/trusted/status.csv'],
  skip_leading_rows = 1
);
```

### Tabela `trips_trusted`
```sql
CREATE OR REPLACE EXTERNAL TABLE `seu-projeto-gcp.seu-dataset.trips_trusted` (
  trip_id INT64,
  duration INT64,
  start_date TIMESTAMP,
  start_station_name STRING,
  start_station_id INT64,
  end_date TIMESTAMP,
  end_station_name STRING,
  end_station_id INT64,
  bike_id INT64,
  subscription_type STRING,
  zip_code STRING,
  created_at TIMESTAMP
)
OPTIONS (
  format = 'CSV',
  uris = ['gs://seu-bucket/trusted/trips.csv'],
  skip_leading_rows = 1
);
```

---

## 3. Camada Refined (Formato CSV)

A camada `refined` tem a mesma estrutura da `trusted`.

### Tabela `stations_refined`
```sql
CREATE OR REPLACE EXTERNAL TABLE `seu-projeto-gcp.seu-dataset.stations_refined` (
  station_id INT64,
  name STRING,
  latitude FLOAT64,
  longitude FLOAT64,
  dockcount INT64,
  landmark STRING,
  installation_date TIMESTAMP,
  created_at TIMESTAMP
)
OPTIONS (
  format = 'CSV',
  uris = ['gs://seu-bucket/refined/stations.csv'],
  skip_leading_rows = 1
);
```

### Tabela `status_refined`
```sql
CREATE OR REPLACE EXTERNAL TABLE `seu-projeto-gcp.seu-dataset.status_refined` (
  station_id INT64,
  bikes_available INT64,
  docks_available INT64,
  time TIMESTAMP,
  created_at TIMESTAMP
)
OPTIONS (
  format = 'CSV',
  uris = ['gs://seu-bucket/refined/status.csv'],
  skip_leading_rows = 1
);
```

### Tabela `trips_refined`
```sql
CREATE OR REPLACE EXTERNAL TABLE `seu-projeto-gcp.seu-dataset.trips_refined` (
  trip_id INT64,
  duration INT64,
  start_date TIMESTAMP,
  start_station_name STRING,
  start_station_id INT64,
  end_date TIMESTAMP,
  end_station_name STRING,
  end_station_id INT64,
  bike_id INT64,
  subscription_type STRING,
  zip_code STRING,
  created_at TIMESTAMP
)
OPTIONS (
  format = 'CSV',
  uris = ['gs://seu-bucket/refined/trips.csv'],
  skip_leading_rows = 1
);
``` 