import json

json_dict = {}
json_dict['Meta'] = {}
json_dict['Device'] = {}

json_dict['Device']['Laser'] = {}

json_dict['Device']['Laser']['06-405-DPL'] = {}
json_dict['Device']['Laser']['06-405-DPL']['Wavelength'] = '405'
json_dict['Device']['Laser']['06-405-DPL']['Port'] = 'COM1'
json_dict['Device']['Laser']['06-405-DPL']['Serialnumber'] = '17211'
json_dict['Device']['Laser']['06-405-DPL']['Mode'] = 'Current'
json_dict['Device']['Laser']['06-405-DPL']['Value'] = '195'

json_dict['Device']['Laser']['06-638-MLD'] = {}
json_dict['Device']['Laser']['06-638-MLD']['Wavelength'] = '638'
json_dict['Device']['Laser']['06-638-MLD']['Modelnumber'] = '0638-06-01-0180-200'
json_dict['Device']['Laser']['06-638-MLD']['Port'] = 'COM3'
json_dict['Device']['Laser']['06-638-MLD']['Serialnumber'] = '16811'
json_dict['Device']['Laser']['06-638-MLD']['Mode'] = 'Current'
json_dict['Device']['Laser']['06-638-MLD']['Value'] = '91'

json_dict['Device']['Laser']['06-561-DPL'] = {}
json_dict['Device']['Laser']['06-561-DPL']['Wavelength'] = '561'
json_dict['Device']['Laser']['06-561-DPL']['Port'] = 'COM7'
json_dict['Device']['Laser']['06-561-DPL']['Serialnumber'] = '12526'
json_dict['Device']['Laser']['06-561-DPL']['Mode'] = 'Current'
json_dict['Device']['Laser']['06-561-DPL']['Value'] = '126'

json_dict['Device']['AOTF'] = {}

with open('settings.json', 'w') as output_file:
    json.dump(json_dict, output_file, indent=4)