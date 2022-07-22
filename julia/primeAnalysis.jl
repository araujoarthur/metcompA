"""
    isPrime(::Integer) [Results in Bool]

    Receives a number and returns true if it is a prime number, false otherwise.
"""
function isPrime(A::Integer)
    if isinteger(sqrt(A))
        return false
    elseif A == 0
        return false
    elseif (A ≠ 2) && (mod(A,2) == 0)
        return false
    else
        nearestSquarert = Int(trunc(sqrt(A)))
        for p ∈ nearestSquarert:-1:2
            if mod(A,p) == 0
                return false
            end
        end
        return true
    end
end

"""
    isPrimeFactor(NUMBER::Integer, FACTOR::Integer) [Results in Bool]

    Receives a number and a POSSIBLE factor. Returns true if FACTOR is a FACTOR and PRIME. Returns false otherwise.
"""
function isPrimeFactor(N::Integer, F::Integer)
    if (mod(N,F) == 0) && isPrime(F)
        return true
    else
        return false
    end
end

"""
    primesTo(::Integer, offset=1::Integer) [Results in Vector{Any}]
    
    Receives a number and an offset and returns a vector with all prime numbers from offset to the number
"""
function primesTo(A::Integer, offset=1::Integer)
    primesVect = Vector()

    for a ∈ offset:1:A
        if isPrime(a)
            push!(primesVect,a)
        end
    end
    return primesVect
end


"""
    primesFrom(::Integer, ::Integer) [Results in Vector{Any}]

    Receives a number and returns all prime numbers from A to the offset
"""
function primesFrom(A::Integer, offset=1::Integer)
    primesVect = Vector()

    for a ∈ A:-1:offset
        if isPrime(a)
            pushfirst!(primesVect,a)
        end
    end
    return primesVect
end


"""
    primesFrom(::Integer, ::Integer, ::Integer) [Results in Vector{Any}]

    Receives a number and returns the count prime numbers from the given number to the offset
"""
function primesFromCount(A::Integer, offset=1::Integer, count=1::Integer)
    primesVect = Vector()

    for a ∈ A:-1:1
        if count == 0
            break
        elseif isPrime(a)
            pushfirst!(primesVect,a)
        end
        count -= 1
    end
    return primesVect
end


"""
    firstPrimeBefore(A <: Real) [Results in <: Real]

    Returns the first prime number that comes before A.
"""
function firstPrimeBefore(A::Real)
    for a in A:-1:1
        if isPrime(a)
            return a
        end

    end
end

"""
    divisorsOf(::Integer, ::String) [Results in Vector{Any}]
    
    Receives a number and a subeset (currently only "primes", "none", "factors") and returns
    the divisors that belong to the subset.

    The subset argument can be hidden.

    ! SUBOPTIOMAL
"""
function divisorsOf(A::Real, subset="none"::String)
    divisorsVect = Vector()
    halfOfA = Int(trunc(A/2))
    nearestSqr = Int(trunc(sqrt(A)))

    for i ∈ 1:1:halfOfA
        if (subset == "primes") && (mod(A,i) == 0) && isPrime(i)
            pushfirst!(divisorsVect, i)
        else mod(A,i) == 0
            pushfirst!(divisorsVect, i)
        end

        if (subset=="factors") && (i >= nearestSqr)
            break
        end
    end

    return divisorsVect
end


"""
    primeFactors(::Integer, ::Integer) [Results in Vector{Any}]

        Returns the count quantity of prime factors of the given number.
        If no count is provided, it i'll bet set to 0 the list will contain all prime factors [! SUBOPTIMAL]
    
        If the count is provided, it'll return the quantity count of prime factors starting from the biggest one.

"""
function primeFactors(A::Integer, count=0::Integer)
    nearestSquarert = Int(trunc(sqrt(A)))
    factors = divisorsOf(A, "factors")
    primeFactorsVect = Vector()
    productory = 1

    for factor ∈ factors
        if isPrimeFactor(A, factor)
            push!(primeFactorsVect,factor)
            productory *= factor
        end

        if productory >= A
            break
        end
    end

    return primeFactorsVect

end

println(@time primeFactors(600851475143, 1))
