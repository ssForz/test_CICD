import math

def equation(a, b, c):
    s1 = "+"
    s2 = "+"
    if (b < 0):
        s1 = "-"
    if (c < 0):
        s2 = "-"

    result = f"{a}*x^2 {s1} {abs(b)}*x {s2} {abs(c)} = 0 <br><br>"

    D = b**2 - 4 * a * c

    if D > 0:
        x1 = (-b - math.sqrt(D)) / (2 * a)
        x2 = (-b + math.sqrt(D)) / (2 * a)
        return result + (f"x1 = {x1}, x2 = {x2}")
    
    if D == 0:
        return result + (f"x1,2 = {-b / (2 * a)}")
    
    if D < 0:
        D = -D
        coef1 = -b / (2 * a)
        coef2 = math.sqrt(D) / (2 * a)
        return result + (f"x1 = {coef1} + ({coef2})*i, x2 = {coef1} - ({coef2})*i")
    
    return "error"
    