# ALLELATOR

## BitsXLaMarató 2025 - PREDICT TO PROTECT

The main focus of this project is to develop a tool that helps detect the genes that can have an effect on reincident cases of Chronic Myelogenous Leukemia patients.


## Repository

This project is distributed into 2 branches. The `main` branch contains the AI model, and the `master` branch contains the T1K code we used and extended to analyse the allele data.

### How to configure the environment

First we need to create a virtual environment and download all the required packages to execute the main code:

```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Once the packages are downloaded we can configure the environment with the following command:

```
make config
```

---

### To Do List

List of tasks to do in this project:

- [ ] Update model code
- [ ] Improve the genereated charts
- [ ] Create validation model the code
- [ ] Integrate medication days in the model
- [ ] Check and test all functionalities
- [ ] Create a functional interface

---

### Contributors
- [Alfonso Martinez](https://github.com/MC-Alfonso)
- [Oriol Ventura](https://github.com/Uri-0405)
- [Pol Verdura](https://github.com/pverdura)
- [Max Villalba](https://github.com/maxerrmax)


To genotype the KIR genes, the repository [T1K](https://github.com/mourisl/T1K) has been used.
