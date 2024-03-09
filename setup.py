from setuptools import setup, find_packages

setup(
    name='myhttpcat',
    version='0.4',
    packages=find_packages(),
    install_requires=[
        # 任何依赖项都在这里列出
        'httpcat-sdk'
    ],
    author='dwge1',
    author_email='dwge1234@outlook.com',
    description='myhttpcat',
    license='MIT',
    keywords='myhttpcat',
    url='https://github.com/dwge1/myhttpcat',
    project_urls={
        'Source':'https://github.com/dwge1/myhttpcat',
    },
    repository={
        "type": "git",
        "url": "https://github.com/dwge1/myhttpcat"
    }
)

