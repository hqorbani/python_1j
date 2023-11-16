from functions.my_lib import *
# file_address = "json_files/emails.json"
# emails_list = read_json(file_address)
# print(emails_list)
api_json_address = "json_files/api.json"
# api_list = read_json(api_json_address)
# print(api_list)
data = read_json(api_json_address)
data.append("www.google.com")
write_json(api_json_address,data)

