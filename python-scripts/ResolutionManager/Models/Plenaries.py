import datetime

PLENARY_FOLDER_TEMPLATE = "{year} {month}"
DATE_TEMPLATE = "{month}, {thurs}-{friday} {year}"

class Plenary(object):

    def __init__(self, id=None, thursday_date=None,  first_reading_folder_id=None,
                 plenary_folder_id=None, feedback_folder_id=None, second_reading_folder_id=None):

        # def __init__(self, year, month, thursday_date=None, friday_date=None, first_reading_folder_id=None, plenary_folder_id=None, feedback_folder_id=None, second_reading_folder_id=None):
        self.id = id
        self.second_reading_folder_id = second_reading_folder_id
        self.feedback_folder_id = feedback_folder_id
        self.plenary_folder_id = plenary_folder_id
        self.first_reading_folder_id = first_reading_folder_id
        self.thursday_date = datetime.datetime.strptime(thursday_date, '%Y-%m-%d').date() if isinstance(thursday_date, str) else thursday_date
        # self.thursday_date = datetime.datetime(thursday_date)
        # self.month = month
        # self.year = year
        # self.friday_date = friday_date

    @property
    def formatted_plenary_date(self):
        # if self.year < 2000:
        #     self.year = self.year + 2000
        return DATE_TEMPLATE.format(month=self.month, thurs=self.thursday_day, friday=self.friday_day, year=self.year)

    @property
    def thursday_day(self):
        return self.thursday_date.day

    @property
    def friday_day(self):
        return self.thursday_date.day + 1
    @property
    def month(self):
        return self.thursday_date.strftime("%B")

    @property
    def year(self):
        return self.thursday_date.strftime('%Y')

    @property
    def two_digit_year(self):
        return self.thursday_date.strftime('%y')
        # if self.year > 2000:
        #     return self.year - 2000

    @property
    def plenary_folder_name(self):
        return PLENARY_FOLDER_TEMPLATE.format(year=self.year, month=self.month)

