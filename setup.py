from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()
    
setup(
    name='df2file',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'openpyxl',
    ],
    entry_points={
       'console_scripts': [
            'df2excel = df2file.df_to_file:append_df_to_excel',
            'df2csv = df2file.df_to_file:append_df_to_csv',
        ],
    },
    author='Tamilselvan Arjunan',
    author_email='nishantamil@gmail.com',
    description='A utility for appending DataFrames to Excel/CSV files.',
    long_description=long_description,  # Add this line
    long_description_content_type='text/markdown',  # Specify the content type if using Markdown
    url='https://github.com/arjunlimat/df2file',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
