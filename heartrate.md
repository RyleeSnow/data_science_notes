pip install heartrate

import heartrate

heartrate.trace(browser=True)


127.0.0.1:9999


from heartrate import trace, files


trace(files=files.path_contains('my_app', 'my_library'))


trace(files=files.all)
