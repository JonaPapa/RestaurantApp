import base_enums

class ApplicationModeManager:

    @staticmethod
    def get_application_mode_from_id(application_mode_id):
        for application_mode in base_enums.ApplicationMode:
            if application_mode.value == application_mode_id:
                return application_mode
        raise Exception("No application mode could be found for given application mode id parameter.")