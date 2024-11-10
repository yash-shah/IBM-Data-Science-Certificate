

from IPython.display import display, HTML
display(HTML("<style>.container { width:95% !important; }</style>"))

#-------  For centering figures 
from IPython.core.display import HTML
HTML("""
<style>
.output_png {
    display: table-cell;
    text-align: center;
    vertical-align: middle;
}
</style>
""")

"""#### Installation for local implementation."""

!pip install matplotlib
!pip install plotly
#!pip install pandas dash
#!pip install sklearn
!pip install pandas
#!pip install fairlearn
#!pip install bokeh
#!pip install matplotlib
!pip install plotly
!pip uninstall werkzeug  --y
!pip install werkzeug==2.0.1
#!pip uninstall dash --y
!pip install dash
#!pip install pandas dash
!pip install jupyter-dash
!pip install Flask==2.1.0
#!pip install environ

#!pip install jupyter-server-proxy
!pip install wget

import wget
import pandas as pd

# Import required libraries  based on "US domestic airline flights performance" assignment in previous course
import pandas as pd
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State
#from jupyter_dash import JupyterDash
import plotly.graph_objects as go
import plotly.express as px
from dash import no_update

# Import required libraries
#from jupyter_dash import JupyterDash

from jupyter_dash.comms import _send_jupyter_config_comm_request
#_send_jupyter_config_comm_request()

from jupyter_dash import JupyterDash

!wget "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/datasets/spacex_launch_dash.csv"

###!wget "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/labs/module_3/spacex_dash_app.py"

"""<span style="color:#0094cf;"> spacex_dash_app.py was opened locally with IDLE Python 3.10. <br>  The content of the app is copied in the following cells and modified. <br> Notes below: <b> some instructions are obsolete ! </b> </span>"""

# Import required libraries  # Done already -  based on "US domestic airline flights performance" assignement in previous course
#mport pandas as pd
#import dash
#import dash_html_components as html    # OBSOLETE !
#import dash_core_components as dcc     # OBSOLETE !
#from dash.dependencies import Input, Output
#import plotly.express as px

# Read data into pandas dataframe
spacex_df = pd.read_csv("spacex_launch_dash.csv")
max_payload = spacex_df['Payload Mass (kg)'].max()
min_payload = spacex_df['Payload Mass (kg)'].min()
print(max_payload)
print(min_payload)

print(spacex_df.shape)
print(spacex_df.dtypes)
spacex_df.head()

"""#### TASK 1: Add a Launch Site Drop-down Input Component  
We have four different launch sites and we would like to first see which one has the largest success count. Then, we would like to select one specific site and check its detailed success rate (class=0 vs. class=1).

As such, we will need a dropdown menu to let us select different launch sites.

Find and complete a commented dcc.Dropdown(id='site-dropdown',...) input with following attributes:
id attribute with value site-dropdown
options attribute is a list of dict-like option objects (with label and value attributes). You can set the label and value all to be the launch site names in the spacex_df and you need to include the default All option. e.g.,
  options=[{'label': 'All Sites', 'value': 'ALL'},{'label': 'site1', 'value': 'site1'}, ...]
value attribute with default dropdown value to be ALL meaning all sites are selected
placeholder attribute to show a text description about this input area, such as Select a Launch Site here
searchable attribute to be True so we can enter keywords to search launch sites
    
    
"""

# DONE ALREADY - 

#dcc.Dropdown(id='id',
 #               options=[
  #                  {'label': 'All Sites', 'value': 'ALL'},
  #                  {'label': 'site1', 'value': 'site1'},
  #              ],
  #              value='ALL',
  #              placeholder="place holder here",
#             searchable=True
#                ),

"""##    Preliminary activities

<span style="color:#0094cf;"> **Preliminary tests for improving pie charts**: Here we test px.pie with options for freezing colors in 'class count' and add nice features: <br> 
<span style="color:#0094cf;">* Red= failure  --  Green or Blue=success. </span> <br>
<span style="color:#0094cf;">* We change the legend labels. </span> <br>
<span style="color:#0094cf;">* we use a nice color palette   </span>  https://plotly.com/python/discrete-color/  <br>
<span style="color:#0094cf;">* we add the total number of launch attempts per site. </span>
"""

