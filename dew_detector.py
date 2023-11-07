import math

# Function to calculate the dew point
def calculate_dew_point(T_ambient, H_ambient):
    a = 17.27
    b = 237.7
    alpha = ((a * T_ambient) / (b + T_ambient)) + math.log(H_ambient/100.0)
    T_dew = (b * alpha) / (a - alpha)
    return T_dew

# Function to detect dew formation
def dew_formation_detector(T_ambient, T_windshield, H_ambient):
    T_dew = calculate_dew_point(T_ambient, H_ambient)
    return T_windshield <= T_dew

# Main function to handle dew point detection
def main():
    try:
        # Get values from user input and convert them to float
        T_ambient = float(input('Enter ambient temperature (°C): '))
        T_windshield = float(input('Enter windshield temperature (°C): '))
        H_ambient = float(input('Enter ambient humidity (%): '))

        # Perform the dew detection
        dew_detected = dew_formation_detector(T_ambient, T_windshield, H_ambient)

        # Output the result message
        dew_message = "Dew formation detected." if dew_detected else "No dew formation detected."
        print(dew_message)
    except ValueError as e:
        # Output the error message if conversion to float fails
        print("Error: Please enter valid numbers for all fields.")

if __name__ == "__main__":
    main()
