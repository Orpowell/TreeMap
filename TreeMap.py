import plotly.express as px
import pandas as pd
import click
import logging
import sys

logging.basicConfig(stream=sys.stdout, format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S',
                    level=logging.INFO)

@click.command()
@click.argument('excel_file')
def main(excel_file):
    """
    Tree Map is a simple tool that shows the positions of previously identified trees as a coloured dots on a map using GPS coordinates. The colour of the dot is determined by the score assigned to a given tree ranging from 0 to 10. See [GITHUB LINK] for full documentation.
    
    TreeMap was delevoped by Oliver Powell on 25/07/23. For more info please contact: treemap@oliverpowell.com 
    """
    logging.info("Loading data...")
    df = pd.read_excel(excel_file)

    logging.info("Analysing data...")
    df['Average Score'] = round(df.groupby('Tree')['Score (0-10)'].transform('mean'))
    Se = pd.DataFrame(df.groupby('Tree')['Score (0-10)'].agg(list))
    Se.columns = ['Score List']
    df = pd.merge(df, Se, on="Tree")
    colour_scale = []


    logging.info("Plotting trees...")
    fig = px.scatter_mapbox(df, 
                            lat="North", 
                            lon="East", 
                            hover_name="Tree", 
                            hover_data=["Tree", "Average Score", "Score List"],
                            color_continuous_scale="bluered",
                            color="Average Score",
                            zoom=8, 
                            height=800,
                            width=800)

    fig.update_layout(mapbox_style="open-street-map")
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    fig.show()

if __name__ == "__main__":
    main()