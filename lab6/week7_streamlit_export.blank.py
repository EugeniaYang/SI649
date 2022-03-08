# Eugenia Yang
# si649w20 altair transforms 2

# imports we will use
import altair as alt
import pandas as pd
from sqlalchemy import case
import streamlit as st

# Title
st.title("Lab6 by Eugenia Yang")

# Import data
df1 = pd.read_csv(
    "https://raw.githubusercontent.com/eytanadar/si649public/master/lab6/hw/data/df1.csv")
df2 = pd.read_csv(
    "https://raw.githubusercontent.com/eytanadar/si649public/master/lab6/hw/data/df2_count.csv")
df3 = pd.read_csv(
    "https://raw.githubusercontent.com/eytanadar/si649public/master/lab6/hw/data/df3.csv")
df4 = pd.read_csv(
    "https://raw.githubusercontent.com/eytanadar/si649public/master/lab6/hw/data/df4.csv")

# change the 'datetime' column to be explicitly a datetime object
df2['datetime'] = pd.to_datetime(df2['datetime'])
df3['datetime'] = pd.to_datetime(df3['datetime'])
df4['datetime'] = pd.to_datetime(df4['datetime'])

# Sidebar
option = st.sidebar.selectbox("Select a visualization to display", [
                              "Vis1", "Vis2", "Vis3", "Vis4"])

# Making of all the charts


# Vis 1

# Interaction requirement 2, change opacity when hover over
selection = alt.selection_single(empty="none", on="mouseover")
opacityCondition = alt.condition(selection, alt.value(1.0), alt.value(0.6))
tooltipCondition = alt.condition(
    selection, alt.Tooltip('EMOJI:N'), alt.value(''))

# Interaction requirement 3 and 4, create brushing filter
brush = alt.selection_interval()
brush2 = alt.selection_interval()

# Static Component - Bars
bar = alt.Chart(df1).mark_bar(
    height=15
).encode(
    x=alt.X('PERCENT:Q', axis=None, scale=alt.Scale(domain=(0, 25)),),
    y=alt.Y('EMOJI:O',
            sort=alt.EncodingSortField(field='-PERCENT'),
            axis=None),
    color=alt.value("orange"),
    text=alt.Text('PERCENT_TEXT:O'),
    tooltip=tooltipCondition,
).transform_filter(
    brush | brush2
)

# Static Component - Emojis
emoji = alt.Chart(df1).mark_text(
    align='center',
    baseline='middle',
).encode(
    x=alt.value(-60),
    y=alt.Y('EMOJI:O',
            sort=alt.EncodingSortField(field='-PERCENT'),
            axis=None),
    text=alt.Text('EMOJI:O'),
).add_selection(brush)

# Static Component - Text
text = alt.Chart(df1).mark_text(
    align='center',
    baseline='middle',
).encode(
    x=alt.value(-20),
    y=alt.Y('EMOJI:O',
            sort=alt.EncodingSortField(field='-PERCENT'),
            axis=None),
    text=alt.Text('PERCENT_TEXT:O'),
).add_selection(brush2)

# Put all together
vis1 = (text + emoji + bar).add_selection(
    selection
).encode(
    opacity=opacityCondition,
).configure_view(
    strokeWidth=0
)


# Vis 2
vis2 = alt.Chart()
#Zooming and Panning
nearest = alt.selection_single(nearest=True, on='mouseover', fields=[
                               'datetime'], empty='none')
selection_int = alt.selection_interval(bind='scales', encodings=['x'])

# vertical line
line = alt.Chart(df2).mark_line(interpolate='basis', size=2.5).encode(
    x=alt.X('datetime:T', title=''),
    y=alt.Y('tweet_count:Q', title='Four-minute rolling average'),
    color='team:N'
)

