from gluon.storage import Storage
settings = Storage()

settings.migrate = True
settings.title = 'Print on Demand Service - KNV'
settings.subtitle = ''
settings.author = 'withanage'
settings.author_email = 'withanage@ub.uni-heidelberg.de'
settings.keywords = 'omp, python, mysql, knv, onix'
settings.description = ''
settings.layout_theme = 'Default'
#settings.database_uri = 'sqlite://storage.sqlite'
settings.database_uri = 'mysql://omp-suer:omp-password@localhost:3306/omptest'
settings.security_key = '1228409b-a1fc-4868-92b1-a973a607d3f1'
settings.email_server = 'login'
settings.email_sender = 'login'
settings.email_login = ''
settings.login_method = 'local'
settings.login_config = ''
settings.plugins = []

settings.omp_url = 'http://localhost/omp/index.php'
