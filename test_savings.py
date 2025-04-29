from Savings import Savings

def test_add_savings():
    s = Savings(100)
    s.add_savings(50)
    assert s.get_savings() == 150
    print("test_add_savings passed")

test_add_savings()
