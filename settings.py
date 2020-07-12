from os import environ
SESSION_CONFIG_DEFAULTS = dict(real_world_currency_per_point=0.01, participation_fee=0.1, mturk_hit_settings=dict(title='Decision making experiment', description='Experiment on decision making', keywords='bonus, study, economics, behavioral, good, pay, easy, anonymity, decision, job, fun, challenge, ', frame_height=500, minutes_allotted_per_assignment=120, expiration_hours=72, grant_qualification_id='', qualification_requirements=[{'QualificationTypeId': '00000000000000000071', 'Comparator': 'EqualTo', 'LocaleValues': [{'Country': 'US'}]}, {'QualificationTypeId': '3Z1HL5WC7KD3AJLBYZO09M3VI276H5', 'Comparator': 'DoesNotExist'}], template='global/mturk_template.html'))
SESSION_CONFIGS = [dict(name='Fist_Session', num_demo_participants=1, app_sequence=['Survey', 'Job1', 'Job2', 'Job3', 'Job4', 'Job5', 'Job6', 'Job7', 'Job8', 'Job9', 'Job10', 'Job11', 'Job12', 'Job13', 'Job14', 'Job15', 'Survey2'])]
LANGUAGE_CODE = 'en'
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True
DEMO_PAGE_INTRO_HTML = ''
ROOMS = []

ADMIN_USERNAME = ''
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

SECRET_KEY = ''

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']