#fig1 = px.colors.qualitative.swatches()
#fig1.show()

entered_site='CCAFS LC-40'
filtered_df=spacex_df[spacex_df['Launch Site']== entered_site]
filtered_df=filtered_df.groupby(['Launch Site','class']).size().reset_index(name='class count')
print(filtered_df.head())
failure_count= filtered_df['class count'][0]
success_count= filtered_df['class count'][1]
total_number_launch=filtered_df['class count'].sum()
print(total_number_launch)
#fig=px.pie(filtered_df,values='class count',names='class',title=f"Total Success Launches for site {entered_site}")
#fig=px.pie(filtered_df,values=[failure_count, success_count],names='class',title=f"Total Success Launches for site {entered_site}")
#fig=px.pie(filtered_df,values=[failure_count, success_count],names=['Failures', 'Success'],       title=f"Total Success Launches for site {entered_site}")
#fig=px.pie(filtered_df,values=[failure_count, success_count],names=['Failures', 'Success'], color=['Failures', 'Success'], color_discrete_map={'Failures':'red',
#'Success':'green'}, color_discrete_sequence=px.colors.qualitative.Pastel, title=f"<b>Launches outcome for site {entered_site}</b>")
#fig=px.pie(filtered_df,values=[failure_count, success_count],names=['Failures', 'Success'], color=['Failures', 'Success'], color_discrete_map={'Failures':'red',
#'Success':'green'}, title=f"<b>Launches outcome for site {entered_site}</b>")
fig=px.pie(filtered_df,values=[failure_count, success_count],names=['<b>Failure</b>', '<b>Success</b>'], color=['Failure', 'Success'], 
           color_discrete_map={'Failure':px.colors.qualitative.G10[1],
           'Success':px.colors.qualitative.G10[5]}, 
           title=f"<b>Launch attempts outcome (%) for site {entered_site}</b>  <br>Total Number of attempts= {total_number_launch} ")
#px.colors.qualitative.Alphabet[6],
#px.colors.qualitative.Alphabet[11]
fig.show()

""" <span style="color:#0094cf;">  **Preliminary tests for improving px.scatter graph** </span>"""

import numpy as np
list = [0  , 10000]
payload=np.array(list)
filtered_df = spacex_df[spacex_df['Payload Mass (kg)'].between(payload[0],payload[1])]
entered_site='CCAFS LC-40'   
fig=px.scatter(filtered_df[filtered_df['Launch Site']==entered_site],       
               x='Payload Mass (kg)',y='class',color='Booster Version Category',
                    title=f"<b>Launch outcome v. payload mass for site {entered_site}</b>")
fig.update_traces(marker=dict(size=12,
                              line=dict(width=2,
                                        color='DarkSlateGrey')),
                  selector=dict(mode='markers'))

"""##    Dash application and Callback function

<span style="color:#0094cf;"> **The development of the Dash application starts here.** </span>
"""

spacex_df['Launch Site'].unique()  # for building Dropdown

# Create a dash application
#app = dash.Dash(__name__)

# Works on Google COLAB
app = JupyterDash(__name__)
JupyterDash.infer_jupyter_proxy_config()   



