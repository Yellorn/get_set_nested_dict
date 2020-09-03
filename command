https://packaging.python.org/tutorials/packaging-projects/
python3 -m pip install --user --upgrade setuptools wheel

python3 setup.py sdist bdist_wheel
python3 -m twine upload --repository testpypi dist/*

twine upload dist/*

