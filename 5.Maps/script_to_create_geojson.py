# This script is used to create the map visualizations of districts in India
import json
import pandas as pd
import sys

# init.geojson is created to represent the districts in the year 2011
init_file = open(r'/Users/adhyadagar/Downloads/Misclassification_MAP/Mehak_Maps/init.geojson', 'r')
init_geojson_data = json.load(init_file)

# The first command line argument holds the name of the result file to be visualized on the map
results_filename = sys.argv[1]
results_to_be_plotted = pd.read_excel(results_filename)
district_codes_in_results = results_to_be_plotted['census_code'].values

# district_code_mapping_2011_2001 dictionary stores the 2001 to 2011 mapping of disticts. census_code_2011 : census_code_2001
district_code_mapping_2011_2001 = {9: 8, 11: 10, 13: 14, 15: 14, 17: 16, 18: 16, 20: 19, 22: 21, 50: 49, 52: 51, 54: 53,
                                   87: 86, 89: 88, 131: 130, 202: 201, 240: 239, 256: 255, 258: 257, 260: 259, 268: 267,
                                   269: 267, 271: 270, 320: 319, 322: 321, 324: 323, 326: 325, 345: 344, 359: 358,
                                   361: 360, 363: 362, 365: 364, 367: 366, 369: 368, 415: 414, 417: 416, 459: 458,
                                   461: 460, 463: 462, 465: 464, 467: 466, 493: 492, 580: 579, 582: 581, 584: 583,
                                   631: 630, 633: 632, 640: 639}

# For each district in init.geojson
for i in range(len(init_geojson_data['features'])):

    # fetch the census code of this district from init.geojson properties
    current_district_code = init_geojson_data['features'][i]['properties']['censuscode']

    # check if this census code exists in the results to be mapped
    if current_district_code in district_codes_in_results:

        matching_row = (results_to_be_plotted.loc[results_to_be_plotted['census_code'] == current_district_code]).iloc[
            0]
        # Add a property corresponding to the result to be plotted to the geojson file
        init_geojson_data['features'][i]['properties']['Cluster'] = int(
            matching_row['Cluster'])

    # check if the current district code of 2011 was split from some district in 2001
    #elif current_district_code in district_code_mapping_2011_2001:
        #matching_row = (results_to_be_plotted.loc[results_to_be_plotted['census_code'] == district_code_mapping_2011_2001[current_district_code]]).iloc[0]
        #init_geojson_data['features'][i]['properties']['Cluster'] = int(
            #matching_row['Cluster'])

    else:
        print(f'{current_district_code} not in both!!!!')

# create a new json file with the resul
# ts added as properties of each district
final_json_file = open('00_MIS_2011' + '.json', 'w')

json.dump(init_geojson_data, final_json_file)
final_json_file.close()
init_file.close()