# Create an app layout
app.layout = html.Div(children=[html.H1('SpaceX Launch Records Dashboard',
                                        style={'textAlign': 'center', 'color': '#503D36',
                                               'font-size': 40}),
                                # TASK 1: Add a dropdown list to enable Launch Site selection
                                # The default select value is for ALL sites
                                # dcc.Dropdown(id='site-dropdown',...)
                                dcc.Dropdown(id='site-dropdown',
                                             options=[
                                                     {'label': 'All Sites', 'value': 'ALL'},
                                                     {'label': 'CCAFS LC-40', 'value': 'CCAFS LC-40'},
                                                     {'label': 'VAFB SLC-4E', 'value': 'VAFB SLC-4E'},
                                                     {'label': 'KSC LC-39A', 'value': 'KSC LC-39A'},
                                                     {'label': 'CCAFS SLC-40', 'value': 'CCAFS SLC-40'}
                                                     ],
                                        value='ALL',
                                        placeholder='Select a Launch Site',
                                        searchable=True
                                             ),
                                
                                html.Br(),

                                # TASK 2: Add a pie chart to show the total successful launches count for all sites
                                # If a specific launch site was selected, show the Success vs. Failed counts for the site
                                html.Div(dcc.Graph(id='success-pie-chart')),
                                html.Br(),

                                html.P(html.Strong("Range of Payload mass (kg):")),
                                # TASK 3: Add a slider to select payload range
                                #dcc.RangeSlider(id='payload-slider',...)
                                dcc.RangeSlider(id='payload-slider', 
                                        min=0, max=10000, step=1000,
                                       # marks={0: '0', 10000: '10000'}, Marks: In Dash >= 2.1, they are autogenerated if not explicitly provided or turned off.
                                    # marks={ 0: {'label': '0', 'style': {'color': '#77b0b1'}},
                                    #           10000: {'label': '10000', 'style': {'color': '#f50'}}   },
                                        value=[min_payload, max_payload]),


                                # TASK 4: Add a scatter chart to show the correlation between payload and launch success
                                html.Div(dcc.Graph(id='success-payload-scatter-chart')),
                                ])

# TASK 2:
# Add a callback function for `site-dropdown` as input, `success-pie-chart` as output
@app.callback( Output(component_id='success-pie-chart', component_property='figure'),
              Input(component_id='site-dropdown', component_property='value') )

def get_pie_chart(entered_site):
    filtered_df = spacex_df
    if entered_site == 'ALL':
        fig = px.pie(filtered_df, values='class', 
        names='Launch Site', 
        title='<b>Share of Successful Launches by Site (%)</b>')
        return fig
    else:
        filtered_df=spacex_df[spacex_df['Launch Site']== entered_site]
        filtered_df=filtered_df.groupby(['Launch Site','class']).size().reset_index(name='class count')
        
        failure_count= filtered_df['class count'][0]
        success_count= filtered_df['class count'][1]
        total_number_launch=filtered_df['class count'].sum()
        
        fig=px.pie( filtered_df,values=[failure_count, success_count],
                   names=['<b>Failure</b>', '<b>Success</b>'], color=['Failure', 'Success'], 
                   color_discrete_map={'Failure':px.colors.qualitative.G10[1], 'Success':px.colors.qualitative.G10[5]}, 
               title=f"<b>Launch attempts outcome (%) for site {entered_site}</b><br>Total number of attempts= {total_number_launch}<br>Number of success= {success_count}<br>Number of failures= {failure_count}"  )
        return fig     
 

# Task 4  Is there a bug above ? .. 
# Add a callback function for `site-dropdown` and `payload-slider` as inputs, `success-payload-scatter-chart` as output    
@app.callback(Output(component_id='success-payload-scatter-chart',component_property='figure'),
                [Input(component_id='site-dropdown',component_property='value'),
                Input(component_id='payload-slider',component_property='value')])

def scatter(entered_site,payload):
    filtered_df = spacex_df[spacex_df['Payload Mass (kg)'].between(payload[0],payload[1])]

    
    if entered_site=='ALL':
        fig=px.scatter(filtered_df,x='Payload Mass (kg)',y='class',color='Booster Version Category',title='<b>Launch outcome v. Payload mass for all sites</b>')
        fig.update_layout(
            xaxis_title="<b>Payload Mass (kg)</b>",
            yaxis_title="<b>Class: Failure=0, Success=1</b>",
            legend_title="<b>Booster Version Category</b>")
        fig.update_traces(marker=dict(size=12,
                              line=dict(width=2,
                                        color='DarkSlateGrey')),
                  selector=dict(mode='markers'))
        
        return fig
    else:
        fig=px.scatter(filtered_df[filtered_df['Launch Site']==entered_site],x='Payload Mass (kg)',y='class',color='Booster Version Category',
                       title=f"<b>Launch outcome v. Payload mass for site {entered_site} </b>")
        
        
        fig.update_layout(
        xaxis_title="<b>Payload Mass (kg)</b>",
        yaxis_title="<b>Class: Failure=0, Success=1</b>",
        legend_title="<b>Booster Version Category</b>")
        fig.update_traces(marker=dict(size=12,
                              line=dict(width=2,
                                        color='DarkSlateGrey')),
                  selector=dict(mode='markers'))
        
        return fig

