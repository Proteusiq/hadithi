from agents import hello

def test_main_output(capfd):
    # Arrange
    hello.main()

    # Act
    captured = capfd.readouterr()

    # Assert
    assert captured.out == "Hello from agents!\n"
