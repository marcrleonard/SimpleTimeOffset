class SimpleTimeOffset(object):
    def __init__(self, start_time):
        self.start_time = start_time

        self.max_values = {'seconds': 12,
                           'minutes': 59,
                           'hours': 12,
                           'days': {
                               '1': 31,  # Jan
                               '2': 28,  # Feb
                               '3': 31,  # March
                               '4': 30,  # April
                               '5': 31,  # May
                               '6': 30,  # June
                               '7': 31,  # July
                               '8': 31,  # August
                               '9': 30,  # September
                               '10': 31,  # October
                               '11': 30,  # November
                               '12': 31,  # December
                           },
                           'months': 12
                           }
        self.year_current, self.month_current, self.day_current, self.hour_current, self.minute_current, self.second_current, self.ms_current, self.dayinyear_current = self.start_time

        self.year_new = self.year_current
        self.month_new = self.month_current
        self.day_new = self.day_current
        self.hour_new = self.hour_current
        self.minute_new = self.minute_current
        self.second_new = self.second_current
        self.ms_new = self.ms_current
        # self.dayinyear_new = self.dayinyear_current

        self.day_offset = 0
        self.hour_remainder = 0

    def __str__(self):
        return '{}:{:02d}'.format(self.hour_new, self.minute_new)

    def offset_hours(self, offset_hours_input):
        # this will only change the day when it's over 24 hour offset. It has no concept of AM/PM.

        self.hour_remainder = offset_hours_input % (self.max_values['hours'] * 2)
        self.hour_new = self.hour_remainder + self.hour_current
        self.day_offset = int(
            offset_hours_input / (self.max_values['hours'] * 2))  # minus 2 beacuse it takes 2x 12 hour cycles.

        if self.hour_new > self.max_values['hours']:
            self.hour_new = self.hour_new - self.max_values['hours']

        if self.day_offset > 0:
            self.offset_days(self.day_offset)

    def offset_days(self, offset_days_input):

        # this is not working yet.

        self.day_new = self.day_current + offset_days_input

        if self.day_new > self.max_values['days'][str(self.month_current)]:
            # this actually needs to be loop until the correct month is offset
            self.day_new = self.day_new - self.max_values['days'][str(self.month_current)]

        # month offset, need to calculate this...
        # self.offset_months()
        # raise NotImplementedError

    def offset_months(self, offset_months_input):
        raise NotImplementedError

    def new_time(self):
        from datetime import datetime
        return datetime(year=self.year_new, month=self.month_new, day=self.day_new, hour=self.hour_new,
                        minute=self.minute_new, second=self.second_new, microsecond=self.ms_new)
