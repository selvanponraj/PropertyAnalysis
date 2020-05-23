from Naked.toolshed.shell import execute_js, muterun_js
import sys
import json
import pandas as pd
import openpyxl
from model import *
#import openpyxl

def main():
    # Run NodeJS script to call MLS API and retrieve properties
    response = muterun_js("get_properties.js")
    if response.exitcode != 0:
        sys.stderr.write(response.stderr)
        return 1

    # Read output.json file and create dataframe
    json_data = json.load(open('output.json'))
    df = pd.DataFrame(json_data['Results'])
    print(df)

    # Export to Excel using Pandas
    #df.to_excel(r'C:\Users\76411\Documents\E\Project\PropertyAnalysis\propertydata.xlsx',sheet_name='df1')
    #df.to_csv(r'C:\Users\76411\Documents\E\Project\PropertyAnalysis\export_df.csv')

    # create df2 as buildings data frame
    #s=df["Building"].apply(lambda x: pd.DataFrame(x))
    df2 = pd.concat([df["Building"].apply(pd.Series)])
    #df2.to_csv(r'C:\Users\76411\Documents\E\Project\PropertyAnalysis\Buildings.csv')

    ##df2 = df["Building"].apply(lambda x: x.read_json(_, orient='records'))
    ##df2.to_csv(r'C:\Users\76411\Documents\E\Project\PropertyAnalysis\export_df2.csv')

    #------------------------------------------------------------------------
    # clean data - "Building"
    # df["Building"] = df["Building"].astype('str')
    # new = df["Building"].str.split(",", n=3, expand=True)
    ## the first of the building list is bathroom
    # df["Bathroom"] = new[0]
    # df["Bathroom"]=df["Bathroom"].str.slice(-2,-1)
    ## the second of the building list is bedroom
    # df["Bedroom"] = new[1]
    # df["Bedroom"] = df["Bedroom"].str.slice(-2,-1)
    ## the third of the buidling list is Type
    # df["Type"] = new[2]
    # df["Type"]=df["Type"].str.slice(10,-1)
    ## the forth and last is Ammenities
    # df["Ammenities"] = new[3]
    # df["Ammenities"]=df["Ammenities"].str.slice(16,-2)
    # df.drop(columns='Building')
    # df.to_csv(r'C:\Users\76411\Documents\E\Project\PropertyAnalysis\export_df1.csv')
    #____________________________________________________________________________________

    ## clean data - "Property"
    # create df3 as property data frame
    df3 = pd.concat([df["Property"].apply(pd.Series)])
    #df3.to_csv(r'C:\Users\76411\Documents\E\Project\PropertyAnalysis\Property.csv')

    #df["Property"] = df["Property"].astype('str')
    #ptylist = df["Property"].str.split("\'",n=75,expand = True)
    ## column 3 is price
    #print(ptylist)
    #df["Price"]= ptylist[3].astype('str').str.slice("")

    ## combine all three dataframe
    df = pd.concat([df,df2,df3],axis=1)
    with pd.ExcelWriter('data.xlsx') as writer:
        df.to_excel(writer,sheet_name='df1')
        df2.to_excel(writer,sheet_name='df2')
        df3.to_excel(writer,sheet_name='df3'
                     )
    linearreg(df)

    ## call model function to pass on the data cleasned


if __name__ == "__main__":
    main()
