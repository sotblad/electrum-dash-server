from setuptools import setup

setup(
    name="electrum-mue-server",
    version="1.0",
    scripts=['run_electrum_mue_server','electrum-mue-server'],
    install_requires=['plyvel','jsonrpclib', 'irc >= 11, <=14.0', 'x11_hash'],
    package_dir={
        'electrumserver':'src'
        },
    py_modules=[
        'electrumserver.__init__',
        'electrumserver.utils',
        'electrumserver.storage',
        'electrumserver.deserialize',
        'electrumserver.networks',
        'electrumserver.blockchain_processor',
        'electrumserver.server_processor',
        'electrumserver.processor',
        'electrumserver.version',
        'electrumserver.ircthread',
        'electrumserver.stratum_tcp'
    ],
    description="MonetaryUnit Electrum Server",
    author="Thomas Voegtlin ,ELM4ever, Propulsion, TheLazieR, sotblad",
    author_email="thomasv@electrum.org, thelazier@gmail.com, swthrhs@protonmail.com",
    license="MIT Licence",
    url="https://github.com/spesmilo/electrum-server/ , https://github.com/sotblad/electrum-mue-server/",
    long_description="""Server for the Electrum Lightweight MonetaryUnit Wallet"""
)
