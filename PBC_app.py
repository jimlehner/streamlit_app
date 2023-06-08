# -*- coding: utf-8 -*-
"""
Created on Sun Jun  4 11:03:20 2023

@author: james
"""
from matplotlib import pyplot as plt
import pandas as pd  # read csv, df manipulation
import plotly.express as px  # interactive charts
import streamlit as st  # 🎈 data web app development

im="chart_with_upwards_trend"
st.set_page_config(
    page_title="Data in Context",
    page_icon=im)
    #layout="wide")
    #page_icon=r"C:\Users\james\OneDrive\Documents\Streamlit Portfolio\PBCs Imbue Meaning\favicon_CHS",
    #layout="wide")

# read_csv from github repo
dataset_url = "https://raw.githubusercontent.com/jimlehner/datasets/main/sales_data.csv"

# Read csv from URL
def get_data() -> pd.DataFrame:
    return pd.read_csv(dataset_url, index_col=False)

# Create dataframe
df = get_data()
df = df[['Month', 'Sales']]
df1 = df.iloc[10:11]
df2 = df.iloc[10:12]
print(df2)

# Calculate limits 
mean = df['Sales'].mean()
mR = abs(df['Sales'].diff())
AmR = mR.mean()

UPL = mean + (2.66*AmR)
LPL = mean - (2.66*AmR)
URL = (3.27*AmR)

def plot(df, X='Month', Y='Sales'):

    fig = px.line(df, x=X, y=Y, markers=True)

    st.plotly_chart(fig)
    

# Dashboard title
st.title("How Process Behavior Charts establish context and imbue meaning")
st.markdown("### By Jim Lehner")

@st.cache_data
def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation at on every rerun
    return df.to_csv().encode('utf-8')

csv = convert_df(df)

st.download_button(
    label='Download sales data as CSV',
    data=csv,
    file_name='sales_data_df.csv',
    mime='text/csv')

# Sidebar
with st.sidebar:
    st.title("About")
    st.markdown("This project is part of a larger effort to imporve data literacy \
                in manufacturing specifically and business in general.")

# Body text and figures begin
st.markdown("The power and utility of the Process Behavior Chart (PBC) rests \
            in its ability to put data into context. The more readily context \
                is established the faster sources of variation can be \
                    identified and processes optimized. Without context, data \
                        is random and miscellaneous. It tells no story and it \
                            has no structure. Without context, all efforts of \
                                improvement using data are meaningless. Luck \
                                    cannot reliably and repeatedly produce \
                                        results. In order to do that numbers \
                                            must be imbued with meaning through \
                                                context. The most effective way \
                                                    to build context is through \
                                                        the understanding and \
                                                            use of PBCs")
                                                            
st.markdown("Figure 1 shows the sales for November. What were they? They were \
            11,700 units. Is this a lot of sales or a little? Does this signify \
                growth or decline? What actions should the individual, team, or \
                    organization take knowing this information? The lack of \
                        context makes it difficult, if not impossible, to turn \
                            this information into insight and that insight into \
                                action. Establishing a path forward requires \
                                    additional context.")
# First plot
plot(df1)
# =============================================================================
# with st.expander("Figure 1"):
#     st.write("Sales from November were 11,700 units. Aside from a numeric label, what context does this analysis \
#              establish? How does the organization move forward knowing this information?",
#              expanded=True)
# =============================================================================
    
st.caption("Figure 1: Sales from November were 11,700 units. Aside from a numeric label, what context does this analysis \
establish? How does the organization move forward knowing this information?")

st.markdown("For many, context takes the form of comparison similar to Figure 2. \
            What were the sales in November? They were 11,700 units. What were \
                the sales in December? They were 10,600 units. Comparison makes \
                    self evident that 1,100 fewer units were sold in December \
                        than November. Outside of this, what purpose does \
                            comparison serve? Is the reduction in sales cause \
                                for concern? Does this signify the business is \
                                    in decline? How does the individual, team, \
                                        and organization move forward? The lack \
                                            of context makes it difficult to \
                                                turn this information into insight \
                                                    and that insight into action. \
                                                        Often, the actions that \
                                                            result from analysis through comparison are misleading. They task employees to explain the drop even though it has no substantive meaning. Avoiding this mistake requires giving the data additional context.")
# Second plot
plot(df2)
st.caption("Figure 2: Sales dropped by 1,100 units between November and December. Aside from quantifying the reduction in \
sales, what context does this comparison provide? How does the organization move forward?")
st.markdown("One way to impart additional context is with a time series plot as shown in Figure 3. Time series expand the scope of analysis by plotting data over time. Rather than pit two months against each other, time \
series plots imbue meaning by setting the data within the context of the year. This context makes a few things clear. First, ups and downs occurred several times over the course of the year. All systems have \
variation (ups and downs) and the month-to-month sales shown in Figure 3 are no different. Second, in this context focusing on the drop in sales from November to December is misleading. Sales dropped \
from October to November by 4,300 units, a drop four times greater than November to December. Is this drop cause for concern? What about the steady increase in sales from April through July? What was being done in these months that wasn’t done in October through December?")