# interaction dots
selectors = alt.Chart(df2).mark_point(color='black').encode(
    x='datetime:T',
    opacity=alt.value(0),
).add_selection(
    nearest
)
points = line.mark_circle(color='black', size=70).encode(
    color=alt.value("black"),
    opacity=alt.condition(nearest, alt.value(1), alt.value(0)),
    tooltip=['tweet_count:Q', 'datetime', 'team']
)

# Static component line chart
rules = alt.Chart(df2).mark_rule(color='lightgray', size=4).encode(
    x='datetime:T',
).transform_filter(
    nearest
)
# Put all together
vis2 = alt.layer(
    line, selectors, rules, points
).properties(
    width=600, height=300
).add_selection(
    selection_int
).transform_filter(
    selection_int
)

# Vis3

# Altair version

input_radio = alt.binding_radio(options=['🔥', '😴'], name='Select Emoji')
emoji_selection = alt.selection_single(
    fields=['emoji'], bind=input_radio, empty='all', clear=True)
inter_selection = alt.selection_interval(empty='none')

line = alt.Chart(df3).mark_line(interpolate='basis', size=2.5).encode(
    x=alt.X('datetime:T', title='', axis=alt.Axis(tickCount=5)),
    y=alt.Y('tweet_count:Q', title='Four-minute rolling average',
            axis=alt.Axis(tickCount=5)),
    color=alt.Color('emoji:N'),
)

points = alt.Chart(df3).mark_circle(opacity=0.7, color='black').encode(
    x=alt.X('datetime:T', title=''),
    y=alt.Y('tweet_count:Q', title='Four-minute rolling average'),
).transform_filter(
    inter_selection
)

vis3 = (line + points).transform_filter(
    emoji_selection
).add_selection(
    inter_selection,
    emoji_selection
)

# Streamlit widget version


def vis3Streamlit():
    select_emoji = st.radio(
        "Select emoji",
        ('🔥', '😴',))

    if select_emoji == '🔥':
        vis3 = (line + points).transform_filter("datum.emoji=='🔥'").add_selection(
        inter_selection)

    else:
        vis3 = (line + points).transform_filter("datum.emoji=='😴'").add_selection(
        inter_selection)
    st.write(vis3)


# Vis4 BONUS OPTIONAL
emoji_selection = alt.selection_multi(
    fields=['emoji'],  empty='all',  clear=True)
opacityCondition = alt.condition(emoji_selection, alt.value(1), alt.value(0.5))
lines4 = alt.Chart(df4).mark_line(interpolate='basis', size=2.5).encode(
    x=alt.X('datetime:T', title='', axis=alt.Axis(tickCount=5)),
    y=alt.Y('tweet_count:Q', title='Four-minute rolling average',
            axis=alt.Axis(tickCount=5)),
    color=alt.condition(emoji_selection, 'emoji:N',
                        alt.value(''), legend=None),
).properties(
    title='Tears were shed-of joy and sorrow'
)

legend = alt.Chart(df4).mark_text(
    size=20, strokeWidth=0,
).encode(
    y=alt.Y('emoji:N', axis=None),
    text=alt.Y('max(emoji):N', title='Legend'),
    opacity=opacityCondition
).add_selection(
    emoji_selection
).properties(
    title='Legend'
)

vis4 = lines4 | legend
# Altair version

# Streamlit widget version


def vis4Streamlit():
    select_emoji = st.radio(
        "Select emoji",
        ('🤣', '😭',))

    if select_emoji == '🤣':
        emoji_selection = "datum.emoji=='🤣'"

    else:
        emoji_selection = "datum.emoji=='😭'"
    st.write(lines4.encode(
        color=alt.condition(emoji_selection, 'emoji:N',
                            alt.value(''), legend=None)))


# Display graphs
if option == "Vis1":
    st.write(vis1)
elif option == "Vis2":
    st.write(vis2)
elif option == "Vis3":
    st.write(vis3)
    vis3Streamlit()
elif option == "Vis4":
    st.write(vis4)
    vis4Streamlit()
