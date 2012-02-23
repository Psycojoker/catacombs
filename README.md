# Installation

On debian-based:

    sudo apt-get install mongodb

Standard way:

    sudo pip install -r pip-requirements.txt
    sudo python setup.py install

In a virtual env:

    virtualenv --distribute --no-site-packages ve
    source ve
    pip install -r pip-requirements.txt

    python setup.py install
    # or
    pip install git+git://github.com/Psycojoker/catacombs.git

# Usage

    catacombs run

Launch server.

    catacombs add [list of books]

Add books to the server.

    catacombs add-peers [list of peers]

Add peers to the server.

    catacombs help

Display help.

# API

Http Rest API

    /

List the available ressources.

    /about

Informations of the server.

    /books

List the books offered by the server.

    /peers

List the peers that the server is connected to.

    /info/{id}

Get informations on a book.

    /get/{id}

Obtain a book.
