from setuptools import setup

setup(
    name='cloudify-local-bootstrap',
    version='0.1',
    author='Cloudify',
    author_email='cosmo-admin@cloudify.co',
    packages=['local_bs'],
    license='LICENSE',
    description='Local bootstrap of a cloudify manager',
    entry_points={
        'console_scripts': [
            'cfy_install = local_bs.main:install',
            'cfy_remove = local_bs.main:remove',
            'cfy_config = local_bs.main:configure'
        ]
    }
)
