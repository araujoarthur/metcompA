#To use Float64:
x = Float64(1.2)
println(typeof(x))
y = 1.2e0
println(typeof(y))

#To use Float32:
כ = Float32(2.5)
println(typeof(כ)) # Another peciliarity: Julia allows usage of ANY unicode character. כ for example is Hebraic.
Ⴔ = 124.5f0 # This one is the Georgian Capital letter Phar Ⴔ
println(typeof(Ⴔ))

#To use Float16 (Only in software. Calculations will be taken in Float64)
Ͳ = Float16(2.5)
println(typeof(Ͳ))

#Hexadecimal floating-point literals are also valid, but only as Float64 values, with p preceding the base-2 exponent
#from: JuliaDocs

#One can use _ as digit separator
イ = 10_000_0000
println(イ)
println(typeof(イ))
