import csv

def select_columns(input_file, output_file, selected_columns):
    with open(input_file, 'r', newline='', encoding='utf-8') as infile, \
            open(output_file, 'w', newline='', encoding='utf-8') as outfile:
        
        reader = csv.DictReader(infile)
        writer = csv.DictWriter(outfile, fieldnames=selected_columns)
        writer.writeheader()
        
        for row in reader:
            writer.writerow({key: row.get(key, '') for key in selected_columns})

input_file = '/Users/shravan/6-mongodb-analysis-shravan-coder/data/listings.csv'
output_file = '/Users/shravan/6-mongodb-analysis-shravan-coder/data/listings_cleaned.csv'

columns_to_extract = [
    "id", "source", "name", "description", "host_id", "host_name", "host_since", 
    "host_location", "host_response_rate", "host_acceptance_rate", 
    "host_is_superhost", "host_total_listings_count", "neighborhood", 
    "neighbourhood_group_cleansed", "latitude", "longitude", "property_type", 
    "room_type", "accommodates", "beds", "price", "minimum_nights", 
    "maximum_nights", "number_of_reviews", "review_scores_rating"
]

select_columns(input_file, output_file, columns_to_extract)
