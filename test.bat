pip freeze
nosetests --with-coverage --cover-package httpfs --cover-package tests tests  docs/source httpfs
