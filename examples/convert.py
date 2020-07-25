import numpy as np

y = np.float64('1.2345')
x = np.float64(1.86359857087)
print(np.uint8(x))
print(np.float16(x))
print(np.float32(x))
print(x)
print(y)
print(type(y))
z = float(y)
print(z)
print(type(z))

b = y.tobytes()
print(b)
# np.from buffer returns an ndarray of the specified type
y1 = np.frombuffer(b, dtype="float64")
y2 = np.frombuffer(b, dtype=np.float64)
print(y1 == y2)
print(y1)
print(type(y1))
print(y1.dtype)
# Calling np.float64 on an ndarray of one element will create an instance
# of that dtype
y3 = np.float64(y1)
print(y3)
print(type(y3))
y4 = np.array([2, 3])
print(type(y4))
y5 = np.float64(y4)
print(type(y5))
print(y5)
