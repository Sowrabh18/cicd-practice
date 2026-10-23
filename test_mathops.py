from mathops import multiply
from mathops import subtract
from mathops import divide
import pytest




def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(10,0)



def test_multiply():
    result=multiply(3,4)

    assert result==12


def test_subtract():
    result=subtract(10,3)

    assert result==7

def test_subtract2():
    result2=subtract(5,5)
    assert result2==0


def test_comparison():
    assert multiply(4,4)>10



def test_float():
    assert 0.1+0.2==pytest.approx(0.3)


@pytest.mark.parametrize("a,b,expected",[(4,2,2),(3,1,2),(5,4,1)])


def test_sub(a,b,expected):
    assert subtract(a,b)==expected