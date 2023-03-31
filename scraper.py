import os
import requests
from datetime import datetime, timedelta

# Base URL
base_url = "https://frettabladid.overcastcdn.com/documents/"

# Output mappa fyrir pdf skjöl sem eru vistuð
output_folder = "pdfs/"

# Býr til output möppu
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Skilgreinir upphafs- og enda dagsetningu (ár, mán, dagur)
start_date = datetime(2005, 12, 3)
end_date = datetime(2023, 3, 31)

# Openar log skrá til að skrá hvort tekist hafi að niðurhala pdf-skrá
with open("log.txt", "w") as log_file:
    # Iteratar yfir dagsetningar og downloadar þeim pdf-skrám sem eru aðgengilegar
    date = start_date
    while date <= end_date:

        # Athugar hvort dagsetning sé valid (milli 1 og 31)
        if date > datetime.now() or date.month not in range(1, 13):
            date += timedelta(days=1)
            continue

        # Býr til URL fyrir pdf-skrá
        date_str = date.strftime("%y%m%d")
        pdf_url = f"{base_url}{date_str}.pdf"
        
        # Býr til path fyrir output 
        output_path = os.path.join(output_folder, f"{date_str}.pdf")
        
        # Athugar hvort pdf skrá sé til 
        response = requests.get(pdf_url)
        if response.status_code == 200:
            # Ef pdf -skrá er til þá er henni downloadað 
            with open(output_path, "wb") as f:
                f.write(response.content)
            
            # Lína skrifuð í log-skrá ef pdf-skrá er til
            log_file.write(f"{date_str}.pdf er til\n")
        else:
            # Lína skrifuð í log-skrá ef pdf-skrá er til
            log_file.write(f"{date_str}.pdf er ekki til\n")

        # Prentar línu í console með status code fyrir hvern dag
        print(f'{date.date()} : {response.status_code}')

        # Áfram í næsta dag
        date += timedelta(days=1)