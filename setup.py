from setuptools import setup, find_packages

setup(
    name="bike-rental-pipeline",
    version="1.0.0",
    description="Bike rental data pipeline with PostgreSQL and Google Cloud Storage",
    author="Your Name",
    packages=find_packages(),
    install_requires=[
        "faker",
        "sqlalchemy",
        "pyyaml",
        "psycopg2-binary",
        "boto3",
        "pandas",
        "pyarrow",
        "google-cloud-storage",
        "apache-beam",
        "python-dotenv",
    ],
    python_requires=">=3.8",
) 