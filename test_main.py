from main import quadratic_multiply, BinaryNumber # I couldnt figure out why it wouldn't work, and I ended up finding out I need to add this for the test + autograder to work



## Feel free to add your own tests here.
def test_multiply():
    assert quadratic_multiply(BinaryNumber(3), BinaryNumber(3)) == 3*3
    assert quadratic_multiply(BinaryNumber(7), BinaryNumber(3)) == 7*3
    assert quadratic_multiply(BinaryNumber(5), BinaryNumber(4)) == 5*4
    assert quadratic_multiply(BinaryNumber(8), BinaryNumber(9)) == 8*9
    assert quadratic_multiply(BinaryNumber(10), BinaryNumber(11)) == 10*11
    assert quadratic_multiply(BinaryNumber(2), BinaryNumber(8)) == 2*8
    assert quadratic_multiply(BinaryNumber(4), BinaryNumber(3)) == 4*3
    assert quadratic_multiply(BinaryNumber(16), BinaryNumber(5)) == 16*5
