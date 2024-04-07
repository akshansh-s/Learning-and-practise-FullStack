import requests
import json

def fetch_data(wschemecodes):
    URL = 'https://fundsapi.wealthy.in/api/v2/mf-funds/'
    HEADER = {'protected'}
    test=0
    results = [] 
    missing_isin_list=[]
    
    for code in wschemecodes:
        params = {'wschemecodes': code}
        response = requests.get(URL, headers=HEADER, params=params)
        
        if response.status_code == 200:
            data = response.json()
            for item in data["mf_fund_meta"]:
                fund_type = item.get("fund_type", "")
                print(fund_type,test)
                test+=1
                if fund_type == "E":
                    category = str(item.get("category", "")).strip().lower()
                    #print(category)
                    if category=="index fund": #type cast
                        year_trail=0.2
                        #print(category)
                    else:
                        year_trail = 1
                elif fund_type == "H":
                    year_trail=1
                elif fund_type == "D" or fund_type == "C":
                    year_trail = 0.25
                else:
                    year_trail = 0.2
                display_name = item.get("display_name") or item.get("scheme_name")
                isin_code= item.get("isin_code") or item.get("isin_reinvestment")
                required_data = {
                        "display_name": display_name,
                        "fund_type": item["fund_type"],
                        "effective_from": "2000-01-01",  
                        "effective_to": "2024-03-31",
                        "wschemecode": item["wschemecode"],
                        "isin_code": isin_code, 
                        "wpc":item["wpc"],
                        "b30_trail": 0 ,
                        "year_trail": year_trail
                    }
                if isin_code:
                    results.append(required_data)
                    #print(isin_code)
                else:
                    missing_isin_list.append(required_data)
        else:
            print(f"Failed to fetch data for {code}. Status code: {response.status_code}")
    
    return results, missing_isin_list


#wschemecodes=['IN966L01CQ2','MSBIL121DGO','INF179KC1ID2', 'INF082J01465', 'INF090I01197', 'INF090I01221','INF192K01932', 'INF090I01536''INF090I01866', 'INF090I01940', 'INF090I01973', 'INF090I01AA5', 'INF0K1H01115', 'INF109K01JK9']
fetched_data, missing_isin_list = fetch_data(wschemecodes)

json_data = json.dumps(fetched_data, indent=4)
#print(json_data)


file = "/Users/wealthy/Desktop/fetched_data.json"
with open(file, 'w') as file:
    file.write(json_data)

missing_isin_data = json.dumps(missing_isin_list, indent=4)
missing_isin_file_path = "/Users/wealthy/Desktop/missing_isin_data2.json"
with open(missing_isin_file_path, 'w') as file:
    file.write(missing_isin_data)

print(f"Data saved to {file}")
print(f"List of items missing ISIN codes saved to {missing_isin_file_path}")