# Third plot
plot(df)
st.caption("Figure 3: The time series puts the data in the context of a year but are the insights gleaned from this additional \
context enough to establish a path forward? No, the data needs more context.")
st.markdown("While the time series plot gives the data more context, this context does little to explain if the drop in \
sales from October to November is of concern. Moreover, it does nothing to establish a path forward. \
The ambiguous context makes it difficult to turn this information into insight and that insight into action.\
Questions asked in response to the times series plot are little more than glorified comparisons. They try \
2 to explain the ups and downs as individual and isolated events and sets the stage for confusing signals \
with noise. Furthermore, the time series does little to move the individual, team, or organization forward. To do this the data requires additional context.")

st.markdown("As shown in Figure 4, it is occasionally useful to include the arithmetic average (mean), a measure of \
data location, on a time series plot. However, its inclusion is a double edge sword. While the arithmetic \
average establishes an overall location for the data, it also acts as easy fodder for month-to-average \
comparisons. Why were sales in October so much higher than the average? Why were sales in January so \
much lower than the average? What does the consecutive drop away from the average in November and \
December mean for business? While the average establishes additional context in terms of data location, \
it also distracts. It sets the stage for comparisons that do little to move the individual, team, and \
organization forward. To do this the data requires additional context. This context is established in the form of the Process Behavior Chart (PBC).")

# Foruth plot
fig = px.line(df, x='Month', y='Sales', markers=True)
# Process limits and centerline
fig.add_hline(mean, line_dash="dash", line_color="black")
# Write plot to streamlit
st.plotly_chart(fig)
st.caption("Figure 4: The arithmetic average is a measure of data location. Its inclusion on the time series plot makes it ripe for \
month-to-average comparison, an approach that hinders more than it helps.")

st.markdown("Figure 5 puts the sales data in the context of a PBC. Rather than attempt to explain the ups and downs as \
            unique and individual events, the PBC facilitates an understanding of the data as a whole. This is \
achieved with the help of process behavior limits. The process behavior limits define how large or how \
small a single monthly value must be before it represents a departure from the historic average[^1]. A \
monthly value in excess of 17,180, the Upper Process Behavior Limit (UPBL), or below 832, the Lower \
Process Behavior Limit (LPBL), would signal that a shift in sales has occurred. Such a shift would be \
cause for concern and reason for further question and investigation. Since all the data falls within the \
upper and lower process behavior limits no shift in sales has occurred. Any effort to explain how one \
month is better or worse than any other is futile and a waste of time.")


# This is the plotly plot
fig = px.line(df, x='Month', y='Sales', markers=True)
# Process limits and centerline
fig.add_hline(UPL, line_dash="dash", line_color="red")
fig.add_hline(LPL, line_dash="dash", line_color="red")
fig.add_hline(mean, line_dash="dash", line_color="black")
# Write plot to streamlit
st.plotly_chart(fig)
st.caption("Figure 5: While sales appear to be down in some months and up in others, the fluctuations are a routine and \
natural part of the underlying system and no cause for concern.")

st.markdown("While sales appear down in some months and up in others, the fluctuations are routine and a natural \
part of the underlying system that produced them. This system will, unless influenced by an outside \
force, sell on average 12,750 units per month over the course of the year. Furthermore, sales ranging \
from 832 units to 17,180 units should be expected. These values act as a boundary between monthly \
sales that are to be expected and monthly sales that are out of the ordinary. If and only if sales exceed \
17,180 units or drop below 832 units in a given month should questions or concerns be raised. In its \
current form the system sales are predictable. Moving forward, rather than waste time trying to explain \
why sales in some months are higher than sales in others, the organization would benefit from asking a few questions.")

st.markdown("First, what can be done to increase the average sales over the course of the year? Answering this \
question requires a holistic view. Such a view considers the months interconnected and interdependent \
rather than separate and autonomous. Second, what can be done to reduce the range of possible \
monthly sales over the course of the year? At present, a single month can produce sales varying from \
812 units to 17,180 units with no cause for concern. Identifying ways to reduce this variation is \
quintessential to improving overall sales.")

st.markdown("Regardless of exactly how things move forward, one thing is clear. Apart from context, data has no \
meaning. Imbuing data with meaning rests on the ability to establish context. Process Behavior Charts \
establish context by considering the data as a whole. This allows individualis, teams, and organizations to \
focus their time and attention on the things that matter. It allows them to develop more robust products \
and more reliable processes. Luck cannot reliably and repeatedly produce results. In order to do that \
numbers must be imbued with meaning through context. The most effective way to build context is \
through the understanding and use of Process Behavior Charts.")
