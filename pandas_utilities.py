def check_df_for_primary_key(df, key_col):
  try:
    assert len(df) == len(df['lead_id'].unique())
    print("Yes, {} is a primary key with {} rows".format(key_col, len(df)))
  except:
    print("No, {} is not a primary key".format(key_col))
