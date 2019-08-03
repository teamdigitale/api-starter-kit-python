import datetime
from random import randint

from connexion import problem
from swagger_server.models.timestamps import Timestamps  # noqa: E501
from throttling_quota import throttle
from flask import after_this_request
from functools import wraps


@throttle
def get_echo():  # noqa: E501
    """Ritorna un timestamp in formato RFC5424.

    Ritorna un timestamp in formato RFC5424 prendendola dal server attuale.  # noqa: E501


    :rtype: Timestamps
    """
    return Timestamps(datetime.datetime.utcnow())


@throttle
def get_status():  # noqa: E501
    """Ritorna lo stato dell'applicazione.

    Ritorna lo stato dell'applicazione.  # noqa: E501


    :rtype: Problem
    """

    @after_this_request
    def cache_no_store(response):
        """Add the 'no-store' cache value to avoid clients and
           intermediaries to store this response.
        """
        response.headers["Cache-Control"] = "no-store"
        return response

    p = randint(0, 10)

    if p < 7:
        return problem(
            status=200,
            title="Success",
            detail="Il servizio funziona correttamente",
            ext={"result": "ok"},
        )
    if p < 9:
        return problem(
            status=503,
            title="Service Unavailable",
            detail="Questo errore viene ritornato randomicamente.",
            headers={"Retry-After": "1"},
        )

    return problem(
        status=429,
        title="Too Many Requests",
        detail="Questo errore viene ritornato randomicamente.",
    )
