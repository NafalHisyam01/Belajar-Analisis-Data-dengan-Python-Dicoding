import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')


#load all_data
all_data = pd.read_csv('all_data.csv')


#Produk yang paling banyak dan paling sedikit terjual
st.subheader("Best & Worst Performing Product")

sum_order_items_df = all_data.groupby(by='product_category_name_english')['product_id'].count().reset_index().sort_values(by = 'product_id', ascending = False)
 
fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(35, 15))

colors = ["#068DA9", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]

sns.barplot(x="product_id", y="product_category_name_english", data=sum_order_items_df.head(5), palette=colors, ax=ax[0])

ax[0].set_ylabel(None)
ax[0].set_xlabel(None)
ax[0].set_title("Best Performing", loc="center", fontsize = 50)
ax[0].tick_params(axis ='y', labelsize = 35)
ax[0].tick_params(axis ='x', labelsize = 30)

sns.barplot(x="product_id", y="product_category_name_english", data=sum_order_items_df.sort_values(by="product_id", ascending=True).head(5), palette=colors, ax=ax[1])

ax[1].set_ylabel(None)
ax[1].set_xlabel(None)
ax[1].invert_xaxis()
ax[1].yaxis.set_label_position("right")
ax[1].yaxis.tick_right()
ax[1].set_title("Worst Performing", loc="center", fontsize = 50)
ax[1].tick_params(axis='y', labelsize=35)
ax[1].tick_params(axis='x', labelsize=30)

st.pyplot(fig)


#Demografi pelanggan
st.subheader('Customers Demographics')

#customer by city
cust_bycity_df = all_data.groupby(by='customer_city')['customer_id'].count().reset_index().sort_values(by = 'customer_id', ascending = False)

colors = ["#068DA9", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]

plt.figure(figsize=(10, 8))

sns.set(style = 'darkgrid')
sns.barplot(x = 'customer_city', y = 'customer_id', data = cust_bycity_df.sort_values(by="customer_id", ascending=False).head(5), palette = colors)

plt.xlabel('City')
plt.ylabel(None)
plt.title('Customer city')

st.pyplot()

#customer by state
cust_bystate_df = all_data.groupby(by='customer_state')['customer_id'].count().reset_index().sort_values(by = 'customer_id', ascending = False)

colors = ["#068DA9", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]

plt.figure(figsize=(10, 8))

sns.set(style = 'darkgrid')
sns.barplot(x = 'customer_state', y = 'customer_id', data = cust_bystate_df.sort_values(by="customer_id", ascending=False).head(5), palette = colors)

plt.xlabel('State')
plt.ylabel(None)
plt.title('Customer State')

st.pyplot()


#demografi seller
st.subheader('Seller Demographic')

#seller by city
seller_bycity_df = all_data['seller_city'].value_counts().sort_values(ascending=False).head(5)

most_common_score = seller_bycity_df.idxmax()

sns.set(style="darkgrid")

plt.figure(figsize=(10, 8))
sns.barplot(x=seller_bycity_df.index,
            y=seller_bycity_df.values,

            palette=["#068DA9" if score == most_common_score else "#D3D3D3" for score in seller_bycity_df.index]
            )
plt.xlabel('City')
plt.ylabel(None)
plt.title('Seller City')

st.pyplot()


#seller by state
seller_bystate_df = all_data['seller_state'].value_counts().sort_values(ascending=False).head(5)

most_common_score = seller_bystate_df.idxmax()

sns.set(style="darkgrid")

plt.figure(figsize=(10, 8))
sns.barplot(x=seller_bystate_df.index,
            y=seller_bystate_df.values,

            palette=["#068DA9" if score == most_common_score else "#D3D3D3" for score in seller_bystate_df.index]
            )
plt.xlabel('State')
plt.ylabel(None)
plt.title('Seller State')

st.pyplot()


#most payment types
st.subheader('Most Panyment Types')

type_payment_df = all_data['payment_type'].value_counts().sort_values(ascending=False)

most_common_score = type_payment_df.idxmax()

sns.set(style = 'darkgrid')

plt.figure(figsize = (10, 8))
sns.barplot(x = type_payment_df.index,
            y = type_payment_df.values,
            palette =["#068DA9" if score == most_common_score else '#D3D3D3' for score in type_payment_df.index] )
plt.xlabel(None)

st.pyplot()