# BCG GAMMA Challenge 2021 – Datathon - Virtual Event

## Project Description

The Igarapé Institute is an independent think and do tank, dedicated to integrating tasks such as security, climate, and development, whose objective is to propose solutions and partnerships for global problems through research, new technologies, public political influence, and communication. In partnership with BCG GAMMA, both proposed the **BCG GAMMA Challenge 2021 - Datathon - Virtual Event**, to understand Brazilian public security and act in the prevention of violence.

This project is a study proposal, based in `Python` and `Jupyter Notebook`, which aims at the related tasks performed by BCG GAMMA Datathon.

## Usage

Major requirements:
- Python 3
- Pip

Clone the repository and install the requeriments:

```sh
git clone https://github.com/dunfrey/BCG-GAMMA-Challenge-2021 bcg-gamma-challenge
cd bcg-gamma-challenge
pip install -r requirements.txt
```

Integrate BCG GAMMA datasets file:
- Download zip file `GAMMAChallenge21Dados.zip`
- Unzip folders from zip file into `./data` folder ('./data/1. SIM..', './data/2. SINAN..', etc.)

```sh
$ ls ./data
'1. SIM (Homicidios)'
'2. SINAN (violencia sexual)'
'3. Atlas de Desenvolvimento Humano'
'4. MUNIC'
'5. PNAD Contínuo'
'6. Assistencia Social'
'7. INEP'
'8. Bolsa Familia'
```

Integrate extra handled datasets from public sources:
- Download zip file `handled.zip` from https://drive.google.com/file/d/10a3kaiy3wak-08dI9W2hY-kOZkBj-i-N/view?usp=sharing
- Unzip folders from zip file into `./data` folder ('./data/1. SIM..', './data/2. SINAN..', etc.)

```sh
$ ls ./data/handled
cbos.parquet # from MTE
sim_pf_homcidios.parquet
sim_municipio_homicidios.parquet
ibge_municipio_populacao_estimada.parquet
ibge_municipio.parquet
ibge_municipio_censo_basico.parquet
ibge_municipio_pib.parquet
inep_municipio_rendimento_escolar.parquet 
rais_caged_municipio_funcionarios.parquet
rfb_municipio_cnaes.parquet
municipios_features_labeled.parquet # target poulation needed for 2_data_understanding (1.2, 1.3).ipynb
```

Install and activate a virtual environment:
- https://virtualenv.pypa.io/en/latest/user_guide.html

Install python requirements:

```sh
pip install -r requirements.txt
```

Reproduce hypothesis 1 validation (social factors):

```sh
jupyter notebook notebooks/2_data_understanding (1.2, 1.3).ipynb
```

Reproduce hypothesis 2 validation (individual factors):

```sh
jupyter notebook notebooks/2_data_understanding (2.1).ipynb
```

Reproduce target population definition:

```sh
jupyter notebook notebooks/1.2_data_target_population.ipynb
```

### Jupyter Notebook Installation
You can find the installation documentation for the [Jupyter platform, on ReadTheDocs](https://jupyter.readthedocs.io/en/latest/install.html).
The documentation for advanced usage of Jupyter notebook can be found [here](https://jupyter-notebook.readthedocs.io/en/latest/).

For a local installation, make sure you have [pip installed](https://pip.readthedocs.io/en/stable/installing/) and run:

    $ pip install notebook

Launch with:

    $ jupyter notebook

## Repository structure

Base folders:
- `./src/`: contains the scripts that supports the analysis as pre-processing data, plotting graphics, engineering data, helper functions, etc
- `./docs/`: contains the documentation of the project
- `./notebooks/`: contains jupyter notebook experiments needed to collect, explore, prepare data, train and evaluate data.
- `./requirements.txt`: contains python dependencies to reproduce the experiments.

Explore the folder `./notebooks/`, which contains:
- `1.1_data_ingesting`: ingestion of public data, which collects, organizes and prepares common data to be investigated throughout the project;
- `1.2_data_target_population`: prepares the target population of the project. In this project, the target population is young adults between 19 and 25 years old and the level of violence related to them;
- `2_data_understanding (1.2, 1.3)`:
    - Hypothesis (1.2): Regions with more public schools have more education and, consequently, less violence
    - Hypothesis (1.3): Families in cities with high unemployment have low income / lower purchasing power (eg, lower income, minimum wage), which encourages illegal alternatives to increase income and, consequently, conflicts with the police and the tax of homicides
- `2_data_understanding (2.1)`: 
    - The provision of public social assistance services helps to minimize the levels of violence in cities

## Authors

Dunfrey Aragão - https://www.linkedin.com/in/dunfrey/
Fernando Felix - https://www.linkedin.com/in/fernandofnjr/
