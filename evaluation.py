import pycanon

def evaluate_k_anonymity(data, quasi_identifiers):
    return pycanon.anonymity.k_anonymity(data, quasi_identifiers)

def evaluate_alpha_k_anonymity(data, quasi_identifiers, sensitive_attributes):
    alpha, _ = pycanon.anonymity.alpha_k_anonymity(data, quasi_identifiers, sensitive_attributes)
    return alpha

def calculate_suppression_stats(original_data, anonymized_data):
    records_suppressed = len(original_data) - len(anonymized_data)
    suppression_percentage = 100 * records_suppressed / len(original_data)
    return records_suppressed, suppression_percentage