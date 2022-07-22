# To use Float64:
x = Float64(1.2)
println(typeof(x))
y = 1.2e0
println(typeof(y))

# To use Float32:
כ = Float32(2.5)
println(typeof(כ))    # Another peciliarity: Julia allows usage of ANY unicode character. כ for example is Hebraic.
Ⴔ = 124.5f0          # This one is the Georgian Capital letter Phar Ⴔ
println(typeof(Ⴔ))

# To use Float16 (Only in software. Calculations will be taken in Float64)
Ͳ = Float16(2.5)
println(typeof(Ͳ))

# Hexadecimal floating-point literals are also valid, but only as Float64 values, with p preceding the base-2 exponent
# from: JuliaDocs

# One can use _ as digit separator
イ = 10_000_0000
println(イ)
println(typeof(イ))


# The bitstring function converts a type to binary and outputs a bit string:
println(bitstring(イ))

# digits() is also a interesting function!

# Special Floating-Point Values:

# Positive infinity:   Inf16 (for Float16)  Inf32 (for Float32)  Inf (for Float64) | Greater than any Floating Point
# Negative inifinity: -Inf16 (for Float16) -Inf32 (for Float32) -Inf (for Float64) | Smaller than any Floating Point
# Not a Number:        NaN16 (for Float16)  NaN32 (for Float32)  NaN (for Float64) | Not == to any floating point including itself

a = 1/Inf
println("1/Inf = ", a, " ", typeof(a))
b = 1/0
println("1/0 = ", b, " ", typeof(b))
c = -2/0
println("-2/0 = ", c, " ", typeof(c))
d = 1e-15/0
println("1e-15/0 = ", d, " ", typeof(d))
e = 0/0
println("0/0 = ", e, " ", typeof(e))
f = -0/0
println("-0/0 = ", f, " ", typeof(f))
g = 500 + Inf
println("500 + Inf = ", g, " ", typeof(g))
h = 500 - Inf
println("500 - Inf = ", h, " ", typeof(h))
i = Inf + Inf
println("Inf + Inf = ", i, " ", typeof(i))
j = Inf - Inf
println("Inf - Inf = ", j, " ", typeof(j))
k = Inf * Inf
println("Inf * Inf = ", k, " ", typeof(k))
l = Inf/Inf
println("Inf / Inf = ", l, " ", typeof(l))
m = (NaN == NaN)
println("NaN == NaN = ", m, " ", typeof(m))
n = (NaN != NaN)
println("NaN == NaN = ", n, " ", typeof(n))
p = (NaN > NaN)
println("NaN > NaN = ", p, " ", typeof(p))
q = (NaN < NaN)
println("NaN < NaN = ", q, " ", typeof(q))

# Julia provides eps, which gives the distance between 1.0 and the next larger representable floating-point value
println()
println(eps(Float16))
println(eps(Float32))
println(eps(Float64))

# Julia also provides the nextfloat and prevfloat functions which return the next largest or smallest representable 
# floating-point number to the argument respectively

aa = 12f4
println(nextfloat(aa))
println(prevfloat(aa))

println(precision(aa)) # Returns the number of bits in the significand

printstyled("Foo\n", underline=true, color=:light_red)

# a ⊻ b :: Bitwise xor (Exclusive Or). 1 for the bits that are different. between a and b, 0 otherwise
# a ⊼ b :: Bitwise nand (Not And). Execute Bitwise and then negate.
# a ⊽ b :: Bitwise nor (Not Or). Execute bitwise or then negate.
# Updating operators +=  -=  *=  /=  \=  ÷=  %=  ^=  &=  |=  ⊻=  >>>=  >>=  <<=

# Dot operators exist for every binary arithmetic operator (.^ .+ .- .* ./) and execute the operation element by element in a vector.
# Dot update operators (.+= .-= .*=) are in-place operators (change the original value. Without using dot: a = [1,2], b = a, b += [2, 2] -> a == [1, 2], b == [3, 4])
# Using dot operator in vectors:  a = [1,2], b = a, b .+= [2, 2] -> a == [3, 4], b == [3, 4])
# \ne = ≠ | \ge = ≥ | \le = ≤ | 0 .< A .< 1 gives a boolean array whose entries are true where the corresponding elements of A are between 0 and 1.

# Base.operator_precedence(:+) gives the precedence of the operator (Higher: preference.)
# Base.operator_associativity(:+) gives the associativity of the operator (Where is it grouped when there is no parenthesis)

# Constant im is bound to imaginary number.

println(im, " ", typeof(im))

# Julia can represent exact ratios:
print(2//3, " ", typeof(2//3))

# dump() is a good function to check how a value is represented
# Anyone can overload (but it is not a good ideia) an operator in julia. But as it is unicode, we can also create others as it were a function:
# @code_lowered macro in julia terminal let you see how the code is actually implemented (@code_lowered 1+2, for example)   

function (⟂)(w,t)
    if w't == 0 # Inner product
        return true
    else
        return false
    end
end

myv = [1, 0]
myt = [0 , 1]

println()
println(myv ⟂ myt)

# Because of the acceptance of UNICODE some strings could have a ∑sizeof(char)/sizeof(Char) smaller than sizeof(string). That's because an UNICODE char can take
# up to 4 bytes (4 octets [8 bits]).

fooBir = "∀ x ∃ FIELD"
ascii = "Field Foo Bar"
fooStr = fooBir
summation_count = 0
summation_size_foo = 0

for char ∈ fooStr
    global summation_count += 1
    global summation_size_foo += sizeof(char)
    println("$char SIZE: ", sizeof(char), " SUMMATION: $summation_count SUMMATION_SIZE: $summation_size_foo" )
end

println("Summation Count: $summation_count")
println("Summation Size: $summation_size_foo")

println("Size Variable: ", summation_size_foo/sizeof(Char))
println("Size of the String: ", sizeof(fooStr))
println("Length of the String: ", length(fooStr))


#\forall = ∀ | \exists = ∃ | \in = ∈

# One can interpolate strings:

mStrN = "1 + 2 is $(1 + 2) and sizeof(Int) is $(sizeof(Int)) "

mStrA = """This adds an \\n at end of each line
            and is finished after the last three "
        """
mStrB = """This won't add a \\n after because it has \
            a backslash (\\) at the end of the line
            """
# findlast(), findfirst(), findnext() and findprev() are used to search for specific char.
#  findnext(isequal('o'), "xylophone", 1)
# occursin can be used for check for specific substring.
# There is also join: join(["apples", "bananas", "pineapples"], ", ", " and ")
# and Repeat: repeat(".:Z:.", 10)

# Copied from JuliaDocs:
# firstindex(str) gives the minimal (byte) index that can be used to index into str (always 1 for strings, not necessarily true for other containers).
# lastindex(str) gives the maximal (byte) index that can be used to index into str.
# length(str) the number of characters in str.
# length(str, i, j) the number of valid character indices in str from i to j.
# ncodeunits(str) number of code units in a string.
# codeunit(str, i) gives the code unit value in the string str at index i.
# thisind(str, i) given an arbitrary index into a string find the first index of the character into which the index points.
# nextind(str, i, n=1) find the start of the nth character starting after index i.
# prevind(str, i, n=1) find the start of the nth character starting before index i.

# Julia accpets regex https://docs.julialang.org/en/v1/manual/strings/#man-regex-literals)

# It is possible to create raw strings without interpolation:
println(raw"foo\test \t \n")

# In Julia, a function is an object that maps a tuple of argument values to a return value
# How to define a function:

function myFun(x,y)
   return x + y
end

(😂)(a,b) = '😂'^(a^b)
println(😂(5,2))