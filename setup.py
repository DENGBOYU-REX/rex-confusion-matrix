from setuptools import setup, find_packages

setup(
    name='RD_confusion_matrix',  # 包名
    version='0.1.0',  # 版本号
    packages=find_packages(),  # 自动发现包
    install_requires=[
        'numpy==1.26.4',
        'matplotlib==3.9.2',
        'scikit-learn==1.5.2',
    ],
    author='Boyu Rex Deng',  # 你的名字
    author_email='dengby_29@163.com',  # 你的邮箱
    description='A package for plotting confusion matrices.',
    url='https://github.com/DENGBOYU-REX/rex-confusion-matrix',  # 项目主页
    classifiers=[
        'Programming Language :: Python :: 3.11.10',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.11',
)