# Run the app
if __name__ == '__main__':
    #app.run_server()

    #app.run_server(host='127.0.0.1', port=8050, debug=True)
    #app.run_server(mode='inline')
    # REVIEW8: Adding dev_tools_ui=False, dev_tools_props_check=False can prevent error appearing before calling callback function
    #app.run_server(mode="inline", host="localhost", debug=False, dev_tools_ui=False, dev_tools_props_check=False)
    #app.run_server( port=8070   , host="localhost", debug=False, dev_tools_ui=False, dev_tools_props_check=False) 
    app.run_server(mode="external",  port=8070   , host="localhost", debug=False, dev_tools_ui=False, dev_tools_props_check=False) 
    #app.run_server( port=8000   , host="localhost", debug=False, dev_tools_ui=False, dev_tools_props_check=False) 
    #app.run_server('jupyterlab')
    #app.run_server(mode='external',port=8090)
    #app.run_server(mode="external")
    #app.run_server(debug=True)

#!pip install  watermark

#%reload_ext watermark
# python, ipython, packages, and machine characteristics
#%watermark -v -m -p wget,pandas,numpy,altair
#%watermark --iversions
# date
#print (" ")
#%watermark -u -n -t -z



"""##    Report

After visual analysis using the dashboard, you should be able to obtain some insights to answer the following five questions:

1. Which site has the largest successful launches? 

<span style="color:#0094cf;">**KSLC-39A:  10 successful launches**</span>


2. Which site has the highest launch success rate? 

<span style="color:#0094cf;">**KSLC-39A:  ~77% or 10 successful launches out of 13**</span>


3. Which payload range(s) has the highest launch success rate? 

<span style="color:#0094cf;">**Most successful launches have a payload mass in an interval [360-5300] kg**</span>


4. Which payload range(s) has the lowest launch success rate? 

<span style="color:#0094cf;">**Above payload mass= 5400 Kg, there is only a single succesful launch, with a 9600 kg payload**</span>

5. Which F9 Booster version (v1.0, v1.1, FT, B4, B5, etc.) has the highest launch success rate?

<span style="color:#0094cf;"> **Best booster version: FT: 15 successful launches out of 23 launch attempts.  ~ 65%**<br>
**Second best: B4 = 6/11  about ~55%** </span>


Estimated time needed: 90 minutes

#### TASK 2: Add a callback function to render success-pie-chart based on selected site dropdown
The general idea of this callback function is to get the selected launch site from site-dropdown and render a pie chart visualizing launch success counts.

Dash callback function is a type of Python function which will be automatically called by Dash whenever receiving an input component updates, such as a click or dropdown selecting event.

If you need to refresh your memory about Plotly Dash callback functions, you may refer to the lab you have learned before:

Plotly Dash Lab

Let's add a callback function in spacex_dash_app.py including the following application logic:

* Input is set to be the site-dropdown dropdown, i.e., Input(component_id='site-dropdown', component_property='value')
* Output to be the graph with id success-pie-chart, i.e., Output(component_id='success-pie-chart', component_property='figure')
* A If-Else statement to check if ALL sites were selected or just a specific launch site was selected
    * If ALL sites are selected, we will use all rows in the dataframe spacex_df to render and return a pie chart graph to show the total success launches (i.e., the total count of class column)
    * If a specific launch site is selected, you need to filter the dataframe spacex_df first in order

to include the only data for the selected site. Then, render and return a pie chart graph to show the success (class=1) count and failed (class=0) count for the selected site. <br>
Here is an example of a callback function:
"""

# Function decorator to specify function input and output
#@app.callback(Output(component_id='success-pie-chart', component_property='figure'),
#              Input(component_id='site-dropdown', component_property='value'))
#def get_pie_chart(entered_site):
#    filtered_df = spacex_df
#    if entered_site == 'ALL':
#        fig = px.pie(data, values='class', 
#        names='pie chart names', 
#        title='title')
#        return fig
#    else:
        # return the outcomes piechart for a selected site

