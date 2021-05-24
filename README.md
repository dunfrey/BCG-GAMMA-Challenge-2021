# BCG GAMMA Challenge 2021 – Datathon - Virtual Event

## Project Description

The Igarapé Institute is an independent think and do tank, dedicated to integrating tasks such as security, climate, and development, whose objective is to propose solutions and partnerships for global problems through research, new technologies, public political influence, and communication. In partnership with BCG GAMMA, both proposed the **BCG GAMMA Challenge 2021 - Datathon - Virtual Event**, to understand Brazilian public security and act in the prevention of violence.

This project is a study proposal, based in `Python` and `Jupyter Notebook`, which aims at the related tasks performed by BCG GAMMA Datathon.

## Usage

Clone the repository and install the requeriments:

```sh
git clone https://github.com/dunfrey/BCG-GAMMA-Challenge-2021 bcg-gamma-challenge
cd bcg-gamma-challenge
pip install -r requirements.txt
```
Explore the folder `\notebooks`, which contains:
- **1.1_data_ingesting**: ingestion of public data, which collects, organizes and prepares common data to be investigated throughout the project;
- **1.2_data_target_population**: prepares the target population of the project. In this project, the target population is young adults between 15 and 29 years old and the level of violence related to them;
- **2_data_understanding (1.2, 1.3)**:
    - Hypothesis (1.2): Regions with more public schools have more education and, consequently, less violence
    - Hypothesis (1.3): Families in cities with high unemployment have low income / lower purchasing power (eg, lower income, minimum wage), which encourages illegal alternatives to increase income and, consequently, conflicts with the police and the tax of homicides
- **2_data_understanding (2.1)**: 
    - The provision of public social assistance services helps to minimize the levels of violence in cities

In the `\src` folder there are codes that help (support) the codes contained in `\notebooks`.

## Repository structure

- `src`: contains the scripts that supports the analysis as pre-processing data, plotting graphics, engineering data, etc
- `docs`: contains the documentation of the project
- `notebooks`: contains jupyter notebook experiments needed to collect, explore, prepare data, train and evaluate data.
- `requirements.txt`: contains python dependencies to reproduce the experiments.
