# Missing-Value-Estimation

## Description
I am given two datasets, that contain missing entries throughout. I fill in these missing entries with estimated values and return the completed dataset

## Details
- Dataset 1 contains 242 genes with 14 samples
- Dataset 2 contains 758 genes with 50 samples
- A missing entry is filled by 1.00000000000000e+99
- There are 4% missing values in Dataset 1
- There are 10% missing values in Dataset 2

## Approach
- For dataset 1, I used a median imputer object to fill in the missing values, due to the lower dataset size
- For dataset 2, I used a mean imputer object to fill in the missing values, due to the larger dataset.


