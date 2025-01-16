from anjana.anonymity import (
    k_anonymity, alpha_k_anonymity, l_diversity, entropy_l_diversity,
    recursive_c_l_diversity, t_closeness, delta_disclosure,
    basic_beta_likeness, enhanced_beta_likeness
)
import time

from test import quasi_ident, sens_att


def apply_anonymization(method, data, **kwargs):
    start_time = time.time()
    anonymized_data = method(data, **kwargs)
    end_time = time.time()
    return anonymized_data, end_time - start_time

def apply_k_anonymity(data, identifiers, quasi_identifiers, k, suppression_level, hierarchies):
    return apply_anonymization(
        k_anonymity,
        data,
        ident=identifiers,
        quasi_ident=quasi_identifiers,
        k=k,
        supp_level=suppression_level,
        hierarchies=hierarchies
    )

def apply_alpha_k_anonymity(data, identifiers, quasi_identifiers, sensitive_attribute, k, alpha, suppression_level, hierarchies):
    return apply_anonymization(
        alpha_k_anonymity,
        data,
        ident=identifiers,
        quasi_ident=quasi_identifiers,
        sens_att=sensitive_attribute,
        k=k,
        alpha=alpha,
        supp_level=suppression_level,
        hierarchies=hierarchies
    )

def apply_l_diversity(data, identifiers, quasi_identifiers, sensitive_attribute, k, l, suppression_level, hierarchies):
    return apply_anonymization(
        l_diversity,
        data,
        ident=identifiers,
        quasi_ident=quasi_identifiers,
        sens_att=sensitive_attribute,
        k=k,
        l_div=l,
        supp_level=suppression_level,
        hierarchies=hierarchies
    )

def apply_entropy_l_diversity(data, identifiers, quasi_identifiers, sensitive_attribute, k, l, suppression_level, hierarchies):
    return apply_anonymization(
        entropy_l_diversity,
        data,
        ident=identifiers,
        quasi_ident=quasi_identifiers,
        sens_att=sensitive_attribute,
        k=k,
        l_div=l,
        supp_level=suppression_level,
        hierarchies=hierarchies
    )

def apply_recursive_c_l_diversity(data, identifiers, quasi_identifiers, sensitive_attribute, k, c, l, suppression_level, hierarchies):
    return apply_anonymization(
        recursive_c_l_diversity,
        data,
        ident=identifiers,
        quasi_ident=quasi_identifiers,
        sens_att=sensitive_attribute,
        k=k,
        c=c,
        l_div=l,
        supp_level=suppression_level,
        hierarchies=hierarchies
    )

def apply_t_closeness(data, identifiers, quasi_identifiers, sensitive_attribute, k, t, suppression_level, hierarchies):
    return apply_anonymization(
        t_closeness,
        data,
        ident=identifiers,
        quasi_ident=quasi_identifiers,
        sens_att=sensitive_attribute,
        k=k,
        t=t,
        supp_level=suppression_level,
        hierarchies=hierarchies
    )

def apply_delta_disclosure(data, identifiers, quasi_identifiers, sensitive_attribute, k, delta, suppression_level, hierarchies):
    return apply_anonymization(
        delta_disclosure,
        data,
        ident=identifiers,
        quasi_ident=quasi_identifiers,
        sens_att=sensitive_attribute,
        k=k,
        delta=delta,
        supp_level=suppression_level,
        hierarchies=hierarchies
    )

def apply_basic_beta_likeness(data, identifiers, quasi_identifiers, sensitive_attribute, k, beta, suppression_level, hierarchies):
    return apply_anonymization(
        basic_beta_likeness,
        data,
        ident=identifiers,
        quasi_ident=quasi_identifiers,
        sens_att=sensitive_attribute,
        k=k,
        beta=beta,
        supp_level=suppression_level,
        hierarchies=hierarchies
    )

def apply_enhanced_beta_likeness(data, identifiers, quasi_identifiers, sensitive_attribute, k, beta, suppression_level, hierarchies):
    return apply_anonymization(
        enhanced_beta_likeness,
        data,
        ident=identifiers,
        quasi_ident=quasi_identifiers,
        sens_att=sensitive_attribute,
        k=k,
        beta=beta,
        supp_level=suppression_level,
        hierarchies=hierarchies
    )