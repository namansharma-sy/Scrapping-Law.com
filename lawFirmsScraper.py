# Loading libraries
from bs4 import BeautifulSoup
import requests
import pandas as pd
import os

# list to save data dictionaries
data_list = []

def getData():
    #scraping first 200 url 
    for page in range(1,100):
        
        # to capture AttributeError
        try:
            url = f"https://www.law.com/law-firm-profile/?id={page}&slreturn=20220906043018"

            source = requests.get(url)
            soup = BeautifulSoup(source.text, "html.parser")

            name = soup.find('h1', class_ = 'page-title left').text
            description = soup.find('p', class_ = 'firms-para').text.replace('\xa0',"")

            Website = soup.find_all('div', class_ = 'inner')
            Website = list(Website)

            website = Website[0].find('a')['href']

            Overview =  soup.find_all('div', class_ = 'col-md-6')
            Overview = list(Overview)

            globalRank = Overview[1].text.strip()
            totalOffices = Overview[3].text.strip()
            totalHeadcount = Overview[5].text.strip()
            equityPartners = Overview[7].text.strip()
            nonEquityPartners = Overview[9].text.strip()
            associates = Overview[11].text.strip()
            totalRevenue = Overview[13].text.strip()
            revenuePerLawyer = Overview[15].text.strip() 
            profitPerEquityPartner = Overview[17].text.strip() 

            rank = soup.find_all('p', class_ = 'rank-firms')
            rank = list(rank)
            
            #Global ranking
            global200_2021 = rank[0].text.strip()
            global200_2020 = rank[1].text.strip()
            global200_2019 = rank[2].text.strip()
            
            #amLaw ranking
            amLaw200_2022 = rank[3].text.strip()
            amLaw200_2021 = rank[4].text.strip()
            amLaw200_2020 = rank[5].text.strip()
            
            #NLJ ranking 
            NLJ500_2022 = rank[6].text.strip()
            NLJ500_2021 = rank[7].text.strip()
            NLJ500_2020 = rank[8].text.strip()
            
            #UK Top ranking 
            UKTop100_2020 = rank[9].text.strip()
            UKTop100_2019 = rank[10].text.strip()
            UKTop100_2018 = rank[11].text.strip()
            
            # saving data into dictionary
            data = {
                "Name" : name,
                "Description" : description,
                "Website" : website,

                "GlobalRank" : globalRank,
                "TotalOffices" : totalOffices,
                "TotalHeadcount" : totalHeadcount,
                "EquityPartners": equityPartners,
                "NonEquityPartners": nonEquityPartners,
                "Associates": associates,
                "TotalRevenue": totalRevenue,
                "RevenuePerLawyer": revenuePerLawyer,
                "ProfitPerEquityPartner": profitPerEquityPartner,

                "Global200_2021": global200_2021,
                "Global200_2020": global200_2020,
                "Global200_2019": global200_2019,

                "AmLaw200_2022": amLaw200_2022,
                "AmLaw200_2021": amLaw200_2021,
                "AmLaw200_2020": amLaw200_2020,

                "NLJ500_2022": NLJ500_2022,
                "NLJ500_2021": NLJ500_2021,
                "NLJ500_2020": NLJ500_2020,

                "UKTop100_2020": UKTop100_2020,
                "UKTop100_2019": UKTop100_2019,
                "UKTop100_2018": UKTop100_2018
            }
            
            #saving dict into lsit
            data_list.append(data)
            
            # coverting data list into dataframe
            df = pd.DataFrame(data_list)

            #creating folder and saving excel sheet for each firm in the folder
            folderDir = r'C:\Users\Naman Sharma\Desktop\Upwork\\'+name
            print(f'folderDir: {folderDir}')
            os.makedirs(folderDir)
            df.to_excel(folderDir +'\\' + name + '.xlsx')

        except AttributeError:
            print(page) # Url sequence for which we are getting the AttributeError

    
    # returning excel sheet
    
    return df.to_excel(excel_writer =  r'C:\Users\Naman Sharma\Desktop\Upwork\LawFirmsLawcom2022.xlsx')

getData()