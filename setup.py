import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
    name="simple_email",
    version="0.1",
    author="ken",
    author_email="596600794@qq.com",
    description="开箱即用的邮件发送包",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/fanfan531/simple-email",
    packages=setuptools.find_packages(),
    install_requires=['psycopg2==2.8.5'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent", ],
)