import csv
import os

DATA_DIRECTORY = "./data"
OUTPUT_FILE_PATH = "./formatted_data.csv"

# open the csv output file
with open(OUTPUT_FILE_PATH, "w") as output_file:
    writer = csv.writer(output_file)

    # add csv header
    header = ["sales", "date", "region"]
    writer.writerow(header)

    # loop through each file in the data directory
    for file_name in os.listdir(DATA_DIRECTORY):
        # read the csv file
        with open (f"{DATA_DIRECTORY}/{file_name}", "r") as input_file:
            reader = csv.reader(input_file)
            # go through each row in the csv file
            row_index = 0
            for input_row in reader:
                # if the row is not header, process the data
                if row_index > 0:
                    # collect data from the row
                    product = input_row[0]
                    raw_price = input_row[1]
                    quantity = input_row[2]
                    purchase_date = input_row[3]
                    region = input_row[4]

                    # if it is a pink morsel purchase, add it
                    if product == "pink morsel":
                        # format data
                        price = float(raw_price[1:])
                        sale = price * int(quantity)

                        # write row to output csv file
                        output_row = [sale, purchase_date, region]
                        writer.writerow(output_row)
                row_index += 1
