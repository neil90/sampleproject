import sample


def test_success():
    assert True


def test_spark_counter():
    assert 10 == sample.spark_counter(10)
