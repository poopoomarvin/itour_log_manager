from LogDatum import *
from LogTag import *

class User():
    def __init__(self, uid, name, checkin_location_dict):
        self.uid = uid
        self.name = name
        self.checkin_location_dict = checkin_location_dict
        self.togo_list = []
        self.viewed_notification = []
        self.viewed_checkin = []
        self.liked_checkin = []
        self.collected_checkin = []
        self.report_anywhere = []
        self.report_checkin = []
    def read_log(tag, checkin, location, timestamp):
        if tag == LOG_TOGO_ADD:
            self.togo_list.append(LogDatum(location, location, True, timestamp))
        elif tag == LOG_TOGO_REMOVE:
            self.togo_list.append(LogDatum(location, location, False, timestamp))
        elif tag == LOG_NOTIFICATION_CLICKED_HOT_CHECKIN:
            self.viewed_notification.append(LogDatum(checkin_id, location, True, timestamp))
        elif tag == LOG_CHECKIN_OPEN:
            self.viewed_checkin.append(LogDatum(checkin_id, location, True, timestamp))
        elif tag == LOG_CHECKIN_LIKE:
            self.liked_checkin.append(LogDatum(checkin_id, location, True, timestamp))
        elif tag == LOG_CHECKIN_UNLIKE:
            self.liked_checkin.append(LogDatum(checkin_id, location, False, timestamp))
        elif tag == LOG_CHECKIN_COLLECT_ADD:
            self.collected_checkin.append(LogDatum(checkin_id, location, True, timestamp))
        elif tag == LOG_CHECKIN_COLLECT_REMOVE:
            self.collected_checkin.append(LogDatum(checkin_id, location, False, timestamp))
        elif tag == LOG_REPORT_CHECKIN:
            self.report_checkin.append(LogDatum(checkin_id, location, True, timestamp))
        elif tag == LOG_REPORT_ANYWHERE:
            self.report_anywhere.append(LogDatum(location, location, True, timestamp))
    def write_data():
        for log in self.report_anywhere:
            is_togo_result = self.is_togo(log)
            is_viewed_from_notification_result = self.is_viewed_from_notification(log)
            is_viewed_from_notification_result = self.is_viewed_from_notification(log)
            is_viewed_from_checkin_result = self.is_viewed_from_checkin(log)
            liked_result = self.liked(log)
            saved_result = self.saved(log)
            type_result = self.type(log)
    def is_togo(log):
        result = False
        for togo_data in self.togo_list:
            if log.location == togo_data.location and log.timestamp > togo_data.timestamp:
                result = togo_data.flag
        return result
    def is_viewed_from_notification(log):
        return True
    def is_viewed_from_checkin(log):
        return True
    def liked(log):
        return True
    def saved(log):
        return True
