from Naked.toolshed.shell import execute_js, muterun_js
import sys
import json
import pandas as pd


def main():
    # Get properties in given location range and price range
    df = get_properties()


def get_properties(min_price=100000, max_price=2000000,
                   min_lat=43.5890, max_lat=44.0384,
                   min_long=-79.2000, max_long=-79.6441):
    # Form command string
    command = "get_properties.js --minLong=" + str(min_long) + " --maxLong=" + str(max_long) + " --minLat=" \
              + str(min_lat) + " --maxLat=" + str(max_lat) + " --minPrice=" + str(min_price) + " --maxPrice=" \
              + str(max_price)

    print(command)

    response = muterun_js(command)
    if response.exitcode != 0:
        sys.stderr.write(response.stderr)
        return 1

    json_data = json.load(open('output.json'))
    return pd.DataFrame(json_data['Results'])


if __name__ == "__main__":
    main()
