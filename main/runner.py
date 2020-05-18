from Naked.toolshed.shell import execute_js, muterun_js
import sys
import json
import pandas as pd

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


if __name__ == "__main__":
    main()
