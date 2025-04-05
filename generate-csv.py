from itertools import product
import pycountry

# Retrieve all ISO 3166-1 alpha-2 country codes
iso_countries = [country.alpha_2 for country in pycountry.countries]

# Generate GF-GT combinations (excluding same-country pairs)
geo_pairs_full = [(gf, gt) for gf, gt in product(iso_countries, repeat=2) if gf != gt]

# Use the previously defined structures with more robust data
types_full = {
    'T': 'Tariff (negative adjustment)',
    'S': 'Subsidy (positive adjustment)',
    'N': 'Non-Tariff Barrier (negative adjustment)',
    'R': 'Relief/Incentive (positive adjustment)'
}

categories_full = {
    '01': 'Market Access Fees',
    '02': 'Export Support Mechanisms',
    '03': 'Trade Compliance Measures',
    '04': 'Emergency or Temporary Policies'
}

subcategories_full = {
    '01': 'MFN Tariff',
    '02': 'Anti-Dumping Duty',
    '03': 'Rebate for Export Growth',
    '04': 'Quota or Licensing',
    '05': 'Disaster Relief Credit',
    '06': 'Carbon Border Adjustment',
    '07': 'Digital Market Access Restriction'
}

ddd_series_full = {
    '1001': 'High Demand Exception',
    '1002': 'Low Supply Surge Tariff',
    '2001': 'Wartime Trade Policy',
    '2002': 'Geopolitical Sanction',
    '2301': 'Climate-based Subsidy',
    '3002': 'Supply Chain Emergency',
    '3101': 'Digital Regulation Conflict',
    '4001': 'Temporary Quarantine Restriction',
    '9999': 'Universal Application'
}

# Limit the dataset to a manageable sample of geo pairs for demonstration
geo_sample = geo_pairs_full[:50]  # generate 50 combinations for initial output

# Build the expanded dataset
expanded_data = []
for (gf, gt) in geo_sample:
    for t_code, t_desc in types_full.items():
        for cat_code, cat_desc in categories_full.items():
            for subcat_code, subcat_desc in subcategories_full.items():
                for dddd, ddesc in ddd_series_full.items():
                    expanded_data.append({
                        'GF': gf,
                        'GT': gt,
                        'Type': t_code,
                        'Type Description': t_desc,
                        'Category Code': cat_code,
                        'Category Description': cat_desc,
                        'Subcategory Code': subcat_code,
                        'Subcategory Description': subcat_desc,
                        'DDDD': dddd,
                        'Detailed Condition': ddesc
                    })

df_expanded = pd.DataFrame(expanded_data)
tools.display_dataframe_to_user(name="Expanded TBF Code Sheet", dataframe=df_expanded)
