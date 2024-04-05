import requests
import json

def fetch_data(wschemecodes):
    URL = 'https://fundsapi.wealthy.in/api/v2/mf-funds/'
    HEADER = {'Protected'}
    test=0
    results = []  
    
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
                
                required_data = {
                    "display_name": display_name,
                    "fund_type": item["fund_type"],
                    "isin_code": item["isin_code"],
                    "effective_from": "2000-01-01",  
                    "effective_to": "2024-03-31",
                    "wschemecode": item["wschemecode"],
                    "isin_code": item["isin_code"], 
                    "wpc":item["wpc"],
                    "b30_trail": 0 ,
                    "year_trail": year_trail
                }
                
                    
                results.append(required_data)
        else:
            print(f"Failed to fetch data for {code}. Status code: {response.status_code}")
    
    return results


wschemecodes=['IN966L01CQ2','MSBIL121DGO','INF179KC1ID2', 'INF082J01465', 'INF090I01197', 'INF090I01221','INF192K01932', 'INF090I01536''INF090I01866', 'INF090I01940', 'INF090I01973', 'INF090I01AA5', 'INF0K1H01115', 'INF109K01JK9']
fetched_data = fetch_data(wschemecodes)

json_data = json.dumps(fetched_data, indent=4)
#print(json_data)


file = "/Users/wealthy/Desktop/fetched_data_final.json"
with open(file, 'w') as file:
    file.write(json_data)

print(f"Data saved to {file}")


