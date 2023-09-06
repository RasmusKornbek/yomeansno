from snowflake.snowpark.context import get_active_session
from snowflake.snowpark.functions import sum, col
import altair as alt
import streamlit as st

# Set page config
st.set_page_config(layout="wide")

# Get current session
session = get_active_session()

@st.cache_data()
def load_data():
    # Load CO2 emissions data
    snow_df_co2 = session.table("streamlit.dsi.mytable").filter(col('NAME') == 'Mary').filter(col('PET') == 'All Type').sort('"Date"').with_column_renamed('"Date"','"Year"')

    return snow_df_co2.to_pandas()

# Load and cache data
df_co2_overtime = load_data()
