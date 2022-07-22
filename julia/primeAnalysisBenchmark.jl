include("./primeAnalysis.jl")

using .primeAnalysis
vectTime = Vector{Float64}([])
for i in 1:1:1000
    push!(vectTime, @elapsed isPrime(38237137127))
end

mymean = sum(vectTime)/length(vectTime)

println("Mean: $mymean")