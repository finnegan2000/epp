import collections
Rectangle = collections.namedtuple("Rectangle", ["x1", "x2", "y1","y2"])
Point = collections.namedtuple("Point", ("x", "y"))

def find_intersection(R, S):
    x1, x2 = max(R.x1, S.x1), min(R.x2, S.x2)
    y1, y2 = max(R.y1, S.y1), min(R.y2, S.y2)
    return Rectangle(x1, x2, y1, y2) if (x1<=x2 and y1<=y2) else None

def is_rectangle(A,B,C,D):
    def gradient(P,Q):
        return float('inf') if P.x == Q.x else (P.y - Q.y)/(P.x - Q.x)
    return (gradient(A,B) == gradient(C,D) and gradient(A,D) == gradient(B,C) and
            (gradient(A,B) * gradient(A,D) == -1 ) or (gradient(A,B) == 0 and
            gradient(A,D) == float('inf')) or (gradient(A,D) == 0 and
            gradient(A,B) == float('inf')))


print(find_intersection(Rectangle(1,7,2,5), Rectangle(5,6,0,8)))
print(find_intersection(Rectangle(0,2,0,2), Rectangle(2,4,2,4)))
print(is_rectangle(Point(0,0), Point(1,1), Point(0,2), Point(-1,2)))
