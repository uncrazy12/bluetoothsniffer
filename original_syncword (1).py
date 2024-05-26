import threading
import os

def find_and_count_access_codes(file_path):
    base_name = os.path.basename(file_path)
    dir_name = os.path.dirname(file_path)
    
    binary_data_str = ''  # Initialize a variable to keep track of the binary data as a string
    
    try:
        with open(file_path, 'rb') as file:
            while True:
                byte = file.read(1)
                if not byte:  # If no more bytes, break the loop
                    break
                # Convert byte to integer and then to '0' or '1'
                binary_data_str += format(int.from_bytes(byte, "big"), '08b')


        print(f"Binary data has been processed from {file_path}")
    except Exception as e:
        print(f"Error processing file: {e}")
        return

    access_codes = []
    total_access_codes = 0
    index = 0

    while index < len(binary_data_str) - 72:
        preamble = binary_data_str[index:index+5]
        if preamble in ['10101', '01010']:
            sync_word = binary_data_str[index+5:index+5+66]  # Extract sync word
            trailer_index = index + 5 + 66  # Start of the trailer
            trailer = binary_data_str[trailer_index:trailer_index+5]
            if trailer in ['10101', '01010']:
                total_access_codes += 1
                access_code = binary_data_str[index:trailer_index+5]  # Capture the entire access code
                access_codes.append(access_code)  # Save the found access code
                index = trailer_index + 5  # Move index to the end of this access code
                continue
        index += 1

    # Save the found access codes to a file
    access_codes_file_path = os.path.join(dir_name, f"{base_name}_access_codes.txt")
    with open(access_codes_file_path, 'w') as ac_file:
        for code in access_codes:
            ac_file.write(f"{code}\n")

    print(f"Total Access Codes Found: {total_access_codes} in {file_path}")
    print(f"Access codes saved to {access_codes_file_path}")


input_file_paths = [
    '/home/edwin/channel1.bin',
    '/home/edwin/channel2.bin',
    '/home/edwin/channel3.bin',
    '/home/edwin/channel4.bin',
    '/home/edwin/channel5.bin',
    
]

threads = []
for file_path in input_file_paths:
    thread = threading.Thread(target=find_and_count_access_codes, args=(file_path,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
