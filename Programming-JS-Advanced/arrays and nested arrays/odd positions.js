function solve(numbers){
    const oddNums = numbers.filter((v, i) => i % 2 == 1)
    const  doubles = oddNums.map(x => x *2)
    doubles.reverse()
    console.log(doubles.join(' '))
}