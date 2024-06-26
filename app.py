import datetime
import json
import numpy as np
import requests
import pandas as pd
import streamlit as st
from copy import deepcopy
from fake_useragent import UserAgent
from footer_utils import image, link, layout, footer

# browser_header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}
# browser_header = {'User-Agent': 'Mozilla/5.0 (Linux; Android 10; ONEPLUS A6000) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.99 Mobile Safari/537.36'}

st.set_page_config(layout='wide',
                   initial_sidebar_state='collapsed',
                   page_icon="http://nasbeer.com/wp-content/uploads/2019/08/cropped-Original-3.png",
                   page_title="CoWIN Slot Availability Checker | Nasbeer")

@st.cache(allow_output_mutation=True, suppress_st_warning=True)
def load_mapping():
    df = pd.read_csv("district_mapping.csv")
    return df

def filter_column(df, col, value):
    df_temp = deepcopy(df.loc[df[col] == value, :])
    return df_temp

def filter_capacity(df, col, value):
    df_temp = deepcopy(df.loc[df[col] > value, :])
    return df_temp

@st.cache(allow_output_mutation=True)
def Pageviews():
    return []

mapping_df = load_mapping()

rename_mapping = {
    'date': 'Available Dates',
    'min_age_limit': 'Age Limit',
    'available_capacity': 'No of Vaccines',
    'available_capacity_dose1': 'First Dose',
    'available_capacity_dose2': 'Second Dose',
    #'slots': 'Slots',
    'vaccine': 'Vaccine',
    'pincode': 'Pincode',
    'name': 'Hospital Name',
    'address': 'Address',
    # 'state_name': 'State',
    # 'district_name': 'District',
    'block_name': 'Block Name',
    'fee_type': 'Fees'
    }

st.title('CoWIN Slot Availability Checker')
st.info('The CoWIN APIs are geo-fenced so sometimes you may not see an output! Please try after sometime if its showing error ')

valid_states = list(np.unique(mapping_df["state_name"].values))

left_column_1, center_column_1, right_column_1 = st.beta_columns(3)
with left_column_1:
    numdays = st.slider('Select upcoming no of days from today', 0, 100, 3)
   #numdays = st.sidebar.date_input("When's your birthday", datetime.date(2019, 7, 6))
with center_column_1:
    state_inp = st.selectbox('Select State', ["Kerala"] + valid_states)
    if state_inp != "":
        mapping_df = filter_column(mapping_df, "state_name", state_inp)


mapping_dict = pd.Series(mapping_df["district id"].values,
                         index = mapping_df["district name"].values).to_dict()

#numdays = st.sidebar.slider('Select Date Range', 0, 100, 10)
#numdays = st.sidebar.date_input("When's your birthday", datetime.date(2019, 7, 6))
unique_districts = list(mapping_df["district name"].unique())
unique_districts.sort()
with right_column_1:
    dist_inp = st.selectbox('Select District', unique_districts)

DIST_ID = mapping_dict[dist_inp]

base = datetime.datetime.today()
date_list = [base + datetime.timedelta(days=x) for x in range(numdays)]
date_str = [x.strftime("%d-%m-%Y") for x in date_list]

temp_user_agent = UserAgent()
browser_header = {'User-Agent': temp_user_agent.random}

final_df = None
for INP_DATE in date_str:
    URL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id={}&date={}".format(DIST_ID, INP_DATE)
    response = requests.get(URL, headers=browser_header)
    if (response.ok) and ('centers' in json.loads(response.text)):
        resp_json = json.loads(response.text)['centers']
        if resp_json is not None:
            df = pd.DataFrame(resp_json)
            if len(df):
                df = df.explode("sessions")
                df['min_age_limit'] = df.sessions.apply(lambda x: x['min_age_limit'])
                df['vaccine'] = df.sessions.apply(lambda x: x['vaccine'])
                #df['slots'] = df.sessions.apply(lambda x: x['slots'])
                df['available_capacity'] = df.sessions.apply(lambda x: x['available_capacity'])
                df['available_capacity_dose1'] = df.sessions.apply(lambda x: x['available_capacity_dose1'])
                df['available_capacity_dose2'] = df.sessions.apply(lambda x: x['available_capacity_dose2'])
                df['date'] = df.sessions.apply(lambda x: x['date'])
               # hospital = dict("name", "**address")
                df = df[["date", "available_capacity", "available_capacity_dose1", "available_capacity_dose2", "vaccine", "min_age_limit", "pincode", "name", "address", "block_name", "fee_type"]]
                if final_df is not None:
                    final_df = pd.concat([final_df, df])
                else:
                    final_df = deepcopy(df)
        else:
            st.error("No rows in the data Extracted from the API")
#     else:
#         st.error("Invalid response")

if (final_df is not None) and (len(final_df)):
    final_df.drop_duplicates(inplace=True)
    final_df.rename(columns=rename_mapping, inplace=True)

    left_column_2, center_column_2, right_column_2, right_column_2a,  right_column_2b,  right_column_2c = st.beta_columns(6)
    with left_column_2:
        valid_pincodes = list(np.unique(final_df["Pincode"].values))
        pincode_inp = st.selectbox('Select Pincode', [""] + valid_pincodes)
        if pincode_inp != "":
            final_df = filter_column(final_df, "Pincode", pincode_inp)

    with center_column_2:
        valid_age = [18, 40, 45]
        age_inp = st.selectbox('Select Age Limits', [""] + valid_age)
        if age_inp != "":
            final_df = filter_column(final_df, "Age Limit", age_inp)

    with right_column_2:
        valid_payments = ["Free", "Paid"]
        pay_inp = st.selectbox('Select Free or Paid', [""] + valid_payments)
        if pay_inp != "":
            final_df = filter_column(final_df, "Fees", pay_inp)

    with right_column_2a:
        valid_dose1 = [1]
        doseo_inp = st.selectbox('Select Dose 1', [""] + valid_dose1)
        if doseo_inp != "":
            final_df = filter_capacity(final_df, "First Dose", doseo_inp)

    with right_column_2b:
        valid_dose2 = [1]
        doset_inp = st.selectbox('Select Dose 2', [""] + valid_dose2)
        if doset_inp != "":
            final_df = filter_column(final_df, "Second Dose", doset_inp)

    with right_column_2c:
        valid_vaccines = ["COVISHIELD", "COVAXIN", "SPUTNIK"]
        vaccine_inp = st.selectbox('Select Vaccine', [""] + valid_vaccines)
        if vaccine_inp != "":
            final_df = filter_column(final_df, "Vaccine", vaccine_inp)


    table = deepcopy(final_df)
    table.reset_index(inplace=True, drop=True)
    st.table(table)
else:
    st.error("Unable to fetch data currently, please try with other set of data..")

# footer="""<style>
# a:link , a:visited{
# color: blue;
# background-color: transparent;
# text-decoration: underline;
# }

# a:hover,  a:active {
# color: red;
# background-color: transparent;
# text-decoration: underline;
# }

# .footer {
# position: fixed;
# left: 0;
# bottom: 0;
# width: 100%;
# background-color: white;
# color: black;
# text-align: center;
# }
# </style>
# <div class="footer">
# <p>Developed with ❤ by <a style='display: block; text-align: center;' href="https://nasbeer.com" target="_blank">Nasbeer Ahammed</a></p>
# </div>
# """
# st.markdown(footer,unsafe_allow_html=True)
# st.markdown("_- Nasbeer Ahammed_")

pageviews=Pageviews()
pageviews.append('dummy')
pg_views = len(pageviews)
footer(pg_views)
