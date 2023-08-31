import pyvo

# Define the coordinates for TON 618
ra, dec = 187.10375, 31.47722222222222

# Search the registry for all services
services = pyvo.regsearch(keywords="DSS", servicetype='image')

# Loop over all the services and perform a cone search
all_results = []
for service in services:
    try:
        results = service.search(pos=(ra, dec), radius=0.1)  # radius in degrees
        all_results.extend(results)
    except Exception as e:
        print(f"Skipping service {service.access_url} due to error: {e}")

# Process results
for record in all_results:
    print(record.title)
    print(record.getdataurl())
