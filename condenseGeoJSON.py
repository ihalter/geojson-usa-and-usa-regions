from urllib.request import urlopen
import json
import pandas as pd

geoJsonRoot = "https://raw.githubusercontent.com/OpenDataDE/State-zip-code-GeoJSON/master/"

regionFeatures = {
    'West': [],
    'South': [],
    'Northeast': [],
    'Midwest': []
}

geoJsonFiles = ['ak_alaska_zip_codes_geo.min.json',
                'al_alabama_zip_codes_geo.min.json',
                'ar_arkansas_zip_codes_geo.min.json',
                'az_arizona_zip_codes_geo.min.json',
                'ca_california_zip_codes_geo.min.json',
                'co_colorado_zip_codes_geo.min.json',
                'ct_connecticut_zip_codes_geo.min.json',
                'dc_district_of_columbia_zip_codes_geo.min.json',
                'de_delaware_zip_codes_geo.min.json',
                'fl_florida_zip_codes_geo.min.json',
                'ga_georgia_zip_codes_geo.min.json',
                'hi_hawaii_zip_codes_geo.min.json',
                'ia_iowa_zip_codes_geo.min.json',
                'id_idaho_zip_codes_geo.min.json',
                'il_illinois_zip_codes_geo.min.json',
                'in_indiana_zip_codes_geo.min.json',
                'ks_kansas_zip_codes_geo.min.json',
                'ky_kentucky_zip_codes_geo.min.json',
                'la_louisiana_zip_codes_geo.min.json',
                'ma_massachusetts_zip_codes_geo.min.json',
                'md_maryland_zip_codes_geo.min.json',
                'me_maine_zip_codes_geo.min.json',
                'mi_michigan_zip_codes_geo.min.json',
                'mn_minnesota_zip_codes_geo.min.json',
                'mo_missouri_zip_codes_geo.min.json',
                'ms_mississippi_zip_codes_geo.min.json',
                'mt_montana_zip_codes_geo.min.json',
                'nc_north_carolina_zip_codes_geo.min.json',
                'nd_north_dakota_zip_codes_geo.min.json',
                'ne_nebraska_zip_codes_geo.min.json',
                'nh_new_hampshire_zip_codes_geo.min.json',
                'nj_new_jersey_zip_codes_geo.min.json',
                'nm_new_mexico_zip_codes_geo.min.json',
                'nv_nevada_zip_codes_geo.min.json',
                'ny_new_york_zip_codes_geo.min.json',
                'oh_ohio_zip_codes_geo.min.json',
                'ok_oklahoma_zip_codes_geo.min.json',
                'or_oregon_zip_codes_geo.min.json',
                'pa_pennsylvania_zip_codes_geo.min.json',
                'ri_rhode_island_zip_codes_geo.min.json',
                'sc_south_carolina_zip_codes_geo.min.json',
                'sd_south_dakota_zip_codes_geo.min.json',
                'tn_tennessee_zip_codes_geo.min.json',
                'tx_texas_zip_codes_geo.min.json',
                'ut_utah_zip_codes_geo.min.json',
                'va_virginia_zip_codes_geo.min.json',
                'vt_vermont_zip_codes_geo.min.json',
                'wa_washington_zip_codes_geo.min.json',
                'wi_wisconsin_zip_codes_geo.min.json',
                'wv_west_virginia_zip_codes_geo.min.json',
                'wy_wyoming_zip_codes_geo.min.json']

sl = pd.read_csv('state_lookup.csv')

# all_features = []
# for each filename
    # get api, append features list to all_features

# export a geoJson file as:
# {'type':"FeatureCollection", 'features': all_features}


if __name__ == '__main__':
    features = []
    for gj in geoJsonFiles:
        f = geoJsonRoot + gj
        with urlopen(f) as resp:
            _fc = json.load(resp)
        features.extend(_fc['features'])
            # lookup region for state append to region json

        _lkp = sl.loc[sl['State Code'] == gj[:2].upper(), 'Region'].values[0]  # don't return a pd.Series
        regionFeatures[_lkp].extend(_fc['features'])


    _outjson = { 'type':'FeatureCollection', 'features': features}
    with open(r"C:/Users/halte/Desktop/geoJson-all-USA.json", 'w') as jf:
        json.dump(_outjson, jf)

    for rf in regionFeatures.keys():
        with open(r"C:/Users/halte/Desktop/geoJson-{0}.json".format(rf), 'w') as _rf:
            regJSON = {'type': 'FeatureCollection', 'features': regionFeatures[rf]}
            json.dump(regJSON, _rf)

