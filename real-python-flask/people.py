"""
This is the people module and supports all the ReST actions for the PEOPLE collection
"""

from datetime import datetime
from flask import make_response, abort

def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))


PEOPLE = {
    "Farrel": {
        "fname": "Doug",
        "lname": "Farrell",
        "timestamp": get_timestamp()
    },
    "Brockman": {
        "fname": "Kent",
        "lname": "Brockman",
        "timestamp": get_timestamp()
    },
    "Easter": {
        "fname": "Bunny",
        "lname": "Easter",
        "timestamp": get_timestamp()
    }
}

def read_all():
    """
    This function responds to a request for /api/people with the complete list of people.

    :return:        json string of list of people
    """

    return [PEOPLE[key] for key in sort(PEOPLE.keys())]

def read_one(lname):
    """
    This function responds to a request for /api/people/{lname}
    with one matching person from people

    :param lname:   last name of person to find
    :return:        person matching last name
    """

    # Does the person exist in people?
    if lname in PEOPLE:
        person = PEOPLE.get(lname)
    
    # otherwise, not found
    else:
        abort (
            404, "Person with last name {lname} not found".format(lname=lname)
        )
    
    return person

def create(person):
    """
    This function creates a new person in the peoples structure
    based on the passed in person data

    :param person:      person to create in people structure
    :return:            201 on success, 406 on person exists
    """
    lname = person.get("lname", None);
    fname = person.get("fname", None);

    # Does the person already exist?
    if lname not in PEOPLE and lname is not None:
        PEOPLE[lname] = {
            "lname": lname,
            "fname": fname,
            "timestamp": get_timestamp(),
        }

        return make_response (
            "{lname} successfully created".format(lname=lname),
            201
        )
    
    # Otherwise, they exist, thats an error
    else:
        abort(
            405,
            "erson with last name {lname} already exists".format(lname=lname),
        )

def update(lname, person):
    """
    This function updates an existing person in the people structure

    :param lname:   last name of person to update in the people structure
    :param person:  person to update
    :return:        updated person structure
    """
    # Does the person exist in people?
    if lname in PEOPLE:
        PEOPLE[lname]["fname"] = person.get("fname")
        PEOPLE[lname]["timestamp"] = get_timestamp()

        return PEOPLE[lname]
    else:
        abort (
            404,
            "Person with the last name {lname} not found.".format(lname=lname)
        )

def delete(lname):
    """
    This function deletes a person from the people structure

    :param lname:       last name of person to delete
    :return:            204 on successful delete, 404 if not found.
    """
    if lname in PEOPLE:
        del PEOPLE[lname]
        return make_response(
            "{lname} successfully deleted.".format(lname=lname),
            204
        )
    else:
        abort(
            404,
            "Person with last name: "{lname}", not found".format(lname=lname)
        )

