import pandas as pd

# Paths to input files
csv_file = 'miniamie_nations_support_5_maxad3_realsupport_full.rules'
tsv_file = 'amie_nations_support_5_maxad3.rules.tsv'
output_file = 'merged_nations.tsv'
#csv_file = 'miniamie_fb15k237_support_5_maxad3_realsupport.rules'
#tsv_file = 'amie_fb15k237_support_5_maxad3.rules'
#output_file = 'merged_fb15k237.tsv'

# Read files
df_csv = pd.read_csv(csv_file)
df_tsv = pd.read_csv(tsv_file, sep='\t')

df_tsv = df_tsv.rename(columns={'Rule': 'rule'})

# Merge on 'rule'
merged_df = pd.merge(df_csv[['rule', 'appPCAConfidence']], 
                     df_tsv[['rule', 'Pca Confidence']], 
                     on='rule', 
                     how='inner')

# Save to TSV
merged_df.to_csv(output_file, sep='\t', index=False)

print(f'Merged file saved to {output_file}')

