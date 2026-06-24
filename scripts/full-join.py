import pandas as pd

# Paths to input files
#csv_file = 'miniamie_fb15k237_support_5_maxad3_realsupport.rules'
#csv_file = 'miniamie_nations_support_5_maxad3_realsupport_full.rules'
csv_file = 'miniamie_kinship_support_100_maxad3.rules'
#tsv_file = 'amie_fb15k237_support_5_maxad3.rules'
#tsv_file = 'amie_nations_support_5_maxad3.rules.tsv'
tsv_file = 'amie_kinship_support_5_maxad3.rules'
#output_file = 'full_merged_fb15k237.tsv'
#output_file = 'full_merged_nations.tsv'
output_file = 'full_merged_kinship.tsv'

# Read files
df_csv = pd.read_csv(csv_file)
df_tsv = pd.read_csv(tsv_file, sep='\t')

df_tsv = df_tsv.rename(columns={'Rule': 'rule'})
#df_tsv.drop(columns=['realSupport', 'realHeadCoverage', 'realSupportNano'])

# Merge on 'rule'
merged_df = pd.merge(df_csv, df_tsv, 
                     on='rule', 
                     how='inner')

# Save to TSV
merged_df.to_csv(output_file, sep='\t', index=False)

print(f'Merged file saved to {output_file}')

