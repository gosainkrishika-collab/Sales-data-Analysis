import pandas as pd
import numpy as np

sales_df = pd.read_csv('amazon.csv')
print(sales_df.columns)
print(sales_df.dtypes)
print(sales_df.isnull().sum())
sales_df.drop(['product_link','img_link','about_product','user_id','user_name','review_id'],
              axis = 1, inplace = True)
print(sales_df.columns)
# print(np.unique(sales_df['actual_price']))

def dtype_float_convert(val,):
    return val.str.replace(r'[₹, %]', '', regex=True).str.strip().astype('float')

sales_df['actual_price'] = dtype_float_convert(sales_df['actual_price'] )
sales_df['discounted_price'] = dtype_float_convert(sales_df['discounted_price'])

# print(sales_df['actual_price'].dtype)
print(np.unique(sales_df['discount_percentage']))

sales_df['discount_percentage'] = (sales_df['discount_percentage']
                            .str.replace(r'[,%]', '', regex=True)
                            .str.strip().astype('int64')
                            )
print(sales_df['discount_percentage'].dtype)
# sales_df['rating'] = (sales_df['rating'].astype('float'))
print(np.unique(sales_df['rating']))
sales_df['rating'] = (sales_df['rating'].drop())




