from ResolutionManager.Models.Committees import Committee
from ResolutionManager.Models.Plenaries import Plenary

from faker import Faker

from ResolutionManager.Models.Resolutions import Resolution


def plenary_factory():
    fake = Faker()

    return Plenary(id=fake.random.randint(1, 99999),
                   thursday_date=fake.date_time(),
                   first_reading_folder_id=fake.sha1(),
                   plenary_folder_id=fake.sha1(),
                   feedback_folder_id=fake.sha1(),
                   second_reading_folder_id=fake.sha1(),
                   agenda_id=fake.sha1())


def resolution_factory():
    fake = Faker()

    committee = committee_factory()

    return Resolution(id=fake.random.randint(1, 99999),
                      number=fake.random.randint(1111, 9999),
                      title=fake.text(),
                      document_id=fake.sha1(),
                      is_waiver=False,
                      committee=committee,
                      cosponsors=[],
                      document_obj=None,
                      is_first_reading=False,
                      is_approved=None,
                      status=None,
                      year=fake.year())


def first_reading_factory():
    r = resolution_factory()
    r.is_first_reading = True
    return r


def second_reading_factory():
    r = resolution_factory()
    r.is_first_reading = False
    r.is_waiver = False
    return r


def waiver_factory():
    r = resolution_factory()
    r.is_waiver = True
    r.is_first_reading = True
    return r

def committee_factory():
    fake = Faker()

    return Committee(full_name=fake.name(), abbreviation=fake.word())
