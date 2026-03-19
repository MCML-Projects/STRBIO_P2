import json
def read_json(json_path, position):
    with open(json_path, 'r') as file:
        data_dict = json.load(file) 

    for key in data_dict:
        print(key, data_dict[key][position-1])
    return 

read_json(r'D:\Master\UAM_MUBBC\2o_cuatri\BioinfEstructural\project\STRBIO_P2\models\Hog1\fold_osm1_monomer_171p\fold_osm1_monomer_171p_full_data_0.json',171)
