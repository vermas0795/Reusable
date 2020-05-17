from setuptools import setup

setup(name='datapeek',
      version='0.1',
      description='A simple library for dealing with raw data.',
      url='https://cds-adc-tfs.visualstudio.com/DefaultCollection/Digital%20Hub%20-%20India%20guild%20projects/_git/re-usable_python_library',
      author='Abhishek Verma',
      author_email='abhishek.verma@cdsazure.onmicrosoft.com',
      license='MIT',
      packages=['datapeek'],
       install_requires=[
          'fuzzywuzzy',
          'pandas'
      ],
#         dependency_links=['http://github.com/user/repo/tarball/master#egg=package-1.0'],
#           classifiers=[
#             'Development Status :: 3 - Alpha',
#             'License :: OSI Approved :: MIT License',
#             'Programming Language :: Python :: 2.7',
#             'Topic :: Text Processing :: Linguistic',
#           ],
      include_package_data=True,
      test_suite='nose.collector',
      tests_require=['nose'],
      zip_safe=False)