import base_enums

class LocationManager:
    
    @staticmethod
    def get_location_from_id(location_id):
        for location in base_enums.Location:
            if location.value == location_id:
                return location
        raise Exception("No locaion could be found for given parameter!")

        