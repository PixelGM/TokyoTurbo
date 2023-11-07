def is_dew_formed(current_temp, dew_point_temp):
    """
    Returns True if dew is formed, False otherwise.
    
    :param current_temp: The current temperature.
    :param dew_point_temp: The dew point temperature.
    :return: Boolean value indicating if dew is formed.
    """
    return current_temp <= dew_point_temp

# Example usage:
current_temperature = 10  # Current temperature in degrees Celsius
dew_point_temperature = 10  # Dew point temperature in degrees Celsius

# Call the function with the example parameters
dew_formed = is_dew_formed(current_temperature, dew_point_temperature)

print(f"Dew formed: {dew_formed}")
