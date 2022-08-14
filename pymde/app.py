import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np 
from shiny import App, render, reactive, ui 

app_ui = ui.page_fluid(

    ui.layout_sidebar(
        ui.panel_sidebar(
        ui.input_file(
            id= "file_in",
            label = "Input File",
            accept = ".csv"
        ),

        ui.br(), 

        ui.input_action_button(
          id = "ok_input",
          label = "OK"  
        )

        ),

        ui.panel_main(

        ui.output_plot(id = "na_plot"),

        ui.br(),

        ui.output_table(id = "na_table")

        )
    )

)


def server(input, output, session):
    def in_data():
        return pd.read_csv(input.file_in()[0]["datapath"] if input.file_in() else "https://vincentarelbundock.github.io/Rdatasets/csv/Stat2Data/Hawks.csv")

    def missing_counts():
        # todo create user choice for ascending 
        return in_data().isna().sum().sort_values(ascending = False).reset_index()
    
    @output 
    @render.table
    def na_table():
        return missing_counts()
    
    @output 
    @render.plot 
    def na_plot():
        fig = plt.figure()
        fig, ax  = plt.subplots()
        ax.bar(x= missing_counts()["index"], height = missing_counts()[0], color = "indianred")
        plt.xticks(rotation = 90)
        fig.tight_layout()
        return fig 



app = App(app_ui, server)