from intuitions.echo import echo


def test_echo():
    assert echo("ping") == "pong"
