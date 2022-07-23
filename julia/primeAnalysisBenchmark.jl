include("./primeAnalysis.jl")

using .primeAnalysis
vectTime2STP = Vector{Float64}([])
vectTime1STP = Vector{Float64}([])


function isPrime2STP(A::Integer)
    if isinteger(sqrt(A))
        return false
    elseif A == 0
        return false
    elseif (A ≠ 2) && (mod(A,2) == 0)
        return false
    else
        nearestSquarert = Int(trunc(sqrt(A)))
        maxFactor = mod(nearestSquarert, 2) == 0 ? nearestSquarert - 1 : nearestSquarert
        println("maxFactor: $maxFactor | nearestSquarert: $nearestSquarert")

        for p ∈ maxFactor:-2:2
            if mod(A,p) == 0
                return false
            end
        end
        return true
    end
end

function isPrime1STP(A::Integer)
    if isinteger(sqrt(A))
        return false
    elseif A == 0
        return false
    elseif (A ≠ 2) && (mod(A,2) == 0)
        return false
    else
        nearestSquarert = Int(trunc(sqrt(A)))
        maxFactor = nearestSquarert
        maxFactor = mod(nearestSquarert, 2) == 0 ? nearestSquarert - 1 : nearestSquarert
        println("maxFactor: $maxFactor | nearestSquarert: $nearestSquarert")

        for p ∈ maxFactor:-1:2
            if mod(A,p) == 0
                return false
            end
        end
        return true
    end
end

println(isPrime(961748941))
for i in 1:1:5
    push!(vectTime1STP, @elapsed isPrime1STP(3823818317456424))
    push!(vectTime2STP, @elapsed isPrime2STP(3823818317456424))
end

mymean1STP = sum(vectTime1STP)/length(vectTime1STP)
mymean2STP = sum(vectTime2STP)/length(vectTime2STP)

println("Mean -1 Step: $mymean1STP")
println("Mean -2 Setp: $mymean2STP")


#= YIELDS
NUMBER             2STP            1STP           nearestSquarert  maxFactor

3823818317456421   0.1165690618    0.2246131326   61837030         61837029
=#