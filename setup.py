from setuptools import setup, find_packages

with open('README.md') as f:
    long_description = f.read()

setup(
    name='fingerprints',
    version='1.0.1',
    description="A library to generate entity fingerprints.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='names people companies normalisation iso20275',
    author='Friedrich Lindenberg',
    author_email='friedrich@pudo.org',
    url='http://github.com/alephdata/fingerprints',
    license='MIT',
    packages=find_packages(exclude=['tests']),
    namespace_packages=[],
    package_data={'': ['fingerprints/types.json']},
    include_package_data=True,
    zip_safe=False,
    test_suite='nose.collector',
    install_requires=['normality>=2.0.0'],
    tests_require=[
        'nose',
        'coverage',
        'wheel'
    ]
)
