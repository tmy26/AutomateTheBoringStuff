import re

file_path = "/Users/tmy/Desktop/HighRPM/HondaCivic2008OriginalFile"


RPM_DATA = {
    "1A F4 00 00 00 14": "",
    "18 38 00 00 00 14": "",
    "1A 2C 13 88 1A F4": "",
    "00 00 00 05 1A F4 1A F4": "",
    "1A 2C 1A 2C 7F FF 7F FF": ""
}


def format_to_hex(number: int) -> str:
    hex_desired_rpm = hex(number)[2:].upper()
    spaced_str = re.sub(r'(.{2})', r'\1 ', hex_desired_rpm).strip()
    return spaced_str


def new_values(desired_rpm: int) -> list:
    new_values = []
    hex_rpm_set_0 = format_to_hex(number=desired_rpm)
    hex_rpm_set_1 = format_to_hex(number=desired_rpm-200)
    hex_rpm_set_2 = format_to_hex(number=desired_rpm-700)
    new_values.append(hex_rpm_set_0)
    new_values.append(hex_rpm_set_1)
    new_values.append(hex_rpm_set_2)
    return new_values


def set_rpm_data_values(rpm_data: dict) -> dict:
    list_of_new_values = new_values(7400)
    highest_rpm = list_of_new_values[0]
    mid_rpm = list_of_new_values[1]
    lowest_rpm = list_of_new_values[2]
    rpm_data.update(
        {"1A F4 00 00 00 14": highest_rpm + " 00 00 00 14",
        "18 38 00 00 00 14": lowest_rpm + " 00 00 00 14",
        "1A 2C 13 88 1A F4": mid_rpm + " 13 88 " + highest_rpm,
        "00 00 00 05 1A F4 1A F4": highest_rpm + " " + highest_rpm + " " + mid_rpm + " " + mid_rpm,
        "1A 2C 1A 2C 7F FF 7F FF": mid_rpm + " " + mid_rpm + " 7F FF 7F FF"}
    )
    return RPM_DATA


def read_file(file_name: str) -> tuple:
    found_patterns = 0
    try:
        with open(file_name, 'r+b') as file:
            data = file.read()  # Read the entire file into memory
        
        # Find the desired in the data
            for key, value in RPM_DATA.items():
                looking_pattern = bytes.fromhex(key)
                index = 0
                while (index := data.find(looking_pattern, index)) != -1:
                    found_patterns += 1   

                    # Move the file pointer to the start of the old pattern
                    file.seek(index)
                    
                    # Convert the value to hex value and write it
                    hex_value = bytes.fromhex(value)
                    file.write(hex_value)

                    # Move the index forward to avoid infinite loops
                    index += len(looking_pattern)
        if found_patterns == 7:
            print('The new rpm is set successfully!')
            file.close()
        else:
            print('error occured!')
    except:
        pass

 
set_rpm_data_values(RPM_DATA)
read_file(file_name=file_path)