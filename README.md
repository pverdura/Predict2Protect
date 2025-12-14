# PREDICT TO PROTECT

## BitsXLaMarató 2025
The main focus of this project is to develop a tool that helps detect the genes that can have an effect on reincident cases of Chronic Myelogenous Leukemia patients.

---

### Contributors
- [Alfonso Martinez](https://github.com/MC-Alfonso)
- [Oriol Ventura](https://github.com/Uri-0405)
- [Pol Verdura](https://github.com/pverdura)
- [Max Villalba](https://github.com/maxerrmax)

---
To genotype the KIR genes, the repository [T1K](https://github.com/mourisl/T1K) has been used.

Clone the repository, and create the folder _kir_reference_. Inside, run command `wget ftp://ftp.ebi.ac.uk/pub/databases/ipd/kir/kir.dat` 
In project root, run command `perl t1k-build.pl -d kir_reference/kir.dat -o kir_t1k_index` and create folder _fastq_
