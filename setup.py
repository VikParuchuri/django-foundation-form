from setuptools import setup, find_packages
from foundationform.meta import VERSION

setup(
    name='django-foundation-form',
    version=str(VERSION),
    description="django-foundation-form",
    classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Framework :: Django",
        "Environment :: Web Environment",
    ],
    keywords='bootstrap,django',
    author='Vik Paruchuri',
    author_email='vik.paruchuri@gmail.com',
    url='https://github.com/VikParuchuri/django-foundation-form',
    license='BSD',
    test_suite='tests',
    install_requires = [
        "django>=1.3",
    ],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)