"""The rendered pie chart should look like the following screenshots:

* Pie chart for all sites are selected


<img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/labs/module_3/images/pie-chart-all.PNG" width="1500" height="500">

* Pie chart for is selected

<img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/labs/module_3/images/pie-chart-one.PNG" width="1500" height="500">

#### TASK 3: Add a Range Slider to Select Payload
Next, we want to find if variable payload is correlated to mission outcome. From a dashboard point of view, we want to be able to easily select different payload range and see if we can identify some visual patterns.

Find and complete a commented dcc.RangeSlider(id='payload-slider',...) input with the following attribute:

* id to be payload-slider
* min indicating the slider starting point, we set its value to be 0 (Kg)
* max indicating the slider ending point to, we set its value to be 10000 (Kg)
* step indicating the slider interval on the slider, we set its value to be 1000 (Kg)
* value indicating the current selected range, we could set it to be min_payload and max_payload

Here is an example of RangeSlider:
"""

#dcc.RangeSlider(id='id',
#                min=0, max=10000, step=1000,
#                marks={0: '0',
#                       100: '100'},
#                value=[min_value, max_value])

"""#### TASK 4: Add a callback function to render the success-payload-scatter-chart scatter plot
Next, we want to plot a scatter plot with the x axis to be the payload and the y axis to be the launch outcome (i.e., class column). As such, we can visually observe how payload may be correlated with mission outcomes for selected site(s).

In addition, we want to color-label the Booster version on each scatter point so that we may observe mission outcomes with different boosters.

Now, let's add a call function including the following application logic:

Input to be [Input(component_id='site-dropdown', component_property='value'), Input(component_id="payload-slider", component_property="value")] Note that we have two input components, one to receive selected launch site and another to receive selected payload range
Output to be Output(component_id='success-payload-scatter-chart', component_property='figure')
A If-Else statement to check if ALL sites were selected or just a specific launch site was selected
If ALL sites are selected, render a scatter plot to display all values for variable Payload Mass (kg) and variable class.
In addition, the point color needs to be set to the booster version i.e., color="Booster Version Category"
If a specific launch site is selected, you need to filter the spacex_df first, and render a scatter chart to show
values Payload Mass (kg) and class for the selected site, and color-label the point using Boosster Version Category likewise.
You rendered scatter point should look like the following screenshot:

<img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/labs/module_3/images/scatter-point.PNG" width="1500" height="500">


 

"""





"""# Import required libraries
import pandas as pd
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State
#from jupyter_dash import JupyterDash
import plotly.graph_objects as go
import plotly.express as px
from dash import no_update

from jupyter_dash.comms import _send_jupyter_config_comm_request
_send_jupyter_config_comm_request()

from jupyter_dash import JupyterDash

#### For "requirements.txt" if we run MyBinder in GitHub
"""

#!pip install  watermark

#%reload_ext watermark

# python, ipython, packages, and machine characteristics
#%watermark -v -m -p wget,pandas,numpy,altair
#%watermark --iversions
# date
#print (" ")
#%watermark -u -n -t -z











"""## Plotly Dash Reference
### Dropdown (input) component
Refer here for more details about dcc.Dropdown()

### Range slider (input) component
Refer here for more details about dcc.RangeSlider()

### Pie chart (output) component
Refer here for more details about plotly pie charts

### Scatter chart (output) component
Refer here for more details about plotly scatter charts

## Summary

Congratulations for completing your dash and plotly assignment.

More information about the libraries can be found [here](https://dash.plotly.com/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkDV0101ENSkillsNetwork20297740-2021-01-01)

## Author

Yan Luo

## Other contributor(s)

Joseph Santarcangelo

## Changelog

| Date       | Version | Changed by       | Change Description              |
|------------|---------|------------------|---------------------------------|
| 03-09-2021 | 1.1     | Lakshmi Holla    | Added a note.                   |
| 06-01-2021 | 1.0     | Yan              | Initial version created         |

## <h3 align="center"> © IBM Corporation 2021. All rights reserved. <h3/>
"""