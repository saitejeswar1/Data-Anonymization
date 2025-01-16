# Privacy Enhancement: Data Anonymization Tool

## Overview

Privacy Umbrella is a comprehensive data anonymization tool that implements various anonymization techniques using the Anjana library. This project aims to provide a flexible and easy-to-use interface for applying different anonymization methods to datasets, with a focus on maintaining privacy while preserving data utility.

## Features

- Supports multiple anonymization techniques:
  - k-anonymity
  - (α,k)-anonymity
  - ℓ-diversity
  - Entropy ℓ-diversity
  - Recursive (c,ℓ)-diversity
  - t-closeness
  - δ-disclosure privacy
  - Basic β-likeness
  - Enhanced β-likeness
- Modular design following SOLID principles
- Configurable parameters for each anonymization method
- Evaluation metrics for assessing anonymization quality
- Support for hierarchical data generalization

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/Privacy_Umbrella.git
   cd Privacy_Umbrella/Anonymization_anjana
    ```
2. Install the required dependencies
3. Ensure you have the Anjana library installed. If not, install it using:
    ```bash
   pip install anjana
   ```


## Configuration

Edit the `config.py` file to set up your anonymization parameters:

- `DATA_PATH`: Path to your input dataset
- `HIERARCHY_DIR`: Directory containing hierarchy files for generalization
- `OUTPUT_DIR`: Directory for saving anonymized datasets
- `QUASI_IDENTIFIERS`: List of quasi-identifier columns
- `IDENTIFIERS`: List of identifier columns
- `SENSITIVE_ATTRIBUTE`: Name of the sensitive attribute column
- `K`, `ALPHA`, `L`, `C`, `T`, `DELTA`, `BETA`: Parameters for different anonymization techniques
- `SUPPRESSION_LEVEL`: Suppression level for anonymization

## Usage

Run the main script to perform anonymization:

   ```bash
   python main.py
   ```

This will apply the configured anonymization methods to your dataset and save the results in the specified output directory.

## Adding New Anonymization Methods

To add a new anonymization method:

1. Add the method to `anonymization_methods.py`
2. Update `config.py` with any new parameters
3. Modify `main.py` to include the new method in the anonymization process

## Evaluation

The `evaluation.py` module provides functions to assess the quality of anonymization, including:

- k-anonymity verification
- α-k-anonymity verification
- Calculation of suppressed records

## Contributing

Contributions to this project are welcome! Please feel free to submit a Pull Request.


## Acknowledgments

- Anjana library for providing the core anonymization algorithms

