# BCG GAMMA Challenge 2021 – Datathon - Virtual Event

## Project Description

The Igarapé Institute is an independent think and do tank, dedicated to integrating tasks such as security, climate, and development, whose objective is to propose solutions and partnerships for global problems through research, new technologies, public political influence, and communication. In partnership with BCG GAMMA, both proposed the **BCG GAMMA Challenge 2021 - Datathon - Virtual Event**, to understand Brazilian public security and act in the prevention of violence.

This project is a study proposal, written in `Python` and `Jupyter Notebook`, which aims at the related tasks performed by BCG GAMMA Datathon.

## Usage

Clone the repository and install the requeriments:

```sh
git clone https://github.com/dunfrey/BCG-GAMMA-Challenge-2021 bcg-gamma-challenge
cd bcg-gamma-challenge
pip install -r requirements.txt
```

The project can be executed in full, obeying the workflow through the following command:
```
python main.py run # Run all model pipeline steps sequencially
```

Or, each step can be performed by the following command:
```
python main.py features # Generate features
python main.py deploy_model # Deploy model
python main.py evaluate_model # Evaluate model
```

For more information:
```
python main.py --help # Shows usage information.
```

## Repository structure

- `scripts`: contains the scripts to collect data
- `docs`: contains the documentation of the project
- `notebooks`: contains jupyter notebook experiments needed to collect, explore, prepare data, train and evaluate data.
- `requirements.txt`: contains python dependencies to reproduce the experiments.
