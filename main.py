from config import *
from data_loader import load_dataset, load_hierarchies
from anonymization_methods import apply_k_anonymity, apply_alpha_k_anonymity, apply_l_diversity
from evaluation import evaluate_k_anonymity, evaluate_alpha_k_anonymity, calculate_suppression_stats

def run_anonymization_method(method, data, **kwargs):
    anonymized_data, elapsed_time = method(data, **kwargs)
    print(f"Elapsed time: {elapsed_time:.2f} seconds")
    
    k_value = evaluate_k_anonymity(anonymized_data, QUASI_IDENTIFIERS)
    print(f"Value of k calculated: {k_value}")
    
    if method == apply_alpha_k_anonymity:
        alpha_value = evaluate_alpha_k_anonymity(anonymized_data, QUASI_IDENTIFIERS, [SENSITIVE_ATTRIBUTE])
        print(f"Value of alpha calculated: {alpha_value}")
    
    records_suppressed, suppression_percentage = calculate_suppression_stats(data, anonymized_data)
    print(f"Number of records suppressed: {records_suppressed}")
    print(f"Percentage of records suppressed: {suppression_percentage:.2f}%")
    
    return anonymized_data

def main():
    data = load_dataset()
    hierarchies = load_hierarchies()
    
    print("Applying k-anonymity:")
    k_anon_data = run_anonymization_method(
        apply_k_anonymity,
        data,
        identifiers=IDENTIFIERS,
        quasi_identifiers=QUASI_IDENTIFIERS,
        k=K,
        suppression_level=SUPPRESSION_LEVEL,
        hierarchies=hierarchies
    )
    k_anon_data.to_csv(f"{OUTPUT_DIR}/adult_k{K}_Sup{SUPPRESSION_LEVEL}.csv", index=False)
    
    print("\nApplying alpha-k-anonymity:")
    alpha_k_anon_data = run_anonymization_method(
        apply_alpha_k_anonymity,
        data,
        identifiers=IDENTIFIERS,
        quasi_identifiers=QUASI_IDENTIFIERS,
        sensitive_attribute=SENSITIVE_ATTRIBUTE,
        k=K,
        alpha=ALPHA,
        suppression_level=SUPPRESSION_LEVEL,
        hierarchies=hierarchies
    )
    alpha_k_anon_data.to_csv(f"{OUTPUT_DIR}/adult_k{K}_A{ALPHA}_Sup{SUPPRESSION_LEVEL}.csv", index=False)
    # l_diverse_data = run_anonymization_method(
    #     apply_l_diversity,
    #     data,
    #     identifiers=IDENTIFIERS,
    #     quasi_identifiers=QUASI_IDENTIFIERS,
    #     sensitive_attribute=SENSITIVE_ATTRIBUTE,
    #     k=K,
    #     l=L,
    #     suppression_level=SUPPRESSION_LEVEL,
    #     hierarchies=hierarchies
    # )
    # l_diverse_data.to_csv(f"{OUTPUT_DIR}/adult_k{K}_L{L}_Sup{SUPPRESSION_LEVEL}.csv", index=False)

if __name__ == "__main__":
    main()