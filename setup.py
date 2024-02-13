from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()
    
setup(
    name='df_to_excel_appender',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'openpyxl',
    ],
    entry_points={
        'console_scripts': [
            'df_to_excel_appender = df_to_excel_appender.df_to_excel:append_df_to_excel_cli',
        ],
    },
    author='Tamilselvan Arjunan',
    author_email='nishantamil@gmail.com',
    description='A utility for appending DataFrames to Excel files.',
    long_description=long_description,  # Add this line
    long_description_content_type='text/markdown',  # Specify the content type if using Markdown
    url='https://github.com/arjunlimat/df_to_excel',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
