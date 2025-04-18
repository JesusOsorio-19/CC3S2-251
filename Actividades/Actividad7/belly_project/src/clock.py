from datetime import datetime

class ClockService:
    def get_current_time(self):
        return datetime.now().timestamp() # Devuelve el tiempo actual 